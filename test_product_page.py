import pytest
from pages.product_page import ProductPage
from pages.base_page import BasePage
from pages.test_link import ProductTestLink


@pytest.mark.parametrize("test_link", ProductTestLink.TEST_LINK)
def test_guest_can_add_product_to_basket(browser, test_link):
    page = ProductPage(browser, test_link)
    page.open()
    page.add_to_basket()

