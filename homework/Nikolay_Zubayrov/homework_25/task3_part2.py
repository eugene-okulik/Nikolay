from selenium import webdriver
from selenium.webdriver.common.by import By


def test_element():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    driver.maximize_window()
    start = driver.find_element(By.XPATH, '//*[@id="start"]/button')
    start.click()

    element = driver.find_element(By.XPATH, '//*[@id="finish"]/h4')
    assert element.is_displayed()
