import webbrowser

from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    Login_Form = (By.CSS_SELECTOR, "#login_form")
    Registration_Form = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    add_cart = (By.CSS_SELECTOR, '.btn-add-to-basket')
    #cart_link = webbrowser.get() надо придумать как хранить ссылку на страницу
    saccess_message = (By.CSS_SELECTOR, '#messages>div:nth-child(1)')
    saccess_price_message = (By.CSS_SELECTOR, '#messages>div:nth-child(2)')
    book_name = (By.CSS_SELECTOR, ".product_main h1")
    book_price = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    book_name_basket = (By.CSS_SELECTOR, "#messages>div:nth-child(1) strong")
    book_price_basket = (By.CSS_SELECTOR, "#messages>div:nth-child(3) strong")


