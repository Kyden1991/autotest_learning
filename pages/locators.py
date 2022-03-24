from selenium.webdriver.common.by import By


class MainPageLocators():
    pass #заглушка которая не работает =(

class LoginPageLocators():
    Login_Form = (By.CSS_SELECTOR, "#login_form")
    Registration_Form = (By.CSS_SELECTOR, "#register_form")
    registration_email = (By.NAME, "registration-email")
    registration_password_1 = (By.NAME, "registration-password1")
    registration_password_2 = (By.NAME, "registration-password2")
    registration_button = (By.NAME, "registration_submit")

class ProductPageLocators():
    add_cart = (By.CSS_SELECTOR, '.btn-add-to-basket')
    #cart_link = webbrowser.get() надо придумать как хранить ссылку на страницу
    saccess_message = (By.CSS_SELECTOR, '#messages>div:nth-child(1)')
    saccess_price_message = (By.CSS_SELECTOR, '#messages>div:nth-child(2)')
    book_name = (By.CSS_SELECTOR, ".product_main h1")
    book_price = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    book_name_basket = (By.CSS_SELECTOR, "#messages>div:nth-child(1) strong")
    book_price_basket = (By.CSS_SELECTOR, "#messages>div:nth-child(3) strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group .btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    items_list = (By.CSS_SELECTOR, "#basket_formset")



