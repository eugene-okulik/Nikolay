from playwright.sync_api import expect
from pages.base_page import BasePage


class FunPage(BasePage):
    page_url = '/shop/furn-9999-office-design-software-7?category=9'

    def enter_cyrillic_text_in_the_search_bar(self):
        input_field = self.page.get_by_placeholder('Search...').nth(1)
        input_field.click()
        input_field.fill('деск')

    def checking_the_input_result_in_cyrillic(self, text):
        self.page.wait_for_load_state('domcontentloaded')
        self.page.locator('.btn-light').nth(0).click()
        element = self.page.get_by_text('No results').first
        expect(element).to_be_visible()
        expect(element).to_have_text(text)

    def entering_a_negative_quantity(self):
        input_field = self.page.locator('[data-min="1"]')
        input_field.click()
        input_field.fill('-1')
        self.page.locator('#add_to_cart').click()

    def check_for_negative_item_quantities_in_the_cart(self, text):
        self.page.locator('.o_wsale_my_cart  ').first.click()

        element = self.page.get_by_text('Your cart is empty!')
        expect(element).to_have_text(text)

    def input_of_an_extremely_large_quantity(self):
        input_field = self.page.locator('[data-min="1"]')
        input_field.click()
        input_field.fill('123456')
        self.page.locator('#add_to_cart').click()

        self.page.wait_for_selector(':has-text("123456")', state='visible', timeout=10000)

    def checking_for_an_excessively_large_quantity_in_the_cart(self):
        self.page.locator('//*[@id="o_main_nav"]/ul[2]/li[2]/a').click()
        element = self.page.get_by_text('123456').first
        expect(element).to_be_visible()
