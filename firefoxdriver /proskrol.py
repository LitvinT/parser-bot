import datetime
import time

import self as self
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('https://ultramining.com/crypto-calc/bitcoin/')
etem = driver.find_element(By.CLASS_NAME, 'b-equipment__box')
etem.screenshot('image.png')
time.sleep(10)


