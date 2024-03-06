from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class SideNavPage(Page):
    SIGN_IN_NAV_BTN = (By.XPATH, "//a[@data-test='accountNav-signIn']//span[text()='Sign in']")
    SIDE_NAV_CART_BTN = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")

    def click_sign_in(self):
        self.click(*self.SIGN_IN_NAV_BTN)
        sleep(3)

    def click_add_to_side_nav(self):
        self.click(*self.SIDE_NAV_CART_BTN)
