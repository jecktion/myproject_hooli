
# -*- coding: utf-8 -*-


import scrapy
from school_3.items import HooliItem
import datetime
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import re
from lxml import etree
import requests
from school_3.getDegree_type import getDegree_type
from school_3.clearSpace import clear_space
from school_3.getItem import get_item

class PlymouthSpider(scrapy.Spider):
    name = 'New_South_Wales_ug'
    allowed_domains = ['www.international.unsw.edu.au']
    start_urls = []
    base_url = 'http://www.international.unsw.edu.au%s'

    Lists = ['/faculty/art-design-undergraduate-degree-programs',
'/faculty/arts-social-sciences-undergraduate-degree-programs',
'/faculty/built-environment-undergraduate-degree-programs',
'/faculty/business-school-undergraduate-degree-programs',
'/faculty/engineering-undergraduate-degree-programs',
'/faculty/law-undergraduate-degree-programs',
'/faculty/medicine-undergraduate-degree-programs',
'/faculty/science-undergraduate-degree-programs']

    for i in Lists:
        fullurl = base_url % i
        start_urls.append(fullurl)

    def parse(self,response):
        print('1,===============',response.url)
        item = get_item(HooliItem)
        url = response.url
        item["url"] = url
        university = 'The University of New South Wales'
        item["university"] = university
        country = 'Australia'
        item["country"] = country
        city = "UNSW Canberra"
        item["city"] = city
        website = 'http://www.international.unsw.edu.au'
        item["website"] = website
        degree_level = '0'
        item["degree_level"] = degree_level
        create_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        item["create_time"] = create_time

        full_department = response.xpath('//div[@class="contentarea-contained"]/div[@class="contentarea-smalltitle"]//h4/span[1]//text()').extract()
        print('full_department:',full_department)
        num_department = len(full_department)
        print(num_department)
        for I in range(2,int(num_department)+2):
            # print(type(I))
            department = response.xpath('//div[@class="contentarea-contained"][' +str(I)+ ']/div[@class="contentarea-smalltitle"]//h4/span[1]/text()').extract()
            department = ''.join(department)
            item["department"] = department
            print('department:',department)

            num =response.xpath('//div[@class="contentarea-contained"][' +str(I)+ ']/div[@class="contentarea-smalltitle"]//h4/span/span[@class="circlenumber-number"]/text()').extract()
            num = ''.join(num)
            print('num:',num)
            for i in range(1,int(num)+1):
                programme = response.xpath('//div[@class="degree-list"][' +str(I-1)+ ']/div[@class="degree js-degree"][' +str(i)+ ']//h5/text()').extract()
                programme = ''.join(programme)
                item["programme"] = programme
                print('programme:',programme)

                ucas_code = response.xpath('//div[@class="degree-list"][' +str(I-1)+ ']/div[@class="degree js-degree"][' +str(i) +']//div[@class="degree-programcode"]/text()').extract()
                ucas_code = ''.join(ucas_code)
                item["ucas_code"] = ucas_code
                print('ucas_code:',ucas_code)

                degree_type = response.xpath('//div[@class="degree-list"][' +str(I-1)+ ']/div[@class="degree js-degree"][' +str(i)+ ']//h5/text()').extract()
                degree_type = ''.join(degree_type)
                getDegree_type(degree_type)
                item["degree_type"] = degree_type
                print('degree_type:',getDegree_type(degree_type))

                start_date = response.xpath('//div[@class="degree-list"][' +str(I-1)+ ']/div[@class="degree js-degree"][' +str(i)+ ']//div[@class="degree-inner"]/div[@class="degree-content js-degree-content"]//dl[1]/dd[2]/text()').extract()
                start_date = ''.join(start_date)
                item["start_date"] = start_date
                print('start_date:',start_date)

                duration = response.xpath('//div[@class="degree-list"][' +str(I-1)+ ']/div[@class="degree js-degree"][' +str(i)+ ']//div[@class="degree-inner"]/div[@class="degree-content js-degree-content"]//dl[1]/dd[1]/text()').extract()
                duration = ''.join(duration)
                item["duration"] = duration
                print('duration:',duration)

                career = response.xpath('//div[@class="degree-list"][' +str(I-1)+ ']/div[@class="degree js-degree"][' +str(i)+ ']//div[@class="degree-inner"]/div[@class="degree-content js-degree-content"]//dl[2]//text()').extract()
                career = ''.join(career)
                item["career"] = career
                print('career:',career)

                tuition_fee = response.xpath('//div[@class="degree-list"][' +str(I-1)+ ']/div[@class="degree js-degree"][' +str(i)+ ']//div[@class="degree-inner"]/div[@class="degree-content js-degree-content"]//dl[1]/dd[4]/text()').extract()
                tuition_fee = ''.join(tuition_fee)
                item["tuition_fee"] = tuition_fee
                print('tuition_fee:',tuition_fee)

                degree_links = response.xpath('//div[@class="degree-list"][' +str(I-1)+ ']/div[@class="degree js-degree"][' +str(i)+ ']//div[@class="degree-inner"]/div[@class="degree-content js-degree-content"]//div[@class="degree-content-cta"]//a/@href').extract()
                print('degree_links:',degree_links)
                self.parse_page(degree_links, item)


    def parse_page(self,degree_links,item):
        print('2,===============', degree_links)
        date = requests.get(degree_links)
        print('date:',date)
        response = etree.HTML(date.text)
        degree_description = response.xpath('//div[@class="content"]//div[@class="field field-type-text-long"]/p/text()')
        degree_description = ''.join( degree_description)
        print('degree_description:',degree_description)
        item["degree_description"] = degree_description

        mode = response.xpath('//div[@class="content"]//div[@class="field field-type-text-long"]/p[2]/text()')
        mode = ''.join(mode)
        print('mode:',mode)
        item["mode"] = mode

        programme_url_s = response.xpath('//*[@id="content"]/article/div[@class="content"]/div[@class="field field-type-text-long"]/ul[2]/li/a/@href')
        print('programme_url_s:',programme_url_s)
        for programme_url in programme_url_s:
            print(programme_url)
            self.parse_item(programme_url,item)




    def parse_item(self,programme_url,item):
        print('programme_url:==========',programme_url)
        dates = requests.get(programme_url)
        print('date:',dates)
        response = etree.HTML(dates.text)
        overview = response.xpath('//div[@class="content"]/div[@class="field field-type-text-long"]/p[@class="intro"]/text()')
        overview = ''.join(overview)
        print('overview:',overview)
        item["overview"] = overview

        modules = response.xpath('//div[@class="content"]/div[@class="field field-type-text-long"]/ul/li/text()')
        modules = ''.join(modules)
        print('modules:',modules)
        item["modules"] = modules

        duration = response.xpath('//div[@class="content"]/div[@class="field field-type-text-long"]/p[@class="dtp"]/text()')
        duration = ''.join(duration)
        print('duration:',duration)
        item["duration"] = duration














