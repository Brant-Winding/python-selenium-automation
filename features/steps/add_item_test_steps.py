from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
CART_ICON = (By.CSS_SELECTOR, '[data-test="@web/CartIcon"]')
SIDE_NAV_CART_BTN = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")
CART_SUMMARY = (By.CSS_SELECTOR, "[class*='CartSummarySpan']")


@when('Click Add to cart')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()


@when('Click Add to cart from side nav')
def click_add_to_side_nav(context):
    context.wait.until(EC.visibility_of_element_located(SIDE_NAV_CART_BTN))
    context.driver.find_element(*SIDE_NAV_CART_BTN).click()


@when('Open Cart page')
def open_cart_page(context):
    context.driver.get("https://www.target.com/cart")


@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    context.wait.until(EC.visibility_of_element_located(CART_SUMMARY))
    cart_summary = context.driver.find_element(*CART_SUMMARY).text
    assert amount in cart_summary, f"Expected {amount} items but got {cart_summary}"



