import os
from fake_useragent import UserAgent

location = os.getcwd()+'/fake_useragent.json'
ua = UserAgent(verify_ssl=False,path=location)

#模拟不同的浏览器

print(f'chrome browser:{ua.chrome}')

print(f'random browser:{ua.random}')


