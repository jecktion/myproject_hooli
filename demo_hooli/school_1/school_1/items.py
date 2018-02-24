# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class School1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

# class HooliItem(scrapy.Item):
#     url = scrapy.Field()
#     university = scrapy.Field()
#     department = scrapy.Field()
#     programme = scrapy.Field()
#     bachelor = scrapy.Field()
#     overview = scrapy.Field()
#     modules = scrapy.Field()
#     Evaluation_method = scrapy.Field()
#     career = scrapy.Field()
#     IELTS = scrapy.Field()
#     ALevel = scrapy.Field()
#     IB = scrapy.Field()
#     crawltime = scrapy.Field()


# class HooliItem(scrapy.Item):
#     url = scrapy.Field()
#     programme = scrapy.Field()
#     modules = scrapy.Field()
#     Evaluation_method = scrapy.Field()

# class HooliItem(scrapy.Item):
#     url = scrapy.Field()
#     university = scrapy.Field()
#     department = scrapy.Field()
#     programme = scrapy.Field()
#     CourseOverview = scrapy.Field()
#     startdate = scrapy.Field()
#     UCAS = scrapy.Field()
#     Course_length = scrapy.Field()
#     modules = scrapy.Field()
#     Evaluation_method = scrapy.Field()
#     Alevel = scrapy.Field()
#     IELTS = scrapy.Field()
#     career = scrapy.Field()
#     tuition_fee = scrapy.Field()
#

#

# class HooliItem(scrapy.Item):
#     url = scrapy.Field()
#     department = scrapy.Field()
#     Course = scrapy.Field()
#     UcasCode = scrapy.Field()
#     Duration = scrapy.Field()
#     Alevel = scrapy.Field()
#     IB = scrapy.Field()
#     Location = scrapy.Field()
#     CourseOverview = scrapy.Field()
#     Modules = scrapy.Field()
#     EntryRequirements = scrapy.Field()
#     Assessment = scrapy.Field()
#     Career = scrapy.Field()
#     Other = scrapy.Field()

#
# class HooliItem(scrapy.Item):
#     url = scrapy.Field()
#     Department = scrapy.Field()
#     Programme = scrapy.Field()
#     Duration = scrapy.Field()
#     Start_Date = scrapy.Field()
#     Location = scrapy.Field()
#     Overview = scrapy.Field()
#     Modules = scrapy.Field()
#     Teaching_and_Assessment = scrapy.Field()
#     Career = scrapy.Field()
#     EntryRequirements = scrapy.Field()
#     TOEFL = scrapy.Field()
#     IELTS = scrapy.Field()
#     Tuition_Fee = scrapy.Field()
#     Master = scrapy.Field()
#     crawltime = scrapy.Field()


class HooliItem(scrapy.Item):
    url = scrapy.Field()
    university = scrapy.Field()
    country = scrapy.Field()
    city = scrapy.Field()
    website = scrapy.Field()
    department = scrapy.Field()
    programme = scrapy.Field()
    ucas_code = scrapy.Field()
    degree_type = scrapy.Field()
    degree_level = scrapy.Field()
    start_date = scrapy.Field()
    degree_description = scrapy.Field()
    overview = scrapy.Field()
    mode = scrapy.Field()
    duration = scrapy.Field()
    modules = scrapy.Field()
    teaching = scrapy.Field()
    assessment = scrapy.Field()
    career = scrapy.Field()
    application_date = scrapy.Field()
    deadline = scrapy.Field()
    application_fee = scrapy.Field()
    tuition_fee = scrapy.Field()
    location = scrapy.Field()
    ATAS = scrapy.Field()
    GPA = scrapy.Field()
    LSAT = scrapy.Field()
    MCAT = scrapy.Field()
    average_score = scrapy.Field()
    accredited_university = scrapy.Field()
    Alevel = scrapy.Field()
    IB = scrapy.Field()
    IELTS = scrapy.Field()
    IELTS_L = scrapy.Field()
    IELTS_S = scrapy.Field()
    IELTS_R = scrapy.Field()
    IELTS_W = scrapy.Field()
    TOEFL = scrapy.Field()
    TOEFL_L = scrapy.Field()
    TOEFL_S = scrapy.Field()
    TOEFL_R = scrapy.Field()
    TOEFL_W = scrapy.Field()
    GRE = scrapy.Field()
    GMAT = scrapy.Field()
    working_experience = scrapy.Field()
    interview = scrapy.Field()
    portfolio = scrapy.Field()
    application_documents = scrapy.Field()
    how_to_apply = scrapy.Field()
    entry_requirements = scrapy.Field()
    chinese_requirements = scrapy.Field()
    school_test = scrapy.Field()
    SATI = scrapy.Field()
    SATII = scrapy.Field()
    SAT_code = scrapy.Field()
    ACT = scrapy.Field()
    ACT_code = scrapy.Field()
    other = scrapy.Field()
    create_time = scrapy.Field()