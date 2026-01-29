from selenium.webdriver.common.by import By



class Locators:
    def __init__(self, driver):
        self.driver = driver
        LOGIN_USERNAME = (By.ID, 'username')
        LOGIN_PASSWORD = (By.ID, 'password')
        LOGIN_SUBMIT_BTN = (By.ID, 'submit')