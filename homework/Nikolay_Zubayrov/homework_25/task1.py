from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://www.qa-practice.com/elements/input/simple')
driver.maximize_window()

element = driver.find_element(By.NAME, 'text_string')
element.send_keys('tester')
element.submit()

new_element = driver.find_element(By.ID, 'result-text')
print(f'Введенное слово: {new_element.text}')
