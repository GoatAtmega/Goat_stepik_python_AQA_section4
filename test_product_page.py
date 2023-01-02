import time
import pytest
from pages.product_page import ProductPage
from pages.base_page import BasePage
from pages.test_link import ProductTestLink
from pages.test_link import ProductBugTestLink


@pytest.mark.skip
@pytest.mark.xfail
@pytest.mark.parametrize("test_link", ProductBugTestLink.TEST_LINK)
def test_guest_can_add_product_to_basket(browser, test_link):
    page = ProductPage(browser, test_link)
    page.open()
    page.add_to_basket()


@pytest.mark.xfail
@pytest.mark.parametrize("test_link", ProductTestLink.TEST_LINK)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, test_link):
    page = ProductPage(browser, test_link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


@pytest.mark.parametrize("test_link", ProductTestLink.TEST_LINK)
def test_guest_cant_see_success_message(browser, test_link):
    page = ProductPage(browser, test_link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
@pytest.mark.parametrize("test_link", ProductTestLink.TEST_LINK)
def test_message_disappeared_after_adding_product_to_basket(browser, test_link):
    page = ProductPage(browser, test_link)
    page.open()
    page.add_to_basket()
    page.should_be_a_disappearing_message()

