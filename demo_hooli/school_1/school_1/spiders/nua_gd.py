




import scrapy
from school_1.items import HooliItem
import datetime
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import re

class PlymouthSpider(CrawlSpider):
    name = 'nua_gd'
    allowed_domains = ['www.nua.ac.uk']
    start_urls = []
    base_url = '%s'

    Lists = ['https://www.nua.ac.uk/courses/postgraduate/',
'https://www.nua.ac.uk/macommunicationdesign/',
'https://www.nua.ac.uk/macuration/',
'https://www.nua.ac.uk/mafashion/',
'https://www.nua.ac.uk/mafineart/',
'https://www.nua.ac.uk/magames/',
'https://www.nua.ac.uk/mamovingimageandsound/',
'https://www.nua.ac.uk/maphotography/',
'https://www.nua.ac.uk/matextiledesign/']

    for i in Lists:
        fullurl = base_url % i
        start_urls.append(fullurl)

    rules = (
        Rule(LinkExtractor(allow=(r'.*'), restrict_xpaths=('//div[@class="courses first pg-left"]/ul/li/a')),callback='parse_item', follow=True),
        # Rule(LinkExtractor(allow=r''),follow=True),
        Rule(LinkExtractor(allow=r'.*'),callback='parse_item', follow=False),
    )

    def parse_item(self,response):
        print('==================================',response.url)
        item = HooliItem()

        url = response.url
        print(1,url)

        university = 'NORWICH UNIVERSITY OF THE ARTS'
        print(2,university)

        department = 'NULL'
        country = 'UK'
        city = 'NULL'
        website = 'NULL'



        programme = response.xpath('').extract()
        programme = ''.join(programme)
        print(3,programme)

        ucas_code = 'NULL'
        degree_level = '1'

        degree_type = response.xpath('').extract()
        degree_type = ''.join(degree_type)
        print(4,degree_type)

        start_date = 'NULL'
        # start_date = ''.join(start_date)
        # print(5,start_date)

        overview = response.xpath('').extract()
        overview = ''.join(overview).replace('\n', '')
        print(6, overview)

        mode = response.xpath('').extract()
        mode = ''.join(mode).replace('\r\n','')
        mode = mode.replace('\n','')
        mode = mode.replace('      ','')
        print(7,mode)


        duration = response.xpath('').extract()
        duration = ''.join(duration).replace('\r\n','')
        duration = duration.replace('\n','')
        duration = duration.replace('    ','')
        print(8,duration)

        modules = response.xpath('').extract()
        modules = ''.join(modules).replace('\r\n','')
        # modules = modules.replace('\n','')
        print(9,modules)

        teaching = 'NULL'

        assessment = response.xpath('').extract()
        assessment = ''.join(assessment)
        print(10,assessment)

        career = 'NULL'
        # career = ''.join(career).replace('\n', '')
        # print(11, career)

        application_date = 'NULL'

        deadline = 'NULL'

        application_fee = 'NULL'

        tuition_fee= response.xpath('').extract()
        tuition_fee = ''.join(tuition_fee).replace('\r\n','')
        tuition_fee = tuition_fee.replace('\n','')
        tuition_fee = tuition_fee.replace('    ','')
        print(11, tuition_fee)

        location = 'NULL'
        # location = ''.join(location)
        # print(13,location)


        GPA = 'NULL'
        ATAS = 'NULL'

        average_score = 'NULL'

        accredited_university = 'NULL'

        Alevel = 'NULL'

        IB = 'NULL'

        IELTS = 'UNLL'
        # IELTS = ''.join(IELTS).replace('\r\n','')
        # # IELTS = re.findall('(IELTS:|IELTS)? (.*){0,5} \d?.\d? .{0,70}',IELTS)
        # print(12, IELTS)

        IELTS_L = 'NULL'
        IELTS_S = 'NULL'
        IELTS_R = 'NULL'
        IELTS_W = 'NULL'

        TOEFL = 'NULL'
        TOEFL_L = 'NULL'
        TOEFL_S = 'NULL'
        TOEFL_R = 'NULL'
        TOEFL_W = 'NULL'


        GRE = 'NULL'

        GMAT = 'NULL'
        LSAT = 'NULL'
        MCAT = 'NULL'

        chinese_requirements = 'NULL'


        working_experience = 'NULL'

        interview = 'NULL'

        portfolio = 'NULL'

        application_documents = 'NULL'

        how_to_apply = response.xpath('').extract()
        how_to_apply = ''.join(how_to_apply).replace('\n','')
        print(13,how_to_apply)

        entry_requirements = response.xpath('').extract()
        entry_requirements = ''.join(entry_requirements).replace('\n','')
        # EntryRequirements = EntryRequirements.replace(' ','')
        print(14,entry_requirements)

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