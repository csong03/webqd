from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chromedriver = "/usr/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=chromedriver)

username = ${{secrets.USERNAME}}  # 账号
password = ${{secrets.PASSWORD}}  # 密码
login_url = 'https://hacpai.com/login?goto=https%3A%2F%2Fhacpai.com%2F'  # 登录URL
checkin_url = 'https://hacpai.com/activity/checkin'  # 签到URL

driver.get(login_url)  # 进入登录页面

try:
    driver.find_element_by_xpath(
        "//*[@id='verifyHacpaiIcon' and @class='fn__flex verify__via icon-hacpai']").click()  # 使用社区账号登录
    time.sleep(1)  # 延时加载
    driver.find_element_by_id('nameOrEmail').send_keys(username)  # 填充用户名和密码
    driver.find_element_by_id('loginPassword').send_keys(password)
    driver.find_element_by_id('loginBtn').click()  # 登录
    time.sleep(1.5)
    driver.get(checkin_url)
    try:  # 未签到
        driver.find_element_by_xpath("//*[@class='btn green']").click()  # 签到
        print("签到成功")
    except NoSuchElementException:
        print("已签到")
except Exception as e:
    print(e)
    print("签到失败")

driver.quit()
