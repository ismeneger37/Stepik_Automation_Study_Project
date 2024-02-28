from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_goods_in_basket(self):
        assert not self.is_not_element_present(*BasketPageLocators.BASKET_IS_EMPTY), \
            "Success message basket is empty, but should not be"

    def should_be_message_basket_is_empty(self):
        message_basket_empty = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY_TEXT).text
        assert message_basket_empty in "Ваша корзина пуста", "No product in basket"


