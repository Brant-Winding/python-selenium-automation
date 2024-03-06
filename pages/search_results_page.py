from selenium.webdriver.common.by import By

from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULT_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")

    def verify_search_results_correct(self, expected_result):
        actual_test = self.find_element(*self.SEARCH_RESULT_HEADER).text
        assert expected_result in actual_test, f'Expected word {expected_result} not in {actual_test}'

    def verify_search_results_page_url(self, expected_part_url):
        url = self.driver.current_url
        assert expected_part_url in url, f'Expected {expected_part_url} not in {url}'

    def click_add_to_cart(self):
        self.click(*self.ADD_TO_CART_BTN)