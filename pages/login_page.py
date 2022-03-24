from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Должен быть url логина"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.Login_Form), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.Registration_Form), "Registration form is not presented"
        assert True

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.registration_email)
        email_field.send_keys(email)
        password_field1 = self.browser.find_element(*LoginPageLocators.registration_password_1)
        password_field1.send_keys(password)
        password_field2 = self.browser.find_element(*LoginPageLocators.registration_password_2)
        password_field2.send_keys(password)
        button_submit = self.browser.find_element(*LoginPageLocators.registration_button)
        button_submit.click()



