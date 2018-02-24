
import scrapy
from school_1.items import HooliItem
import datetime
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import re

class PlymouthSpider(CrawlSpider):
    name = 'mastersportal_USA'
    allowed_domains = ['www.mastersportal.com']
    start_urls = ['https://www.mastersportal.com/ranking-country/82/united-states.html']

    rules = (
        Rule(LinkExtractor(allow=(r'.*'), restrict_xpaths=('//*[@id="RankingXCountryChart"]/table/tbody/tr/td/a')),callback='parse_item',follow=True),
        # Rule(LinkExtractor(allow=(r'.*'), restrict_xpaths=('')), follow=True),
        # Rule(LinkExtractor(allow=(r'.*'), restrict_xpaths=('//*[@id="LinkTrail"]/ul/li[4]/a')), callback='parse_item', follow=False),
    )

    def parse_item(self,response):
        print('==================================',response.url)
        item = HooliItem()
        # url = response.url
        # print(url)
        #
        # university = ''
        # department = 'NULL'
        # country = 'UK'
        # city = 'NULL'
        # website = 'NULL'
        #
        # programme= ''
        # # programme= ' '.join(programme)
        # # print(programme,1)
        #
        # ucas_code = 'NULL'
        #
        # degree_level = 'NULL'
        #
        # degree_type = 'NULL'
        #
        # start_date = 'NULL'
        #
        # overview = 'NULL'
        #
        # mode = 'NULL'
        #
        # duration = 'NULL'
        #
        # modules = ''
        # # modules = ''.join(modules)
        # # modules = str(modules)
        # # print(2,modules)
        #
        # teaching = 'NULL'
        #
        # assessment = ''
        # # assessment = ' '.join(assessment)
        # # assessment = str(assessment)
        # # print(assessment, 3)
        #
        # career = 'NULL'
        #
        # application_date = 'NULL'
        #
        # deadline = 'NULL'
        #
        # application_fee = 'NULL'
        #
        # tuition_fee = 'NULL'
        #
        # location = 'NULL'
        #
        # GPA = 'NULL'
        # average_score = 'NULL'
        #
        # Alevel = 'NULL'
        #
        # IB = 'NULL'
        #
        # accredited_university = 'NULL'
        #
        # IELTS = 'NULL'
        # IELTS_L = 'NULL'
        # IELTS_S = 'NULL'
        # IELTS_R = 'NULL'
        # IELTS_W = 'NULL'
        #
        # TOEFL = 'NULL'
        # TOEFL_L = 'NULL'
        # TOEFL_S = 'NULL'
        # TOEFL_R = 'NULL'
        # TOEFL_W = 'NULL'
        #
        # GRE = 'NULL'
        #
        # GMAT = 'NULL'
        # ATAS = 'NULL'
        # LSAT = 'NULL'
        # MCAT = 'NULL'
        #
        # working_experience =  'NULL'
        #
        # interview = 'NULL'
        #
        # portfolio = 'NULL'
        #
        # application_documents = 'NULL'
        #
        # how_to_apply = 'NULL'
        #
        # entry_requirements = 'NULL'
        #
        # chinese_requirements = 'NULL'
        #
        # school_test = 'NULL'
        #
        # degree_description = 'NULL'
        #
        # SATI = 'NULL'
        #
        # SATII = 'NULL'
        #
        # SAT_code = 'NULL'
        #
        # ACT = 'NULL'
        #
        # ACT_code = 'NULL'
        #
        # other = 'NULL'
        #
        # create_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # print(15, create_time)
        #
        # item["url"] = url
        # item["university"] = university
        # item["country"] = country
        # item["city"] = city
        # item["website"] = website
        # item["department"] = department
        # item["programme"] = programme
        # item["ucas_code"] = ucas_code
        # item["degree_level"] = degree_level
        # item["degree_type"] = degree_type
        # item["start_date"] = start_date
        # item["degree_description"] = degree_description
        # item["overview"] = overview
        # item["mode"] = mode
        # item["duration"] = duration
        # item["modules"] = modules
        # item["teaching"] = teaching
        # item["assessment"] = assessment
        # item["career"] = career
        # item["application_date"] = application_date
        # item["deadline"] = deadline
        # item["application_fee"] = application_fee
        # item["tuition_fee"] = tuition_fee
        # item["location"] = location
        # item["ATAS"] = ATAS
        # item["GPA"] = GPA
        # item["average_score"] = average_score
        # item["accredited_university"] = accredited_university
        # item["Alevel"] = Alevel
        # item["IB"] = IB
        # item["IELTS"] = IELTS
        # item["IELTS_L"] = IELTS_L
        # item["IELTS_S"] = IELTS_S
        # item["IELTS_R"] = IELTS_R
        # item["IELTS_W"] = IELTS_W
        # item["TOEFL"] = TOEFL
        # item["TOEFL_L"] = TOEFL_L
        # item["TOEFL_S"] = TOEFL_S
        # item["TOEFL_R"] = TOEFL_R
        # item["TOEFL_W"] = TOEFL_W
        # item["GRE"] = GRE
        # item["GMAT"] = GMAT
        # item["LSAT"] = LSAT
        # item["MCAT"] = MCAT
        # item["working_experience"] = working_experience
        # item["interview"] = interview
        # item["portfolio"] = portfolio
        # item["application_documents"] = application_documents
        # item["how_to_apply"] = how_to_apply
        # item["entry_requirements"] = entry_requirements
        # item["chinese_requirements"] = chinese_requirements
        # item["school_test"] = school_test
        # item["SATI"] = SATI
        # item["SATII"] = SATII
        # item["SAT_code"] = SAT_code
        # item["ACT"] = ACT
        # item["ACT_code"] = ACT_code
        # item["other"] = other
        # item["create_time"] = create_time
        #
        # yield item

