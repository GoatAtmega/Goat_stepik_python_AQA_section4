from pages.main_page import MainPage
import pages.login_page
from pages.product_page import ProductPage
from pages.base_page import BasePage
from pages.test_link import ProductTestLink
from pages.test_link import ProductBugTestLink
import pytest


@pytest.mark.login_guest
@pytest.mark.parametrize("test_link", ProductTestLink.TEST_LINK)
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                      # открываем страницу
    #    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
        login_page = page.go_to_login_page()
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser, test_link):
        page = MainPage(browser, test_link)
        page.open()
        page.go_to_view_basket()
