from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SIGN_IN_BTN = (By.LINK_TEXT, "Sign in")
SIGN_IN_NAV_BTN = (By.XPATH, "//a[@data-test='accountNav-signIn']//span[text()='Sign in']")
SIGN_IN_MESSAGE = (By.CSS_SELECTOR, "h1[class*='StyledHeading']")


@when('Click Sign In')
def click_sign_in(context):
    context.app.header.click_sign_in()


@then('From right side navigation menu, click Sign In')
def click_sign_in(context):
    context.app.side_nav_page.click_sign_in()


@then('Verify Sign In form opened')
def verify_sign_in(context):
    context.app.sign_in_page.verify_sign_in()
