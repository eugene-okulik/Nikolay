from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://demoqa.com/automation-practice-form')
driver.maximize_window()

first_name = driver.find_element(By.ID, 'firstName')
first_name.send_keys('Nikolay')

last_name = driver.find_element(By.ID, 'lastName')
last_name.send_keys('Nikolaev')

email = driver.find_element(By.ID, 'userEmail')
email.send_keys('test@mail.ru')

gender = driver.find_element(By.ID, 'gender-radio-1')
gender.click()

mobile = driver.find_element(By.ID, 'userNumber')
mobile.send_keys('1234567890')

date_of_birth = driver.find_element(By.ID, 'dateOfBirthInput')
date_of_birth.click()
month = driver.find_element(By.CLASS_NAME, 'react-datepicker__month-select')
month.click()
month.send_keys(Keys.ARROW_DOWN * 2)
year = driver.find_element(By.CLASS_NAME, 'react-datepicker__year-select')
year.click()
year.send_keys(Keys.ARROW_UP * 3)
year.click()
day = driver.find_element(By.CLASS_NAME, 'react-datepicker')
day.click()

subject = driver.find_element(By.ID, 'subjectsInput')
subject.send_keys('r')
subject.send_keys(Keys.ARROW_DOWN * 2)
subject.send_keys(Keys.ENTER)

hobbies = driver.find_element(By.ID, 'hobbies-checkbox-1')
hobbies.click()
hobbies = driver.find_element(By.ID, 'hobbies-checkbox-3')
hobbies.click()

current_adress = driver.find_element(By.ID, 'currentAddress')
current_adress.send_keys('USSR')

state = driver.find_element(By.ID, 'react-select-3-input')
state.click()
state.send_keys(Keys.ARROW_DOWN * 2)
state.send_keys(Keys.ENTER)

city = driver.find_element(By.ID, 'react-select-4-input')
city.click()
city.send_keys(Keys.ARROW_DOWN * 1)
city.send_keys(Keys.ENTER)

button_submit = driver.find_element(By.ID, 'submit')
button_submit.click()

element = driver.find_element(By.CLASS_NAME, 'modal-content')
print(element.text)
