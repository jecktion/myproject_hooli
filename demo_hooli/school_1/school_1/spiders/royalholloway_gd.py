


import scrapy
from school_1.items import HooliItem
import datetime
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import re

class PlymouthSpider(CrawlSpider):
    name = 'royalholloway_gd'
    allowed_domains = ['www.royalholloway.ac.uk']
    start_urls = []
    base_url = 'https://www.royalholloway.ac.uk/%s'

    Lists = ['/courses/postgraduate/management/accounting-and-financial-management.aspx',
'/courses/postgraduate/music/advanced-musical-studies.aspx',
'/courses/postgraduate/social-work/advanced-practice.aspx',
'/courses/postgraduate/classics/ancient-history.aspx',
'/courses/postgraduate/psychology/applied-social-psychology.aspx',
'/courses/postgraduate/biological-sciences/biological-sciences.aspx',
'/courses/postgraduate/management/business-information-systems.aspx',
'/courses/postgraduate/classics/classical-art-and-archaeology.aspx',
'/courses/postgraduate/classics/classical-reception.aspx',
'/courses/postgraduate/classics/classics.aspx',
'/courses/postgraduate/psychology/clinical-psychology.aspx',
'/courses/postgraduate/mllc/comparative-literature-and-culture.aspx',
'/courses/postgraduate/computer-science/computational-finance.aspx',
'/courses/postgraduate/computer-science/computational-finance-with-a-year-in-industry.aspx',
'/courses/postgraduate/management/consumption-culture-and-marketing.aspx',
'/courses/postgraduate/management/consumption-culture-and-marketing-london.aspx',
'/courses/postgraduate/drama-theatre/contemporary-performance-practices.aspx',
'/courses/postgraduate/english/creative-writing.aspx',
'/courses/postgraduate/history/crusader-studies.aspx',
'/courses/postgraduate/geography/cultural-geography-research.aspx',
'/courses/postgraduate/computer-science/data-science-and-analytics.aspx',
'/courses/postgraduate/computer-science/data-science-and-analytics-year-in-industry.aspx',
'/courses/postgraduate/management/digital-innovation-and-analytics-london.aspx',
'/courses/postgraduate/computer-science/distributed-and-networked-systems.aspx',
'/courses/postgraduate/computer-science/distributed-and-networked-systems-year-in-industry.aspx',
'/courses/postgraduate/media-arts/documentary-by-practice.aspx',
'/courses/postgraduate/economics/economics.aspx',
'/courses/postgraduate/economics/economics-2-year-programme.aspx',
'/courses/postgraduate/pir/elections-campaigns-and-democracy.aspx',
'/courses/postgraduate/electronic-engineering/electronic-engineering.aspx',
'/courses/postgraduate/professional-studies/engineering-management.aspx',
'/courses/postgraduate/english/english-literature.aspx',
'/courses/postgraduate/management/entrepreneurship-and-innovation.aspx',
'/courses/postgraduate/management/entrepreneurship-and-innovation-year-in-business.aspx',
'/courses/postgraduate/earth-sciences/environmental-diagnosis-and-management.aspx',
'/courses/postgraduate/philosophy/european-philosophy.aspx',
'/courses/postgraduate/media-arts/film-television-and-digital-production.aspx',
'/courses/postgraduate/economics/finance.aspx',
'/courses/postgraduate/economics/finance-2-year-programme.aspx',
'/courses/postgraduate/law/forensic-psychology.aspx',
'/courses/postgraduate/mllc/french-studies.aspx',
'/courses/postgraduate/geography/geopolitics-and-security.aspx',
'/courses/postgraduate/mllc/german-studies.aspx',
'/courses/postgraduate/history/hellenic-studies.aspx',
'/courses/postgraduate/mllc/hispanic-studies.aspx',
'/courses/postgraduate/history/history.aspx',
'/courses/postgraduate/history/holocaust-studies.aspx',
'/courses/postgraduate/management/human-resource-management.aspx',
'/courses/postgraduate/information-security/information-security.aspx',
'/courses/postgraduate/information-security/information-security-with-a-year-in-industry.aspx',
'/courses/postgraduate/management/mba.aspx',
'/courses/postgraduate/management/international-management.aspx',
'/courses/postgraduate/management/international-management-marketing.aspx',
'/courses/postgraduate/management/mba-year-in-business.aspx',
'/courses/postgraduate/pir/international-public-policy.aspx',
'/courses/postgraduate/pir/international-relations.aspx',
'/courses/postgraduate/pir/international-security.aspx',
'/courses/postgraduate/professional-studies/international-supply-chain-management.aspx',
'/courses/postgraduate/media-arts/international-television-industries.aspx',
'/courses/postgraduate/pir/islamic-and-west-asian-studies.aspx',
'/courses/postgraduate/mllc/italian-studies.aspx',
'/courses/postgraduate/history/late-antique-and-byzantine-studies.aspx',
'/courses/postgraduate/computer-science/machine-learning.aspx',
'/courses/postgraduate/computer-science/machine-learning-year-in-industry.aspx',
'/courses/postgraduate/management/marketing.aspx',
'/courses/postgraduate/management/marketing-london.aspx',
'/courses/postgraduate/mathematics/mathematics-for-applications.aspx',
'/courses/postgraduate/mathematics/mathematics-of-cryptography-and-communications.aspx',
'/courses/postgraduate/media-arts/media-management.aspx',
'/courses/postgraduate/pir/media-power-and-public-affairs.aspx',
'/courses/postgraduate/english/medieval-studies.aspx',
'/courses/postgraduate/philosophy/modern-philosophy.aspx',
'/courses/postgraduate/music/music-performance.aspx',
'/courses/postgraduate/earth-sciences/petroleum-geoscience.aspx',
'/courses/postgraduate/earth-sciences/petroleum-geoscience-by-distance-learning.aspx',
'/courses/postgraduate/physics/physics-euromasters.aspx',
'/courses/postgraduate/physics/physics-by-research.aspx',
'/courses/postgraduate/drama-theatre/playwriting.aspx',
'/courses/postgraduate/philosophy/political-philosophy.aspx',
'/courses/postgraduate/pir/politics-of-development.aspx',
'/courses/postgraduate/geography/practising-sustainable-development.aspx',
'/courses/postgraduate/media-arts/producing-film-and-television.aspx',
'/courses/postgraduate/professional-studies/project-management.aspx',
'/courses/postgraduate/history/public-history.aspx',
'/courses/postgraduate/geography/quaternary-science.aspx',
'/courses/postgraduate/classics/rhetoric.aspx',
'/courses/postgraduate/media-arts/screenwriting-for-television-and-film.aspx',
'/courses/postgraduate/english/shakespeare.aspx',
'/courses/postgraduate/social-work/social-work.aspx',
'/courses/postgraduate/social-work/social-work-step-up-to-social-work.aspx',
'/courses/postgraduate/geography/sustainability-and-management.aspx',
'/courses/postgraduate/computer-science/the-internet-of-things.aspx',
'/courses/postgraduate/computer-science/the-internet-of-things-year-in-industry.aspx',
'/courses/postgraduate/drama-theatre/theatre-directing.aspx',
'/courses/postgraduate/english/victorian-literature-art-and-culture.aspx',]

    for i in Lists:
        fullurl = base_url % i
        start_urls.append(fullurl)

    rules = (
        Rule(LinkExtractor(allow=r'www.royalholloway.ac.uk/courses/postgraduate/home.aspx\?GenericList_AtoZLetter=[A-Z]'),follow=True),
        Rule(LinkExtractor(allow=r'/courses/postgraduate/.*\.aspx'), callback='parse_item', follow=False),
    )

    def parse_item(self,response):
        print('==================================',response.url)
        item = HooliItem()

        url = response.url
        print(1,url)

        university = 'Royal Holloway University of LondonEgham'
        print(2,university)

        department = response.xpath('//div[@id="details"]/table/tbody/tr[4]/td/a/div/text()').extract()
        department = ''.join(department)
        print(3,department)

        country = 'UK'
        city = 'NULL'
        website = 'https://www.royalholloway.ac.uk'

        programme = response.xpath('//div[@class="sys_large-col"]/h1/text()').extract()
        programme = ''.join(programme)
        print(4,programme)

        ucas_code = 'NULL'
        degree_level = '1'

        degree_type = response.xpath('//div[@class="sys_large-col"]/h1/text()').extract()
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
        print(5,degree_type)

        start_date = response.xpath('//div[@id="details"]/table/tbody/tr[2]/td/div/text()').extract()
        start_date = ''.join(start_date)
        print(6,start_date)

        overview = response.xpath('//div[@id="tab-1"]//text()').extract()
        overview = ''.join(overview).replace('\n', '')
        print(7, overview)

        mode = response.xpath('//div[@id="details"]/table/tbody/tr[3]/td/div/text()').extract()
        mode = ''.join(mode)
        print(8, mode)


        duration = response.xpath('//div[@id="details"]/table/tbody/tr[3]/td/div/text()').extract()
        duration = ''.join(duration)
        print(9,duration)

        modules = 'NULL'

        teaching = 'NULL'

        assessment = response.xpath('//div[@id="tab-3"]/p/text()').extract()
        assessment = ''.join(assessment)
        print(10, assessment)

        career = response.xpath('//div[@id="tab-5"]//text()').extract()
        career = ''.join(career).replace('\n', '')
        print(11, career)

        application_date = 'NULL'

        deadline = 'NULL'

        application_fee = 'NULL'

        tuition_fee_s = response.xpath('//div[@id="tab-6"]/p//text()').extract()
        tuition_fee_s = ''.join(tuition_fee_s)
        tuition_fee_s = self.getTuition_fee(tuition_fee_s)
        try:
            if tuition_fee_s > 0:
                tuition_fee = tuition_fee_s
            else:
                tuition_fee = 'NULL'
        except:
            tuition_fee = '报错!'

        print(12, tuition_fee)

        location = response.xpath('//div[@id="details"]/table/tbody/tr[5]/td/a/div/text()').extract()
        location = ''.join(location)
        print(13,location)

        ATAS = 'NULL'

        GPA = 'NULL'

        average_score = 'NULL'

        accredited_university = 'NULL'

        Alevel = 'NULL'

        IB = 'NULL'

        IELTS_s = response.xpath('//div[@id="tab-4"]/p/text()').extract()
        IELTS_s = ''.join(IELTS_s)
        try:
            if "IELTS" in IELTS_s:
                start = IELTS_s.find("IELTS")
                IELTS = IELTS_s[start:]
                IELTS = IELTS[:100]
                item["IELTS"] = IELTS
            else:
                IELTS = "NULL"
        except:
            IELTS = "报错!"
        print(14, IELTS)

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

        working_experience = 'NULL'

        interview = 'NULL'

        portfolio = 'NULL'

        application_documents = 'NULL'

        how_to_apply = 'NULL'

        entry_requirements = response.xpath('//div[@id="tab-4"]//text()').extract()
        entry_requirements = ''.join(entry_requirements).replace('\n','')
        # entry_requirements = entry_requirements.replace('({})','')
        print(15,entry_requirements)

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


