import requests
from bs4 import BeautifulSoup as bs

def get_url_name(myurl):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
    header = {'user-agent':user_agent}
    response = requests.get(myurl,headers=header)
    bs_info = bs(response.text,'html.parser')

    for tags in bs_info.find_all('div',attrs={'class':'hd'}):
        for atag in tags.find_all('a'):
            print(atag.get('href'))
            print(atag.find('span').text)

urls = tuple(f'https://movie.douban.com/top250?start={ page *25}&filter=' for page in range(10))

print(urls)

from time import sleep

for page in urls:
    get_url_name(page)
    sleep(5)