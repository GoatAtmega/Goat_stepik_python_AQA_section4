import time
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from .login_page import LoginPage
from pages.url_rout import ProductPageUrl
from pages.url_rout import ProductBugPageUrl
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_BASKET).click()
        self.check_promo()
        self.check_price()
        item_name_in_notification = self.browser.find_element(*ProductPageLocators.ITEM_NAME_IN_NOTIF).text
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        assert item_name == item_name_in_notification, \
            f"AT ERROR! Excepted - '{item_name}', result - {item_name_in_notification}"

    def check_price(self):
        price = self.browser.find_element(*ProductPageLocators.CHECK_PRICE).text
        print(price)

    def check_promo(self):
        if (ProductPageUrl.PROMO_URL) in self.url:
            print("\nAT! Promo detected..")
            self.solve_quiz_and_get_code()
        else:
            print("\nAT! Test without promo ..")

    def should_be_a_disappearing_message(self):
        assert self.is_disappeared(*ProductPageLocators.ITEM_NAME_IN_NOTIF), \
            "Success message is presented, but should not be"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ITEM_NAME_IN_NOTIF), \
            "Success message is presented, but should not be"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
