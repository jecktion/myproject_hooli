# -*- coding: utf-8 -*-






import scrapy
from school_3.items import HooliItem
import datetime
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor

import re
import time
from lxml import etree
import requests

class PlymouthSpider(scrapy.Spider):
    name = 'Edith_Cowan_pg'
    allowed_domains = ['www.ecu.edu.au']
    start_urls = []
    base_url = '%s'

    Lists = ['http://www.ecu.edu.au/degrees/courses/master-of-business-administration',
'http://www.ecu.edu.au/degrees/courses/master-of-business-administration-international',
'http://www.ecu.edu.au/degrees/courses/master-of-clinical-nursing',
'http://www.ecu.edu.au/degrees/courses/master-of-communication',
'http://www.ecu.edu.au/degrees/courses/master-of-computer-science',
'http://www.ecu.edu.au/degrees/courses/master-of-counselling-and-psychotherapy',
'http://www.ecu.edu.au/degrees/courses/master-of-critical-care-paramedicine',
'http://www.ecu.edu.au/degrees/courses/master-of-cyber-security',
'http://www.ecu.edu.au/degrees/courses/master-of-design',
'http://www.ecu.edu.au/degrees/courses/master-of-disaster-and-emergency-response',
'http://www.ecu.edu.au/degrees/courses/master-of-education',
'http://www.ecu.edu.au/degrees/courses/master-of-education-advanced',
'http://www.ecu.edu.au/degrees/courses/master-of-engineering',
'http://www.ecu.edu.au/degrees/courses/master-of-environmental-management',
'http://www.ecu.edu.au/degrees/courses/master-of-environmental-science',
'http://www.ecu.edu.au/degrees/courses/master-of-exercise-science-strength-and-conditioning',
'http://www.ecu.edu.au/degrees/courses/master-of-finance-and-banking',
'http://www.ecu.edu.au/degrees/courses/master-of-human-resource-management',
'http://www.ecu.edu.au/degrees/courses/master-of-information-technology',
'http://www.ecu.edu.au/degrees/courses/master-of-international-hospitality-management',
'http://www.ecu.edu.au/degrees/courses/master-of-management-information-systems',
'http://www.ecu.edu.au/degrees/courses/master-of-marketing-and-innovation-management',
'http://www.ecu.edu.au/degrees/courses/master-of-midwifery-practice',
'http://www.ecu.edu.au/degrees/courses/master-of-nurse-education',
'http://www.ecu.edu.au/degrees/courses/master-of-nursing',
'http://www.ecu.edu.au/degrees/courses/master-of-nursing-graduate-entry',
'http://www.ecu.edu.au/degrees/courses/master-of-nursing-nurse-practitioner',
'http://www.ecu.edu.au/degrees/courses/master-of-nutrition-and-dietetics',
'http://www.ecu.edu.au/degrees/courses/master-of-occupational-health-and-safety',
'http://www.ecu.edu.au/degrees/courses/master-of-occupational-hygiene-and-toxicology',
'http://www.ecu.edu.au/degrees/courses/master-of-paramedic-practitioner',
'http://www.ecu.edu.au/degrees/courses/master-of-professional-accounting',
'http://www.ecu.edu.au/degrees/courses/master-of-professional-communication',
'http://www.ecu.edu.au/degrees/courses/master-of-professional-design',
'http://www.ecu.edu.au/degrees/courses/master-of-project-management',
'http://www.ecu.edu.au/degrees/courses/master-of-psychology',
'http://www.ecu.edu.au/degrees/courses/master-of-public-health',
'http://www.ecu.edu.au/degrees/courses/master-of-science-assisted-reproductive-technology',
'http://www.ecu.edu.au/degrees/courses/master-of-screen-studies',
'http://www.ecu.edu.au/degrees/courses/master-of-teaching-early-childhood',
'http://www.ecu.edu.au/degrees/courses/master-of-teaching-primary',
'http://www.ecu.edu.au/degrees/courses/master-of-teaching-secondary',
'http://www.ecu.edu.au/degrees/courses/master-of-arts-performing-arts',
'http://www.ecu.edu.au/degrees/courses/master-of-arts-by-research',
'http://www.ecu.edu.au/degrees/courses/master-of-business-by-research',
'http://www.ecu.edu.au/degrees/courses/master-of-criminal-justice-by-research',
'http://www.ecu.edu.au/degrees/courses/master-of-education-by-research',
'http://www.ecu.edu.au/degrees/courses/master-of-engineering-science',
'http://www.ecu.edu.au/degrees/courses/master-of-laws-research',
'http://www.ecu.edu.au/degrees/courses/master-of-midwifery-research',
'http://www.ecu.edu.au/degrees/courses/master-of-nursing-research',
'http://www.ecu.edu.au/degrees/courses/master-of-paramedical-science-by-research',
'http://www.ecu.edu.au/degrees/courses/master-of-public-health-by-research',
'http://www.ecu.edu.au/degrees/courses/master-of-science-biological-sciences',
'http://www.ecu.edu.au/degrees/courses/master-of-science-chemistry',
'http://www.ecu.edu.au/degrees/courses/master-of-science-computer-science',
'http://www.ecu.edu.au/degrees/courses/master-of-science-environmental-management',
'http://www.ecu.edu.au/degrees/courses/master-of-science-interdisciplinary-studies',
'http://www.ecu.edu.au/degrees/courses/master-of-science-mathematics-and-planning',
'http://www.ecu.edu.au/degrees/courses/master-of-science-medical-science',
'http://www.ecu.edu.au/degrees/courses/master-of-science-sports-science',
'http://www.ecu.edu.au/degrees/courses/master-of-social-science',
'http://www.ecu.edu.au/degrees/courses/doctor-of-philosophy',
'http://www.ecu.edu.au/degrees/courses/doctor-of-philosophy-integrated']

    for i in Lists:
        fullurl = base_url % i
        start_urls.append(fullurl)

    # rules = (
    #     # Rule(LinkExtractor(allow=(r'.*'), restrict_xpaths=('')),callback='parse_item', follow=True),
    #     # Rule(LinkExtractor(allow=r''),follow=True),
    #     Rule(LinkExtractor(allow=(r'.*'),restrict_xpaths=('//*[@id="degree-1-content"]/ul/li/a')),callback='parse_item', follow=False),
    # )

    def parse(self,response):
        print('==================================',response.url)
        item = HooliItem()

        url = response.url
        print(1,url)

        university = 'Edith Cowan University'
        print(2,university)

        department = "NULL"
        # department_s = ''.join(department_s)
        # try:
        #     if "Faculty:" in department_s:
        #         start = department_s.find("Faculty:")
        #         department = department_s[start:]
        #         department = department[:48]
        #         item["department"] = department
        #     else:
        #         department = "NULL"
        #
        # except:
        #     department = "报错!"

        # print(3,department)

        country = 'Australia'
        city = "NULL"
        website = 'http://www.ecu.edu.au'
        degree_level = '1'

        # programme = response.xpath('//div[@class="section picture-nav"]/h1/text()').extract()
        programme = response.xpath('//*[@id="content-2013"]/div/div/div/div/h2/text()').extract()
        programme = ''.join(programme)
        print(3,programme)

        ucas_code = response.xpath('//*[@id="content-2013"]//div[@class="courseOverview__meta"]/span//text()').extract()
        ucas_code = ''.join(ucas_code)
        # try:
        #     if "Course Code:" in ucas_code_s:
        #         start = ucas_code_s.find("Course Code:")
        #         ucas_code = ucas_code_s[start:]
        #         ucas_code = ucas_code[:20]
        #         ucas_code = ucas_code.lstrip("Course Code:")
        #         item["ucas_code"] = ucas_code
        #     else:
        #         ucas_code = "NULL"
        # except:
        #     ucas_code = "报错!"
        print(4,ucas_code)

        # degree_type = response.xpath('//div[@class="section picture-nav"]/h1/text()').extract()
        degree_type = response.xpath('//*[@id="content-2013"]/div/div/div/div/h2/text()').extract()
        degree_type = ''.join(degree_type)
        # degree_type = self.getDegree_type(degree_type)
        try:
            if "Associate Degree" in degree_type:
                degree_type = "Associate Degree"
            elif "Bachelor" in degree_type:
                degree_type = "Bachelor"
            elif "Master" in degree_type:
                degree_type = "Master"
            elif "Graduate" in degree_type:
                degree_type = "Graduate"
            else:
                degree_type = "NULL"
        except:
            degree_type = "报错!"
        print(5,degree_type)

        start_date = 'NULL'
        # start_date = ''.join(start_date)
        # print(5,start_date)

        # overview = response.xpath('//div[@class="left logo-bg"]//text()').extract()
        overview = response.xpath('//*[@id="content-2013"]//div[@class="course-related-info more courseIntro block-overview"]//p/text()').extract()
        overview = ''.join(overview)
        print(6, overview)

        mode_s = response.xpath('//div[@class="studyCampus__location studyCampus__location--joondalup studyCampus__location--active"]//text() | //*[@id="content-2013"]//div[@class="courseOverview__info courseOverview__info--international"]//header[@class="studyCampus__header"]//text()').extract()
        mode_s = ''.join(mode_s).replace('\r\n','').replace('\t','').replace('\n','')
        # mode = mode.replace('\n','')
        # mode = mode.replace('      ','')
        try:
            if len(mode_s) > 255:
                mode = mode_s[:255]
            else:
                mode = mode_s
        except:
            mode = "报错!"
        print(7,mode)



        duration_s = response.xpath('//div[@class="studyCampus__location studyCampus__location--joondalup studyCampus__location--active"]//text() | //*[@id="content-2013"]//div[@class="courseOverview__info courseOverview__info--international"]//header[@class="studyCampus__header"]//text()').extract()
        duration_s = ''.join(duration_s).replace('\r\n','').replace('\t','').replace('\n','')
        # duration = duration.replace('\n','')
        # duration = duration.replace('    ','')
        if len(duration_s) > 255:
            duration = duration_s[:255]
        else:
            duration = duration_s

        print(8,duration)

        modules = response.xpath('//*[@id="during-the-course"]//div[@class="structure-heading"]//text()').extract()
        time.sleep(1)
        modules = ''.join(modules).replace('\t','')
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
        print(9,modules)

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

        career = response.xpath('//*[@id="during-the-course"]/div[@class="course-detail-info"]/p/text()').extract()
        career = ''.join(career)

        # try:
        #     if "Career opportunities" in career_s:
        #         start = career_s.find("Career opportunities")
        #         end = career_s.find("Course specific information")
        #         career = career_s[start:end]
        #         item["career"] = career
        #     else:
        #         career = "NULL"
        # except:
        #     career = "报错!"
        print(10, career)

        application_date = "NULL"

        deadline = 'NULL'
        # deadline = ''.join(deadline)
        # print(9,deadline)

        application_fee = 'NULL'

        tuition_fee= "NULL"
        # tuition_fee = ''.join(tuition_fee)
        # # tuition_fee = tuition_fee.replace('\n','')
        # # tuition_fee = tuition_fee.replace('    ','')
        # tuition_fee = self.getTuition_fee(tuition_fee)
        # # try:
        #     if tuition_fee_s > 0:
        #         tuition_fee = tuition_fee_s
        #     else:
        #         tuition_fee = "NULL"
        # except:
        #     tuition_fee = "报错!"

        # print(9, tuition_fee)

        location = "NULL"
        # location_s = ''.join(location_s)
        # try:
        #     if "Location:" in location_s:
        #         start = location_s.find("Location:")
        #         location = location_s[start:]
        #         location = location[:30]
        #         item["location"] = location
        #     else:
        #         location = "NULL"
        # except:
        #     location = "报错!"
        # print(10,location)

        ATAS = 'NULL'

        GPA = 'NULL'

        average_score = 'NULL'

        accredited_university = 'NULL'

        Alevel = 'NULL'

        IB = 'NULL'

        IELTS = "NULL"
        # IELTS_s = ''.join(IELTS_s)
        # # IELTS = re.findall('(IELTS:|IELTS)? (.*){0,5} \d?.\d? .{0,70}',IELTS)
        # try:
        #     if "English Language Requirements:" in IELTS_s:
        #         start = IELTS_s.find("English Language Requirements:")
        #         IELTS = IELTS_s[start:]
        #         IELTS = IELTS[:150]
        #         item["IELTS"] = IELTS
        #     else:
        #         IELTS = "NULL"
        # except:
        #     IELTS = "报错!"
        # print(11, IELTS)

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

        entry_requirements_url = response.xpath('//*[@id="before-you-start"]/div[@class="course-detail-info"]/div[@class="row-fluid"]/div[@class="span12 courseOverview__beforeRequirement"]/p[1]/a/@href | //*[@id="before-you-start"]/div[@class="course-detail-info"]/div[@class="row-fluid"]/div[@class="span6 courseOverview__beforeRequirement"][2]/p[1]/a/@href').extract()
        entry_requirements_url = ''.join(entry_requirements_url).replace('//', 'http://')
        print('entry_requirements_url:', entry_requirements_url)
        self.parse_entry_requirements(entry_requirements_url, item)
        # entry_requirements = response.xpath('//*[@id="before-you-start"]//div[@class="row-fluid"]//text()').extract()
        # entry_requirements = ''.join(entry_requirements).replace('\t','').replace('\n','')
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

        # print(11,entry_requirements)

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
        # item["entry_requirements"] = entry_requirements
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

    def parse_entry_requirements(self,entry_requirements_url,item):
        print('2,==================',entry_requirements_url)
        data = requests.get(entry_requirements_url)
        response = etree.HTML(data.text)
        entry_requirements_url_s = response.xpath('//div[@class="span6"]/div[@id="content_container_667316"]/p[5]/a[1]/@href')
        entry_requirements_url_s = ''.join(entry_requirements_url_s)
        self.parse_entry_requirements_s(entry_requirements_url_s,item)

    def parse_entry_requirements_s(self,entry_requirements_url_s,item):
        print('3,=================',entry_requirements_url_s)
        data = requests.get(entry_requirements_url_s)
        response = etree.HTML(data.text)
        entry_requirements_a = response.xpath('//div[@class="school-results"]/following-sibling::script//text()')
        print('entry_requirements_a:', entry_requirements_a)
        entry_requirements_a = ''.join(entry_requirements_a)

        entry_requirements_b = re.findall(r'/degrees/shared-content/nested-content/.*\?country=',entry_requirements_a)
        entry_requirements_b = ''.join(entry_requirements_b)
        print('entry_requirements_b:',entry_requirements_b)
        entry_requirements_c = 'http://www.ecu.edu.au' + entry_requirements_b + 'china'
        print('entry_requirements_c:',entry_requirements_c)
        self.parse_entry_requirements_item(entry_requirements_c,item)

    def parse_entry_requirements_item(self,entry_requirements_c,item):
        print('4,=======================',entry_requirements_c)
        data = requests.get(entry_requirements_c)
        response = etree.HTML(data.text)
        entry_requirements = response.xpath('/html/body//text()')
        entry_requirements = ''.join(entry_requirements)
        print("entry_requirements:",entry_requirements)
        item["entry_requirements"] = entry_requirements


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

