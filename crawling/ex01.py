import requests
from bs4 import BeautifulSoup
import json
import streamlit as st

url = "http://www.cgv.co.kr/movies/?lt=1&ft=0"
res = requests.get(url)
res.raise_for_status()
#print(res.text)

soup = BeautifulSoup(res.text, 'lxml')
#title = soup.title.get_text()
#print(title)
#print(soup.a) #처음 발견되는 a element를 반환
#print(soup.a.attrs) #a element의 속성들 정보 출력
#print(soup.a['href']) #a element의 href 속성 '값' 정보 출력

chart = soup.find('div', attrs={'class':'sect-movie-chart'})
movies = chart.find_all('li')
print(len(movies))
print('-' * 50)

json_movies = []

for movie in movies:
    # 예약 사이트
    link = 'http://www.cgv.co.kr'
    link = link + movie.find('a', attrs={'class' : 'link-reservation'})['href']
    
    # 예매율
    percent = movie.find('strong', attrs={'class':'percent'})
    percent = percent.span.get_text()
    
    # 포스터
    image = movie.find('img')['src']
    
    # 영화순위
    rank = movie.find('strong', attrs={'class':'rank'}).get_text()
    
    # 영화제목
    title = movie.find('strong',attrs={'class':'title'}).get_text()
    
    # 결과 출력
    # print(rank + ' ' + title)
    # print(f'순위 : {rank}')
    # print(f'제목 : {title}')
    # print(f'포스터 : {image}')
    # print(f'예매율 : {percent}')
    # print(f'예약 : {link}')
    # print('-' * 50)
    
    json_movie = {'rank' : rank, 'title' : title, 'image' : image, 'percent' : percent, 'link' : link}
    json_movies.append(json_movie)
    
# with open('movie.json', 'w', encoding='utf-8') as file:
#     json.dump(json_movies, file, indent='\t', ensure_ascii=False)

# print(len(json_movies))

st.set_page_config(layout='wide')
st.header('CGV 무비차트')

idx = 0
for row in range(0, 5) :
    cols = st.columns(4)
    for col in cols:
        if idx > 18 :
            break
        else:
            movie = json_movies[idx]
            col.image(movie['image']) # 이미지 출력
            col.write(movie['title']) # 제목 출력
            idx += 1