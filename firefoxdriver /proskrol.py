import datetime
import time

import self as self
from selenium import webdriver
from selenium.webdriver.common import by

driver = webdriver.Firefox()
driver.get('https://ultramining.com/crypto-calc/bitcoin/')

now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
name_screenshot = 'screenshot' + now_date + '.png'
driver.execute_script("window.scrollTo(0, 150)")
driver.save_screenshot(name_screenshot)
time.sleep(10)


