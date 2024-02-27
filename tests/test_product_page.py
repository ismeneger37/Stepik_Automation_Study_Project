import time
from pages.product_page import ProductPage
import pytest


@pytest.mark.parametrize('links', [0, 1, 2, 3, 4, 5, 6,
                                  pytest.param(7, marks=pytest.mark.xfail),
                                  8, 9])
def test_guest_can_add_product_to_basket(browser, links):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{links}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart_button()
    page.solve_quiz_and_get_code()
    time.sleep(3)
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()



