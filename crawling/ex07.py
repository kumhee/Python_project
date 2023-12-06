import requests
from bs4 import BeautifulSoup

url='https://www.google.com/search?q=%EC%86%A1%EA%B0%95&sca_esv=587611622&hl=ko&tbm=isch&source=lnms&sa=X&ved=2ahUKEwjA19OnrfWCAxVUsVYBHUTzD-QQ_AUoAXoECAEQAw&biw=1278&bih=923&dpr=1'
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
res = requests.get(url, headers=header)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
images = soup.find_all('div', attrs={'class':'isv-r PNCib ViTmJb BUooTd'})
for idx, image in enumerate(images):
    title=image.find('div', attrs={'class': 'zbRPDe M2qv4b P4HtKe'}).get_text()
    print(idx + 1, title)