from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target main page')
def open_target_main(context):
    context.driver.get("https://www.target.com/")


@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(By.ID, 'search').send_keys(product)
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(6)


@then('Search results for {expected_result} is shown')
def verify_search_results_correct(context, expected_result):
    actual_test = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert expected_result in actual_test, f'Expected word {expected_result} not in {actual_test}'
    print('Test case passed')