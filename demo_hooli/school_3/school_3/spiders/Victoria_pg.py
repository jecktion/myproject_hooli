# -*- coding: utf-8 -*-






import scrapy
from school_3.items import HooliItem
import datetime
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import re

class PlymouthSpider(CrawlSpider):
    name = 'Victoria_pg'
    allowed_domains = ['www.vu.edu.au']
    start_urls = ['https://www.vu.edu.au/courses/search?f%5B0%5D=field_unit_lev%3Apostgrad&f%5B1%5D=field_study_mode%3AFull%20Time&page=0']
    # base_url = 'https://www.worcester.ac.uk%s'
    #
    # Lists = []
    #
    # for i in Lists:
    #     fullurl = base_url % i
    #     start_urls.append(fullurl)

    rules = (
        # Rule(LinkExtractor(allow=(r'.*'), restrict_xpaths=('')),callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'https://www.vu.edu.au/courses/search\?f%5B0%5D=field_unit_lev%3Apostgrad&f%5B1%5D=field_study_mode%3AFull%20Time&page=[0-8]'),follow=True),
        Rule(LinkExtractor(allow=(r'.*'),restrict_xpaths=('//*[@id="block-system-main"]/div/div/div/ol/li/h3/a')),callback='parse_item', follow=False),
        # Rule(LinkExtractor(allow=(r'.*'), restrict_xpaths=('//*[@id="wrapper"]//div[@class="component component--wysiwyg"]/p/font/a')),callback='parse_item', follow=False),
    )

    def parse_item(self,response):
        print('==================================',response.url)
        item = HooliItem()

        url = response.url
        print(1,url)

        university = 'Victoria University'
        print(2,university)

        department_s = response.xpath('//*[@id="block-ds-extras-title-area-course-information"]//text()').extract()
        department_s = ''.join(department_s).replace('\n','')
        try:
            if "Offered by:" in department_s:
                start = department_s.find("Offered by:")
                department = department_s[start:]
                department = department[:80]
                department = department.lstrip("Offered by:")
                item["department"] = department
            else:
                department = "NULL"

        except:
            department = "报错!"

        print(3,department)

        country = 'Australia'
        city = "Sydney"
        website = 'https://www.westernsydney.edu.au'
        degree_level = '1'

        # programme = response.xpath('//div[@class="section picture-nav"]/h1/text()').extract()
        programme = response.xpath('//*[@id="title-box"]//div/h1/text()').extract()
        programme = ''.join(programme)
        print(4,programme)

        ucas_code_s = response.xpath('//*[@id="block-ds-extras-title-area-course-information"]//text()').extract()
        ucas_code_s = ''.join(ucas_code_s).replace('    ','').replace('\n','')
        try:
            if "VU course code:" in ucas_code_s:
                start = ucas_code_s.find("VU course code:")
                ucas_code = ucas_code_s[start:]
                ucas_code = ucas_code[:50]
                ucas_code = ucas_code.lstrip("VU course code:")
                item["ucas_code"] = ucas_code
            else:
                ucas_code = "NULL"
        except:
            ucas_code = "报错!"
        print(5,ucas_code)

        # degree_type = response.xpath('//div[@class="section picture-nav"]/h1/text()').extract()
        degree_type = response.xpath('//*[@id="title-box"]//div/h1/text()').extract()
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

        start_date = "NULL"
        # start_date_s = ''.join(start_date_s)
        # try:
        #     if "Autumn" in start_date_s:
        #         start = start_date_s.find("Autumn")
        #         start_date = start_date_s[start:]
        #         item["start_date"] = start_date
        #     else:
        #         start_date = "NULL"
        # except:
        #     start_date = "报错!"
        # print(7,start_date)

        # overview = response.xpath('//div[@class="left logo-bg"]//text()').extract()
        overview = response.xpath('//*[@id="overview"]//text()').extract()
        overview = ''.join(overview).replace('\n','')
        print(7, overview)

        mode_s = response.xpath('//*[@id="block-ds-extras-course-essentials"]//text()').extract()
        mode_s = ''.join(mode_s)
        try:
            if "Delivery mode:" in mode_s:
                start = mode_s.find("Delivery mode:")
                mode = mode_s[start:]
                mode = mode[:80]
                mode = mode.lstrip("Delivery mode:")
                item["mode"] = mode
            else:
                mode = "NULL"
        except:
            mode = "报错!"
        print(8,mode)



        duration_s = response.xpath('//*[@id="block-ds-extras-course-essentials"]//text()').extract()
        duration_s = ''.join(duration_s)
        # duration = duration.replace('\n','')
        # duration = duration.replace('    ','')
        try:
            if "Duration:" in duration_s:
                start = duration_s.find("Duration:")
                end = duration_s.find("Location:")
                duration = duration_s[start:end]
                duration = duration.lstrip("Duration:")
                item["duration"] = duration
            else:
                duration = "NULL"
        except:
            duration = "报错!"
        print(9,duration)

        modules = response.xpath('//*[@id="course-structure"]//text()').extract()
        modules = ''.join(modules)
        modules = modules.replace('\n','')
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
        print(10,modules)

        teaching = 'NULL'

        assessment_s = response.xpath('//*[@class="section"]//text()').extract()
        assessment_s = ''.join(assessment_s).replace("\r\n","").replace('      ','').replace('\n','')
        try:
            if "Admission & pathways" in assessment_s:
                start = assessment_s.find("Admission & pathways")
                end = assessment_s.find("How to apply")
                assessment = assessment_s[start:end]
                item["assessment"] = assessment
            else:
                assessment = "NULL"
        except:
            assessment = "报错!"
        print(11, assessment)

        career = response.xpath('//*[@id="careers"]//text()').extract()
        career = ''.join(career).replace('\r\n','').replace('      ','').replace('\n','')

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
        print(12, career)

        application_date = "NULL"

        deadline = 'NULL'
        # deadline = ''.join(deadline)
        # print(9,deadline)

        application_fee = 'NULL'

        tuition_fee_s = response.xpath('//*[@id="block-vu-core-vu-cbs-course-fees"]/p/text()').extract()
        tuition_fee_s = ''.join(tuition_fee_s)
        # tuition_fee = tuition_fee.replace('\n','')
        # tuition_fee = tuition_fee.replace('    ','')
        tuition_fee_s = self.getTuition_fee(tuition_fee_s)
        try:
            if tuition_fee_s > 0:
                tuition_fee = tuition_fee_s
            else:
                tuition_fee = "CSP"
        except:
            tuition_fee = "报错!"

        print(13, tuition_fee)

        location_s = response.xpath('//*[@id="block-ds-extras-course-essentials"]//text()').extract()
        location_s = ''.join(location_s)
        try:
            if "Location:" in location_s:
                start = location_s.find("Location:")
                location = location_s[start:]
                location = location[:30]
                location = location.lstrip("Location:")
                item["location"] = location
            else:
                location = "NULL"
        except:
            location = "报错!"
        print(14,location)

        ATAS = 'NULL'

        GPA = 'NULL'

        average_score = 'NULL'

        accredited_university = 'NULL'

        Alevel = 'NULL'

        IB = 'NULL'

        IELTS = 'NULL'
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

        how_to_apply = response.xpath('//*[@class="section"]//div[@class="pane-content"]/p/text()').extract()
        how_to_apply = ''.join(how_to_apply)
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
        print(15,how_to_apply)

        entry_requirements = "NULL"
        # entry_requirements = ''.join(entry_requirements)
        # # EntryRequirements = EntryRequirements.replace(' ','')
        # # try:
        # #     if "Entry requirements" in entry_requirements_s:
        # #         start = entry_requirements_s.find("Entry requirements")
        # #         end = entry_requirements_s.find("Study options")
        # #         entry_requirements = entry_requirements_s[start:end]
        # #         item["entry_requirements"] = entry_requirements
        # #     else:
        # #         entry_requirements = entry_requirements_s
        # #
        # # except:
        # #     entry_requirements = '报错!'
        #
        # print(12,entry_requirements)

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
        print(16, create_time)

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

        # yield item

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

