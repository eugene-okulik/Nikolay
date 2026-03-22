from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as conditions
import pytest



@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


def test_basket(driver):
    driver.get('http://testshop.qa-practice.com/')
    driver.switch_to.new_window('tab')
    driver.get('http://testshop.qa-practice.com/shop/customizable-desk-9#attr=1,3')
    all_pages = driver.window_handles
    driver.find_element(By.ID, 'add_to_cart').click()
    wait = WebDriverWait(driver, 10)
    wait.until(conditions.visibility_of_element_located((By.CLASS_NAME, 'modal-title')))
    driver.find_element(By.CLASS_NAME, 'btn-secondary').click()
    driver.close()
    driver.switch_to.window(all_pages[0])
    driver.find_element(By.XPATH, '//*[@id="o_main_nav"]/ul[2]/li[2]/a').click()
    assert driver.find_element(By.CLASS_NAME, 'd-inline').text == 'Customizable Desk (Steel, White)'


def test_product(driver):
    driver.get('http://testshop.qa-practice.com/')
    driver.implicitly_wait(6)

    desk = driver.find_element(By.CLASS_NAME, 'img-fluid')
    popup = driver.find_element(By.CLASS_NAME, 'a-submit')
    actions = ActionChains(driver)
    actions.move_to_element(desk)
    actions.click(popup)
    actions.perform()
    new_page = driver.find_element(By.CLASS_NAME, 'product_display_name')
    assert new_page.text == '[FURN_0096] Customizable Desk (Steel, White)'

