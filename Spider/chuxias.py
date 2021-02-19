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

USERNAME = '${{ secrets.USERNAME }}'  # 账号
PASSWORD = '${{ secrets.PASSWORD }}'  # 密码
login_url = 'https://www.chuxias.com/'  # 登录URL
checkin_url = 'https://acgdonghua.com/task'  # 签到URL

driver.get(login_url)  # 进入登录页面
driver.find_element_by_xpath('//*[@id="inn-sign__login-btn__container"]/a').click()  # 使用社区账号登录
def hover(self,by,value):
      element = self.findElement(by,value)
      ActionChains(self.driver).move_to_element(element).perform()
time.sleep(2)  # 延时加载
driver.find_element_by_xpath('//*[@id="inn-sign__dialog__fm"]/div/div/div/div[2]/label/span[2]/input').send_keys(USERNAME)# 填充用户名和密码
time.sleep(1) 
driver.find_element_by_xpath('//*[@id="inn-sign__dialog__fm"]/div/div/div/div[3]/label/span[2]/input').send_keys(PASSWORD)
time.sleep(1) 
driver.find_element_by_xpath('//*[@id="inn-sign__dialog__fm"]/footer/button').click()  # 登录
time.sleep(3)
#driver.get(checkin_url)
#time.sleep(1)
driver.find_element_by_xpath('//*[@id="inn-nav__point-sign-daily"]/a').click()
time.sleep(1)
driver.quit()
