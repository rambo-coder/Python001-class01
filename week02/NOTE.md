学习笔记

一：解决问题

1. FakeUserAgentError('Maximum amount of retries reached')
解决办法：
首先，下载： https://fake-useragent.herokuapp.com/browsers/0.1.11 并另存为：fake_useragent.json 存在代码当前路径下
然后，添加代码：
location = os.getcwd()+'/fake_useragent.json'
ua = Useragent(path=location)


二：学习记录
1.git push -u origin master