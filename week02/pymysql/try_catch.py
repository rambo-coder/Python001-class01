from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware
from collections import defaultdict
from scrapy.exceptions import NotConfigured
from urllib.parse import urlparse
import scrapy
from scrapy.selector import Selector
import pymysql


db = pymysql.connect(host='localhost',port=3306,user='root',db='maoyan',password='')
cursor=db.cursor()

# cursor.execute("select version()")
# data = cursor.fetchone()
#
# cursor.execute("drop database if exists test")
# sql = "create database maoyan"
#
# cursor.execute(sql)

# sql = "create table movie(name char(30),type char(30),onDate char(30))"
# cursor.execute(sql)

sql = "INSERT INTO movie (name,type,onDate) VALUES (%s,%s,%s)"
#
cursor.execute(sql,('哥斯拉2：怪兽之王','科幻／灾难／动作','2019-05-31'))

db.commit()
