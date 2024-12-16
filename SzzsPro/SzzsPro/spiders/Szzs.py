import scrapy
import re
import json
from SzzsPro.items import SzzsproItem
from urllib.parse import urlparse

from selenium import webdriver  # 导入selenium
from selenium.webdriver.chrome.service import Service


# 创建一个函数来判断url是否有效
def is_url_valid(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


class SzzsSpider(scrapy.Spider):
    # 爬虫文件的名称，爬虫源文件的唯一标识
    name = 'Szzs'

    # 允许的域名，通常会被注释掉"#"
    # allowed_domains = ['www.xxx.com']

    # 启始的url列表：该列表存放的url会被scrapy自动请求发送

    start_page_num = 68239
    start_urls = ['http://guba.eastmoney.com/list,zssh000001_{}.html'.format(start_page_num)]
    # start_urls = ['https://guba.eastmoney.com/list,601901.html'] #避免反爬虫，方正证券吧测试

    # 生成一个通用的url模板(不可变的)
    url = 'http://guba.eastmoney.com/list,zssh000001_%d.html/'  ##而不是'http://guba.eastmoney.com/list,zssh000001,f_%d.html/'

    page_num = start_page_num + 1

    #
    # def parse_detail(self, response):
    #     item = response.meta['item']
    #     detail_time = response.xpath(
    #         '//*[@id="main"]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[2]/text()').extract_first()
    #     print(detail_time)
    #     item['posttime'] = detail_time
    #     yield item

    # 用作于数据解析，response表示的是请求成功后的响应对象

    def __init__(self):
        # 实例化一个浏览器对象
        service = Service('/Users/ccmac/PycharmProjects/scrapy/chromedriver')

        self.bro = webdriver.Chrome(service=service)
        # executable_path = chrome_driver_path

    def parse(self, response):

        list_item = response.xpath('//*[@id="mainlist"]/div/ul/li[1]/table//tr')
        print(list_item)

        for tr in list_item[1:]:
            item = SzzsproItem()
            # posttime = tr.xpath('.//div[contains(@class,"update")]/text()').extract_first()

            # detail_url = 'http://guba.eastmoney.com' + tr.xpath('.//div[@class="title"]/a/@href').extract_first()
            # print(detail_url)
            # detail_url_1 = 'http:' + tr.xpath('.//div[@class="title"]/a/@href').extract_first()
            # detail_url_2 = 'http://guba.eastmoney.com' + tr.xpath('.//div[@class="title"]/a/@href').extract_first()
            #
            # if is_url_valid(detail_url_1) == True:
            #     detail_url = detail_url_1
            # else:
            #     detail_url = detail_url_2

            guba_name = tr.xpath('//*[@id="hotlist"]//div[contains(@class,"barname" )]/text()[1]').extract_first()
            print(guba_name)

            title = tr.xpath('.//div[@class="title"]/a/text()').extract_first()
            username = tr.xpath('.//div[contains(@class,"author" )]/a/text()').extract_first()
            posttime = tr.xpath('.//div[contains(@class,"update" )]/text()').extract_first()
            readcount = tr.xpath('.//div[@class="read"]/text()').extract_first()
            reply = tr.xpath('.//div[@class="reply"]/text()').extract_first()
            # print(title, username, posttime, readcount, reply)
            item["title"] = title
            item["username"] = username
            item["posttime"] = posttime
            item["readcount"] = readcount
            item["reply"] = reply

            if guba_name == '上证指数吧':
                print(title, username, posttime, readcount, reply)

                yield item  # 将item提交给管道
            else:

                break

            # yield scrapy.Request(url=detail_url, callback=self.parse_detail,
            #                      meta={'item': item})
        if self.page_num <= 85000:
            new_url = format(self.url % self.page_num)

            self.page_num += 1

            # 手动请求发送
            yield scrapy.Request(url=new_url, callback=self.parse)

        pass
