# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class School2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class HooliItem(scrapy.Item):
    url = scrapy.Field()
    university = scrapy.Field()
    country = scrapy.Field()
    city = scrapy.Field()
    overview = scrapy.Field()
    history = scrapy.Field()
    education = scrapy.Field()
    rank_W = scrapy.Field()
    rank_A = scrapy.Field()
    masters = scrapy.Field()
    research = scrapy.Field()
    career = scrapy.Field()
    student_services = scrapy.Field()
    housing_services = scrapy.Field()
    library_services = scrapy.Field()
    ICT_services = scrapy.Field()
    medical_services = scrapy.Field()
    campus_life = scrapy.Field()
    sports_facilities = scrapy.Field()
    student_clubs = scrapy.Field()
    students_number = scrapy.Field()
    other = scrapy.Field()
    create_time = scrapy.Field()