from pages.cart_page import CartPage


def test_that_the_text_is_displayed(cart_page: CartPage):
    cart_page.open_page()
    cart_page.checking_that_the_specified_text_is_displayed_in_an_empty_basket('Your cart is empty!')


def test_search(cart_page: CartPage):
    cart_page.open_page()
    cart_page.find_the_input_field_and_enter_the_desired_product_there()
    cart_page.check_that_the_specified_product_was_found('Desk Combination')


def test_logo_returns_to_the_home_page_when_clicked(cart_page: CartPage):
    cart_page.open_page()
    cart_page.checking_the_click_on_the_logo_and_returning_to_the_main_page()
