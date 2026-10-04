"""Page Object for the locally served SeleniumBase demonstration page."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.color import Color


class DemoPage:
    TEXT_INPUT = (By.ID, "myTextInput")
    TEXTAREA = (By.ID, "myTextarea")
    BUTTON = (By.ID, "myButton")
    PARAGRAPH = (By.ID, "pText")
    SELECT = (By.ID, "mySelect")
    METER = (By.ID, "meterBar")
    CHECKBOX = (By.ID, "checkBox1")

    def __init__(self, driver):
        self.driver = driver

    def enter_text(self, text):
        element = self.driver.find_element(*self.TEXT_INPUT)
        element.clear()
        element.send_keys(text)
        return element.get_attribute("value")

    def enter_notes(self, text):
        element = self.driver.find_element(*self.TEXTAREA)
        element.clear()
        element.send_keys(text)
        return element.get_attribute("value")

    def change_button_colour(self):
        button = self.driver.find_element(*self.BUTTON)
        button.click()
        return {
            "text": button.text,
            "colour": Color.from_string(button.value_of_css_property("color")).hex,
            "paragraph": self.driver.find_element(*self.PARAGRAPH).text,
        }

    def select_percentage(self, text):
        select = Select(self.driver.find_element(*self.SELECT))
        select.select_by_visible_text(text)
        return {
            "value": select.first_selected_option.get_attribute("value"),
            "meter": float(self.driver.find_element(*self.METER).get_attribute("value")),
        }

    def set_checkbox(self, checked):
        element = self.driver.find_element(*self.CHECKBOX)
        if element.is_selected() != checked:
            element.click()
        return element.is_selected()
