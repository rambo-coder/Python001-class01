import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
header = {'user-agent':user_agent}

myurl = "https://maoyan.com/films?showType=3&offset=0"
# myurl = "https://movie.douban.com/top250"
response = requests.get(myurl,headers=header)
bs_info = bs(response.text, 'html.parser')

# print(1)
# for tags in bs_info.find_all('div',attrs={'class':'hd'}):
#     for atag in tags.find_all('a'):
#         print(atag.find_all('span'))
        # print(atag.get('href'))
        # print(atag.find('span').text)
# print(bs_info.find_all('div',attrs={'class':'movie-hover-info'})[0].find_all('div'))

# for atag in bs_info.find_all('div',attrs={'class':'movie-hover-info'})[0].find_all('div'):
#     print(atag.text)
# lis = []
# print(bs_info.find_all('div',attrs={'class':'movie-hover-info'}))
l = []
for tags in bs_info.find_all('div',attrs={'class':'movie-hover-info'}):
      name = tags.find('div').find('span').text
      name = "".join(name.split())
      tp = tags.find_all('div')[1].text
      tp = "".join(tp.split())
      tp = tp.split(':')[1]
      plan_time = tags.find_all('div')[-1].text
      plan_time = "".join(plan_time.split())
      plan_time = plan_time.split(':')[1]
      l.append([name,tp,plan_time])
      

    

col = ['name','movie_type','plan_time']
frame = pd.DataFrame(columns=col,data=l[:10])
frame.to_csv('./maoyan.csv',encoding='utf-8',index=True)

# print(bs_info.find_all('div',attrs={'class':'movie-hover-info'})[0].find('div').find('span').text)
# a = bs_info.find_all('div',attrs={'class':'movie-hover-info'})[0].find_all('div')[1].text
# print("".join(a.split()))
# b = bs_info.find_all('div',attrs={'class':'movie-hover-info'})[0].find_all('div')[-1].text
# print("".join(b.split()))

# print(lis)
# print(1)