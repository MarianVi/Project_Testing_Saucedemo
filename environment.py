from browser import Browser
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def before_all(context):
    context.browser = Browser()
    context.login_page_object = LoginPage()
    context.products_page_object = ProductsPage()


def after_all(context):
    context.browser.close()
