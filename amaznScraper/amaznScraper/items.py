# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmaznscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    productTitle = scrapy.Field()
    dealPrice = scrapy.Field()
    originalPrice = scrapy.Field()
    thumbnail = scrapy.Field()
    productLink = scrapy.Field()

    pass
