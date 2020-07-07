# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class MaoyanspiderPipeline:
    def process_item(self, item, spider):
        name = item['name']
        type_m = item['type_m']
        time = item['time']
        data = (name,type_m,time)
        print(data)
        save_data_to_sql(data)

def save_data_to_sql(data):
    connection = pymysql.connect(host='localhost',port=3306,user='root',password='',db='maoyan',charset='utf8')
    try:
        # with connection.cursor() as cursor:
        #     # Read a single record
        #     sql = "SELECT * FROM movieInfo"
        #     cursor.execute(sql)
        #     result = cursor.fetchone()
        #     print(result)
        with connection.cursor() as cursor:
            print('p0')
            sql = "INSERT INTO movie (name,type,onDate) VALUES (%s,%s,%s)"
            print('p1')
            cursor.execute(sql,(data[0],data[1],data[2]))
            print('p2')
            connection.commit()
            print('p3')
    except:
        print("Hi")
        connection.rollback()
    finally:
        connection.close()
