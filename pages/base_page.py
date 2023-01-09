from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.url_rout import ProductPageUrl
from .locators import BasePageLocators


class BasePage():
    def expectation_that_there_are_no_items_in_the_cart(self):
        empty_basket = self.browser.find_element(*BasePageLocators.EMPTY_BASKET)
        assert self.is_not_element_present(empty_basket), "basket is not empty"

    def expecting_there_is_text_that_the_cart_is_empty(self):
        empty_cart_message = self.browser.find_element(*BasePageLocators.EMPTY_CART_MESSAGE)
        assert empty_cart_message, "Empty cart message missing"

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
        link.click()

    def go_to_view_basket(self):
        view_basket = self.browser.find_element(*BasePageLocators.VIEW_BASKET)
        view_basket.click()
        self.expectation_that_there_are_no_items_in_the_cart()
        self.expecting_there_is_text_that_the_cart_is_empty()

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def is_element_present(self, how, what):  # how (CSS/ID/XPATH) what (Selector)
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def open(self):
        self.browser.get(self.url)

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
