import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TiebaSpider(CrawlSpider):
    name = 'Tieba'
    # allowed_domains = ['www.xxx.com']
    # start_urls = ['https://blog.csdn.net/weixin_41931602/article/details/80200695']
    start_urls = ['http://guba.eastmoney.com/list,zssh000001,f.html/']

    #链接提取器：根据指定规则（allow="正则"）在启始链接中进行提取指定链接
    link=LinkExtractor(restrict_xpaths='//ul[@class="paging"]//li')

    rules = (
        #规则解析器
        Rule(link, callback='parse_item', follow=False),
    )

    def parse_item(self, response):


        print(response)

