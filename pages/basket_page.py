from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def guest_cant_see_product_in_basket_opened_from_main_page(self):
        assert self.is_not_element_present(*BasketPageLocators.items_list), "Items in basket"

