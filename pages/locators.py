from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK_NEW = (By.CSS_SELECTOR, "#registration_link")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


