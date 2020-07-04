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



二：学习记录
1.git push -u origin master