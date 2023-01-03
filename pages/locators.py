from selenium.webdriver.common.by import By


class MainPageLocators():
    """The class combines locators main page"""
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") 

class BasePageLocators():
    """The class combines locators base page"""
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    """The class combines locators basket page"""
    BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_ITEM = (By.CSS_SELECTOR, "#basket_formset > div")

class LoginPageLocators():
    """The class combines locators login page"""
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form") 
    LOGIN_REGISTER = (By.CSS_SELECTOR, "#register_form")
    EMAIL_REGISTRATION_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    PSW_REGISTRATION_INPUT1 = (By.CSS_SELECTOR, "#id_registration-password1")
    PSW_REGISTRATION_INPUT2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")

class ProductPageLocators():
    """The class combines locators product page"""
    BEGINING_LINK = (By.CSS_SELECTOR, "#default > div.container-fluid.page > div > ul > li:nth-child(1) > a")
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    BUTTON_GO_TO_BASKET = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    NAME_PRODUCT_BASKET = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    PRICE_PRODUCT_BASKET = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")
