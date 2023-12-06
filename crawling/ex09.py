import requests
from bs4 import BeautifulSoup
import time

url ="https://search.naver.com/search.naver?ie=UTF-8&sm=whl_nht&query=%EC%98%A4%EB%8A%98%EC%9D%98+%EB%82%A0%EC%94%A8"
res = requests.get(url)
res.raise_for_status()
# print(res.text)

soup = BeautifulSoup(res.text, 'lxml')

# 어제 날씨 비교
summary = soup.find('p', attrs={'class' : 'summary'}).get_text()

# 현재 온도
temp_text = soup.find('div', attrs={ 'class' : 'temperature_text' })
cur_temp = temp_text.strong.contents[1]
cur_temp +=temp_text.find('span', attrs={'class' : 'celsius'}).get_text()

# 체감, 습도, 동풍
sum_list = soup.find_all('dd', attrs={'class' : 'desc'})

# 강수확률
cell_weather = soup.find('div', attrs={'class' : 'cell_weather'}).find_all('span', attrs={'class' : 'rainfall'})

# 미세먼지
item_today= soup.find('li', attrs={'class' : 'item_today level1'}).find_all('span', attrs={'class' : 'txt'})

print('[오늘의 날씨]')
print('-' * 50)
print(summary)
print(f'현재 : {cur_temp} , 체감 :  {sum_list[0].get_text()} , 습도 : {sum_list[1].get_text()}')
print(f'오전 강수확률 : {cell_weather[0].get_text()}')
print(f'오후 강수확률 : {cell_weather[1].get_text()}')
print(f'미세먼지 : {item_today[0].get_text()}')
print(f'초미세먼지 : {item_today[0].get_text()}')
print('-' * 50)