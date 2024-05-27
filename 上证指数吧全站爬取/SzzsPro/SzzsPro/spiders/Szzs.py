import scrapy


class SzzsSpider(scrapy.Spider):
    #爬虫文件的名称，爬虫源文件的唯一标识
    name = 'Szzs'

    #允许的域名，通常会被注释掉"#"
    #allowed_domains = ['www.xxx.com']

    #启始的url列表：该列表存放的url会被scrapy自动请求发送
    start_urls = ['http://guba.eastmoney.com/list,zssh000001,f.html/']

    #用作于数据解析，response表示的是请求成功后的响应对象
    def parse(self, response):
        pass
