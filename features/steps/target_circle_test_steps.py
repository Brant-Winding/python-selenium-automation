from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

BENEFIT_BOXES = (By.CSS_SELECTOR, "[class*='BenefitCardImageContainer']")


@given('Open Target circle page')
def open_target_main(context):
    context.driver.get("https://www.target.com/circle")


@then('Verify there are 5 benefit boxes')
def verify_benefit_boxes(context):
    benefit_boxes = context.driver.find_elements(*BENEFIT_BOXES)
    print(benefit_boxes)
