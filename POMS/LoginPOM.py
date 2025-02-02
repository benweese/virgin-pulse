#!/usr/bin/env python

"""
LoginPOM.py: .
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os


__author__ = "Ben Weese"
__copyright__ = "Copyright 2019, Python Automation"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Ben Weese"
__email__ = "ben@benweese.dev"
__status__ = "refactor"


class LoginPOM(object):
    """
    This is the Page Object Model used in test_forms_Page.py for the filling out forms section
    of Ultimate QA's Automation Exercises.
    """
    URL = 'https://member.virginpulse.com/login.aspx'

    username = (By.ID, 'username')
    password = (By.ID, 'password')
    submit = (By.CLASS_NAME, 'login-submit')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def login(self):
        USER = os.getenv('vp_username')
        PASSWORD = os.environ.get('vp_password')
        username_field = self.browser.find_element(*self.username)
        username_field.send_keys(USER)
        password_field = self.browser.find_element(*self.password)
        password_field.send_keys(PASSWORD)
        submit_btn = self.browser.find_element(*self.submit)
        submit_btn.click()

    def wait(self):
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(self.username))
