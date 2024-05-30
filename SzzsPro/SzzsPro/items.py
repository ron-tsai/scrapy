# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SzzsproItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    user = scrapy.Field()
    time = scrapy.Field()
    read = scrapy.Field()
    reply = scrapy.Field()

    # pass
