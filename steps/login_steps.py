from behave import *


@given('I am on the login page')
def step_impl(context):
    context.login_page_object.go_to_login_page()


@when('I enter a valid email')
def step_impl(context):
    context.login_page_object.set_valid_username()


@when('I enter a valid password')
def step_impl(context):
    context.login_page_object.set_valid_password()


@when('I click the login button')
def step_impl(context):
    context.login_page_object.click_login_button()


@then('I should be on the products page')
def step_impl(context):
    context.products_page_object.get_app_logo()


@when('I enter an invalid password')
def step_impl(context):
    context.login_page_object.set_invalid_password()


@then('I should see an error message')
def step_impl(context):
    result = context.login_page_object.get_error_message()
    assert result, 'Error message not displayed'
    assert result.text == 'Epic sadface: Username and password do not match any user in this service'


@when('I enter an invalid email')
def step_impl(context):
    context.login_page_object.set_invalid_username()


@when('I enter "{username}" as username')
def step_impl(context, username):
    context.login_page_object.set_username(username)


@when('I enter "{passw}" as password')
def step_impl(context, passw):
    context.login_page_object.set_password(passw)
