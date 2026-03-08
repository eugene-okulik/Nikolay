from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_text():
    driver = webdriver.Chrome()
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    driver.maximize_window()
    input_data = 'Python'
    choose = driver.find_element(By.ID, 'id_choose_language')
    choose.click()
    choose.send_keys(Keys.ARROW_DOWN)
    choose.click()
    submit = driver.find_element(By.ID, 'submit-id-submit')
    submit.click()
    result = driver.find_element(By.ID, 'result-text')
    assert result.text == input_data
