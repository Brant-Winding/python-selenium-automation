from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class SignInPage(Page):
    SIGN_IN_MESSAGE = (By.CSS_SELECTOR, "h1[class*='StyledHeading']")

    def verify_sign_in(self):
        actual_text = self.find_element(*self.SIGN_IN_MESSAGE).text
        assert 'Sign into your Target account' == actual_text, f"Expected 'Sign into your Target account' but got {actual_text}"