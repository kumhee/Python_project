from selenium import webdriver
from bs4 import BeautifulSoup

import time

def fn_soup(res):
    soup = BeautifulSoup(res, "lxml")
    images = soup.find_all('div', attrs={'class':'isv-r PNCib ViTmJb BUooTd'})
    for idx, image in enumerate(images):
        title=image.find('div', attrs={'class': 'zbRPDe M2qv4b P4HtKe'}).get_text()
        print(idx + 1, title)
        
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')

browser = webdriver.Chrome(options=options)
browser.maximize_window()
url='https://www.google.com/search?q=%EC%86%A1%EA%B0%95&sca_esv=587611622&hl=ko&tbm=isch&source=lnms&sa=X&ved=2ahUKEwjA19OnrfWCAxVUsVYBHUTzD-QQ_AUoAXoECAEQAw&biw=1278&bih=923&dpr=1'
browser.get(url)

# 이전 스크롤높이
prev_height = browser.execute_script('return document.body.scrollHeight')
print('이전 높이 ' , prev_height)

while True :
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(3)
    curr_height = browser.execute_script('return document.body.scrollHeight')
    if prev_height == curr_height : # 현재 위치와 이전 위치가 같을 때까지 반복하면서 아래로 스크롤
        break
    prev_height = curr_height

res = browser.page_source
fn_soup(res)
time.sleep(1)