from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup

import time

url = 'https://land.naver.com/'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)
time.sleep(1)

search = browser.find_element(By.ID, 'queryInputHeader')
search.send_keys('청라 자이')
time.sleep(1)

search_btn = browser.find_element(By.CLASS_NAME, 'search_button')
search_btn.click()
time.sleep(5)

url = ""

print('-' * 12)