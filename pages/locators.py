from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK_NEW = (By.CSS_SELECTOR, "#registration_link")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class ProductPageLocators():
    ADD_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ITEM_NAME_IN_NOTIF = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
    CHECK_PRICE = (By.CSS_SELECTOR, ".price_color:nth-child(2)")



class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


