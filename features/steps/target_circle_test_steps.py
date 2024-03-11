from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

BENEFIT_BOXES = (By.CSS_SELECTOR, "[class*='BenefitCardImageContainer']")


@given('Open Target circle page')
def open_circle_page(context):
    context.app.circle_page.open_circle_page()


@then('Verify there are {amount} benefit boxes')
def verify_benefit_boxes(context, amount):
    context.app.circle_page.verify_benefit_boxes(amount)


@given('Store original window')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle
    print('Current window is', context.original_window)
    print('All windows', context.driver.window_handles)


@when('Click Google Play button')
def click_google_play_btn(context):
    context.app.circle_page.click_google_play_btn()
    # sleep(2)
    # print('All windows after GPlay click', context.driver.window_handles)


@when('Switch to new window')
def switch_to_new_window(context):
    context.app.circle_page.switch_to_new_window()
    print('Switching to a new window:')
    print('Current window is', context.original_window)
    print('All windows', context.driver.window_handles)


@then('Verify Google Play Target page opened')
def verify_google_play_opened(context):
    context.app.circle_page.verify_google_play_opened()


@then('Close current page')
def close(context):
    context.driver.close()


@then('Return to original window')
def switch_to_original_window(context):
    context.app.circle_page.switch_to_window_by_id(context.original_window)
    print('After switching back:')
    print('Current window is', context.original_window)