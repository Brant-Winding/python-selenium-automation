from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, '[data-test="@web/CartIcon"]')
    SIGN_IN_BTN = (By.LINK_TEXT, "Sign in")

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(6)

    def cart(self):
        self.click(*self.CART_ICON)
        sleep(3)

    def click_sign_in(self):
        self.click(*self.SIGN_IN_BTN)
        