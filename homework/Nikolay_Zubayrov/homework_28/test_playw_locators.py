from playwright.sync_api import Page


def test_by_role(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    page.get_by_role('link', name='Form Authentication').click()
    username = page.get_by_role('textbox', name='Username')
    username.click()
    username.fill('tester')
    password = page.get_by_role('textbox', name='Password')
    password.click()
    password.fill('tester')
    button = page.get_by_role('button', name='Login')
    button.click()


def test_form(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')
    name = page.get_by_placeholder('First Name')
    name.click()
    name.fill('Nikolay')

    last = page.get_by_placeholder('Last Name')
    last.click()
    last.fill('Ivanov')

    email = page.get_by_placeholder('name@example.com')
    email.click()
    email.fill('test@mail.ru')

    check = page.locator('//*[@id="gender-radio-1"]')
    check.click()

    mobile = page.get_by_placeholder('Mobile Number')
    mobile.click()
    mobile.fill('78907776532')

    date = page.locator('//*[@id="dateOfBirthInput"]')
    date.click()
    date.press('Control+A')
    date.fill('16.12.1988')

    subject = page.locator('//*[@id="subjectsContainer"]/div/div[1]/div[2]')
    subject.click()
    subject.press('e')
    subject.press('ArrowDown')
    subject.press('Enter')

    hobbies = page.locator('//*[@id="hobbies-checkbox-3"]')
    hobbies.click()

    adress = page.get_by_placeholder('Current Address')
    adress.fill('tratata')

    state = page.locator('//*[@id="state"]/div/div[2]/div')
    state.click()
    state.press('Enter')

    city = page.locator('//*[@id="stateCity-wrapper"]/div[3]')
    city.click()
    city.press('ArrowDown')
    city.press('ArrowDown')
    city.press('Enter')

    button = page.get_by_text('Submit')
    button.click()
