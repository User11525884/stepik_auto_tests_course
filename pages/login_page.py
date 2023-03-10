from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    """Class combines methods for login page"""
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        substring = 'login'
        assert substring in self.browser.current_url, "URL is not correct"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTER), "Registration form is not presented"

    def register_new_user(self, email, password):
        email_register = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTRATION_INPUT)
        email_register.send_keys(email)
        password_input1 = self.browser.find_element(*LoginPageLocators.PSW_REGISTRATION_INPUT1)
        password_input1.send_keys(password)
        password_input2 = self.browser.find_element(*LoginPageLocators.PSW_REGISTRATION_INPUT2)
        password_input2.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
