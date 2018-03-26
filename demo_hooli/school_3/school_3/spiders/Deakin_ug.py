
# -*- coding: utf-8 -*-






import scrapy
from school_3.items import HooliItem
import datetime
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import re

class PlymouthSpider(scrapy.Spider):
    name = 'Deakin_ug'
    allowed_domains = ['www.deakin.edu.au']
    start_urls = []

    # url = 'http://www.deakin.edu.au/courses/find-a-course/results?dkncoursestudent=International&dkncoursequal=under_diploma&dkncoursequal=under_associate&dkncoursequal=under_bachelor_degree&dkncoursequal=under_bachelor_honours&q=&dknpagetype=Course&startrow='
    # offset = 0
    # start_urls = [url + str(offset)]
    # print(start_urls)

    base_url = '%s'

    Lists = ['http://www.deakin.edu.au/course/bachelor-commerce-international',
'http://www.deakin.edu.au/course/bachelor-information-technology-international',
'http://www.deakin.edu.au/course/bachelor-arts-international',
'http://www.deakin.edu.au/course/bachelor-psychological-science-international',
'http://www.deakin.edu.au/course/bachelor-nutrition-science-international',
'http://www.deakin.edu.au/course/bachelor-science-international',
'http://www.deakin.edu.au/course/bachelor-criminology-bachelor-cyber-security-international',
'http://www.deakin.edu.au/course/bachelor-biomedical-science-international',
'http://www.deakin.edu.au/course/bachelor-medicine-bachelor-surgery-international',
'http://www.deakin.edu.au/course/bachelor-sport-development-international',
'http://www.deakin.edu.au/course/bachelor-health-and-physical-education-international',
'http://www.deakin.edu.au/course/bachelor-nursing-international',
'http://www.deakin.edu.au/course/bachelor-nursing-honours-international',
'http://www.deakin.edu.au/course/bachelor-electrical-and-electronics-engineering-honours-international',
'http://www.deakin.edu.au/course/bachelor-science-master-teaching-secondary-international',
'http://www.deakin.edu.au/course/bachelor-communication-journalism-international',
'http://www.deakin.edu.au/course/bachelor-creative-arts-drama-international',
'http://www.deakin.edu.au/course/bachelor-information-technology-honours-international',
'http://www.deakin.edu.au/course/bachelor-mechanical-engineering-honours-international',
'http://www.deakin.edu.au/course/bachelor-design-architecture-international',
'http://www.deakin.edu.au/course/bachelor-nursing-bachelor-public-health-and-health-promotion-international',
'http://www.deakin.edu.au/course/bachelor-health-and-medical-science-honours-international',
'http://www.deakin.edu.au/course/bachelor-creative-writing-international',
'http://www.deakin.edu.au/course/bachelor-psychological-science-honours-international',
'http://www.deakin.edu.au/course/bachelor-film-television-and-animation-international',
'http://www.deakin.edu.au/course/bachelor-education-early-years-international',
'http://www.deakin.edu.au/course/bachelor-arts-master-teaching-secondary-international',
'http://www.deakin.edu.au/course/bachelor-arts-chinese-bachelor-commerce-international',
'http://www.deakin.edu.au/course/bachelor-arts-bachelor-laws-international',
'http://www.deakin.edu.au/course/bachelor-arts-bachelor-science-international',
'http://www.deakin.edu.au/course/bachelor-biological-science-international',
'http://www.deakin.edu.au/course/bachelor-civil-engineering-honours-international',
'http://www.deakin.edu.au/course/bachelor-commerce-bachelor-information-systems-international',
'http://www.deakin.edu.au/course/bachelor-commerce-bachelor-science-international',
'http://www.deakin.edu.au/course/bachelor-communication-public-relations-international',
'http://www.deakin.edu.au/course/bachelor-computer-science-international',
'http://www.deakin.edu.au/course/bachelor-creative-arts-honours-international',
'http://www.deakin.edu.au/course/bachelor-creative-arts-photography-international',
'http://www.deakin.edu.au/course/bachelor-creative-arts-visual-arts-international',
'http://www.deakin.edu.au/course/bachelor-criminology-international',
'http://www.deakin.edu.au/course/bachelor-criminology-bachelor-laws-international',
'http://www.deakin.edu.au/course/bachelor-criminology-bachelor-psychological-science-international',
'http://www.deakin.edu.au/course/bachelor-design-architecture-bachelor-construction-management-honours-international',
'http://www.deakin.edu.au/course/bachelor-education-primary-international',
'http://www.deakin.edu.au/course/bachelor-environmental-science-environmental-management-and-sustainability-international',
'http://www.deakin.edu.au/course/bachelor-environmental-science-honours-international',
'http://www.deakin.edu.au/course/bachelor-exercise-and-sport-science-international',
'http://www.deakin.edu.au/course/bachelor-exercise-and-sport-science-bachelor-business-sport-management-international',
'http://www.deakin.edu.au/course/bachelor-forensic-science-international',
'http://www.deakin.edu.au/course/bachelor-forensic-science-honours-international',
'http://www.deakin.edu.au/course/bachelor-forensic-science-bachelor-criminology-international',
'http://www.deakin.edu.au/course/bachelor-health-sciences-international',
'http://www.deakin.edu.au/course/bachelor-health-sciences-bachelor-arts-international',
'http://www.deakin.edu.au/course/bachelor-cyber-security-international',
'http://www.deakin.edu.au/course/bachelor-information-systems-international',
'http://www.deakin.edu.au/course/bachelor-information-systems-bachelor-information-technology-international',
'http://www.deakin.edu.au/course/bachelor-international-studies-international',
'http://www.deakin.edu.au/course/bachelor-international-studies-bachelor-commerce-international',
'http://www.deakin.edu.au/course/bachelor-laws-honours-international',
'http://www.deakin.edu.au/course/bachelor-property-and-real-estate-international',
'http://www.deakin.edu.au/course/bachelor-public-health-and-health-promotion-international',
'http://www.deakin.edu.au/course/bachelor-public-health-and-health-promotion-bachelor-commerce-international',
'http://www.deakin.edu.au/course/bachelor-science-bachelor-laws-international',
'http://www.deakin.edu.au/course/bachelor-social-work-international',
'http://www.deakin.edu.au/course/bachelor-vision-science-master-optometry-international',
'http://www.deakin.edu.au/course/bachelor-zoology-and-animal-science-international',
'http://www.deakin.edu.au/course/bachelor-arts-psychology-honours-international',
'http://www.deakin.edu.au/course/bachelor-exercise-and-sport-science-honours-international',
'http://www.deakin.edu.au/course/bachelor-health-sciences-honours-international',
'http://www.deakin.edu.au/course/bachelor-public-health-and-health-promotion-honours-international',
'http://www.deakin.edu.au/course/bachelor-nutrition-science-bachelor-commerce-international',
'http://www.deakin.edu.au/course/bachelor-arts-advanced-honours-international',
'http://www.deakin.edu.au/course/bachelor-international-studies-global-scholar-international',
'http://www.deakin.edu.au/course/bachelor-food-and-nutrition-sciences-honours-international',
'http://www.deakin.edu.au/course/bachelor-arts-master-arts-international-relations-international',
'http://www.deakin.edu.au/course/bachelor-business-international',
'http://www.deakin.edu.au/course/bachelor-design-3d-animation-international',
'http://www.deakin.edu.au/course/bachelor-design-digital-technologies-international',
'http://www.deakin.edu.au/course/bachelor-business-sport-management-international',
'http://www.deakin.edu.au/course/bachelor-commerce-bachelor-laws-international',
'http://www.deakin.edu.au/course/bachelor-communication-honours-international',
'http://www.deakin.edu.au/course/bachelor-construction-management-honours-international',
'http://www.deakin.edu.au/course/bachelor-environmental-science-marine-biology-international',
'http://www.deakin.edu.au/course/bachelor-environmental-science-wildlife-and-conservation-biology-international',
'http://www.deakin.edu.au/course/bachelor-laws-bachelor-international-studies-international',
'http://www.deakin.edu.au/course/bachelor-mechatronics-engineering-honours-international',
'http://www.deakin.edu.au/course/bachelor-nursing-bachelor-midwifery-international',
'http://www.deakin.edu.au/course/bachelor-occupational-therapy-international',
'http://www.deakin.edu.au/course/bachelor-property-and-real-estate-bachelor-commerce-international',
'http://www.deakin.edu.au/course/bachelor-property-and-real-estate-bachelor-laws-international',
'http://www.deakin.edu.au/course/bachelor-science-honours-international',
'http://www.deakin.edu.au/course/bachelor-arts-honours-international',
'http://www.deakin.edu.au/course/bachelor-communication-digital-media-international',
'http://www.deakin.edu.au/course/bachelor-software-engineering-honours-international',
'http://www.deakin.edu.au/course/bachelor-arts-bachelor-commerce-international',
'http://www.deakin.edu.au/course/bachelor-communication-advertising-international',
'http://www.deakin.edu.au/course/bachelor-environmental-engineering-honours-international',
'http://www.deakin.edu.au/course/bachelor-laws-international',
'http://www.deakin.edu.au/course/bachelor-arts-psychology-international',
'http://www.deakin.edu.au/course/bachelor-nursing-bachelor-psychological-science-international',
'http://www.deakin.edu.au/course/bachelor-design-visual-communication-international']



    for i in Lists:
        fullurl = base_url % i
        start_urls.append(fullurl)

    # rules = (
    #     # Rule(LinkExtractor(allow=(r'.*'), restrict_xpaths=('')),callback='parse_item', follow=True),
    #     Rule(LinkExtractor(allow=r'http://www.murdoch.edu.au/course-search-results/[1-10]\?searchQuery=undergraduate&studyLevel=undergraduate&indexCatalogue=rses&wordsMode=AllWords&studyLevel_radio=undergraduate&atarMin=60&atarMax=100&studyMode=all&schools=all'),follow=True),
    #     Rule(LinkExtractor(allow=(r'.*'),restrict_xpaths=('//*[@id="Contentplaceholder1_T7528D088016_Col01"]//div[@class="sf-media-body media-body"]/h3/a')),callback='parse_item', follow=False),
    # )


    # def parse(self,response):
    #     print('######################################')
    #     # 每一页里的所有详情页的链接集合
    #     links = response.xpath('//*[@id="content_container_541268"]//div[@class="module_search-text"]//a/@href').extract()
    #     # print(links)
    #     # 迭代取出集合里的链接
    #     for link in links:
    #         # 提取列表里每个详情页的链接，发送请求放到请求队列里,并调用self.parse_item来处理
    #         yield scrapy.Request(link, callback=self.parse_item)
    #
    #     if self.offset <= 100:
    #         self.offset += 20
    #         # print(self.offset)
    #         # 发送请求放到请求队列里，调用self.parse处理response
    #         yield scrapy.Request(self.url + str(self.offset), callback=self.parse)


    def parse(self,response):
        print('==================================',response.url)
        item = HooliItem()
#
        url = response.url
        print(1,url)

        university = 'Deakin University'
        print(2,university)

        department ="NULL"
        # department_s = ''.join(department_s).replace('\r\n','')
        # try:
        #     if "School" in department_s:
        #         start = department_s.find("School")
        #         department = department_s[start:]
        #         department = department[:100]
        #         department = department.lstrip("School")
        #         item["department"] = department
        #     else:
        #         department = "NULL"
        #
        # except:
        #     department = "报错!"
        #
        # print(3,department)

        country = 'Australia'
        city = "Melbourne"
        website = 'http://www.deakin.edu.au'
        degree_level = '0'

        # programme = response.xpath('//div[@class="section picture-nav"]/h1/text()').extract()
        programme = response.xpath('//*[@id="main-content"]//div[@class="module__hero-banner--content--inner"]/h1/text()').extract()
        programme = ''.join(programme)
        print(4,programme)

        ucas_code_s = response.xpath('//*[@id="main-content"]//div[@class="module__key-information--item"]//text()').extract()
        ucas_code_s = ''.join(ucas_code_s).replace('\r\n','').replace('\n','').replace(' ','')
        try:
            if "CRICOS" in ucas_code_s:
                start = ucas_code_s.find("CRICOS")
                end = ucas_code_s.find("Level")
                ucas_code = ucas_code_s[start:end]
                ucas_code = ucas_code[:20]
                ucas_code = ucas_code.lstrip("CRICOS").lstrip("code")
                item["ucas_code"] = ucas_code
            else:
                ucas_code = "NULL"
        except:
            ucas_code = "报错!"

        print(5,ucas_code)

        # degree_type = response.xpath('//div[@class="section picture-nav"]/h1/text()').extract()
        degree_type = response.xpath('//*[@id="main-content"]//div[@class="module__hero-banner--content--inner"]/h1/text()').extract()
        degree_type = ''.join(degree_type)
        # degree_type = self.getDegree_type(degree_type)
        try:
            if "Associate Degree" in degree_type:
                degree_type = "Associate Degree"
            elif "Bachelor" in degree_type:
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
        overview = response.xpath('//*[@id="main-content"]/div[4]//div[@class="module__overview--content module__toggle-content"]/p/text()').extract()
        overview = ''.join(overview)
        print(7, overview)

        mode_s = response.xpath('//*[@id="main-content"]//div[@class="module__summary--item"]//text()').extract()
        mode_s = ''.join(mode_s).replace('\n','').strip().replace('   ','')
        # mode = mode.replace('\n','')
        # mode = mode.replace('      ','')
        try:
            if "Duration" in mode_s:
                start = mode_s.find("Duration")
                mode = mode_s[start:]
                mode = mode[:50]
                mode = mode.lstrip("Duration")
                item["mode"] = mode
            else:
                mode = "NULL"
        except:
            mode = "报错!"
        print(8,mode)



        duration_s = response.xpath('//*[@id="main-content"]//div[@class="module__summary--item"]//text()').extract()
        duration_s = ''.join(duration_s).replace('\n','').strip().replace('   ','')
        # duration = duration.replace('\n','')
        # duration = duration.replace('    ','')
        if "Duration" in duration_s:
            start= duration_s.find("Duration")
            end = duration_s.find("Campuses")
            duration = duration_s[start:end]
            # duration = duration[:100]
            duration = duration.lstrip("Duration")
            item["duration"] = duration
        else:
            duration = "NULL"

        print(9,duration)

        modules = response.xpath('//*[@id="module__course-structure"]//text()').extract()
        modules = ''.join(modules).replace('\n','').replace('   ','')
        # try:
        #     if "Modules" in modules_s:
        #         start = modules_s.find("")
        #
        #         end = modules_s.find("Assessment")
        #         modules = modules_s[start:end]
        #         item["modules"] = modules
        #     else:
        #         modules = modules_s
        # except:
        #     modules = modules_s
        print(10,modules)

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

        career = "NULL"
        # career = ''.join(career)

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
        # print(10, career)

        application_date = "NULL"

        deadline = 'NULL'
        # deadline = ''.join(deadline)
        # print(9,deadline)

        application_fee = 'NULL'

        tuition_fee_s = response.xpath('//*[@id="main-content"]//div[@class="module__content-panel"]//text()').extract()
        tuition_fee_s = ''.join(tuition_fee_s).replace('\n','')
        # # tuition_fee = tuition_fee.replace('\n','')
        # # tuition_fee = tuition_fee.replace('    ','')
        # tuition_fee = self.getTuition_fee(tuition_fee)
        try:
            if "Fees and scholarships" in tuition_fee_s:
                start = tuition_fee_s.find("Fees and scholarships")
                end = tuition_fee_s.find("Entry pathways")
                tuition_fee = tuition_fee_s[start:end]
                tuition_fee = self.getTuition_fee(tuition_fee)
                item["tuition_fee"] = tuition_fee
            else:
                tuition_fee = "NULL"
        except:
            tuition_fee = "报错!"

        print(11, tuition_fee)

        location_s = response.xpath('//*[@id="main-content"]//div[@class="module__summary--item"]//text()').extract()
        location_s = ''.join(location_s).replace('\n','')
        try:
            if "Campuses" in location_s:
                start = location_s.find("Campuses ")
                location = location_s[start:]
                location = location[:150]
                # location = location.lstrip("Campuses")
                item["location"] = location
            else:
                location = "NULL"
        except:
            location = "报错!"
        print(12,location)

        ATAS = 'NULL'

        GPA = 'NULL'

        average_score = 'NULL'

        accredited_university = 'NULL'

        Alevel = 'NULL'

        IB = 'NULL'

        IELTS = response.xpath('//div[@class="module__summary--items"]/div[1]/div[2]//text()').extract()
        # IELTS = self.clear_space(IELTS)
        IELTS = ''.join(IELTS).replace('\n','').strip()
        # # IELTS = re.findall('(IELTS:|IELTS)? (.*){0,5} \d?.\d? .{0,70}',IELTS)
        # try:
        #     if "English language requirements" in IELTS_s:
        #         start = IELTS_s.find("English language requirements")
        #         IELTS = IELTS_s[start:]
        #         IELTS = IELTS[:150]
        #         IELTS = IELTS.lstrip("English language requirements")
        #         item["IELTS"] = IELTS
        #     else:
        #         IELTS = "NULL"
        # except:
        #     IELTS = "报错!"
        print(13, IELTS)

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

        how_to_apply = response.xpath('//*[@id="main-content"]/div[@class="module__bleed-top--wrapper module__content-panel--wrapper module__content-panel--wrapper--content-spacing"]//text()').extract()
        how_to_apply = ''.join(how_to_apply).replace('\n','')
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
        print(14,how_to_apply)

        entry_requirements_s = response.xpath('//*[@id="main-content"]//div[@class="module__content-panel"]//text()').extract()
        entry_requirements_s = ''.join(entry_requirements_s).replace(' ','')

        try:
            if "Entry requirements" in entry_requirements_s:
                start = entry_requirements_s.find("Entry requirements")
                end = entry_requirements_s.find("Fees and scholarships")
                entry_requirements = entry_requirements_s[start:end]
                item["entry_requirements"] = entry_requirements
            else:
                entry_requirements = "NULL"

        except:
            entry_requirements = '报错!'

        print(15,entry_requirements)

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
            elif "LLB+BSc" in degree_type:
                degree_type = 'LLB+BSc'
            elif "(LLB)+(BSc)" in degree_type:
                degree_type = '(LLB)+(BSc)'
            elif "(BCrim)+(BA)" in degree_type:
                degree_type = '(BCrim)+(BA)'
            elif "BCrim+BCommun" in degree_type:
                degree_type = 'BCrim+BCommun'
            elif "BCrMedia" in degree_type:
                degree_type = 'BCrMedia'
            elif "BBus" in degree_type:
                degree_type = 'BBus'
            elif "(BEd)+(BA)" in degree_type:
                degree_type = '(BEd)+(BA)'
            elif "(BE(Hons))" in degree_type:
                degree_type = '(BE(Hons))'
            elif "BCrMedia" in degree_type:
                degree_type = 'BCrMedia'
            elif "(BEd)+(BSc)" in degree_type:
                degree_type = '(BEd)+(BSc)'
            elif "LLB/LLB(Hons)" in degree_type:
                degree_type = 'LLB/LLB(Hons)'
            elif "(BSc)+(BClinChiro)" in degree_type:
                degree_type = '(BSc)+(BClinChiro)'
            elif "(BCommun)" in degree_type:
                degree_type = '(BCommun)'
            elif "(BCrim)" in degree_type:
                degree_type = '(BCrim)'
            elif "BSc/BLabMed" in degree_type:
                degree_type = 'BSc/BLabMed'
            elif "BSportExSc" in degree_type:
                degree_type = 'BSportExSc'
            elif "BCommun+LLB" in degree_type:
                degree_type = 'BCommun+LLB'
            elif len(degree_type) == 0:
                degree_type = 'NULL'

            else:
                degree_type = degree_type
        except:
            degree_type = "NULL"
        return degree_type
#
