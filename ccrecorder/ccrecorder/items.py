# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CCdocument(scrapy.Item):
    # a single line in the table of records
    pass

class CCrecord(scrapy.Item):
    record_number = scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
