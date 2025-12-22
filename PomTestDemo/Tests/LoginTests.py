from selenium import webdriver
from PomTestDemo.Pages.LoginPage import LoginPage
from time import sleep


driver = webdriver.Chrome()

def positive_login():
    login_page = LoginPage(driver)
    login_page.open_page('https://practicetestautomation.com/practice-test-login/')
    login_page.login('student', 'Password123')
    print('Positive test passed, successfully logged in')

positive_login()
sleep(2)
driver.quit()
