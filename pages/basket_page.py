from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    """Class combines methods for basket page"""
    def should_be_not_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), \
        "Item is presented in basket, but should not be"

    def should_be_text_stating_that_basket_is_empty(self):
        """Ожидаем, что есть текст о том что корзина пуста"""
        assert self.is_element_present(*BasketPageLocators.BASKET_TEXT), "Basket is not empty"