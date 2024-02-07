from selenium.webdriver.common.by import By

from browser import Browser
from pages.login_page import LoginPage


class ProductsPage(Browser):
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, '.inventory_list>.inventory_item>.pricebar>button')
    ITEMS_COUNTER_SPAN = (By.CSS_SELECTOR, 'span.shopping_cart_badge')
    APP_LOGO = (By.CSS_SELECTOR, '.app_logo')

    def go_to_products_page(self):
        login_page = LoginPage()
        login_page.go_to_login_page()
        login_page.set_valid_username()
        login_page.set_valid_password()
        login_page.click_login_button()

    def add_product_to_basket(self):
        self.browser.find_elements(*self.ADD_TO_CART_BUTTONS)[0].click()

    def get_number_of_products_from_basket(self):
        return self.browser.find_element(*self.ITEMS_COUNTER_SPAN).text

    def get_remove_button(self):
        return self.browser.find_elements(*self.ADD_TO_CART_BUTTONS)[0]

    def get_app_logo(self):
        return self.browser.find_element(*self.APP_LOGO)
