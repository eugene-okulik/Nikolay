from playwright.sync_api import Page


class BasePage:
    base_url = 'http://testshop.qa-practice.com'
    page_url = None

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        if self.base_url:
            self.page.goto(f'{self.base_url}{self.page_url}')
        else:
            print('Not possible to open page without url')
