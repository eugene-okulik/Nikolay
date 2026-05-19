from playwright.sync_api import Page, expect, Dialog


def test_visible_word(page: Page):
    def ok_alert(alert: Dialog):
        alert.accept()

    page.on('dialog', ok_alert)
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.get_by_role('link', name='Click').click()
    word = page.locator('#result')
    expect(word).to_contain_text('Ok')

