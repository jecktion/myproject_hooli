

# -*- coding: utf-8 -*-






# -*- coding: utf-8 -*-






import scrapy
from school_3.items import HooliItem
import datetime
import time
from lxml import etree
import requests
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import re
from school_3.getDegree_type import getDegree_type
from school_3.clearSpace import clear_space
from school_3.getItem import get_item


class PlymouthSpider(scrapy.Spider):
    name = 'Newcastle_pg'
    allowed_domains = ['www.newcastle.edu.au']
    start_urls = []
    base_url = 'https://www.newcastle.edu.au/%s'

    Lists = ['degrees/master-applied-finance',
'degrees/master-applied-linguistics',
'degrees/master-applied-management-nursing',
'degrees/master-architecture',
'degrees/research/master-of-philosophy-aboriginal-health-studies',
'degrees/research/master-of-philosophy-aboriginal-studies',
'degrees/research/master-of-philosophy-accounting-and-finance',
'degrees/research/master-of-philosophy-anatomical-pathology',
'degrees/research/master-of-philosophy-anatomy',
'degrees/research/master-of-philosophy-architecture',
'degrees/research/phd-aboriginal-health-studies',
'degrees/research/phd-aboriginal-studies',
'degrees/research/phd-accounting-and-finance',
'degrees/research/phd-anatomical-pathology',
'degrees/research/phd-anatomy',
'degrees/research/phd-architecture',
'degrees/teach-out/master-of-applied-linguistics-semester-1-2015',
'degrees/teach-out/master-of-aviation-management',
'degrees/teach-out/master-of-aviation-management-pre-2015',
'degrees/master-bio-innovation-design',
'degrees/master-business-administration-mba',
'degrees/master-business-administration-mba-global',
'degrees/master-business-administration-applied-finance',
'degrees/master-business-administration-human-resource-management',
'degrees/master-business-administration-international-business',
'degrees/master-business-administration-marketing',
'degrees/master-business-psychology',
'degrees/master-business-research',
'degrees/research/master-of-philosophy-behavioural-science-in-relation-to-medicine',
'degrees/research/master-of-philosophy-biological-sciences',
'degrees/research/master-of-philosophy-building',
'degrees/research/phd-behavioural-science-in-relation-to-medicine',
'degrees/research/phd-biological-sciences',
'degrees/research/phd-building',
'degrees/teach-out/doctor-of-business-administration-pre-2014',
'degrees/teach-out/master-of-business-pre-2015',
'degrees/teach-out/master-of-business-administration-pre-2015',
'degrees/teach-out/master-of-business-administration-pre-2018',
'degrees/teach-out/master-of-business-administration-applied-finance-pre-2015',
'degrees/teach-out/master-of-business-administration-master-of-applied-finance-pre-2018',
'degrees/teach-out/master-of-business-administration-human-resource-management-pre-2015',
'degrees/teach-out/master-of-business-administration-master-of-human-resource-management-pre-2018',
'degrees/teach-out/master-of-business-administration-information-technology-professional-pre-2015',
'degrees/teach-out/master-of-business-administration-master-of-international-business-pre-2018',
'degrees/teach-out/master-of-business-administration-marketing-pre-2015',
'degrees/teach-out/master-of-business-administration-master-of-marketing-pre-2018',
'degrees/master-clinical-epidemiology',
'degrees/master-clinical-medicine-leadership-management',
'degrees/master-clinical-psychology',
'degrees/master-creative-industries',
'degrees/research/master-of-philosophy-chemical-engineering',
'degrees/research/master-of-philosophy-chemistry',
'degrees/research/master-of-philosophy-civil-engineering',
'degrees/research/master-of-philosophy-classics',
'degrees/research/master-of-philosophy-clinical-pharmacology',
'degrees/research/master-of-philosophy-communication-and-media-arts',
'degrees/research/master-of-philosophy-community-medicine-and-clinical-epidemiology',
'degrees/research/master-of-philosophy-computer-engineering',
'degrees/research/master-of-philosophy-computer-science',
'degrees/research/master-of-philosophy-cultural-studies',
'degrees/research/phd-chemical-engineering',
'degrees/research/phd-chemistry',
'degrees/research/phd-civil-engineering',
'degrees/research/phd-classics',
'degrees/research/phd-clinical-pharmacology',
'degrees/research/phd-communication-and-media-arts',
'degrees/research/phd-community-medicine-and-clinical-epidemiology',
'degrees/research/phd-computer-engineering',
'degrees/research/phd-computer-science',
'degrees/research/phd-cultural-studies',
'degrees/teach-out/doctor-of-clinical-and-health-psychology-pre-2014',
'degrees/teach-out/master-of-clinical-epidemiology-pre-2018',
'degrees/teach-out/master-of-creative-industries-pre-2018',
'degrees/master-digital-media',
'degrees/master-disaster-resilience-sustainable-development',
'degrees/research/master-of-philosophy-design',
'degrees/research/master-of-philosophy-disaster-management',
'degrees/research/master-of-philosophy-drama',
'degrees/research/phd-design',
'degrees/research/phd-disaster-management',
'degrees/research/phd-drama',
'degrees/teach-out/master-of-digital-media-pre-2015',
'degrees/teach-out/master-of-disaster-preparedness-reconstruction',
'degrees/master-education',
'degrees/master-engineering-management',
'degrees/master-environmental-business-management',
'degrees/master-environmental-law',
'degrees/master-environmental-management-sustainability',
'degrees/master-environmental-risk-assessment-remediation',
'degrees/research/master-of-philosophy-earth-sciences',
'degrees/research/master-of-philosophy-economics',
'degrees/research/master-of-philosophy-education',
'degrees/research/master-of-philosophy-electrical-engineering',
'degrees/research/master-of-philosophy-english',
'degrees/research/master-of-philosophy-environmental-and-occupational-health',
'degrees/research/master-of-philosophy-environmental-engineering',
'degrees/research/master-of-philosophy-environmental-science',
'degrees/research/master-of-philosophy-exercise-and-sport-sciences',
'degrees/research/master-of-philosophy-experimental-pharmacology',
'degrees/master-professional-engineering',
'degrees/master-professional-engineering-chemical',
'degrees/master-professional-engineering-civil',
'degrees/master-professional-engineering-computer-systems',
'degrees/master-professional-engineering-electrical-electronic',
'degrees/master-professional-engineering-environmental',
'degrees/master-professional-engineering-mechanical',
'degrees/master-professional-engineering-mechatronics',
'degrees/master-professional-engineering-software',
'degrees/research/phd-earth-sciences',
'degrees/research/phd-economics',
'degrees/research/phd-education',
'degrees/research/phd-electrical-engineering',
'degrees/research/phd-engineering',
'degrees/research/phd-english',
'degrees/research/phd-environmental-and-occupational-health',
'degrees/research/phd-environmental-engineering',
'degrees/research/phd-environmental-science',
'degrees/research/phd-exercise-and-sport-sciences',
'degrees/research/phd-experimental-pharmacology',
'degrees/teach-out/master-of-early-childhood-education-pre-2014',
'degrees/teach-out/master-of-educational-studies-pre-2015',
'degrees/teach-out/master-of-educational-studies-pre-2018',
'degrees/master-family-studies',
'degrees/research/master-of-philosophy-fine-art',
'degrees/research/master-of-philosophy-food-science',
'degrees/research/phd-fine-art',
'degrees/research/phd-food-science',
'degrees/research/master-of-philosophy-general-practice',
'degrees/research/master-of-philosophy-geology',
'degrees/research/phd-gender-and-health',
'degrees/research/phd-general-practice',
'degrees/research/phd-geology',
'degrees/master-health-science',
'degrees/master-human-resource-management',
'degrees/master-human-resources-law',
'degrees/research/master-of-philosophy-history',
'degrees/research/master-of-philosophy-human-geography',
'degrees/research/master-of-philosophy-human-physiology',
'degrees/research/phd-history',
'degrees/research/phd-human-geography',
'degrees/research/phd-human-physiology',
'degrees/research/phd-humanities',
'degrees/teach-out/master-of-human-resource-management-pre-2015',
'degrees/teach-out/master-of-human-resource-management-pre-2018',
'degrees/master-innovation-management-entrepreneurship',
'degrees/master-information-technology',
'degrees/master-international-business',
'degrees/research/master-of-philosophy-immunology-and-microbiology',
'degrees/research/master-of-philosophy-industrial-design',
'degrees/research/master-of-philosophy-information-systems',
'degrees/research/master-of-philosophy-information-technology',
'degrees/research/phd-immunology-and-microbiology',
'degrees/research/phd-industrial-design',
'degrees/research/phd-information-systems',
'degrees/research/phd-information-technology',
'degrees/teach-out/master-of-information-technology-pre-2015',
'degrees/juris-doctor-graduate-diploma-legal-practice',
'degrees/master-laws',
'degrees/master-leadership-management-education',
'degrees/research/master-of-philosophy-law',
'degrees/research/master-of-philosophy-leisure-and-tourism',
'degrees/research/master-of-philosophy-linguistics',
'degrees/research/phd-law',
'degrees/research/phd-leisure-and-tourism',
'degrees/research/phd-linguistics',
'degrees/teach-out/master-of-leadership-and-management-in-education-pre-2015',
'degrees/teach-out/master-of-leadership-and-management-in-education-semester-1-2015',
'degrees/master-marketing',
'degrees/master-medical-statistics',
'degrees/master-mental-health-nursing',
'degrees/master-midwifery-studies',
'degrees/research/master-of-philosophy-magnetic-resonance-in-medicine',
'degrees/research/master-of-philosophy-management',
'degrees/research/master-of-philosophy-marine-science',
'degrees/research/master-of-philosophy-mathematics',
'degrees/research/master-of-philosophy-mechanical-engineering',
'degrees/research/master-of-philosophy-medical-biochemistry',
'degrees/research/master-of-philosophy-medical-genetics',
'degrees/research/master-of-philosophy-medical-physics',
'degrees/research/master-of-philosophy-medical-radiation-science',
'degrees/research/master-of-philosophy-medicine',
'degrees/research/master-of-philosophy-midwifery',
'degrees/research/master-of-philosophy-modern-languages',
'degrees/research/master-of-philosophy-music',
'degrees/research/phd-magnetic-resonance-in-medicine',
'degrees/research/phd-management',
'degrees/research/phd-marine-science',
'degrees/research/phd-mathematics',
'degrees/research/phd-mechanical-engineering',
'degrees/research/phd-medical-biochemistry',
'degrees/research/phd-medical-genetics',
'degrees/research/phd-medical-radiation-science',
'degrees/research/phd-medicine',
'degrees/research/phd-midwifery',
'degrees/research/phd-modern-languages',
'degrees/research/phd-music',
'degrees/teach-out/master-of-marketing-pre-2018',
'degrees/teach-out/master-of-medical-statistics-pre-2018',
'degrees/teach-out/master-of-mental-health-nursing-nurse-practitioner-pre-2018',
'degrees/teach-out/master-of-midwifery-studies-pre-2018',
'degrees/master-nursing',
'degrees/research/master-of-philosophy-natural-history-illustration',
'degrees/research/master-of-philosophy-nursing',
'degrees/research/master-of-philosophy-nutrition-and-dietetics',
'degrees/research/master-of-philosophy-nutritional-biochemistry',
'degrees/newstep',
'degrees/research/phd-natural-history-illustration',
'degrees/research/phd-nursing',
'degrees/research/phd-nutrition-and-dietetics',
'degrees/research/phd-nutritional-biochemistry',
'degrees/teach-out/master-of-nursing-advanced-practice-pre-2018',
'degrees/teach-out/master-of-nursing-nurse-practitioner-pre-2018',
'degrees/bachelor-of-occupational-therapy-honours',
'degrees/bachelor-of-oral-health-therapy',
'degrees/research/master-of-philosophy-occupational-therapy',
'degrees/research/master-of-philosophy-oral-health',
'degrees/open-foundation',
'degrees/research/phd-occupational-therapy',
'degrees/research/phd-oral-health',
'degrees/research/master-of-philosophy-paediatrics',
'degrees/research/master-of-philosophy-pharmacy',
'degrees/research/master-of-philosophy-philosophy',
'degrees/research/master-of-philosophy-physical-geography',
'degrees/research/master-of-philosophy-physics',
'degrees/research/master-of-philosophy-physiotherapy',
'degrees/research/master-of-philosophy-podiatry',
'degrees/research/master-of-philosophy-politics',
'degrees/research/master-of-philosophy-psychiatry',
'degrees/research/master-of-philosophy-psychology',
'degrees/master-professional-accounting',
'degrees/master-professional-accounting-advanced',
'degrees/master-professional-accounting-business-administration',
'degrees/master-professional-accounting-business-administration-2019-onwards',
'degrees/master-project-management-built-environment',
'degrees/master-property',
'degrees/master-public-health',
'degrees/research/phd-paediatrics',
'degrees/research/phd-pharmacy',
'degrees/research/phd-philosophy',
'degrees/research/phd-physical-geography',
'degrees/research/phd-physics',
'degrees/research/phd-physiotherapy',
'degrees/research/phd-podiatry',
'degrees/research/phd-politics',
'degrees/research/phd-psychiatry',
'degrees/research/phd-psychology-science',
'degrees/teach-out/master-of-pharmacy-pre-2016',
'degrees/teach-out/master-of-professional-accounting-business-administration-pre-2018',
'degrees/teach-out/master-of-professional-economics-pre-2018',
'degrees/teach-out/master-of-project-management-for-the-built-environment-pre-2015',
'degrees/research/master-of-philosophy-religious-studies',
'degrees/research/master-of-philosophy-reproductive-medicine',
'degrees/research/phd-religious-studies',
'degrees/research/phd-reproductive-medicine',
'degrees/research/master-of-philosophy-social-inclusion',
'degrees/research/master-of-philosophy-social-work',
'degrees/research/master-of-philosophy-sociology-and-anthropology',
'degrees/research/master-of-philosophy-software-engineering',
'degrees/research/master-of-philosophy-speech-pathology',
'degrees/research/master-of-philosophy-statistics',
'degrees/research/master-of-philosophy-surgical-science',
'degrees/research/master-of-philosophy-surveying',
'degrees/research/master-of-philosophy-sustainable-resource-management',
'degrees/master-social-change-development',
'degrees/master-special-inclusive-education',
'degrees/master-studies',
'degrees/research/phd-social-inclusion',
'degrees/research/phd-social-work',
'degrees/research/phd-sociology-and-anthropology',
'degrees/research/phd-software-engineering',
'degrees/research/phd-speech-pathology',
'degrees/research/phd-statistics',
'degrees/research/phd-surgical-science',
'degrees/research/phd-surveying',
'degrees/research/phd-sustainable-resource-management',
'degrees/teach-out/master-of-social-change-and-development-pre-2015',
'degrees/teach-out/master-of-special-education-pre-2015',
'degrees/teach-out/master-of-special-education-pre-2018',
'degrees/teach-out/master-of-special-education-semester-1-2015',
'degrees/research/master-of-philosophy-theology',
'degrees/master-teaching-primary',
'degrees/master-teaching-secondary',
'degrees/master-traumatology',
'degrees/research/phd-theology',
'degrees/teach-out/master-of-theology-pre-2015',
'degrees/master-workplace-health-safety'
]

    for i in Lists:
        fullurl = base_url % i
        start_urls.append(fullurl)



    def parse(self,response):
        print('1,============',response.url)
        item = get_item(HooliItem)

        num_programme = response.xpath('//div[@class="majors-list grid-content grid-3-column"]/div[@class="grid-block"]//text()').extract()
        print('num_programme:',len(num_programme))
        for i in range(1,len(num_programme)+1):
            print(i)
            programme = response.xpath('//div[@class="majors-list grid-content grid-3-column"]/div[@class="grid-block"][' +str(i)+ ']//text()').extract()
            programme = ''.join(programme)
            item["programme"] = programme
            print('programme:',programme)

            programme_url = response.xpath('//div[@class="grid-block"][' +str(i)+ ']/a/@href').extract()
            for u in programme_url:
                if "https" not in u:
                    programme_urls = 'https://www.newcastle.edu.au/degrees/' + u
                    print('programme_urls:',programme_urls)
                    self.parse_overview(programme_urls,item)

            url = response.url
            item["url"] = url
            university = 'The University of Newcastle'
            item["university"] = university
            country = 'Australia'
            item["country"] = country
            city = "Newcastle"
            item["city"] = city
            website = 'www.newcastle.edu.au'
            item["website"] = website
            degree_level = '1'
            item["degree_level"] = degree_level

            department = response.xpath('').extract()
            department = ''.join(department)
            item["department"] = department
            print('department:',department)


            degree_type = response.xpath('//*[@id="page-header"]/div[@class="header-tint"]/div[@class="inner clearfix"]/a/h1//text()').extract()
            degree_type = ''.join(degree_type)
            item["degree_type"] = degree_type
            print('degree_type:',degree_type)

            start_date = response.xpath('//*[@class="fast-facts-content"]/div[@class="fast-fact-items" and @data-region="international"]/div[@class="flex-inner"][1]/div[@class="fast-fact-item"]/ul/li/text()').extract()
            start_date = ''.join(start_date)
            item["start_date"] = start_date
            print('start_date:',start_date)

            mode = response.xpath('//*[@id="tab-how-to-apply"]/div[@class="fast-facts fast-facts-ug"]/div[@class="fast-facts-content"]/div[@data-region="international"]/div[@class="flex-inner"][3]/div[@class="fast-fact-item"][2]//text()').extract()
            mode = ''.join(mode)
            item["mode"] = mode
            print('mode:',mode)

            duration = response.xpath('//*[@id="tab-how-to-apply"]/div[@class="fast-facts fast-facts-ug"]/div[@class="fast-facts-content"]/div[@data-region="international"]/div[@class="flex-inner"][3]/div[@class="fast-fact-item"][1]//text()').extract()
            duration = ''.join(duration)
            item["duration"] = duration
            print('duration:',duration)

            career = response.xpath('//*[@id="accordion-careers-majors"]/div[@class="uon-accordion-panel"]//text()').extract()
            career = ''.join(career)
            item["career"] = career
            print('career:',career)

            tuition_fee_link = response.xpath('//*[@id="tab-how-to-apply"]/div[@class="fast-facts fast-facts-ug"]/div[@class="fast-facts-content"]/div[@data-region="international"]/div[@class="flex-inner"][2]/div[@class="fast-fact-item"][1]/p/a/@href').extract()
            tuition_fee_link = ''.join(tuition_fee_link)
            tuition_fee_links = 'https://www.newcastle.edu.au' + str(tuition_fee_link)
            self.parse_tuition_fee(tuition_fee_links,item)

            modules_url = response.xpath('//*[@id="what-you-will-study"]/div[@class="clearfix"]/div[@class="col w40"]/p/a/@href').extract()
            modules_url = ''.join(modules_url)
            if "https" not in modules_url:
                modules_fullurl = 'https://www.newcastle.edu.au/degrees/' + modules_url
                self.parse_modules(modules_fullurl,item)

            location = response.xpath('//*[@id="tab-how-to-apply"]/div[@class="fast-facts fast-facts-ug"]/div[@class="fast-facts-content"]/div[@data-region="international"]/div[@class="flex-inner"][1]/div[@class="fast-fact-item"][1]/p/a/text()').extract()
            location = ''.join(location)
            item["location"] = location
            print('location:',location)

            IELTS = response.xpath('//*[@class="fast-facts-content"]/div[@class="fast-fact-items" and @data-region="international"]/div[@class="flex-inner"][2]/div[@class="fast-fact-item"]/ul/li/text()').extract()
            IELTS = ''.join(IELTS)
            item["IELTS"] = IELTS
            print('IELTS:',IELTS)

            chinese_requirements = response.xpath('//*[@class="fast-facts fast-facts-ug"]/div[@class="fast-facts-content"]/div[@class="entrance-rank"]//div[@class="fast-fact-item"]/ul/li//text()').extract()
            chinese_requirements = ''.join(chinese_requirements)
            item["chinese_requirements"] = chinese_requirements
            print('chinese_requirements:',chinese_requirements)

            degree_description = response.xpath('//*[@id="uon-body"]/div[@class="wrapped clearfix"]/div[@class="body-content"]/div[@class="grid-content grid-2-column"]/div[@class="grid-block"]/p/text() | //*[@id="what-you-will-study"]/div[@class="clearfix"]/div[@class="col w60"]/p/text() ').extract()
            degree_description = ''.join(degree_description)
            item["degree_description"] = degree_description
            print('degree_description:',degree_description)

            how_to_apply = response.xpath('//*[@class="grid-block"]/div[@class="apply-info"]/div[@data-region="international"]/p/a/@href').extract()
            how_to_apply = ''.join(how_to_apply)
            item["how_to_apply"] = how_to_apply
            print('how_to_apply:',how_to_apply)

            entry_requirements = response.xpath('//*[@data-region="international"]//div[@class="uon-accordion-content"]//text()').extract()
            entry_requirements = ''.join(entry_requirements)
            item["entry_requirements"] = entry_requirements
            print('entry_requirements:',entry_requirements)

            create_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            item["create_time"] = create_time

            yield item




    def parse_tuition_fee(self,tuition_fee_links,item):
        print('2,==================',tuition_fee_links)
        data = requests.get(tuition_fee_links)
        response = etree.HTML(data.text)
        tuition_fee = response.xpath('//*[@id="content-main"]/div[@class="pdf"]/a/@href')
        tuition_fee = ''.join(tuition_fee)
        item["tuition_fee"] = tuition_fee

    def parse_overview(self,programme_urls, item):
        print('3,==================',programme_urls)
        data = requests.get(programme_urls)
        response = etree.HTML(data.text)
        overview = response.xpath('//*[@id="uon-body"]/div[@class="wrapped clearfix"]/div[@class="body-content"]//text()')
        overview = ''.join(overview)
        item["overview"] = overview
        print('overview:',overview)

    def parse_modules(self,modules_fullurl,item):
        print('4,==================',modules_fullurl)
        date = requests.get(modules_fullurl)
        response = etree.HTML(date.text)
        modules = response.xpath('//div[@id="section-program-structure"]//text()')
        modules = ''.join(modules)
        item["modules"] = modules



        # item = HooliItem()
        #
        # url = response.url
        # print(1,url)
        #
        # university = 'The University of Newcastle'
        # print(2,university)
        #
        # department = "NULL"
        # # department = ''.join(department).replace('\r\n','')
        # # try:
        # #     if "School" in department_s:
        # #         start = department_s.find("School")
        # #         department = department_s[start:]
        # #         department = department[:100]
        # #         department = department.lstrip("School")
        # #         item["department"] = department
        # #     else:
        # #         department = "NULL"
        #
        # # except:
        # #     department = "报错!"
        #
        # # print(3,department)
        #
        # country = 'Australia'
        # city = "Newcastle"
        # website = 'www.newcastle.edu.au'
        # degree_level = '0'
        #
        # # programme = response.xpath('//div[@class="section picture-nav"]/h1/text()').extract()
        # programme = response.xpath('').extract()
        # programme = ''.join(programme)
        # print(3,programme)
        #
        # ucas_code_s = response.xpath('()').extract()
        # ucas_code_s = ''.join(ucas_code_s).replace('\r\n','')
        # try:
        #     if "UCAS Code:" in ucas_code_s:
        #         start = ucas_code_s.find("UCAS Code:")
        #         ucas_code = ucas_code_s[start:]
        #         ucas_code = ucas_code[:20]
        #         ucas_code = ucas_code.lstrip("UCAS Code:")
        #         item["ucas_code"] = ucas_code
        #     else:
        #         ucas_code = "NULL"
        # except:
        #     ucas_code = "报错!"
        #
        # print(4,ucas_code)
        #
        # # degree_type = response.xpath('//div[@class="section picture-nav"]/h1/text()').extract()
        # degree_type = response.xpath('').extract()
        # degree_type = getDegree_type(''.join(degree_type))
        #
        # # degree_type = self.getDegree_type(degree_type)
        # # try:
        # #     if "Associate Degree" in degree_type:
        # #         degree_type = "Associate Degree"
        # #     elif "Bachelor" in degree_type:
        # #         degree_type = "Bachelor"
        # #     elif "Master" in degree_type:
        # #         degree_type = "Master"
        # #     else:
        # #         degree_type = "NULL"
        # # except:
        # #     degree_type = "报错!"
        # print(5,degree_type)
        #
        # start_date = response.xpath('').extract()
        # # start_date = ''.join(start_date)
        # # print(5,start_date)
        #
        # # overview = response.xpath('//div[@class="left logo-bg"]//text()').extract()
        # overview_s = response.xpath('').extract()
        # clear_space(overview_s)
        # overview_s = ''.join(overview_s).replace('\r\n','')
        # try:
        #     if "Course Overview" in overview_s:
        #         start = overview_s.find("Course Overview")
        #         end = overview_s.find("Highlights of this degree")
        #         overview = overview_s[start:end]
        #         item["overview"] = overview
        #     else:
        #         overview = "NULL"
        # except:
        #     overview = "报错!"
        # print(6, overview)
        #
        # mode = response.xpath('').extract()
        # mode = ''.join(mode).replace('','')
        # # mode = mode.replace('\n','')
        # # mode = mode.replace('      ','')
        # # try:
        # #     if "Study Mode" in mode_s:
        # #         start = mode_s.find("Study Mode")
        # #         mode = mode_s[start:]
        # #         mode = mode[:100]
        # #         mode = mode.lstrip("Study Mode")
        # #         item["mode"] = mode
        # #     else:
        # #         mode = "NULL"
        # # except:
        # #     mode = "报错!"
        # print(7,mode)
        #
        #
        #
        # duration = response.xpath('').extract()
        # duration = ''.join(duration).replace('','')
        # # duration = duration.replace('\n','')
        # # duration = duration.replace('    ','')
        # # if "Course Duration" in duration_s:
        # #     start= duration_s.find("Course Duration")
        # #     duration = duration_s[start:]
        # #     duration = duration[:100]
        # #     duration = duration.lstrip("Course Duration")
        # #     item["duration"] = duration
        # # else:
        # #     duration = "NULL"
        #
        # print(8,duration)
        #
        # modules_s = response.xpath('').extract()
        # clear_space(modules_s)
        # modules_s = ''.join(modules_s)
        #
        # try:
        #     if "Modules" in modules_s:
        #         start = modules_s.find("Modules")
        #         end = modules_s.find("Teaching and assessment")
        #         modules = modules_s[start:end]
        #         item["modules"] = modules
        #     else:
        #         modules = modules_s
        # except:
        #     modules = modules_s
        # print(9,modules)
        #
        # teaching = 'NULL'
        #
        # assessment_s = response.xpath('').extract()
        # clear_space(assessment_s)
        # assessment_s = ''.join(assessment_s)
        # try:
        #     if "Assessment methods" in assessment_s:
        #         start = assessment_s.find("Assessment methods")
        #         assessment = assessment_s[start:]
        #         assessment = assessment[:300]
        #         item["assessment"] = assessment
        #     else:
        #         assessment = "NULL"
        # except:
        #     assessment = "报错!"
        # print(10, assessment)
        #
        # career_s = response.xpath('').extract()
        # career_s = ''.join(career_s).replace('\r\n','').replace('\n','')
        # try:
        #     if "Careers" in career_s:
        #         start = career_s.find("Careers")
        #         end = career_s.find("Next step:")
        #         career = career_s[start:end]
        #         item["career"] = career
        #     else:
        #         career = "NULL"
        # except:
        #     career = "报错!"
        # print(11, career)
        #
        # application_date = "NULL"
        #
        # deadline = 'NULL'
        # # deadline = ''.join(deadline)
        # # print(9,deadline)
        #
        # application_fee = 'NULL'
        #
        # tuition_fee_s= response.xpath('').extract()
        # tuition_fee_s = ''.join(tuition_fee_s).replace('\n','')
        # # # tuition_fee = tuition_fee.replace('\n','')
        # # # tuition_fee = tuition_fee.replace('    ','')
        # # tuition_fee = self.getTuition_fee(tuition_fee)
        # try:
        #     if "Tuition Fees (International students)" in tuition_fee_s:
        #         start = tuition_fee_s.find("Tuition Fees (International students)")
        #         end = tuition_fee_s.find("Scholarships and Financial Support (UK students)")
        #         tuition_fee = tuition_fee_s[start:end]
        #         tuition_fee = self.getTuition_fee(tuition_fee)
        #         item["tuition_fee"] = tuition_fee
        #     else:
        #         tuition_fee = "NULL"
        # except:
        #     tuition_fee = "报错!"
        #
        # print(12, tuition_fee)
        #
        # location = "Newcastle"
        # # location_s = ''.join(location_s).replace('\r\n','')
        # # try:
        # #     if "Location" in location_s:
        # #         start = location_s.find("Location")
        # #         location = location_s[start:]
        # #         location = location[:100]
        # #         location = location.lstrip("Location")
        # #         item["location"] = location
        # #     else:
        # #         location = "NULL"
        # # except:
        # #     location = "报错!"
        # print(13,location)
        #
        # ATAS = 'NULL'
        #
        # GPA = 'NULL'
        #
        # average_score = 'NULL'
        #
        # accredited_university = 'NULL'
        #
        # Alevel = 'NULL'
        #
        # IB = 'NULL'
        #
        # IELTS_s = response.xpath('').extract()
        # clear_space(IELTS_s)
        # IELTS_s = ''.join(IELTS_s)
        # # IELTS = re.findall('(IELTS:|IELTS)? (.*){0,5} \d?.\d? .{0,70}',IELTS)
        # try:
        #     if "English Language Requirements" in IELTS_s:
        #         start = IELTS_s.find("English Language Requirements")
        #         IELTS = IELTS_s[start:]
        #         IELTS = IELTS[:200]
        #         item["IELTS"] = IELTS
        #     else:
        #         IELTS = "NULL"
        # except:
        #     IELTS = "报错!"
        # print(14, IELTS)
        #
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
        # LSAT = "NULL"
        # MCAT = 'NULL'
        #
        # working_experience = 'NULL'
        #
        # interview = 'NULL'
        #
        # portfolio = 'NULL'
        #
        # application_documents = 'NULL'
        #
        # how_to_apply_s = response.xpath('').extract()
        # clear_space(how_to_apply_s)
        # how_to_apply_s = ''.join(how_to_apply_s)
        # try:
        #     if "Apply" in how_to_apply_s:
        #         start = how_to_apply_s.find("Apply")
        #         how_to_apply = how_to_apply_s[start:]
        #         item["how_to_apply"] = how_to_apply
        #     else:
        #         how_to_apply = how_to_apply_s
        # except:
        #     how_to_apply = '报错!'
        # print(15,how_to_apply)
        #
        # entry_requirements_s = response.xpath('').extract()
        # clear_space(entry_requirements_s)
        # entry_requirements_s = ''.join(entry_requirements_s)
        #
        # try:
        #     if "Entry Requirements" in entry_requirements_s:
        #         start = entry_requirements_s.find("Entry Requirements")
        #         end = entry_requirements_s.find("Careers")
        #         entry_requirements = entry_requirements_s[start:end]
        #         item["entry_requirements"] = entry_requirements
        #     else:
        #         entry_requirements = entry_requirements_s
        #
        # except:
        #     entry_requirements = '报错!'
        #
        # print(16,entry_requirements)
        #
        # chinese_requirements = "NULL"
        #
        # school_test = 'NULL'
        #
        # degree_description = "NULL"
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
        # print(17, create_time)
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
        #
        #
