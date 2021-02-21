from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chromedriver = "/usr/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=chromedriver)

WYYNAME = '${{ secrets.WYYNAME }}'  # 账号
WYYPSW = '${{ secrets.WYYPSW }}'  # 密码

driver.get('https://api.wanpeng.life/')
sleep(2)
driver.find_element_by_xpath('//*[@id="uin"]').send_keys(WYYNAME)
driver.find_element_by_xpath('//*[@id="pwd"]').send_keys(WYYPSW)
sleep(1)
driver.find_element_by_xpath('//*[@id="submit"]').click()
sleep(1)
driver.find_element_by_xpath('//*[@id="sign"]').click()
driver.find_element_by_xpath('//*[@id="daka"]').click()
sleep(2)
driver.quit()
