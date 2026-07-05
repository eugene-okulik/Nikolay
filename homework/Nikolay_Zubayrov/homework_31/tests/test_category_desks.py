from pages.category_desks_page import CategoryDesksPage


def test_url_page(category_desks_page: CategoryDesksPage):
    category_desks_page.open_page()
    category_desks_page.checking_the_page_url('http://testshop.qa-practice.com/shop/category/desks-1')


def test_adding_a_product_to_a_cart(category_desks_page: CategoryDesksPage):
    category_desks_page.open_page()
    category_desks_page.add_the_product_to_the_cart()
    category_desks_page.checking_that_the_product_has_been_added_to_the_cart()


def test_removing_an_item_from_the_cart(category_desks_page: CategoryDesksPage):
    category_desks_page.open_page()
    category_desks_page.add_the_product_to_the_cart()
    category_desks_page.removing_an_item_from_the_cart()
