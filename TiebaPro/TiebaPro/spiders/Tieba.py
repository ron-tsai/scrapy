import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TiebaSpider(CrawlSpider):
    name = 'Tieba'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://guba.eastmoney.com/list,zssh000001,f.html/']

    #链接提取器：根据指定规则（allow="正则"）在启始链接中进行提取指定链接
    link=LinkExtractor(allow=r'http://guba.eastmoney.com/list,zssh000001,f_\d+')

    rules = (
        #规则解析器
        Rule(link, callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()

        print(response)
        return item
