from selenium.webdriver.common.by import By
from .base_page import BasePage 

class FormPage(BasePage):  
    URL = "https://practice-automation.com/form-fields/"

    # Локаторы элементов 
    NAME_FIELD = (By.ID, "name")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#password") 
    DRINKS_MILK_CHECKBOX = (By.XPATH, "//input[@value='milk']") 
    DRINKS_COFFEE_CHECKBOX = (By.XPATH, "//input[@value='coffee']") 
    COLOR_DROPDOWN = (By.ID, "color")
    COLOR_YELLOW_OPTION = (By.CSS_SELECTOR, "#color > option[value='yellow']") 
    AUTOMATION_RADIO_YES = (By.XPATH, "//input[@value='yes']")
    EMAIL_FIELD = (By.CSS_SELECTOR, "input#email") 
    MESSAGE_FIELD = (By.ID, "message")
    SUBMIT_BUTTON = (By.ID, "submit")

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get(self.URL)

    def fill_name(self, name):
        self.send_keys(self.NAME_FIELD, name)

    def fill_password(self, password):
        self.send_keys(self.PASSWORD_FIELD, password)

    def select_drinks(self):
        self.click(self.DRINKS_MILK_CHECKBOX)
        self.click(self.DRINKS_COFFEE_CHECKBOX)

    def select_color_yellow(self):
        self.click(self.COLOR_DROPDOWN) 
        self.click(self.COLOR_YELLOW_OPTION) 

    def select_automation_yes(self):
        self.click(self.AUTOMATION_RADIO_YES)

    def fill_email(self, email):
        self.send_keys(self.EMAIL_FIELD, email)

    def fill_message(self, message):
        self.send_keys(self.MESSAGE_FIELD, message)

    def submit_form(self):
        self.click(self.SUBMIT_BUTTON)
