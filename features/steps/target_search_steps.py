from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
SEARCH_RESULT_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")


@given('Open Target main page')
def open_target_main(context):
    # context.driver.get("https://www.target.com/")
    context.app.main_page.open_main()


@when('Search for {product}')
def search_product(context, product):
    context.app.header.search_product(product)


@then('Search results for {expected_result} is shown')
def verify_search_results_correct(context, expected_result):
    context.app.search_results_page.verify_search_results_correct(expected_result)


@then('Page URL has search term {expected_part_url}')
def verify_search_results_page_url(context, expected_part_url):
    context.app.search_results_page.verify_search_results_page_url(expected_part_url)