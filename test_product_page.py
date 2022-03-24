from .pages.product_page import ProductPage
import pytest


def test_guest_can_add_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.AlertAnswer()


def test_should_be_message_to_add_to_cart(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.AlertAnswer()
    page.should_be_message_to_add_to_cart()

@pytest.mark.xfail(reason="not disappiring")
def test_should_not_be_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.AlertAnswer()
    page.should_not_be_success_message()


def test_should_be_message_about_price_cart(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.AlertAnswer()
    page.should_be_message_about_price_cart()

@pytest.mark.parametrize('url', ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
def test_product_name_valid(browser, url):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{url}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.AlertAnswer()
    page.product_name_valid()


def test_product_price_valid(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.AlertAnswer()
    page.product_price_valid()

















