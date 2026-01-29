import pytest
import os
from testdemo.src.pages import MyAccountSignInPage

@pytest.mark.tcid12
@pytest.mark.usefixtures('init_driver')
class PositiveLoginTest:

    def test_positive_login(self):
        my_account = MyAccountSignInPage(self.driver)
        my_account.go_to_login_page()
        my_account.input_login_username()
        my_account.input_login_password()
        my_account.click_login_button()