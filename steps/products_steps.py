from behave import *


@given('I am on products page')
def step_impl(context):
    context.products_page_object.go_to_products_page()


@when('I press add to cart a product')
def step_impl(context):
    context.products_page_object.add_product_to_basket()


@then('I should see a red icon with one as number above basket icon')
def step_impl(context):
    context.products_page_object.get_number_of_products_from_basket()


@then('Add to cart button should change in remove button')
def step_impl(context):
    context.products_page_object.get_remove_button()
