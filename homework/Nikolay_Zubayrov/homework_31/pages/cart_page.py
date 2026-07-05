from playwright.sync_api import expect
from pages.base_page import BasePage


class CartPage(BasePage):
    page_url = '/shop/cart'

    def checking_that_the_specified_text_is_displayed_in_an_empty_basket(self, text):
        element = self.page.get_by_text('Your cart is empty!')
        expect(element).to_be_visible()
        expect(element).to_have_text(text)

    def find_the_input_field_and_enter_the_desired_product_there(self):
        self.page.locator('.o_not_editable').first.click()
        self.page.locator('[data-limit="5"]').first.fill('desk')
        self.page.locator('//*[@id="o_search_modal"]/div/div/form/div[2]/a[4]/div/div[1]').click()

    def check_that_the_specified_product_was_found(self, text):
        element = self.page.get_by_role('heading', name='Desk Combination')
        expect(element).to_be_visible()
        expect(element).to_have_text(text)

    def checking_the_click_on_the_logo_and_returning_to_the_main_page(self):
        self.page.locator('[data-name="Navbar Logo"]').first.click()
        expect(self.page).to_have_url('http://testshop.qa-practice.com/')
