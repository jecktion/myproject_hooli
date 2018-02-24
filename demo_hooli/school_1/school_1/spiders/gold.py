# -*- coding: utf-8 -*-
import scrapy
from school_1.items import HooliItem
import datetime
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import re

class GoldSpider(CrawlSpider):

    name = 'gold'
    allowed_domains = ['www.gold.ac.uk']
    # start_urls = ['https://www.gold.ac.uk/ug/integrated-degree-psychology/']
    start_urls = []
    base_url = 'https://www.gold.ac.uk/%s'

    Lists = ['/ug/ba-anthropology-media/',
'/ug/ba-anthropology-sociology/',
'/ug/ba-anthropology-visual-practice/',
'/ug/ba-anthropology/',
'/ug/ba-community-youth-work/',
'/ug/ba-arts-management/',
'/ug/ba-criminology/',
'/ug/ba-curating/',
'/ug/ba-drama-theatre-arts/',
'/ug/ba-drama-comedy-satire/',
'/ug/ba-drama-performance-politics-society/',
'/ug/ba-economics/',
'/ug/ba-economics-politics-public/',
'/ug/ba-education-culture-society/',
'/ug/ba-english-american-literature/',
'/ug/ba-english-comparative-literature/',
'/ug/ba-english-drama/',
'/ug/ba-english-history/',
'/ug/ba-english-language-literature/',
'/ug/ba-english-creative-writing/',
'/ug/ba-english/',
'/ug/ba-fine-art-history-of-art/',
'/ug/ba-fine-art-extension/',
'/ug/ba-fine-art/',
'/ug/ba-history-anthropology/',
'/ug/ba-history-journalism/',
'/ug/ba-history-politics/',
'/ug/ba-history-of-art/',
'/ug/ba-history/',
'/ug/ba-international-relations-chinese/',
'/ug/ba-international-relations/',
'/ug/ba-journalism/',
'/ug/ba-media-communications/',
'/ug/ba-media-english/',
'/ug/ba-media-sociology/',
'/ug/ba-politics-international-relations/',
'/ug/ba-politics/',
'/ug/ba-politics-philosophy-economics/',
'/ug/ba-psychosocial-studies/',
'/ug/ba-religion/',
'/ug/ba-social-work/',
'/ug/ba-sociology-chinese/',
'/ug/ba-sociology-politics/',
'/ug/ba-sociology-criminology/',
'/ug/ba-sociology/',
'/ug/ba-design/',
'/ug/bmus-music/',
'/ug/bmus-popular-music/',
'/ug/bsc-business-computing-entrepreneurship/',
'/ug/bsc-computer-science/',
'/ug/bsc-computing-chinese/',
'/ug/bsc-creative-computing/',
'/ug/bsc-digital-arts-computing/',
'/ug/bsc-economics-econometrics/',
'/ug/bsc-games-programming/',
'/ug/bsc-management-economics/',
'/ug/bsc-management-with-entrepreneurship/',
'/ug/bsc-management-marketing/',
'/ug/bsc-marketing/',
'/ug/bsc-clinical-psychology/',
'/ug/bsc-psychology-cognitive-neuroscience/',
'/ug/bsc-psychology-forensic-psychology/',
'/ug/bsc-psychology-management/',
'/ug/bsc-psychology/',
'/ug/foundation-computing/',
'/ug/integrated-degree-anthropology/',
'/ug/integrated-degree-english/',
'/ug/integrated-degree-history/',
'/ug/integrated-degree-media/',
'/ug/integrated-degree-psychology/']

    for i in Lists:
        fullurl = base_url % i
        start_urls.append(fullurl)


    rules = (
        Rule(LinkExtractor(allow=r'https://www.gold.ac.uk/course-finder/results/\?collection=goldsmiths-courses&sort=Title&f.Level|level=Undergraduate&start_rank=\d+'),follow=True),
        Rule(LinkExtractor(allow=(r'/ug/.*'),restrict_xpaths=('//h3[@class="teaser__title"]/a')),callback='parse_item',follow=False),
    )

    def parse_item(self,response):

        item = HooliItem()
        # item = {}
        url = response.url
        print(url)
        print('----------------------------------------------------')
        # var1=url.split('/')
        # if 'ug' in var1:
        #     print('----------------------------------------',response.url)
        # else:
        #     print('```````````````````````')


        university = 'Goldsmiths University of London'
        print(1,university)

        department_str = response.xpath('//*[@id="maincontent"]/article/header/div/div/div/div/div//text()').extract()
        department_str = ' '.join(department_str)
        try:
            if "Department" in department_str:
                start = department_str.find("Department")
                department = department_str[start:]
                department = department[:50]
                item["department"] = department
            else:
                department = "NULL"
        except:
            department = "报错"
        print(2,department)

        country = 'UK'
        city = "NULL"
        website = 'https://www.gold.ac.uk'

        programme = response.xpath('//div[@class="hero__content"]//h1//text()').extract()
        programme = ''.join(programme)
        print(3,programme)

        ucas_code = response.xpath('//ul[@class="split-list split-list--hero"]/li/text()').extract()
        ucas_code = ''.join(ucas_code)
        print(4,ucas_code)

        degree_level = '0'

        degree_type = response.xpath('//div[@class="hero__content"]/h1/text()').extract()
        degree_type = ''.join( degree_type)
        print(5, degree_type)

        start_date = 'NULL'

        overview = response.xpath('//div[@class="rich-content rich-content-section full-wrap"]/p/text()').extract()
        overview = ''.join(overview)
        print(6,overview)

        mode = 'NULL'



        duration = response.xpath('//ul[@class="split-list split-list--hero"]/li/text()').extract()
        duration = ''.join(duration)
        print(7,duration)

        modules = response.xpath('//div[@class="grid-push grid-push--two"]/div[@class="rich-content rich-content-section full-wrap"]/p/text()').extract()
        modules = ' '.join(modules)
        modules = str(modules)
        print(8,modules)

        teaching = 'NULL'

        assessment = response.xpath('//div[@class="rich-content rich-content-section full-wrap"]/p[11]/text()').extract()
        assessment = ' '.join(assessment)
        # Evaluation_method = Evaluation_method.replace('\n', '')
        assessment = str(assessment)
        print(9,assessment)

        career_lists = response.xpath('//section[@class="section section--accordion"]//text()').extract()
        career_str = ' '.join(career_lists)
        if "Skills & careers" in career_str:
            cstart = career_str.find("Skills & careers")
            cend = career_str.find("Fees & funding")
            career = career_str[cstart:cend]
            item["career"] = career
        else:
            career = 'NULL'
        print(10,career)

        application_date = 'NULL'

        deadline = 'NULL'

        application_fee = 'NULL'

        tuition_fee = 'NULL'

        location = 'NULL'

        GPA = 'NULL'

        average_score = 'NULL'

        accredited_university = 'NULL'

        Alevel = response.xpath('//div[@class="hero__content"]/ul/li/text()').extract()
        Alevel = ' '.join(Alevel)
        print(11,Alevel)

        IB = response.xpath('//div[@class="hero__content"]/ul/li/text()').extract()
        IB = ' '.join(IB)
        print(12,IB)

        IELTS_str = response.xpath('//div[@class="rich-content rich-content-section full-wrap"]//p//text()').extract()
        IELTS_str = ' '.join(IELTS_str)
        try:
            if "IELTS" in IELTS_str:
                start = IELTS_str.find("IELTS")
                end = IELTS_str.find("If you need")
                IELTS = IELTS_str[start:end]
                # IELTS = IELTS[:80]
                item["IELTS"] = IELTS
            else:
                IELTS = 'NULL'
        except:
            IELTS = '报错'

        print(13,IELTS)

        IELTS_L = "NULL"
        IELTS_S = "NULL"
        IELTS_R = "NULL"
        IELTS_W = "NULL"


        TOEFL = 'NULL'
        TOEFL_L = 'NULL'
        TOEFL_S = 'NULL'
        TOEFL_R = 'NULL'
        TOEFL_W = 'NULL'

        GRE = 'NULL'

        GMAT = 'NULL'

        LSAT = 'UNLL'

        ATAS = 'NULL'
        MCAT = 'NULL'

        working_experience = 'NULL'

        interview = 'NULL'

        portfolio = 'NULL'

        application_documents = 'NULL'

        how_to_apply = 'NULL'

        entry_requirements = 'NULL'
        chinese_requirements = 'NULL'

        school_test = 'NULL'

        degree_description = 'NULL'

        SATI = 'NULL'

        SATII = 'NULL'

        SAT_code = 'NULL'

        ACT = 'NULL'

        ACT_code = 'NULL'

        other = 'NULL'

        create_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(15, create_time)

        item["url"] = url
        item["university"] = university
        item["country"] = country
        item["city"] = city
        item["website"] = website
        item["department"] = department
        item["programme"] = programme
        item["ucas_code"] = ucas_code
        item["degree_level"] = degree_level
        item["degree_type"] = degree_type
        item["start_date"] = start_date
        item["degree_description"] = degree_description
        item["overview"] = overview
        item["mode"] = mode
        item["duration"] = duration
        item["modules"] = modules
        item["teaching"] = teaching
        item["assessment"] = assessment
        item["career"] = career
        item["application_date"] = application_date
        item["deadline"] = deadline
        item["application_fee"] = application_fee
        item["tuition_fee"] = tuition_fee
        item["location"] = location
        item["ATAS"] = ATAS
        item["GPA"] = GPA
        item["average_score"] = average_score
        item["accredited_university"] = accredited_university
        item["Alevel"] = Alevel
        item["IB"] = IB
        item["IELTS"] = IELTS
        item["IELTS_L"] = IELTS_L
        item["IELTS_S"] = IELTS_S
        item["IELTS_R"] = IELTS_R
        item["IELTS_W"] = IELTS_W
        item["TOEFL"] = TOEFL
        item["TOEFL_L"] = TOEFL_L
        item["TOEFL_S"] = TOEFL_S
        item["TOEFL_R"] = TOEFL_R
        item["TOEFL_W"] = TOEFL_W
        item["GRE"] = GRE
        item["GMAT"] = GMAT
        item["LSAT"] = LSAT
        item["MCAT"] = MCAT
        item["working_experience"] = working_experience
        item["interview"] = interview
        item["portfolio"] = portfolio
        item["application_documents"] = application_documents
        item["how_to_apply"] = how_to_apply
        item["entry_requirements"] = entry_requirements
        item["chinese_requirements"] = chinese_requirements
        item["school_test"] = school_test
        item["SATI"] = SATI
        item["SATII"] = SATII
        item["SAT_code"] = SAT_code
        item["ACT"] = ACT
        item["ACT_code"] = ACT_code
        item["other"] = other
        item["create_time"] = create_time

        yield item

    def getTuition_fee(self, tuition_fee):
        allfee = re.findall(r'\d+,\d+', tuition_fee)
        # print(allfee)
        for index in range(len(allfee)):
            fee = allfee[index].split(",")
            allfee[index] = ''.join(fee)
            # print(allfee[index])
        # print(allfee)
        maxfee = 0
        for fee in allfee:
            if int(fee) >= maxfee:
                maxfee = int(fee)
        return maxfee













