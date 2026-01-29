from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class SeleniumExtra:

    def __init__(self,driver):
        self.driver = driver
        self.default_timeout = 10
        self.wait = WebDriverWait(self.driver, self.default_timeout)

    def wait_and_input_text(self, locator, text, timeout = None):
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def wait_and_click_text(self, locator, timeout = None):
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator)).click()