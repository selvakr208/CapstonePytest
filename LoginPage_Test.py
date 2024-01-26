
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


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

    driver.get("https://www.saucedemo.com/");
    userid_elem = driver.find_element(By.ID,"user-name")
    userid_elem.click()
    userid_elem.clear()
    userid_elem.send_keys(username)

    password_elem = driver.find_element(By.ID,"password")
    password_elem.click()
    password_elem.clear()
    password_elem.send_keys(password)

    driver.find_element(By.ID, "login-button").click()



    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click();
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click();

    removecart_elem = driver.find_element(By.ID,"remove-sauce-labs-backpack");

    assert removecart_elem.is_displayed()
    time.sleep(5)

def test_verifyLogout(driver):
    driver.get("https://www.saucedemo.com/");
    userID_elem = driver.find_element(By.ID, "user-name");
    userID_elem.click();
    userID_elem.clear();
    userID_elem.send_keys("standard_user")

    password_elem = driver.find_element(By.ID, "password");
    password_elem.click();
    password_elem.clear();
    password_elem.send_keys("secret_sauce")

    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click();
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click();

    time.sleep(5)
    removecart_elem = driver.find_element(By.ID, "remove-sauce-labs-backpack");
    removecart_elem.click();

    time.sleep(2)
    driver.find_element(By.XPATH, "//*[text()='Open Menu']").click()

    driver.find_element(By.XPATH, "//a[text()='Logout']").click()

    time.sleep(5)
    assert driver.find_element(By.ID, "login-button").is_displayed()
    time.sleep(2)


def login_to_app(driver):
    userID_elem = driver.find_element(By.ID, "user-name");
    userID_elem.click();
    userID_elem.clear();
    userID_elem.send_keys("standard_user")

    password_elem = driver.find_element(By.ID, "password");
    password_elem.click();
    password_elem.clear();
    password_elem.send_keys("secret_sauce")

    driver.find_element(By.ID, "login-button").click()
