
# -*- coding: utf-8 -*-






import scrapy
from school_3.items import HooliItem
import datetime
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import re

class PlymouthSpider(CrawlSpider):
    name = 'Queensland_ug'
    allowed_domains = ['www.cqu.edu.au']
    start_urls = ['https://www.cqu.edu.au/courses/undergraduate']
    # base_url = 'https://www.worcester.ac.uk%s'
    #
    # Lists = []
    #
    # for i in Lists:
    #     fullurl = base_url % i
    #     start_urls.append(fullurl)

    rules = (
        # Rule(LinkExtractor(allow=(r'.*'), restrict_xpaths=('')),callback='parse_item', follow=True),
        # Rule(LinkExtractor(allow=r''),follow=True),
        Rule(LinkExtractor(allow=(r'.*'),restrict_xpaths=('//*[@id="new_div_53285"]/li/a')),callback='parse_item', follow=False),
        # Rule(LinkExtractor(allow=r'.*\?show=international'),callback='parse_item',follow=False),
    )

    def parse_item(self,response):
        print('==================================',response.url)
        item = HooliItem()

        url = response.url
        print(1,url)

        university = 'Central Queensland University'
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
        city = "Queensland"
        website = 'https://www.cqu.edu.au'
        degree_level = '0'

        # programme = response.xpath('//div[@class="section picture-nav"]/h1/text()').extract()
        programme = response.xpath('//*[@id="main"]/div/h1/text()').extract()
        programme = ''.join(programme)
        print(3,programme)

        ucas_code_s = response.xpath('//*[@id="main"]//div/table/tbody/tr//text()').extract()
        ucas_code_s = ''.join(ucas_code_s)
        try:
            if "CRICOS" in ucas_code_s:
                start = ucas_code_s.find("CRICOS")
                ucas_code = ucas_code_s[start:]
                ucas_code = ucas_code[:20]
                ucas_code = ucas_code.lstrip("CRICOS")
                item["ucas_code"] = ucas_code
            else:
                ucas_code = "NULL"
        except:
            ucas_code = "报错!"
        print(4,ucas_code)

        # degree_type = response.xpath('//div[@class="section picture-nav"]/h1/text()').extract()
        degree_type = response.xpath('//*[@id="main"]/div/h1/text()').extract()
        degree_type = ''.join(degree_type)
        # degree_type = self.getDegree_type(degree_type)
        try:
            if "Bachelor" in degree_type:
                degree_type = "Bachelor"
            elif "Graduate " in degree_type:
                degree_type = "Graduate "
            else:
                degree_type = "NULL"
        except:
            degree_type = "报错!"
        print(5,degree_type)

        start_date_s = response.xpath('//*[@id="main"]//div/table/tbody/tr//text()').extract()
        start_date_s = ''.join(start_date_s)
        try:
            if "Intake dates" in start_date_s:
                start = start_date_s.find("Intake dates")
                start_date = start_date_s[start:]
                start_date = start_date[:40]
                start_date = start_date.lstrip("Intake dates")
                item["start_date"] = start_date
            else:
                start_date = "NULL"
        except:
            start_date = "报错!"
        print(5.0,start_date)

        # overview = response.xpath('//div[@class="left logo-bg"]//text()').extract()
        overview = response.xpath('//*[@id="main"]//*[@class="tab overview-tab"]//text()').extract()
        overview = ''.join(overview).replace('\r\n','').replace('      ','')
        print(6, overview)


        mode_s = response.xpath('//*[@id="main"]//div/table/tbody/tr//text()').extract()
        mode_s = ''.join(mode_s)
        try:
            if "Duration" in mode_s:
                start = mode_s.find("Duration")
                end = mode_s.find("Intake dates")
                mode = mode_s[start:end]
                mode = mode[:80]
                item["mode"] = mode
            else:
                mode = "NULL"
        except:
            mode = "报错!"

        print(7,mode)



        duration_s = response.xpath('//*[@id="main"]//div/table/tbody/tr//text()').extract()
        duration_s = ''.join(duration_s)
        try:
            if "Duration" in duration_s:
                start = duration_s.find("Duration")
                end = duration_s.find("Intake dates")
                duration = duration_s[start:end]
                duration = duration[:80]
                item["duration"] = duration
            else:
                duration = "NULL"
        except:
            duration = "报错!"

        print(8,duration)

        modules = "NULL"
        # modules = ''.join(modules)
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
        # print(8,modules)

        teaching = 'NULL'

        assessment = response.xpath('//*[@id="main"]//div[@class="tab structure-tab"]//text()').extract()
        assessment = ''.join(assessment).replace('\r\n','').replace('    ','')
        # try:
        #     if "Assessment" in assessment_s:
        #         start = assessment_s.find("Assessment")
        #         assessment = assessment_s[start:]
        #         item["assessment"] = assessment
        #     else:
        #         assessment = assessment_s
        # except:
        #     assessment = assessment_s
        print(9, assessment)

        career = response.xpath('//*[@id="main"]//*[@class="careers"]//text()').extract()
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

        tuition_fee= response.xpath('//*[@id="main"]//div[@class="tab fees-tab"]//h4/text()').extract()
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

        print(11, tuition_fee)

        location = "Queensland"
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
        print(12,location)

        ATAS = 'NULL'

        GPA = 'NULL'

        average_score = 'NULL'

        accredited_university = 'NULL'

        Alevel = 'NULL'

        IB = 'NULL'

        IELTS_s = response.xpath('//*[@id="main"]//*[@class="tab entry-reqs-tab"]//text()').extract()
        IELTS_s = ''.join(IELTS_s).replace('    ','')
        # IELTS = re.findall('(IELTS:|IELTS)? (.*){0,5} \d?.\d? .{0,70}',IELTS)
        try:
            if "English Requirement" in IELTS_s:
                start = IELTS_s.find("IELTS")
                IELTS = IELTS_s[start:]
                IELTS = IELTS[:250]
                item["IELTS"] = IELTS
            else:
                IELTS = "NULL"
        except:
            IELTS = "报错!"
        print(12, IELTS)

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

        how_to_apply = response.xpath('//*[@id="main"]//div[@class="tab apply-tab"]//text()').extract()
        how_to_apply = ''.join(how_to_apply).replace('\r\n','').replace('    ','')
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
        print(13,how_to_apply)

        entry_requirements = response.xpath('//*[@id="main"]//*[@class="tab entry-reqs-tab"]//text()').extract()
        entry_requirements = ''.join(entry_requirements).replace('\r\n','').replace('    ','')
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

        print(14,entry_requirements)

        chinese_requirements = "NULL"

        school_test = 'NULL'

        degree_description = response.xpath('//*[@id="main"]//*[@class="tab details-tab"]//text()').extract()
        degree_description = ''.join(degree_description).replace('\r\n','').replace('    ','')
        print(15,degree_description)

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
        allfee = re.findall(r'\d+\s\d+', tuition_fee)
        # print(allfee)
        for index in range(len(allfee)):
            fee = allfee[index].split(" ")
            allfee[index] = ''.join(fee)
            # print(allfee[index])
        # print(allfee)
        maxfee = 0
        for fee in allfee:
            if int(fee) >= maxfee:
                maxfee = int(fee)
        return maxfee



