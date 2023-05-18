import datetime

from selenium import webdriver
import time
from selenium.webdriver import ActionChains

url = "https://ultramining.com/crypto-calc/bitcoin/"
driver = webdriver.Firefox(executable_path="/Users/tima/Downloads/parser/firefoxdriver /geckodriver-v0.33.0-macos.tar")


try:
    driver.get(url=url)
    now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
    name_screenshot = 'screenshot' + now_date + '.png'
    driver.execute_script("window.scrollTo(0, 150)")
    driver.save_screenshot(name_screenshot)
    time.sleep(10)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()


# action = ActionChains(driver)
# all = driver.find_element("//div[@class='dataTables_scroll dtfc-has-left']")
# action.move_to_element(all).perform()



# driver.execute_script("window.scrollTo(0, 150)")
