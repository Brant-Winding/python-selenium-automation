from selenium.webdriver.common.by import By
from pages.base_page import Page

from time import sleep


class CirclePage(Page):
    BENEFIT_BOXES = (By.CSS_SELECTOR, "[class*='BenefitCardImageContainer']")
    TABS = (By.CSS_SELECTOR, "[class*='PageSelectionText'] a")
    BONUS_TAB = (By.CSS_SELECTOR, "[data-test='bonus-tab']")
    GOOGLE_PLAY_BTN = (By.CSS_SELECTOR, "[alt='Get it on Google Play']")

    def open_circle_page(self):
        self.open("https://www.target.com/circle")
        sleep(3)

    def verify_benefit_boxes(self, amount):
        amount = int(amount)
        benefit_boxes = self.find_elements(*self.BENEFIT_BOXES)
        assert len(benefit_boxes) == amount, f'Expected {amount} benefit boxes, but got {len(benefit_boxes)}'

    def click_google_play_btn(self):
        self.wait_element_clickable_click(*self.GOOGLE_PLAY_BTN)

    def verify_google_play_opened(self):
        self.verify_partial_url('https://play.google.com/store/apps')
