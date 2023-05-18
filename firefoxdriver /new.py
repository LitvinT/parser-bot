import datetime

from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

url = "https://whattomine.com/asic?sha256f=true&factor%5Bsha256_hr%5D=140.0&factor%5Bsha256_p%5D=3010.0&factor%5Bscrypt_hash_rate%5D=9.5&factor%5Bscrypt_power%5D=3425.0&factor%5Bx11_hr%5D=1286.0&factor%5Bx11_p%5D=3148.0&factor%5Bsia_hr%5D=17.0&factor%5Bsia_p%5D=3300.0&factor%5Bqk_hr%5D=28.0&factor%5Bqk_p%5D=800.0&factor%5Bqb_hr%5D=28.0&factor%5Bqb_p%5D=850.0&factor%5Bmg_hr%5D=28.0&factor%5Bmg_p%5D=350.0&factor%5Bsk_hr%5D=14.0&factor%5Bsk_p%5D=300.0&factor%5Blbry_hr%5D=1620.0&factor%5Blbry_p%5D=1450.0&factor%5Bbk14_hr%5D=52.0&factor%5Bbk14_p%5D=2200.0&factor%5Bcn_hr%5D=360.0&factor%5Bcn_p%5D=720.0&factor%5Bcst_hr%5D=13.9&factor%5Bcst_p%5D=65.0&factor%5Beq_hr%5D=420.0&factor%5Beq_p%5D=1510.0&factor%5Blrev2_hr%5D=13.0&factor%5Blrev2_p%5D=1100.0&factor%5Bbcd_hr%5D=278.0&factor%5Bbcd_p%5D=708.0&factor%5Bl2z_hr%5D=93.0&factor%5Bl2z_p%5D=708.0&factor%5Bkec_hr%5D=34.9&factor%5Bkec_p%5D=708.0&factor%5Bgro_hr%5D=28.0&factor%5Bgro_p%5D=450.0&factor%5Besg_hr%5D=1050.0&factor%5Besg_p%5D=215.0&factor%5Bct31_hr%5D=126.0&factor%5Bct31_p%5D=2800.0&factor%5Bct32_hr%5D=36.0&factor%5Bct32_p%5D=2800.0&factor%5Bkd_hr%5D=40.2&factor%5Bkd_p%5D=3350.0&factor%5Bhk_hr%5D=4.3&factor%5Bhk_p%5D=3250.0&factor%5Brmx_hr%5D=17.5&factor%5Brmx_p%5D=150.0&factor%5Bcost%5D=0.1&factor%5Bcost_currency%5D=USD&sort=Profit24&volume=0&revenue=24h&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=binance&factor%5Bexchanges%5D%5B%5D=bitfinex&factor%5Bexchanges%5D%5B%5D=bitforex&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=coinex&factor%5Bexchanges%5D%5B%5D=exmo&factor%5Bexchanges%5D%5B%5D=gate&factor%5Bexchanges%5D%5B%5D=graviex&factor%5Bexchanges%5D%5B%5D=hitbtc&factor%5Bexchanges%5D%5B%5D=ogre&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=stex&dataset=Main&commit=Calculate"
driver = webdriver.Firefox(executable_path="/Users/tima/Downloads/parser/firefoxdriver /geckodriver-v0.33.0-macos.tar")


try:
    driver.get(url=url)
    now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
    name_screenshot = 'screenshot' + now_date + '.png'
    time.sleep(5)
    etem = driver.find_element(By.TAG_NAME, 'table')
    time.sleep(5)
    etem.screenshot(name_screenshot)
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()




# action = ActionChains(driver)
# all = driver.find_element("//div[@class='dataTables_scroll dtfc-has-left']")
# action.move_to_element(all).perform()



# driver.execute_script("window.scrollTo(0, 150)")
