from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart_button(self):
        btn_add_to_bascket = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn_add_to_bascket.click()

    def should_be_message_about_adding(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), "Message about adding is not presented"

        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_book_title = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text

        assert product_name == message_book_title, "No product name in the message"

    def should_be_message_basket_total(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL_PRICE), "Message basket total is not presented"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE),  "Product price is not presented"

        message_basket_total = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL_PRICE).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

        assert product_price == message_basket_total, "No product price in the message"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), \
            "Success message is presented, but should not be"

    def should_be_message_of_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ABOUT_ADDING), \
            "Success message is not disappeared"




