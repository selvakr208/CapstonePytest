import time

from selenium.webdriver.common.by import By
from PomDemo.pages.home_page import HomePage


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_textbox = (By.ID, "user-name")
        self.password_textbox = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def open_page(self, url):
        self.driver.get(url)

    def enter_username(self, username_param):
        username_elem = self.driver.find_element(*self.username_textbox)
        username_elem.click()
        username_elem.clear()
        username_elem.send_keys(username_param)

    def enter_password(self, password_param):
        password_elem = self.driver.find_element(*self.password_textbox)
        password_elem.click()
        password_elem.clear()
        password_elem.send_keys(password_param)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()
        return HomePage(self.driver)

    def verify_login_page_is_displayed(self):
        time.sleep(2)
        return self.driver.find_element(*self.login_button).is_displayed()
