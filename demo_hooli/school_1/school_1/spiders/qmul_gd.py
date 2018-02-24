



import scrapy
from school_1.items import HooliItem
import datetime
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import re

class PlymouthSpider(CrawlSpider):
    name = 'qmul_gd'
    allowed_domains = ['search.qmul.ac.uk']
    start_urls = ['http://search.qmul.ac.uk/s/search.html?collection=queenmary-coursefinder-pg&query=&sort=title']
    # base_url = '/%s'
    #
    # Lists = []
    #
    # for i in Lists:
    #     fullurl = base_url % i
    #     start_urls.append(fullurl)

    rules = (
        # Rule(LinkExtractor(allow=(r'.*'), restrict_xpaths=('//div[@class="result-title"]/h4/a')), follow=True),
        Rule(LinkExtractor(allow=r'search.qmul.ac.uk/s/search.html\?collection=queenmary-coursefinder-pg&query=&sort=title&start_rank=\d+'),follow=True),
        # Rule(LinkExtractor(allow=r'/postgraduate/taught/coursefinder/courses/.*\.html'),callback='parse_item', follow=False),
        Rule(LinkExtractor(allow=(r'.*\.html'), restrict_xpaths=('//div[@class="result-title"]/h4/a')),callback='parse_item', follow=True),
        #Rule(LinkExtractor(allow=r'.*\/englishlanguagerequirements/'), callback='parse_item_e', follow=False),
    )

    def parse_item(self,response):
        print('==================================',response.url)
        item = HooliItem()

        url = response.url
        print(1,url)

        university = 'Queen Mary Universty of London'
        print(2,university)

        department = 'NULL'
        country = 'UK'
        city = 'NULL'
        website = 'http://search.qmul.ac.uk'

        programme = response.xpath('//section[@id="count"]/article/header//text()').extract()
        programme = ''.join(programme)
        print(3,programme)

        ucas_code = 'NULL'
        degree_level = '1'

        degree_type = response.xpath('//section[@id="count"]/article/header/h2/text()').extract()
        degree_type = ''.join(degree_type)
        try:
            if "BSc" in degree_type:
                degree_type = 'Bsc'
            elif "MSc" in degree_type:
                degree_type = "MSc"
            elif "BA" in degree_type:
                degree_type = 'BA'
            elif "MNSW" in degree_type:
                degree_type = 'MNSW'
            elif "PGCert" in degree_type:
                degree_type = 'PGCert'
            elif "MBA" in degree_type:
                degree_type = 'MBA'
            elif "MA" in degree_type:
                degree_type = 'MA'
            elif "MComp" in degree_type:
                degree_type = 'MComp'
            elif "PhD" in degree_type:
                degree_type = 'PhD'
            elif "FdA" in degree_type:
                degree_type = 'FdA'
            elif "PGCE" in degree_type:
                degree_type = 'PGCE'
            elif "IFP" in degree_type:
                degree_type = 'IFP'
            elif "LLB" in degree_type:
                degree_type = 'LLB'
            elif "MHealth Res" in degree_type:
                degree_type = 'MHealth Res'
            elif "MRes" in degree_type:
                degree_type = 'MRes'
            elif "MMed" in degree_type:
                degree_type = 'MMed'
            elif "MSci" in degree_type:
                degree_type = 'MSci'
            elif "MCh" in degree_type:
                degree_type = 'MCh'
            elif "LLM" in degree_type:
                degree_type = "LLM"
            elif "Y2QF" in degree_type:
                degree_type = "Y2QF"
            elif "Y2QG" in degree_type:
                degree_type = "Y2QG"
            else:
                degree_type = 'Ordinary degree'
        except:
            degree_type = "NULL"
        print(4,degree_type)

        start_date = 'NULL'
        # Sstart_date = ''.join(start_date)
        # print(5,start_date)

        overview = response.xpath('//div[@id="first"]//text()').extract()
        overview = ''.join(overview).replace('\n', '')
        print(6, overview)

        mode = response.xpath('//section[@id="count"]/article/header/h2/text()').extract()
        mode = ''.join(mode).replace('\r\n','')
        mode = mode.replace('   ','')
        print(7, mode)


        duration = response.xpath('//section[@id="count"]/article/header/h2/text()').extract()
        duration = ''.join(duration).replace('\r\n','')
        duration = duration.replace('   ','')
        print(8,duration)

        modules = response.xpath('//div[@id="second"]//text()').extract()
        modules = ''.join(modules).replace('\r\n','')
        modules = modules.replace('\n','')
        print(9,modules)

        teaching = 'NULL'

        assessment = response.xpath('//div[@id="fourth"]//text()').extract()
        assessment = ''.join(assessment)
        print(10, assessment)

        career = 'NULL'
        # career = ''.join(career).replace('\n', '')
        # print(11, career)

        application_date = 'NULL'

        deadline = 'NULL'

        application_fee = 'NULL'

        tuition_fee_s = response.xpath('//div[@id="fifth"]//text()').extract()
        tuition_fee_s = ''.join(tuition_fee_s).replace('\r\n','')
        tuition_fee_s = tuition_fee_s.replace('   ','')
        tuition_fee_s = self.getTuition_fee(tuition_fee_s)
        try:
            if tuition_fee_s > 0:
                tuition_fee = tuition_fee_s
            else:
                tuition_fee = 'NULL'
        except:
            tuition_fee = '报错!'

        print(12, tuition_fee)

        location = 'NULL'
        # location = ''.join(location)
        # print(13,location)


        GPA = 'NULL'

        average_score = 'NULL'

        accredited_university = 'NULL'

        Alevel = 'NULL'

        IB = 'NULL'

        IELTS = 'NULL'
        # IELTS = ''.join(IELTS).replace('\r\n','')
        # # IELTS = re.findall('(IELTS:|IELTS)? (.*){0,5} \d?.\d? .{0,70}',IELTS)
        # print(14, IELTS)

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
        ATAS = 'NULL'
        LSAT = 'NULL'
        MCAT = 'NULL'
        chinese_requirements = 'NULL'

        working_experience = 'NULL'

        interview = 'NULL'

        portfolio = 'NULL'

        application_documents = 'NULL'

        how_to_apply = 'NULL'

        entry_requirements = response.xpath('//div[@id="third"]//text()').extract()
        entry_requirements = ''.join(entry_requirements).replace('\n','')
        # EntryRequirements = EntryRequirements.replace(' ','')
        print(15,entry_requirements)

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