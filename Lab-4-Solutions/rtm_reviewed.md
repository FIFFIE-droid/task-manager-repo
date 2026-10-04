AI-assisted RTM reviewed against the sample code, existing tests and recorded terminal results. Requirements are inferred, not lecturer-supplied. TC12–TC15 are planned and have not been executed.

| Requirement ID | Requirement description | Test case ID(s) | Test description | Test level | Status |
|---|---|---|---|---|---|
| R01 | Add an unfinished task with the correct fields | TC03 | Add “Study” with priority `2` and tag “school”; check all stored fields | Unit | Passed |
| R02 | Complete an existing task; handle an unknown ID | TC04, TC05 | Complete ID `1`; try ID `99` and check that the existing task remains unfinished | Unit | Passed |
| R03 | Return every unfinished task | TC06, TC07 | Check a mixture of finished/unfinished tasks; check that all-completed tasks produce an empty list | Unit | Passed |
| R04 | Calculate average priority; handle an empty list | TC08, TC09 | Priorities `1` and `3` return `2`; an empty list returns `0` | Unit | Passed |
| R05 | Return the first exact title match or `None` | TC10, TC11 | Search duplicate “Study” titles; search for “Missing” | Unit | Passed |
| R06 | Remove a matching task; preserve the list for an unknown ID | TC12, TC13 | Remove ID `2` and retain the other tasks; try ID `99` and expect no change | Unit | Not Run |
| R07 | Save/load task data; handle a missing file | TC14, TC15 | Save then reload and compare data; load a nonexistent file and expect `[]` | Integration / Unit | Not Run |
| R08 | Apply the premium discount; preserve the regular price | TC01, TC02 | Price `100` returns `80` for premium and `100` for regular customers | Unit | Passed—earlier run |