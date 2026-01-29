import os
import pytest


@pytest.mark.usefixtures('init_driver')
class TestDummy():

    def test_login(self):
          print("hello")
    def test_dummy_func(self):
          browser = os.environ.get("BROWSER", "chrome")
          self.driver.get("https://amazon.com")
          print('Skeleton setup valid')


