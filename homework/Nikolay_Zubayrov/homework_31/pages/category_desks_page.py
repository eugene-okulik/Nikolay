from playwright.sync_api import expect
from pages.base_page import BasePage


class CategoryDesksPage(BasePage):
    page_url = '/shop/category/desks-1'

    def checking_the_page_url(self, url):
        expect(self.page).to_have_url(url)

    def add_the_product_to_the_cart(self):
        self.page.locator('.oe_product').first.click()
        self.page.get_by_role('button', name='Add to cart').click()
        self.page.get_by_text('Continue Shopping').click()

    def checking_that_the_product_has_been_added_to_the_cart(self):
        self.page.wait_for_load_state('domcontentloaded')
        self.page.get_by_role('link', name='Cart').click()
        element = self.page.get_by_text('Customizable Desk (Steel, White)')
        expect(element).to_be_visible()

    def removing_an_item_from_the_cart(self):
        self.page.get_by_role('link', name='Cart').click()
        self.page.get_by_title('Remove one').click()
        element = self.page.get_by_text('Your cart is empty!')
        expect(element).to_have_text('Your cart is empty!')
