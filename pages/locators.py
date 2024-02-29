from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main > h1")
    MESSAGE_BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BTN_BASKET = (By.CSS_SELECTOR, "span > a")
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner")
    BASKET_IS_EMPTY_TEXT = (By.CSS_SELECTOR, "#promotions")


class RegistrationFormPageLocators():
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FIELD_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_FIELD_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, "#register_form > button")




