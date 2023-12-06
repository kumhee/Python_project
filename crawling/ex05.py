from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys #key를 입력할때 사용하는 함수
import time

url = 'https://www.naver.com'
browser = webdriver.Chrome()
browser.get(url)
time.sleep(1)

login = browser.find_element(By.CLASS_NAME, 'MyView-module__link_login___HpHMW')
login.click()
time.sleep(1)

id = browser.find_element(By.ID, 'id')
id.send_keys('eu_un2')
time.sleep(1)

pw = browser.find_element(By.ID, 'pw')
pw.send_keys(1234)
time.sleep(1)

loginbtn = browser.find_element(By.ID, 'log.login')
loginbtn.click()
time.sleep(10)