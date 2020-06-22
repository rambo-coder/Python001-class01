import requests
import lxml.etree

url = 'https://movie.douban.com/subject/1292052/'
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
header = {'user-agent':user_agent}

response = requests.get(url,headers=header)

selector = lxml.etree.HTML(response.text)

film_name = selector.xpath('//*[@id="content"]/h1/span[1]/text()')
print(f'film name: {film_name}')

plan_date = selector.xpath('//*[@id="info"]/span[10]/text()')
print(f'plan_date:{plan_date}')

rating = selector.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
print(f'rating:{rating}')


mylist = [film_name,plan_date,rating]
print(mylist)

import pandas as pd

movie1 = pd.DataFrame(data=mylist)
movie1.to_csv('./movie1.csv',encoding='utf-8',index=False,header=False)
