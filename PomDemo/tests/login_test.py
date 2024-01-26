import time

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from PomDemo.pages.login_page import LoginPage
from PomDemo.GenericFunctions.resuable_Functions import AppReusableFunctions


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window();
    yield driver
    driver.close()
    driver.quit()


@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce")
])
def test_verify_addcart(driver, username, password):
    url = "https://www.saucedemo.com/"
    login_page = LoginPage(driver)
    login_page.open_page(url)
    login_page.enter_username(username)
    login_page.enter_password(password)
    assert (login_page.click_login()
            .add_item_to_basket()
            .click_cart_icon()
            .verify_remove_button_is_displayed())
    time.sleep(2)


def test_verify_logout(driver):
    url = "https://www.saucedemo.com/"
    appreusablefunctions = AppReusableFunctions(driver)
    (appreusablefunctions.login_to_the_app(url,'standard_user', 'secret_sauce')
     .add_item_to_basket().click_cart_icon()
     .click_remove_item()
     .click_openmenu_icon()
     .click_logout_menu())
    loginpage = LoginPage(driver)
    assert loginpage.verify_login_page_is_displayed()


