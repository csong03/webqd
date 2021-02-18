from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chromedriver = "/usr/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=chromedriver)

NAME = '${{ secrets.NAME }}'  # 账号
PASSWORD = '${{ secrets.PASSWORD }}'  # 密码
login_url = 'https://xdlciyuan.com/'  # 登录URL
checkin_url = 'https://xdlciyuan.com/mission/today'  # 签到URL

driver.get(login_url)  # 进入登录页面
driver.find_element_by_xpath('//*[@id="page"]/div[1]/div/div[2]/div/div[2]/div[3]/div/div/div[1]/button[1]').click()  # 使用社区账号登录
time.sleep(2)  # 延时加载
driver.find_element_by_xpath('//*[@id="login-box"]/div/div/div/form/div[2]/label[2]/input').send_keys(NAME)# 填充用户名和密码
time.sleep(1) 
driver.find_element_by_xpath('//*[@id="login-box"]/div/div/div/form/div[2]/label[5]/input').send_keys(PASSWORD)
time.sleep(1) 
driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div/form/div[2]/div[3]/button').click()  # 登录
time.sleep(3)
driver.get(checkin_url)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[1]/div[2]/button').click()

driver.quit()
