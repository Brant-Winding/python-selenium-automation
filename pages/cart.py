from selenium.webdriver.common.by import By

from pages.base_page import Page


class Cart(Page):
    CART_MESSAGE = (By.CSS_SELECTOR, "h1[class*='StyledHeading']")
    CART_SUMMARY = (By.CSS_SELECTOR, "[class*='CartSummarySpan']")

    def open_cart_page(self):
        self.open("https://www.target.com/cart")

    def verify_cart_empty_message(self):
        actual_text = self.find_element(*self.CART_MESSAGE).text
        assert 'Your cart is empty' == actual_text, f"Expected 'Your cart is empty' but got {actual_text}"

    def verify_cart_items(self, amount):
        cart_summary = self.find_element(*self.CART_SUMMARY).text
        assert amount in cart_summary, f"Expected {amount} items but got {cart_summary}"
