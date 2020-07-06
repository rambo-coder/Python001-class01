import time
import requests
from fake_useragent import UserAgent
import os

location = os.getcwd()+'/fake_useragent.json'
ua = UserAgent(verify_ssl=False,path=location)
headers = {
'User-Agent' : ua.random,
'Referer' : 'https://shimo.im/login',
# 防止csrf检测
'x-requested-with': 'XmlHttpRequest'
}

s = requests.Session()
# 会话对象：在同一个 Session 实例发出的所有请求之间保持 cookie，
# 期间使用 urllib3 的 connection pooling 功能。
# 向同一主机发送多个请求，底层的 TCP 连接将会被重用，从而带来显著的性能提升。

login_url = 'https://shimo.im/lizard-api/auth/password/login'

#手机号是私人信息，这里就不显示真的了
form_data = {
'mobile':'+8615001787928',
'password':'Zhangyi178',
}

response = s.post(login_url, data = form_data, headers = headers)

print(response.status_code)
print(response.text)

# 登陆后访问一下个人中心页面看是否成功
url2 = 'https://shimo.im/dashboard/used'
response2 = s.get(url2,headers = headers)
print(response2.status_code)
print(response2.text)
