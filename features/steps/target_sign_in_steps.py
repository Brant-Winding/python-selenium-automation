from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.LINK_TEXT, "Sign in").click()


@then('From right side navigation menu, click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']//span[text()='Sign in']").click()


@then('Verify Sign In form opened')
def verify_sign_in(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "h1[class*='StyledHeading']").text
    assert 'Sign into your Target account' == actual_text, f"Expected 'Sign into your Target account' but got {actual_text}"