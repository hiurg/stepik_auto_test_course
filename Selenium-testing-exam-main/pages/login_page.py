from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email="abracadabra@new.com", password="1234445abcA55661"):
        self.browser.find_element(*LoginPageLocators.REGISTER_USERNAME).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_REPEAT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT_BUTTON).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login page url is incorrect!"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME) and \
            self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), \
                "Login form is absent on login page"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_USERNAME) and \
            self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD) and \
                self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_REPEAT), \
                    "Register form is absent on login page"
