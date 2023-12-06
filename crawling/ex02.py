import requests
from bs4 import BeautifulSoup

seq = 0

def fn_soup(text):
    soup = BeautifulSoup(text, 'lxml')
    items = soup.find_all('div', attrs={'class' : 'box__item-container'})

    # print(len(items))
    seq = 0
    
    for i, item in  enumerate(items) :
        
        name = item.find('span', attrs={'class' : 'text__item'})['title']
        price = item.find('strong', attrs={'class' : 'text text__value'}).get_text()
        rate = item.find('span', attrs={'class' : 'image__awards-points'})
        
        if rate :
            rate = rate['style']
            index = rate.find(':') + 1
            rate = rate[index : -1]
        else :
            #rate='평점없음'
            continue
            
        count = item.find('li', attrs={'class' : 'list-item list-item__feedback-count'})
        if count :
            count = count.find('span', attrs={'class' : 'text'}).get_text()
            count = count.replace('(','').replace(')','').replace(',','')
        else :
            #count = '상품평 없음'
            continue
        
        #image = 'https:' + item.find('img')['src']
        
        if int(rate) >= 90 and int(count) >= 300 :
            seq = seq + 1
            print(f'{seq} : {name} : {price} : 평점 : {rate} : 피드백수 : {count}')
            
for i in range(1,6):
    print(i, '-' * 100)
    url='https://browse.gmarket.co.kr/search?keyword={}&k=41&p={}'.format('키보드' , i)
    res = requests.get(url)
    res.raise_for_status()
    fn_soup(res.text)