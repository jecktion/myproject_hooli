# -*- coding: utf-8 -*-






import scrapy
from school_3.items import HooliItem
import datetime
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import re

class PlymouthSpider(CrawlSpider):
    name = 'canberra_ug'
    allowed_domains = ['search.canberra.edu.au']
    start_urls = ['http://search.canberra.edu.au/s/search.html?collection=courses&form=course-search&profile=_default&query=!padre&course-search-widget__submit=&meta_C_and=COURSE&sort=metaH&f.Type|B=undergraduate&start_rank=1']
    # base_url = 'https://www.worcester.ac.uk%s'
    #
    # Lists = []
    #
    # for i in Lists:
    #     fullurl = base_url % i
    #     start_urls.append(fullurl)

    rules = (
        # Rule(LinkExtractor(allow=(r'.*'), restrict_xpaths=('')),callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'http://search.canberra.edu.au/s/search.html?collection=courses&form=course-search&profile=_default&query=!padre&course-search-widget__submit=&meta_C_and=COURSE&sort=metaH&f.Type|B=undergraduate&start_rank=\d+'),follow=True),
        Rule(LinkExtractor(allow=(r'.*'),restrict_xpaths=('//*[@id="main"]/div/div/div/table/tbody/tr/td/small/a')),callback='parse_item', follow=False),
    )

    def parse_item(self,response):
        print('==================================',response.url)
        item = HooliItem()

        url = response.url
        print(1,url)

        university = 'University of Canberra'
        print(2,university)

        department_s = response.xpath('//*[@id="main"]/div//tr//text()').extract()
        department_s = ''.join(department_s)
        try:
            if "Faculty:" in department_s:
                start = department_s.find("Faculty:")
                department = department_s[start:]
                department = department[:48]
                item["department"] = department
            else:
                department = "NULL"

        except:
            department = "报错!"

        print(3,department)

        country = 'Australia'
        city = "canberra"
        website = 'http://www.canberra.edu.au'
        degree_level = '0'

        # programme = response.xpath('//div[@class="section picture-nav"]/h1/text()').extract()
        programme = response.xpath('//*[@id="main"]/div/h1/text()').extract()
        programme = ''.join(programme)
        print(4,programme)

        ucas_code_s = response.xpath('//*[@id="main"]/div//tr//text()').extract()
        ucas_code_s = ''.join(ucas_code_s)
        try:
            if "Course Code:" in ucas_code_s:
                start = ucas_code_s.find("Course Code:")
                ucas_code = ucas_code_s[start:]
                ucas_code = ucas_code[:20]
                ucas_code = ucas_code.lstrip("Course Code:")
                item["ucas_code"] = ucas_code
            else:
                ucas_code = "NULL"
        except:
            ucas_code = "报错!"
        print(5,ucas_code)

        # degree_type = response.xpath('//div[@class="section picture-nav"]/h1/text()').extract()
        degree_type = response.xpath('//*[@id="main"]/div/h1/text()').extract()
        degree_type = ''.join(degree_type)
        # degree_type = self.getDegree_type(degree_type)
        try:
            if "Bachelor" in degree_type:
                degree_type = "Bachelor"
            elif "Master" in degree_type:
                degree_type = "Master"
            else:
                degree_type = "NULL"
        except:
            degree_type = "报错!"
        print(6,degree_type)

        start_date = 'NULL'
        # start_date = ''.join(start_date)
        # print(5,start_date)

        # overview = response.xpath('//div[@class="left logo-bg"]//text()').extract()
        overview = response.xpath('//*[@id="introduction"]//text()').extract()
        overview = ''.join(overview)
        print(7, overview)

        mode = 'NULL'
        # mode = ''.join(mode).replace('\r\n','')
        # mode = mode.replace('\n','')
        # mode = mode.replace('      ','')
        # print(7,mode)



        duration = 'NULL'
        # duration = ''.join(duration).replace('\r\n','')
        # duration = duration.replace('\n','')
        # duration = duration.replace('    ','')
        # print(8,duration)

        modules = response.xpath('//*[@id="unit_delivery_modes"]//text()').extract()
        modules = ''.join(modules)
        # modules = modules.replace('\n','')
        # try:
        #     if "Modules" in modules_s:
        #         start = modules_s.find("Modules")
        #         end = modules_s.find("Assessment")
        #         modules = modules_s[start:end]
        #         item["modules"] = modules
        #     else:
        #         modules = modules_s
        # except:
        #     modules = modules_s
        print(8,modules)

        teaching = 'NULL'

        assessment = "NULL"
        # assessment_s = ''.join(assessment_s)
        # try:
        #     if "Assessment" in assessment_s:
        #         start = assessment_s.find("Assessment")
        #         assessment = assessment_s[start:]
        #         item["assessment"] = assessment
        #     else:
        #         assessment = assessment_s
        # except:
        #     assessment = assessment_s
        # print(7, assessment)

        career_s = response.xpath('//*[@id="introduction"]//text()').extract()
        career_s = ''.join(career_s)

        try:
            if "Career opportunities" in career_s:
                start = career_s.find("Career opportunities")
                end = career_s.find("Course specific information")
                career = career_s[start:end]
                item["career"] = career
            else:
                career = "NULL"
        except:
            career = "报错!"
        print(8.5, career)

        application_date = "NULL"

        deadline = 'NULL'
        # deadline = ''.join(deadline)
        # print(9,deadline)

        application_fee = 'NULL'

        tuition_fee= response.xpath('//*[@id="fees"]//tr/td/text()').extract()
        tuition_fee = ''.join(tuition_fee)
        # tuition_fee = tuition_fee.replace('\n','')
        # tuition_fee = tuition_fee.replace('    ','')
        tuition_fee = self.getTuition_fee(tuition_fee)
        # try:
        #     if tuition_fee_s > 0:
        #         tuition_fee = tuition_fee_s
        #     else:
        #         tuition_fee = "NULL"
        # except:
        #     tuition_fee = "报错!"

        print(9, tuition_fee)

        location_s = response.xpath('//*[@id="main"]/div//tr//text()').extract()
        location_s = ''.join(location_s)
        try:
            if "Location:" in location_s:
                start = location_s.find("Location:")
                location = location_s[start:]
                location = location[:30]
                item["location"] = location
            else:
                location = "NULL"
        except:
            location = "报错!"
        print(10,location)

        ATAS = 'NULL'

        GPA = 'NULL'

        average_score = 'NULL'

        accredited_university = 'NULL'

        Alevel = 'NULL'

        IB = 'NULL'

        IELTS_s = response.xpath('//*[@id="main"]/div//tr//text()').extract()
        IELTS_s = ''.join(IELTS_s)
        # IELTS = re.findall('(IELTS:|IELTS)? (.*){0,5} \d?.\d? .{0,70}',IELTS)
        try:
            if "English Language Requirements:" in IELTS_s:
                start = IELTS_s.find("English Language Requirements:")
                IELTS = IELTS_s[start:]
                IELTS = IELTS[:150]
                item["IELTS"] = IELTS
            else:
                IELTS = "NULL"
        except:
            IELTS = "报错!"
        print(11, IELTS)

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
        LSAT = "NULL"
        MCAT = 'NULL'

        working_experience = 'NULL'

        interview = 'NULL'

        portfolio = 'NULL'

        application_documents = 'NULL'

        how_to_apply = 'NULL'
        # how_to_apply_s = ''.join(how_to_apply_s)
        # try:
        #     if "How to Apply" in how_to_apply_s:
        #         start = how_to_apply_s.find("How to Apply")
        #         end = how_to_apply_s.find("Entry requirements")
        #         how_to_apply = how_to_apply_s[start:end]
        #         item["how_to_apply"] = how_to_apply
        #     else:
        #         how_to_apply = how_to_apply_s
        # except:
        #     how_to_apply = '报错!'
        # print(11,how_to_apply)

        entry_requirements = response.xpath('//*[@id="admission"]//text()').extract()
        entry_requirements = ''.join(entry_requirements)
        # EntryRequirements = EntryRequirements.replace(' ','')
        # try:
        #     if "Entry requirements" in entry_requirements_s:
        #         start = entry_requirements_s.find("Entry requirements")
        #         end = entry_requirements_s.find("Study options")
        #         entry_requirements = entry_requirements_s[start:end]
        #         item["entry_requirements"] = entry_requirements
        #     else:
        #         entry_requirements = entry_requirements_s
        #
        # except:
        #     entry_requirements = '报错!'

        print(12,entry_requirements)

        chinese_requirements = "NULL"

        school_test = 'NULL'

        degree_description = "NULL"

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

    def getDegree_type(self, degree_type):
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
            elif "HND" in degree_type:
                degree_type = 'HND'
            elif len(degree_type) == 0:
                degree_type = 'NULL'

            else:
                degree_type = 'Ordinary degree'
        except:
            degree_type = "NULL"
        return degree_type

