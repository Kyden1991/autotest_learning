from .base_page import BasePage
from .locators import MainPageLocators
from .locators import BasePageLocators
from .login_page import LoginPage

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
        #return LoginPage(browser=self.browser, url=self.browser.current_url) #реализовал другой метод(этот не срабатывал)
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"











