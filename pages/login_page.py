from pages.base_page import BasePage
from pages.locators import LoginPageLocators
from pages.locators import RegistrationFormPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "/login/" in self.url, "login is absent in current url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        email_gener = self.browser.find_element(*RegistrationFormPageLocators.EMAIL_FIELD)
        email_gener.send_keys(email)
        password_1 = self.browser.find_element(*RegistrationFormPageLocators.PASSWORD_FIELD_1)
        password_1.send_keys("afadfadfad")
        password_2 = self.browser.find_element(*RegistrationFormPageLocators.PASSWORD_FIELD_2)
        password_2.send_keys("afadfadfad")
        registration_submit = self.browser.find_element(*RegistrationFormPageLocators.REGISTRATION_SUBMIT)
        registration_submit.click()


