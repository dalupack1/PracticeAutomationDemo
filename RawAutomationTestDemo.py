# Test case 1: Positive LogIn test
# Open page
# Type username student into Username field
# Type password Password123 into Password field
# Push Submit button
# Verify new page URL contains practicetestautomation.com/logged-in-successfully/
# Verify new page contains expected text ('Congratulations' or 'successfully logged in')
# Verify button Log out is displayed on the new page
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

username_field_id = 'username'
password_field_id = 'password'
submit_button_id = 'submit'
logout_button_id = 'a.wp-block-button__link'

driver = webdriver.Chrome()
url = "https://practicetestautomation.com/practice-test-login/"
driver.get(url)
sleep(1)

username_field = driver.find_element(By.ID, 'username')
username_field.send_keys('student')
sleep(1)

password_field = driver.find_element(By.ID, 'password')
password_field.send_keys('Password123')
sleep(2)

submit_field = driver.find_element(By.ID, 'submit')
submit_field.click()
sleep(2)


assert 'https://practicetestautomation.com/logged-in-successfully/' in driver.current_url
sleep(1)
print("Test Passed: Correct URL")

logged_in_successfully_message = driver.find_element(By.XPATH, '//h1[@class="post-title"]')
assert logged_in_successfully_message.text == 'Logged In Successfully'
sleep(1)
print(("Test Passed: Successfully logged in"))

logout_button = driver.find_element(By.CLASS_NAME, 'wp-block-button__link')
assert logout_button.text == 'Log out', f'Log out button not visible: {logout_button.text}'
sleep(1)
print("Test Passed: Log out button available")
driver.close()
driver.quit()