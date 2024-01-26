from selenium.webdriver.common.by import By
from PomDemo.pages.shoppingcart_page import ShoppingCartPage

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.addToCart_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.shoppingCart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def add_item_to_basket(self):
        self.driver.find_element(*self.addToCart_button).click()
        return self

    def click_cart_icon(self):
        self.driver.find_element(*self.shoppingCart_icon).click()
        return ShoppingCartPage(self.driver)
