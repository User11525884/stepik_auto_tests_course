from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    """Class combines methods for product page"""
    def should_be_product_page(self):
        self.should_be_button_add_to_basket()
        self.add_to_product_basket()
        self.coincidence_of_names()
        self.prices_are_equal()

    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), "Button add to basket is not presented"    	
    
    def add_to_product_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)  
        button.click()
        #  if "promo=offer" in self.browser.current_url:
        self.solve_quiz_and_get_code()

    def coincidence_of_names(self):
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        assert self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_BASKET).text == name_product, \
        f"In basket not product with name - {name_product}"
        
    def prices_are_equal(self):
        price_product = float(self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text.split("&")[0][1:])
        assert float(self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_BASKET).text.split("&")[0][1:]) == price_product, \
        f"In basket other price {str(price_product)}"

    def should_be_message_disappeared_after_adding_product_to_basket(self):
        self.add_to_product_basket()
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is not disappeared"

    def should_not_be_success_message_after_adding_product_to_basket(self):
        self.add_to_product_basket()
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    def should_be_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is not presented"
