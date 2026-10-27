"""Small reproducible mutation harness for the three Lab 6 target functions.
Mutants are source-level changes applied only to a temporary copy of the repository."""
from pathlib import Path
import csv, json, shutil, subprocess, sys, tempfile
HERE=Path(__file__).resolve().parent
REPO=HERE.parent
SOURCE=REPO/'app'/'tasks.py'
AI=REPO/'Lab-6-Solutions'/'test_ai_generated.py'
MANUAL=REPO/'Lab-6-Solutions'/'test_manual.py'
MUTANTS=[
 ('M1_remove_comparison','if tasks[i]["id"] == task_id:', 'if tasks[i]["id"] != task_id:', 'remove_task'),
 ('M2_remove_no_match_break','            break\n', '            pass  # mutant: omitted break\n', 'remove_task'),
 ('M3_save_wrong_payload','json.dump(tasks, f)', 'json.dump([], f)', 'save_tasks'),
 ('M4_missing_file_wrong_default','    return []', '    return None', 'load_tasks'),
 ('M5_load_wrong_mode','open(TASKS_FILE, "r")','open(TASKS_FILE, "w")','load_tasks'),
 ('M6_save_no_write','json.dump(tasks, f)','json.dump([], f)','save_tasks'),
]
def run_one(mutant, suite):
    name, old, new, target=mutant
    original=SOURCE.read_text(encoding='utf-8')
    start=original.find('def '+target+'(')
    end=original.find('\ndef ', start+1)
    if start < 0: return {'mutant':name,'suite':suite,'status':'INVALID','detail':'target function not found'}
    if end < 0: end=len(original)
    function=original[start:end]
    if old not in function: return {'mutant':name,'suite':suite,'status':'INVALID','detail':'replacement anchor not found in target function'}
    changed=original[:start]+function.replace(old,new,1)+original[end:]
    with tempfile.TemporaryDirectory(prefix='comp441_mut_') as td:
        dst=Path(td)/'repo'; (dst/'app').mkdir(parents=True); (dst/'Lab-6-Solutions').mkdir()
        (dst/'app'/'__init__.py').write_text('',encoding='utf-8')
        (dst/'app'/'tasks.py').write_text(changed,encoding='utf-8')
        shutil.copy2(AI,dst/'Lab-6-Solutions'/'test_ai_generated.py')
        shutil.copy2(MANUAL,dst/'Lab-6-Solutions'/'test_manual.py')
        tests=[dst/'Lab-6-Solutions'/'test_ai_generated.py'] if suite=='ai' else [dst/'Lab-6-Solutions'/'test_manual.py'] if suite=='manual' else [dst/'Lab-6-Solutions'/'test_ai_generated.py',dst/'Lab-6-Solutions'/'test_manual.py']
        try:
            p=subprocess.run([sys.executable,'-m','pytest','-q',*map(str,tests)],cwd=dst,capture_output=True,text=True,timeout=5)
        except subprocess.TimeoutExpired:
            return {'mutant':name,'suite':suite,'status':'TIMEOUT','detail':'Test process exceeded 5 seconds'}
        killed=p.returncode!=0
        return {'mutant':name,'suite':suite,'status':'KILLED' if killed else 'SURVIVED','detail':(p.stdout+p.stderr).strip()[-500:]}

def main():
    rows=[]
    for suite in ('ai','manual','combined'):
        for mutant in MUTANTS:
            rows.append(run_one(mutant,suite))
    out=HERE/'reports'; out.mkdir(exist_ok=True)
    with (out/'mutation_results.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=['mutant','suite','status','detail']);w.writeheader();w.writerows(rows)
    summaries={}
    for suite in ('ai','manual','combined'):
        subset=[r for r in rows if r['suite']==suite and r['status'] in ('KILLED','SURVIVED')]
        killed=sum(r['status']=='KILLED' for r in subset)
        summaries[suite]={'valid_mutants':len(subset),'killed':killed,'survived':len(subset)-killed,'mutation_score_percent':round(killed/len(subset)*100,2) if subset else None}
    (out/'mutation_summary.json').write_text(json.dumps(summaries,indent=2),encoding='utf-8')
    print(json.dumps(summaries,indent=2)); print('Detailed results:',out/'mutation_results.csv')
if __name__=='__main__': main()
