from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

s = Service(executable_path='chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)

try:

    driver.maximize_window()
    driver.get('http://127.0.0.1:8000')
    time.sleep(2)

    #ЗАПИСЬ НЕСКОЛЬКИХ РЕЦЕПТОВ. Если убрать цикл, то создается один рецепт и идет поиск в ALL RECIPIES


    name = 'ПОСЛЕДНИЙ ТЕСТ'
    opisanie = 'ПОСЛЕДНИЙ ТЕСТ'

    create = driver.find_element(By.ID,'create').click()

    time.sleep(2)

    driver.find_element(By.ID, 'knopka').send_keys(Keys.PAGE_DOWN)

    time.sleep(2)

    title = driver.find_element(By.NAME, 'title').send_keys(name)
    describe = driver.find_element(By.NAME, 'describe').send_keys(opisanie)

    time.sleep(2)

    image = driver.find_element(By.NAME, 'image').send_keys('z')

    time.sleep(2)

    submit = driver.find_element(By.CLASS_NAME, 'add_btn').click()

    time.sleep(2)

    all_rec = driver.find_element(By.ID, 'all_rec').click()

    time.sleep(2)

    driver.find_element(By.LINK_TEXT, name).send_keys(Keys.END)

    time.sleep(2)

    recipe = driver.find_element(By.LINK_TEXT, name).click()

    time.sleep(2)

    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)

    time.sleep(10)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()