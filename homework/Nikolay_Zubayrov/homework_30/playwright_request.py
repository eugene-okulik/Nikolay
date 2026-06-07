from playwright.sync_api import Page, expect, Route


def test_header_and_query_replacement(page: Page):
    def change_response(route: Route):
        print(f'Перехвачен: {route.request.url}')
        response = route.fetch()

        # Получаем текст ответа
        text = response.text()

        # Неразрывный пробел в HTML/JSON выглядит как \u00a0
        # Заменяем оба варианта
        text = text.replace('iPhone\u00a017\u00a0Pro', 'яблокофон 17 про')  # неразрывные пробелы
        text = text.replace('iPhone 17 Pro', 'яблокофон 17 про')  # обычные пробелы

        route.fulfill(
            status=response.status,
            headers=dict(response.headers),
            body=text
        )

    # Перехватываем запрос
    page.route('**/digital-mat?path=library/step0_iphone/digitalmat&fae=true', change_response)

    page.goto('https://www.apple.com/shop/buy-iphone')
    page.wait_for_load_state('networkidle')

    page.locator('#shelf-1_section h3:has-text("iPhone 17 Pro")').click()
    page.wait_for_timeout(2000)

    popup_title = page.locator('#rf-digitalmat-overlay-label-0').first
    actual_text = popup_title.inner_text()
    print(f"Заголовок в попапе: '{actual_text}'")

    expect(popup_title).to_have_text('яблокофон 17 про')
