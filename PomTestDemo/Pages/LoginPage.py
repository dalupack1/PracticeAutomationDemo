from time import sleep

from selenium.webdriver.common.by import By
from selenium import webdriver
import time


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_field_id = (By.ID, 'username')
        self.password_field_id = (By.ID, 'password')
        self.submit_field_id = (By.ID, 'submit')


    def open_page(self, url):
        self.driver.get(url)


    def login(self, username, password):
        self.driver.find_element(*self.username_field_id).send_keys(username)
        sleep(1)
        self.driver.find_element(*self.password_field_id).send_keys(password)
        sleep(1)
        self.driver.find_element(*self.submit_field_id).click()