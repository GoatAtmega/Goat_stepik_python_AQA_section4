import time
import pytest
from pages.product_page import ProductPage
from pages.base_page import BasePage
from pages.test_link import ProductTestLink
from pages.test_link import ProductBugTestLink
from pages.main_page import MainPage


@pytest.mark.skip
@pytest.mark.xfail
@pytest.mark.parametrize("test_link", ProductBugTestLink.TEST_LINK)
def test_guest_can_add_product_to_basket(browser, test_link):
    page = ProductPage(browser, test_link)
    page.open()
    page.add_to_basket()


@pytest.mark.skip
@pytest.mark.xfail
@pytest.mark.parametrize("test_link", ProductTestLink.TEST_LINK)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, test_link):
    page = ProductPage(browser, test_link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


@pytest.mark.skip
@pytest.mark.parametrize("test_link", ProductTestLink.TEST_LINK)
def test_guest_cant_see_success_message(browser, test_link):
    page = ProductPage(browser, test_link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip
@pytest.mark.xfail
@pytest.mark.parametrize("test_link", ProductTestLink.TEST_LINK)
def test_message_disappeared_after_adding_product_to_basket(browser, test_link):
    page = ProductPage(browser, test_link)
    page.open()
    page.add_to_basket()
    page.should_be_a_disappearing_message()


@pytest.mark.parametrize("test_link", ProductTestLink.TEST_LINK)
def test_guest_should_see_login_link_on_product_page(browser, test_link):
    page = ProductPage(browser, test_link)
    page.open()
    page.should_be_login_link()


@pytest.mark.parametrize("test_link", ProductTestLink.TEST_LINK)
def test_guest_can_go_to_login_page_from_product_page(browser, test_link):
    page = ProductPage(browser, test_link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()


@pytest.mark.parametrize("test_link", ProductTestLink.TEST_LINK)
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, test_link):
    page = ProductPage(browser, test_link)
    page.open()
    page.go_to_view_basket()