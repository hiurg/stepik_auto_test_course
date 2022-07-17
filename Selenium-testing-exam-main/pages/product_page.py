from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
        self.solve_quiz_and_get_code()

    def should_be_equal_product_price_and_basket_total(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == \
            self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text, \
                "Product price and basket total doesn't match after product added to basket"
    
    def should_be_correct_added_product(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text == \
            self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_TITLE).text, \
                "Added product does not match product on page"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is present, but should not be"

    def should_dissapear_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message should've dissapeared, but it didn't"

