from .base_page import BasePage
from .locators import ProductPageLocators



class ProductPage(BasePage):


    def add_to_basket(self):
        cart_button = self.browser.find_element(*ProductPageLocators.add_cart)
        cart_button.click()

    def AlertAnswer(self):
        self.solve_quiz_and_get_code()

    def should_be_message_to_add_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.saccess_message), "must be a message about add to cart"

    def should_be_message_about_price_cart(self):
        assert self.is_element_present(*ProductPageLocators.saccess_message), "must be a message about product price"

    def product_name_valid(self):
        book_name = self.browser.find_element(*ProductPageLocators.book_name).text
        book_name_basket = self.browser.find_element(*ProductPageLocators.book_name_basket).text
        assert book_name == book_name_basket, "Name is not same"

    def product_price_valid(self):
        book_price = self.browser.find_element(*ProductPageLocators.book_price).text
        book_price_basket = self.browser.find_element(*ProductPageLocators.book_price_basket).text
        assert book_price == book_price_basket, "Price is not same"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.saccess_message), "Success message is presented, but should not be"





