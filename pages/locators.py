from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GO_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "div#content_inner>p")
    BASKET_ITEMS_BLOCK = (By.CSS_SELECTOR, "div.basket-items")


class MainPageLocators:
    LOGIN_LINK = (By.ID, "login_link")


class LoginPageLocators:
    LOGIN_USERNAME = (By.ID, "id_login-username")
    LOGIN_PASSWORD = (By.ID, "id_login-password")

    REGISTER_USERNAME = (By.ID, "id_registration-email")
    REGISTER_PASSWORD = (By.ID, "id_registration-password1")
    REGISTER_PASSWORD_REPEAT = (By.ID, "id_registration-password2")
    REGISTER_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div#messages div:nth-child(1)")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "div.product_main h1")
    ADDED_PRODUCT_TITLE = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    BASKET_TOTAL = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")
