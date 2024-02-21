from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/CartIcon"]').click()


@then('Verify “Your cart is empty” message is shown')
def verify_cart_is_empty(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "h1[class*='StyledHeading']").text
    assert 'Your cart is empty' == actual_text, f"Expected 'Your cart is empty' but got {actual_text}"
