学习笔记

一：解决问题

1. FakeUserAgentError('Maximum amount of retries reached')
解决办法：
首先，下载： https://fake-useragent.herokuapp.com/browsers/0.1.11 并另存为：fake_useragent.json 存在代码当前路径下
然后，添加代码：
location = os.getcwd()+'/fake_useragent.json'
ua = Useragent(path=location)

2. Message: session not created:This version of ChromeDriver only supports Chrome version78
解决办法：
1.从http://chromedriver.storage.googleapis.com/index.html 下载下来的chrome driver 加压后 放在运行代码当前目录
2.用虚拟环境运行，将chromedriver.exe放在venv\bin下

3.Pytesseract : “TesseractNotFound Error: tesseract is not installed or it's not in your path”?
解决办法：
1.github.com/tesseract-ocr/tesseract/wiki 下载
2.将pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe" 添加到代码中。

4.error: You have not concluded your merge (MERGE_HEAD exists).hint: Please, commit your changes before merging.
fatal: Exiting because of unfinished merge.
解决办法：
git reset --hard origin/master 放弃本地修改

5.mac 删除mysql 并重新安装
https://blog.csdn.net/killerabby/article/details/88651690

https://blog.csdn.net/youzhouliu/article/details/80782892



二：学习记录
**1.git push -u origin master**

**2.cookie**
1.服务器采用cookie的机制来识别具体哪一个用户的访问。https://blog.csdn.net/zwq912318834/article/details/79571110

**3.session**
1.session 的整个过程：
one: 服务器根据用户名和密码，生成一个session ID，存储到服务器的数据库中
two: 用户登录访问时，服务器会将对应的session ID发送给用户，本地浏览器。
three：浏览器会将这个session ID存储到cookie中，作为一个键值项
four：以后，浏览器每次请求，就会将含有session ID的cookie信息，一起发送给服务器
five：服务器收到请求之后，通过cookie中的session id，到数据库中查询，解析出对应的用户名，就知道哪个用户请求了。

**4.cookie在客户端，session在服务器端**
one:cookie 在客户端，session在服务器端，cookie是一种浏览器本地存储机制。存储在本地浏览器中，和服务器没有关系。每次请求，用户会带上
本地cookie的信息。这些信息也是服务器之前发送给浏览器的，或者是用户之前填写的一些信息。

two：cookie有不安全机制。你不能把用户信息都存在本地，一旦别人窃取，就知道你的用户名和密码。所以引入了session机制

three：服务器在发送id时引入了一种session的机制，很简单，就是根据用户名和密码，生成一段随机字符串，这些字符串时有时间限制的

four：session是服务器生成的，存储在服务器的数据库或者文件中，然后把sessionID发送给用户，用户存储在本地cookie中。每次请求时，把这个sessionID
带给服务器，服务器根据ID到数据库中去查询，找到哪个用户，就可以进行标注了。

five：session是存在cookie中的。

**5.windows mysql 启动**
one: 已管理员身份启动cmd
two：找到已解压的mysql文件夹，进入该文件目录，例如：cd C:\Users\I506596\Downloads\mysql-8.0.20-winx64\bin
three：mysql -u root -p

6. 爬虫过程：

one.  scrapy startproject <爬虫名称>
eg: scrapy startproject proxyspider
two. cd proxyspider/proxyspider
three. scrapy genspider httpbin httpbin.org
four. 找到cfg所在目录，在此目录执行 scrapy crawl httpbin
