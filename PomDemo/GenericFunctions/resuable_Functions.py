from selenium.webdriver.common.by import By
from PomDemo.pages.home_page import HomePage
from PomDemo.pages.login_page import LoginPage


class AppReusableFunctions:

    def __init__(self, driver):
        self.driver = driver

    def login_to_the_app(self, url, username, password):
        # url = "https://www.saucedemo.com/"
        login_page = LoginPage(self.driver)
        login_page.open_page(url)
        login_page.enter_username(username)
        login_page.enter_password(password)

        return login_page.click_login()
