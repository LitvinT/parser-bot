from selenium import webdriver
import time

url = "https://ultramining.com/crypto-calc/bitcoin/"
driver = webdriver.Firefox(executable_path="/Users/tima/Downloads/parser/firefoxdriver /geckodriver-v0.33.0-macos.tar")


try:
    driver.get(url=url)
    driver.execute_script("window.scrollTo(0, 150)")
    driver.get_screenshot_as_file("2.png")
    driver.refresh()
    time.sleep(10)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()



