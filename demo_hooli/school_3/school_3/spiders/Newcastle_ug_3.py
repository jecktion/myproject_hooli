# -*- coding: utf-8 -*-






import scrapy
from school_3.items import HooliItem
import datetime
import time
from lxml import etree
import requests
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re
from school_3.getDegree_type import getDegree_type
from school_3.clearSpace import clear_space
from school_3.getItem import get_item


class PlymouthSpider(scrapy.Spider):
    name = 'Newcastle_ug_3'
    allowed_domains = ['www.newcastle.edu.au']
    start_urls = []
    base_url = 'https://www.newcastle.edu.au/%s'

    Lists = [
        'degrees/bachelor-of-aboriginal-professional-practice',
        'degrees/bachelor-of-aboriginal-professional-practice-laws-honours',
        'degrees/bachelor-of-aboriginal-studies-honours',
        'degrees/bachelor-of-arts',
        'degrees/bachelor-of-arts-honours',
        'degrees/bachelor-of-arts-innovation-and-entrepreneurship',
        'degrees/bachelor-of-arts-laws-honours',
        'degrees/bachelor-of-arts-science',
        'degrees/bachelor-of-biomedical-science',
        'degrees/bachelor-of-biomedical-science-honours',
        'degrees/bachelor-of-biotechnology',
        'degrees/bachelor-of-biotechnology-honours',
        'degrees/bachelor-of-business',
        'degrees/bachelor-of-business-honours',
        'degrees/bachelor-of-business-commerce',
        'degrees/bachelor-of-business-innovation-and-entrepreneurship',
        'degrees/bachelor-of-business-laws-honours',
        'degrees/bachelor-of-commerce-honours',
        'degrees/bachelor-of-commerce',
        'degrees/bachelor-of-commerce-innovation-and-entrepreneurship',
        'degrees/bachelor-of-commerce-laws-honours',
        'degrees/bachelor-of-communication',
        'degrees/bachelor-of-communication-honours',
        'degrees/bachelor-of-communication-laws-honours',
        'degrees/bachelor-of-computer-science',
        'degrees/bachelor-of-computer-science-honours',
        'degrees/bachelor-of-construction-management-building-honours',
        'degrees/bachelor-of-design-architecture',
        'degrees/bachelor-of-development-studies',
        'degrees/bachelor-of-development-studies-honours',
        'degrees/bachelor-of-development-studies-business',
        'degrees/bachelor-of-development-studies-laws-honours',
        'degrees/bachelor-of-development-studies-social-science',
        'degrees/bachelor-of-education-early-childhood-and-primary',
        'degrees/bachelor-of-education-early-childhood-and-primary-honours',
        'degrees/bachelor-of-education-primary',
        'degrees/bachelor-of-education-primary-honours',
        'degrees/bachelor-of-education-secondary',
        'degrees/bachelor-of-education-secondary-honours',
        'degrees/bachelor-of-engineering-honours-chemical',
        'degrees/bachelor-of-engineering-honours-chemical-business',
        'degrees/bachelor-of-engineering-honours-chemical-mathematics',
        'degrees/bachelor-of-engineering-honours-chemical-science',
        'degrees/bachelor-of-engineering-honours-civil',
        'degrees/bachelor-of-engineering-honours-civil-business',
        'degrees/bachelor-of-engineering-honours-civil-environmental',
        'degrees/bachelor-of-engineering-honours-civil-surveying',
        'degrees/bachelor-of-engineering-honours-civil-mathematics',
        'degrees/bachelor-of-engineering-honours-computer-systems',
        'degrees/bachelor-of-engineering-honours-computer-systems-business',
        'degrees/bachelor-of-engineering-honours-computer-systems-computer-science',
        'degrees/bachelor-of-engineering-honours-computer-systems-mathematics',
        'degrees/bachelor-of-engineering-honours-computer-systems-science',
        'degrees/bachelor-of-engineering-honours-electrical-and-electronic',
        'degrees/bachelor-of-engineering-honours-electrical-and-electronic-business',
        'degrees/bachelor-of-engineering-honours-electrical-and-electronic-computer-systems',
        'degrees/bachelor-of-engineering-honours-electrical-and-electronic-mathematics',
        'degrees/bachelor-of-engineering-honours-electrical-and-electronic-science',
        'degrees/bachelor-of-engineering-honours-environmental',
        'degrees/bachelor-of-engineering-honours-environmental-science',
        'degrees/bachelor-of-engineering-honours-mechanical',
        'degrees/bachelor-of-engineering-honours-mechanical-business',
        'degrees/bachelor-of-engineering-honours-mechanical-mechatronics',
        'degrees/bachelor-of-engineering-honours-mechanical-mathematics',
        'degrees/bachelor-of-engineering-honours-mechanical-science',
        'degrees/bachelor-of-engineering-honours-mechatronics',
        'degrees/bachelor-of-engineering-honours-mechatronics-business',
        'degrees/bachelor-of-engineering-honours-mechatronics-electrical-and-electronic',
        'degrees/bachelor-of-engineering-honours-mechatronics-mathematics',
        'degrees/bachelor-of-engineering-honours-mechatronics-science',
        'degrees/bachelor-of-engineering-honours-software',
        'degrees/bachelor-of-engineering-honours-surveying',
        'degrees/bachelor-of-engineering-honours-surveying-business',
        'degrees/bachelor-of-engineering-mining-transfer-program',
        'degrees/bachelor-of-environmental-and-occupational-health-and-safety',
        'degrees/bachelor-of-environmental-science-and-management',
        'degrees/bachelor-of-environmental-science-and-management-honours',
        'degrees/bachelor-of-exercise-and-sport-science',
        'degrees/bachelor-of-exercise-and-sport-science-honours',
        'degrees/bachelor-of-medical-engineering-honours',
        'degrees/bachelor-of-food-science-and-human-nutrition',
        'degrees/bachelor-of-food-science-and-human-nutrition-honours',
        'degrees/bachelor-of-food-science-and-human-nutrition-business',
        'degrees/bachelor-of-industrial-design',
        'degrees/bachelor-of-information-technology',
        'degrees/bachelor-of-information-technology-honours',
        'degrees/bachelor-of-information-technology-business',
        'degrees/bachelor-of-innovation-and-entrepreneurship-laws-honours',
        'degrees/bachelor-of-laws-honours-diploma-of-legal-practice',
        'degrees/bachelor-of-laws-honours',
        'degrees/bachelor-of-mathematics',
        'degrees/bachelor-of-mathematics-honours',
        'degrees/bachelor-of-mathematics-computer-science',
        'degrees/bachelor-of-mathematics-science',
        'degrees/bachelor-of-medical-radiation-science-honours-diagnostic-radiography',
        'degrees/bachelor-of-medical-radiation-science-honours-nuclear-medicine',
        'degrees/bachelor-of-medical-radiation-science-honours-radiation-therapy',
        'degrees/bachelor-of-medical-science',
        'degrees/bachelor-of-medical-science-doctor-of-medicine-joint-medical-program',
        'degrees/bachelor-of-midwifery',
        'degrees/bachelor-of-midwifery-honours',
        'degrees/bachelor-of-music',
        'degrees/bachelor-of-music-honours',
        'degrees/bachelor-of-music-arts',
        'degrees/bachelor-of-natural-history-illustration',
        'degrees/bachelor-of-natural-history-illustration-honours',
        'degrees/bachelor-of-nursing',
        'degrees/bachelor-of-nursing-honours',
        'degrees/bachelor-of-nutrition-and-dietetics-honours',
        'degrees/bachelor-of-occupational-therapy-honours',
        'degrees/bachelor-of-oral-health-therapy',
        'degrees/bachelor-of-pharmacy-honours',
        'degrees/bachelor-of-physiotherapy-honours',
        'degrees/bachelor-of-podiatry',
        'degrees/bachelor-of-psychological-science',
        'degrees/bachelor-of-psychological-science-honours',
        'degrees/bachelor-of-science',
        'degrees/bachelor-of-science-honours',
        'degrees/bachelor-of-science-laws-honours',
        'degrees/bachelor-of-social-science',
        'degrees/bachelor-of-social-science-honours',
        'degrees/bachelor-of-social-science-laws-honours',
        'degrees/bachelor-of-social-work-honours',
        'degrees/bachelor-of-speech-pathology-honours',
        'degrees/bachelor-of-technology-renewable-energy-systems',
        'degrees/teach-out/bachelor-of-arts-pre-2018',
        'degrees/teach-out/bachelor-of-arts-laws-honours-pre-2018',
        'degrees/teach-out/bachelor-of-arts-laws-pre-2014',
        'degrees/teach-out/bachelor-of-biomedical-science-pre-2017',
        'degrees/teach-out/bachelor-of-business-pre-2016',
        'degrees/teach-out/bachelor-of-business-commerce-pre-2016',
        'degrees/teach-out/bachelor-of-business-laws-honours-pre-2016',
        'degrees/teach-out/bachelor-of-commerce-pre-2016',
        'degrees/teach-out/bachelor-of-commerce-laws-honours-pre-2016',
        'degrees/teach-out/bachelor-of-communication-laws-pre-2014',
        'degrees/teach-out/bachelor-of-computer-science-pre-2017',
        'degrees/exit-award/bachelor-of-education-studies-exit-award',
        'degrees/teach-out/bachelor-of-engineering-honours-chemical-pre-2017',
        'degrees/teach-out/bachelor-of-engineering-honours-chemical-bachelor-of-business-pre-2017',
        'degrees/teach-out/bachelor-of-engineering-honours-chemical-bachelor-of-mathematics-pre-2017',
        'degrees/teach-out/bachelor-of-engineering-honours-chemical-bachelor-of-science-pre-2017',
        'degrees/teach-out/bachelor-of-engineering-honours-civil-pre-2017',
        'degrees/teach-out/bachelor-of-engineering-honours-civil-bachelor-of-business-pre-2017',
        'degrees/teach-out/bachelor-of-engineering-honours-civil-bachelor-of-engineering-honours-environmental-pre-2017',
        'degrees/teach-out/bachelor-of-engineering-honours-civil-bachelor-of-engineering-honours-surveying-pre-2017',
        'degrees/teach-out/bachelor-of-engineering-honours-civil-bachelor-of-mathematics-pre-2017',
        'degrees/teach-out/bachelor-of-engineering-honours-computer-pre-2017',
        'degrees/teach-out/bachelor-of-engineering-honours-computer-bachelor-of-computer-science-pre-2017',
        'degrees/teach-out/bachelor-of-engineering-honours-computer-bachelor-of-mathematics-pre-2017',
        'degrees/teach-out/bachelor-of-engineering-honours-computer-bachelor-of-science-pre-2017',
        'degrees/teach-out/bachelor-of-engineering-honours-electrical-pre-2017',
        'degrees/teach-out/bachelor-of-engineering-honours-electrical-bachelor-of-business-pre-2017',
        'degrees/teach-out/bachelor-of-engineering-honours-electrical-bachelor-of-mathematics-pre-2017',
        'degrees/teach-out/bachelor-of-engineering-honours-environmental-pre-2017',
        'degrees/teach-out/bachelor-of-engineering-honours-environmental-bachelor-of-science-pre-2017',
        'degrees/teach-out/bachelor-of-engineering-honours-mechanical-pre-2017',
        'degrees/teach-out/bachelor-of-engineering-honours-mechanical-bachelor-of-business-pre-2017',
        'degrees/teach-out/bachelor-of-engineering-honours-mechanical-bachelor-of-engineering-honours-mechatronics-pre-2017',
        'degrees/teach-out/bachelor-of-engineering-honours-mechanical-bachelor-of-mathematics-pre-2017',
        'degrees/teach-out/bachelor-of-engineering-honours-mechanical-bachelor-of-science-pre-2017',
        'degrees/teach-out/bachelor-of-engineering-honours-mechatronics-pre-2017',
        'degrees/teach-out/bachelor-of-engineering-honours-mechatronics-bachelor-of-mathematics-pre-2017',
        'degrees/teach-out/bachelor-of-engineering-honours-software-pre-2017',
        'degrees/teach-out/bachelor-of-engineering-honours-surveying-pre-2017',
        'degrees/teach-out/bachelor-of-engineering-honours-telecommunications-pre-2016',
        'degrees/teach-out/bachelor-of-engineering-mining-transfer-program-pre-2017',
        'degrees/teach-out/bachelor-of-fine-art',
        'degrees/exit-award/associate-degree-in-health-exit-award',
        'degrees/exit-award/bachelor-of-health-exit-award',
        'degrees/exit-award/bachelor-of-innovation-and-entrepreneurship-exit-award',
        'degrees/teach-out/bachelor-of-laws-graduate-entry-pre-2014',
        'degrees/teach-out/bachelor-of-laws-pre-2014',
        'degrees/teach-out/bachelor-of-laws-diploma-of-legal-practice-pre-2014',
        'degrees/teach-out/bachelor-of-medical-radiation-science-diagnostic-radiography-pre-2016',
        'degrees/teach-out/bachelor-of-medical-radiation-science-nuclear-medicine-pre-2016',
        'degrees/teach-out/bachelor-of-medical-radiation-science-radiation-therapy-pre-2016',
        'degrees/teach-out/bachelor-of-medicine-pre-2017',
        'degrees/teach-out/bachelor-of-music-pre-2017',
        'degrees/teach-out/bachelor-of-music-bachelor-of-arts-pre-2017',
        'degrees/teach-out/bachelor-of-music-arts-pre-2018',
        'degrees/exit-award/bachelor-of-psychological-science-exit-award',
        'degrees/teach-out/bachelor-of-psychology-honours-pre-2018',
        'degrees/teach-out/bachelor-of-psychology-pre-2014',
        'degrees/teach-out/bachelor-of-science-laws-pre-2014',
        'degrees/teach-out/bachelor-of-social-science-laws-pre-2014',
        'degrees/teach-out/bachelor-of-surveying-pre-2015',

    ]

    for i in Lists:
        fullurl = base_url % i
        start_urls.append(fullurl)
        # global fullurl

    def parse(self, response):
        print('1,============', response.url)
        item = get_item(HooliItem)

        # item["url"] = url
        university = 'The University of Newcastle'
        # item["university"] = university
        country = 'Australia'
        # item["country"] = country
        city = "Newcastle"
        # item["city"] = city
        website = 'www.newcastle.edu.au'
        # item["website"] = website
        degree_level = '0'
        # item["degree_level"] = degree_level
        degree_type = response.xpath(
            '//*[@id="page-header"]/div[@class="header-tint"]/div[@class="inner clearfix"]/a/h1//text()').extract()
        degree_type = ''.join(degree_type)
        degree_type = getDegree_type(degree_type)
        # item["degree_type"] = degree_type
        # print('degree_type:', degree_type)

        start_date = response.xpath(
            '//*[@class="fast-facts-content"]/div[@class="fast-fact-items" and @data-region="international"]/div[@class="flex-inner"][1]/div[@class="fast-fact-item"]/ul/li/text()').extract()
        start_date = ''.join(start_date)
        # item["start_date"] = start_date
        # print('start_date:', start_date)

        mode = response.xpath(
            '//*[@id="tab-how-to-apply"]/div[@class="fast-facts fast-facts-ug"]/div[@class="fast-facts-content"]/div[@data-region="international"]/div[@class="flex-inner"][3]/div[@class="fast-fact-item"][2]//text()').extract()
        mode = ''.join(mode)
        # item["mode"] = mode
        # print('mode:', mode)

        duration = response.xpath(
            '//*[@id="tab-how-to-apply"]/div[@class="fast-facts fast-facts-ug"]/div[@class="fast-facts-content"]/div[@data-region="international"]/div[@class="flex-inner"][3]/div[@class="fast-fact-item"][1]//text()').extract()
        duration = ''.join(duration)
        # item["duration"] = duration
        # print('duration:', duration)

        career = response.xpath(
            '//*[@id="accordion-careers-majors"]/div[@class="uon-accordion-panel"]//text()').extract()
        career = ''.join(career)
        # item["career"] = career
        # print('career:', career)

        tuition_fee_link = response.xpath(
            '//*[@id="tab-how-to-apply"]/div[@class="fast-facts fast-facts-ug"]/div[@class="fast-facts-content"]/div[@data-region="international"]/div[@class="flex-inner"][2]/div[@class="fast-fact-item"][1]/p/a/@href').extract()
        tuition_fee_link = ''.join(tuition_fee_link)
        tuition_fee_links = 'https://www.newcastle.edu.au' + str(tuition_fee_link)
        self.parse_tuition_fee(tuition_fee_links, item)

        modules_url = response.xpath('//*[@id="what-you-will-study"]/div[@class="clearfix"]/div[@class="col w40"]/p/a/@href | //*[@id="what-you-will-study"]/div[@class="clearfix"]/div[@class="col w40"]//p[2]/a/@href').extract()
        modules_url = ''.join(modules_url)
        print('modules_url:',modules_url)
        if "https" not in modules_url:
            modules_fullurl = 'https://www.newcastle.edu.au/degrees/' + modules_url
            print('modules_fullurl:', modules_fullurl)
            self.parse_modules(modules_fullurl, item)

        location = response.xpath(
            '//*[@id="tab-how-to-apply"]/div[@class="fast-facts fast-facts-ug"]/div[@class="fast-facts-content"]/div[@data-region="international"]/div[@class="flex-inner"][1]/div[@class="fast-fact-item"][1]/p/a/text()').extract()
        location = ''.join(location)
        # item["location"] = location
        # print('location:', location)

        IELTS = response.xpath(
            '//*[@class="fast-facts-content"]/div[@class="fast-fact-items" and @data-region="international"]/div[@class="flex-inner"][2]/div[@class="fast-fact-item"]/ul/li/text()').extract()
        IELTS = ''.join(IELTS)
        # item["IELTS"] = IELTS
        # print('IELTS:', IELTS)

        chinese_requirements = response.xpath(
            '//*[@class="fast-facts fast-facts-ug"]/div[@class="fast-facts-content"]/div[@class="entrance-rank"]//div[@class="fast-fact-item"]/ul/li//text()').extract()
        chinese_requirements = ''.join(chinese_requirements)
        # item["chinese_requirements"] = chinese_requirements
        # print('chinese_requirements:', chinese_requirements)

        degree_description = response.xpath(
            '//*[@id="uon-body"]/div[@class="wrapped clearfix"]/div[@class="body-content"]/div[@class="grid-content grid-2-column"]/div[@class="grid-block"]/p/text() | //*[@id="what-you-will-study"]/div[@class="clearfix"]/div[@class="col w60"]/p/text() ').extract()
        degree_description = ''.join(degree_description)
        # item["degree_description"] = degree_description
        # print('degree_description:', degree_description)

        how_to_apply = response.xpath(
            '//*[@class="grid-block"]/div[@class="apply-info"]/div[@data-region="international"]/p/a/@href').extract()
        how_to_apply = ''.join(how_to_apply)
        # item["how_to_apply"] = how_to_apply
        # print('how_to_apply:', how_to_apply)

        entry_requirements = response.xpath(
            '//*[@data-region="international"]//div[@class="uon-accordion-content"]//text()').extract()
        entry_requirements = ''.join(entry_requirements)
        # item["entry_requirements"] = entry_requirements
        # print('entry_requirements:', entry_requirements)

        create_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # item["create_time"] = create_time

        num_programme = response.xpath(
            '//div[@class="majors-list grid-content grid-3-column"]/div[@class="grid-block"]//text()').extract()
        # print('num_programme:',len(num_programme))
        for i in range(1, len(num_programme) + 1):
            # print(i)
            programme = response.xpath(
                '//div[@class="majors-list grid-content grid-3-column"]/div[@class="grid-block"][' + str(
                    i) + ']//text()').extract()
            programme = ''.join(programme)
            # item["programme"] = programme
            print('programme:', programme)

            programme_url = response.xpath('//div[@class="grid-block"][' + str(i) + ']/a/@href').extract()
            for u in programme_url:
                if "https" not in u:
                    url = 'https://www.newcastle.edu.au/degrees/' + u
                    print('url:', url)
                    yield scrapy.Request(url, callback=self.parse_item,
                                         meta={"degree_type": degree_type, "duration": duration, "mode": mode,"city":city,"website":website,"career":career,"tuition_fee_links":tuition_fee_links,"programme":programme,
                                               "location": location,"university":university,"country":country,"degree_level":degree_level,"start_date":start_date,"modules_fullurl":modules_fullurl,
                                               "degree_description": degree_description, "IELTS":IELTS,"chinese_requirements":chinese_requirements,"how_to_apply":how_to_apply,"entry_requirements":entry_requirements,"create_time":create_time,
                                               })

        # yield item

    def parse_item(self,response):
        print('2,====================',response.url)
        item = get_item(HooliItem)
        overview = response.xpath('//*[@id="uon-body"]//text()').extract()
        overview = ''.join(overview)
        item["overview"] = overview
        url = response.url
        item["url"] = url
        university = response.meta["university"]
        item["university"] = university

        country = response.meta["country"]
        item["country"] = country
        city = response.meta["city"]
        item["city"] = city
        website = response.meta["website"]
        item["website"] = website
        degree_level = response.meta["degree_level"]
        item["degree_level"] = degree_level
        degree_type = response.meta["degree_type"]
        item["degree_type"] = degree_type
        print('degree_type:', degree_type)

        start_date = response.meta["start_date"]
        item["start_date"] = start_date
        print('start_date:', start_date)

        mode = response.meta["mode"]
        item["mode"] = mode
        print('mode:', mode)

        duration = response.meta["duration"]
        item["duration"] = duration
        print('duration:', duration)

        career = response.meta["career"]
        item["career"] = career
        print('career:', career)

        location = response.meta["location"]
        item["location"] = location
        print('location:', location)

        IELTS = response.meta["IELTS"]
        item["IELTS"] = IELTS
        print('IELTS:', IELTS)

        chinese_requirements = response.meta["chinese_requirements"]
        item["chinese_requirements"] = chinese_requirements
        print('chinese_requirements:', chinese_requirements)

        degree_description = response.meta["degree_description"]
        item["degree_description"] = degree_description
        print('degree_description:', degree_description)

        how_to_apply = response.meta["how_to_apply"]
        item["how_to_apply"] = how_to_apply
        print('how_to_apply:', how_to_apply)

        entry_requirements = response.meta["entry_requirements"]
        item["entry_requirements"] = entry_requirements
        print('entry_requirements:', entry_requirements)

        create_time = response.meta["create_time"]
        item["create_time"] = create_time

        yield item

    # def parse_overview(self, programme_urls, item):
    #     print('3,==================',programme_urls)
    #     data = requests.get(programme_urls)
    #     response = etree.HTML(data.text)
    #     overview = response.xpath('//*[@id="uon-body"]//text()')
    #     overview = ''.join(overview)
    #     item["overview"] = overview

        # print('overview:',overview)

    def parse_modules(self, modules_fullurl, item):
        print('4,==================',modules_fullurl)
        date = requests.get(modules_fullurl)
        response = etree.HTML(date.text)

        department = response.xpath('//*[@id="section-details"]/table/tbody//text()')
        department = ''.join(department)
        if "Managing faculty" in department:
            start = department.find("Managing faculty")
            end = department.find("Contributing schools")
            department = department[start:end]
        else:
            department = ""
        item["department"] = department
        # print('department:', department)

        modules = response.xpath('//div[@id="section-program-structure"]//text()')
        modules = ' '.join(modules)
        item["modules"] = modules
        # print('modules:',modules)

    def parse_tuition_fee(self, tuition_fee_links, item):
        # print('2,==================',tuition_fee_links)
        data = requests.get(tuition_fee_links)
        response = etree.HTML(data.text)
        tuition_fee = response.xpath('//*[@id="content-main"]/div[@class="pdf"]/a/@href')
        tuition_fee = ' '.join(tuition_fee)
        item["tuition_fee"] = tuition_fee



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
