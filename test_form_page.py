from .pages.form_page import FormPage
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome
    driver.maximize_window()
    yield driver
    driver.quit()

def test_form_submission(driver):
    form_page = FormPage(driver)
    form_page.open()

    form_page.fill_name("Big Boss")

    form_page.fill_password("Qwerty12")

    form_page.select_drinks()

    form_page.select_color_yellow()

    form_page.select_automation_yes()

    form_page.fill_email("barabulka@gmail.com")

    message = f"5"
    form_page.fill_message(message)


    form_page.submit_form()


    alert = driver.switch_to.alert
    assert alert.text == "Message received!"
    alert.accept()
