from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from browser import Browser


class LoginPage(Browser):
    USERNAME_FIELD = (By.ID, 'user-name')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '[data-test="error"]')

    def go_to_login_page(self):
        self.browser.get('https://www.saucedemo.com/v1/index.html')

    def set_valid_username(self):
        self.browser.find_element(*self.USERNAME_FIELD).send_keys('standard_user')

    def set_valid_password(self):
        self.browser.find_element(*self.PASSWORD_FIELD).send_keys('secret_sauce')

    def click_login_button(self):
        self.browser.find_element(*self.LOGIN_BUTTON).click()

    def set_invalid_password(self):
        self.browser.find_element(*self.PASSWORD_FIELD).send_keys('wrong')

    def set_invalid_username(self):
        self.browser.find_element(*self.USERNAME_FIELD).send_keys('username1')

    def set_username(self, username):
        self.browser.find_element(*self.USERNAME_FIELD).send_keys(username)

    def set_password(self, password):
        self.browser.find_element(*self.PASSWORD_FIELD).send_keys(password)

    # folosim try / except, deoarece exista posibilitatea sa nu apara elementul
    # si dorim sa gestionam noi exceptia
    def get_error_message(self):
        try:
            return self.browser.find_element(*self.ERROR_MESSAGE)

        except NoSuchElementException:
            return False

