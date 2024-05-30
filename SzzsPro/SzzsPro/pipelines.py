# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


# class SzzsproPipeline(object):
#     fp = None
#
#     # 重写父类方法：该方法只在开始爬取时被调用一次
#     def open_spider(self, spider):
#         print("开始爬虫……")
#         self.fp = open('./szzs.txt', 'w', encoding='utf-8')
#
#     # 专门用来处理item类型对象的
#     # 该方法可以接收 爬虫文件提交过来的item对象
#     # 该方法每接收一个item就会被调用一次
#     def process_item(self, item, spider):
#         title = item["title"]
#         user = item["user"]
#         time = item["time"]
#         read = item["read"]
#         reply = item["reply"]
#         # self.fp.write(title + ':' + user + ':' + time + ':' + read + '+' + reply + '\n') #因为字符串和数字型无法放在一起所以报错
#         self.fp.write(title + ':' + user + ':' + time + '\n')
#
#         return item
#
#     def close_spider(self, spider):
#         print("爬虫结束")
#         self.fp.close()

# 管道文件中一个管道类对应将一组数据存储到一个平台或者载体中

class mysqlPipeline():
    conn = None
    cursor = None

    def open_spider(self, spider):
        self.conn = pymysql.Connect(host="127.0.0.1", port=3306, user='root', password="acginor1992", db="sz",
                                    charset="utf-8")

    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute('insert into sz values ("%s","%s","%s","%s","%s")'
                                % (item["title"], item["user"], item["time"], item["read"], item["reply"]))
            self.conn.commit()

        except Exception as e:
            print(e)
            self.conn.rollback()

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
