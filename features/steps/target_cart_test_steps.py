from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_ICON = (By.CSS_SELECTOR, '[data-test="@web/CartIcon"]')
CART_MESSAGE = (By.CSS_SELECTOR, "h1[class*='StyledHeading']")


@when('Click cart icon')
def click_cart_icon(context):
    context.app.header.cart()
    sleep(3)


@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty_message(context):
    context.app.cart.verify_cart_empty_message()
