# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrappingRetailItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ParamsItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    price = scrapy.Field()
    special_price = scrapy.Field()