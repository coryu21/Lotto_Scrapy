# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LottoItem(scrapy.Item):
    round = scrapy.Field()
    num1 = scrapy.Field()
    num2 = scrapy.Field()
    num3 = scrapy.Field()
    num4 = scrapy.Field()
    num5 = scrapy.Field()
    num6 = scrapy.Field()
    specialNum = scrapy.Field()
    money = scrapy.Field()

