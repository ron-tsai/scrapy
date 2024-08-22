# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
import pandas as pd
import os


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
#         username = item["username"]
#         posttime = item["posttime"]
#         readcount = item["readcount"]
#         reply = item["reply"]
#         # self.fp.write(title + ':' + username + ':' + posttime + ':' + readcount + ':' + reply + '\n') #因为字符串和数字型无法放在一起所以报错
#         self.fp.write(title + ':' + username + '\n')
#
#         return item
#
#     def close_spider(self, spider):
#         print("爬虫结束")
#         self.fp.close()


# 管道文件中一个管道类对应将一组数据存储到一个平台或者载体中

class mysqlPipeline(object):
    conn = None
    cursor = None
    print("开始爬虫……")

    def open_spider(self, spider):
        self.conn = pymysql.Connect(host="127.0.0.1", port=3306, user='root', db="szz",
                                    charset="utf8")  # 原本有密码password="88888888"，因为vscode里设置密码就看不到数据，所以直接删了密码

    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()
        try:
            # self.cursor.execute('insert into sz values ("%s")' % (
            # item["title"]))  # 之前因为数据类型的问题无法运行,原因是charset="utf-8"是错的，应该是charset="utf8"
            ###这里表明了数据库里表格的名称是szz
            self.cursor.execute('insert into szz values ("%s","%s","%s","%s","%s")' %
                                (item["title"], item["username"], item["reply"], item["readcount"],
                                 item["posttime"]
                                 ))  # 时间的格式为timestamp，且输入value的顺序要和mysql列的顺序一致
            self.conn.commit()
            print('mysql数据传给管道')

        except Exception as e:
            print(e)
            self.conn.rollback()

        return item

    def close_spider(self, spider):
        print("爬虫结束")
        self.cursor.close()
        self.conn.close()
