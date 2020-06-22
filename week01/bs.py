import requests
from bs4 import BeautifulSoup as bs

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
header = {'user-agent':user_agent}

myurl = 'https://movie.douban.com/top250'
response = requests.get(myurl,headers=header)
bs_info = bs(response.text, 'html.parser')

for tags in bs_info.find_all('div',attrs={'class':'hd'}):
    for atag in tags.find_all('a'):
        print(atag.get('href'))
        print(atag.find('span').text)