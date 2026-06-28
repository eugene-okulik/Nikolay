import pytest
from playwright.sync_api import Page
from pages.cart_page import CartPage
from pages.category_desks_page import CategoryDesksPage
from pages.fun_9999_page import FunPage


@pytest.fixture
def cart_page(page: Page):
    return CartPage(page)


@pytest.fixture
def category_desks_page(page: Page):
    return CategoryDesksPage(page)


@pytest.fixture
def fun_9999_page(page: Page):
    return FunPage(page)
