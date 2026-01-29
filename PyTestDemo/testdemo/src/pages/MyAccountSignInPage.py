from testdemo.src.helpers.Locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from testdemo.src.helpers.SeleniumExtra import SeleniumExtra

# def login(self, username, password):
#     self.driver.find_element(*self.username_field_id).send_keys(username)
#     sleep(1)
#     self.driver.find_element(*self.password_field_id).send_keys(password)
#     sleep(1)
#     self.driver.find_element(*self.submit_field_id).click()


class MyAccountSignedIn(Locators):

    def __init__(self, driver):
            self.driver = driver
            self.sl = SeleniumExtra(self.driver)

    def go_to_login_page(self):
        self.driver.get('https://practicetestautomation.com/practice-test-login/')

    def input_login_username(self, username):
        self.sl.wait_and_input_text(self.LOGIN_USERNAME, username)

    def input_login_password(self, password):
        self.sl.wait_and_input_text(self.LOGIN_PASSWORD, password)

    def click_submit_button(self):
        self.sl.wait_and_click_text(self.LOGIN_SUBMIT_BTN)