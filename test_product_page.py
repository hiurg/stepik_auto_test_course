from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import pytest
import time

# necessary links
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
login_link = "http://selenium1py.pythonanywhere.com/accounts/login/"
# add "promo=offer to links and mark offer 7 with xfail"
urls = [f"{link}?promo=offer{i}" \
    if i != 7 else pytest.param(f"{link}?promo=offer{i}", marks=pytest.mark.xfail) \
         for i in range(10)]


@pytest.mark.login_guest
class TestLoginFromProductPage:
    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(autouse=True, scope='function')
    def setup(self, browser):
        login_page = LoginPage(browser, login_link)
        login_page.open()
        login_page.register_new_user(str(time.time()) + "@fake.com")

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link, 0)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_be_equal_product_price_and_basket_total()
        page.should_be_correct_added_product()


@pytest.mark.need_review
@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_equal_product_price_and_basket_total()
    page.should_be_correct_added_product()

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link, 0)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link, 0)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link, 0)
    page.open()
    page.add_product_to_basket()
    page.should_dissapear_message()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
