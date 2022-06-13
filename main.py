from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

options = webdriver.ChromeOptions()
binary_yandex_driver_file = 'yandexdriver.exe'
driver = webdriver.Chrome(binary_yandex_driver_file, options=options)
driver.get('https://yandex.ru')
driver.quit()
