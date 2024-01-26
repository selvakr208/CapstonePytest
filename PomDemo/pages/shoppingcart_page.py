import time

from selenium.webdriver.common.by import By


# from PomDemo.pages.login_page import LoginPage


class ShoppingCartPage:
    def __init__(self, driver):
        self.driver = driver
        self.remove_button = (By.ID, "remove-sauce-labs-backpack")
        self.openmenu_icon = (By.XPATH, "//*[text()='Open Menu']")
        self.logout_menu = (By.XPATH, "//a[text()='Logout']")

    def click_remove_item(self):
        time.sleep(2)
        self.driver.find_element(*self.remove_button).click()
        return self

    def verify_remove_button_is_displayed(self):
        time.sleep(2)
        removeitem_elem = self.driver.find_element(*self.remove_button)
        return removeitem_elem.is_displayed()

    def click_openmenu_icon(self):
        self.driver.find_element(* self.openmenu_icon).click()
        return self

    def click_logout_menu(self):
        self.driver.find_element(* self.logout_menu).click()
        return self

    def verify_opemmenu_is_displayed(self):
        openmenu_elem = self.driver.find_element(* self.openmenu_icon)
        return openmenu_elem.is_displayed()




