from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def email_gen(self):
        email = str(time.time()) + "@fakemail.org"
        return email

    def register_new_user(self):
        email = self.email_gen()
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASS).send_keys("11111111Q")
        self.browser.find_element(*LoginPageLocators.PASS_CONFIRM).send_keys("11111111Q")
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = self.browser.current_url
        assert "login" in login_url, "AT ERROR! this is not login url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "AT Error! Login form is not present."

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "AT Error! Login form is not present."
