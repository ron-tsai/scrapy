import scrapy
import re
import json
from SzzsPro.items import SzzsproItem


class SzzsSpider(scrapy.Spider):
    # 爬虫文件的名称，爬虫源文件的唯一标识
    name = 'Szzs'

    # 允许的域名，通常会被注释掉"#"
    # allowed_domains = ['www.xxx.com']

    # 启始的url列表：该列表存放的url会被scrapy自动请求发送
    start_urls = ['http://guba.eastmoney.com/list,zssh000001,f.html/']

    # 生成一个通用的url模板(不可变的)
    url = 'http://guba.eastmoney.com/list,zssh000001,f_%d.html/'
    page_num = 2

    # 用作于数据解析，response表示的是请求成功后的响应对象
    def parse(self, response):
        # .extract()  把变为Selector对象的列表转为字符串
        script = response.xpath('//html/body/script/text()').extract()

        data = script[0]
        print(data)
        obj = re.compile(r'var article_list=(?P<json>.*?);')
        content = obj.search(data).group('json')
        # print(content)
        dic = json.loads(content)  # 好像是变成python字典对象
        lst = dic["re"]
        # print(lst)
        for each in lst:
            title = each["post_title"]
            user = each["user_nickname"]
            time = each["post_publish_time"]
            read = each["post_click_count"]
            reply = each["post_comment_count"]
            print(title, user, time, read, reply)

            item = SzzsproItem()
            item["title"] = title
            item["user"] = user
            item["time"] = time
            item["read"] = read
            item["reply"] = reply

            yield item  # 将item提交给管道

        if self.page_num <= 3:
            new_url = format(self.url % self.page_num)
            self.page_num += 1
            # 手动请求发送
            yield scrapy.Request(url=new_url, callback=self.parse)

        pass
