from selenium.webdriver.common.by import By

from pages.base_page import Page


class Cart(Page):
    CART_MESSAGE = (By.CSS_SELECTOR, "h1[class*='StyledHeading']")

    def verify_cart_empty_message(self):
        actual_text = self.find_element(*self.CART_MESSAGE).text
        assert 'Your cart is empty' == actual_text, f"Expected 'Your cart is empty' but got {actual_text}"
