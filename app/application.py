from pages.base_page import Page
from pages.cart import Cart
from pages.main_page import MainPage
from pages.header import Header
from pages.search_results_page import SearchResultsPage
from pages.side_nav_page import SideNavPage
from pages.sign_in_page import SignInPage
from pages.circle_page import CirclePage


class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.cart = Cart(driver)
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.sign_in_page = SignInPage(driver)
        self.side_nav_page = SideNavPage(driver)
        self.circle_page = CirclePage(driver)
