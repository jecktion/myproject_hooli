








import scrapy
from school_1.items import HooliItem
import datetime
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import re

class PlymouthSpider(CrawlSpider):
    name = 'uwtsd_gd'
    allowed_domains = ['www.uwtsd.ac.uk']
    start_urls = []
    base_url = 'http://www.uwtsd.ac.uk%s'

    Lists = ['/ma-outdoor-education/',
'/cipd-postgraduate-diploma-in-human-resource-development/',
'/cipd-postgraduate-diploma-in-human-resource-management/',
'/phd/',
'/ma-3d-computer-animation/',
'/ma-ancient-history/',
'/ma-ancient-religions/',
'/ma-biblical-interpretation/',
'/ma-celtic-studies/',
'/ma-chinese-buddhist-textual-studies/',
'/ma-chinese-daoist-textual-studies/',
'/ma-classical-studies/',
'/ma-classics/',
'/ma-confucian-classical-studies/',
'/ma-creative-script-writing/',
'/ma-creative-writing/',
'/ma-cultural-astronomy-astrology/',
'/postgraduate/ma-cyfarwyddo/',
'/ma-ecology-spirituality/',
'/ma-engaged-anthropology/',
'/ma-equality-diversity-society/',
'/ma-fine-art/',
'/ma-glass/',
'/ma-heritage-practice/',
'/ma-heritage-tourism/',
'/ma-human-resource-development/',
'/ma-advanced-vocal-studies/',
'/ma-international-tourism-management/',
'/ma-islamic-studies/',
'/ma-landscape-management-environmental-archaeology/',
'/ma-local-history/',
'/ma-medieval-early-modern-literature/',
'/ma-medieval-studies/',
'/ma-modern-literature/',
'/ma-philosophy/',
'/ma-photography/',
'/ma-physical-education/',
'/ma-product-design/',
'/ma-sinology/',
'/ma-study-of-religions/',
'/ma-surface-pattern-design/',
'/ma-textiles/',
'/postgraduate/ma-theatr-a-pherfformio/',
'/ma-transportation-design/',
'/ma-visual-communication/',
'/mphil/',
'/mphil-business/',
'/mba/',
'/mdes-design-crafts/',
'/mdes-architectural-glass-arts/',
'/postgraduate/mres-ancient-history/',
'/mres-anthropology/',
'/postgraduate/mres-art-and-design/',
'/mres-biblical-interpretation/',
'/mres-classical-studies/',
'/mres-computing/',
'/mres-contemporary-literature/',
'/mres-cultural-astronomy-astrology/',
'/mres-early-modern-literature/',
'/mres-heritage-practice/',
'/mres-islamic-studies/',
'/mres-landscape-environmental-archaeology/',
'/mres-medieval-literature/',
'/mres-medieval-studies/',
'/mres-philosophy/',
'/mres-religious-experience/',
'/postgraduate/mres-study-of-religions/',
'/msc-accounting-finance/',
'/msc-applied-computing/',
'/msc-applied-social-health-psychology/',
'/msc-computer-networks/',
'/msc-ecommerce/',
'/msc-engineering-product-design/',
'/msc-engineering-project-management/',
'/msc-environmental-conservation-management/',
'/msc-financial-management/',
'/msc-financial-management-pld/',
'/msc-industrial-design/',
'/msc-lean-agile-manufacturing/',
'/msc-mechanical-engineering/',
'/msc-non-destructive-testing-and-evaluation/',
'/msc-software-engineering/',
'/msc-sustainable-construction/',
'/msc-trading-financial-markets/',
'/mth-christian-theology/',
'/mth-church-history/',
'/pgce-primary/',
'/postgraduate/pgce-secondary-art--design-with-qts/',
'/postgraduate/pgce--secondary-biology-with-qts/',
'/postgraduate/pgce-secondary-business-studies-with-qts/',
'/postgraduate/pgce-secondary-chemistry-with-qts/',
'/postgraduate/pgce-secondary-computing-and-ict-with-qts/',
'/postgraduate/pgce-secondary-design-and-technology-with-qts/',
'/postgraduate/pgce-secondary-english-with-qts/',
'/postgraduate/pgce-secondary-geography-with-qts/',
'/postgraduate/pgce-secondary-history-with-qts/',
'/postgraduate/pgce-secondary-maths-11-16-with-ict-and-qts/',
'/postgraduate/pgce-secondary-maths-11-18-with-qts/',
'/postgraduate/pgce-secondary-modern-foreign-languages-with-qts/',
'/postgraduate/pgce-secondary-physics-with-qts/',
'/postgraduate/pgce-secondary-religious-education-with-qts/',
'/postgraduate/pgce-secondary-science-11-16-with-qts/',
'/postgraduate/pgce-secondary-welsh-with-qts/',
'/pce-post-compulsory-education-training/']

    for i in Lists:
        fullurl = base_url % i
        start_urls.append(fullurl)

    rules = (
        Rule(LinkExtractor(allow=(r'.*'), restrict_xpaths=('//p[@class="lead"]/a')),follow=True),
        Rule(LinkExtractor(allow=r'.*'),callback='parse_item',follow=False),
        # Rule(LinkExtractor(allow=(r'.*'), restrict_xpaths=('')),callback='parse_item',follow=False),
    )

    # def parse(self, response):
    #     if self.start_urls == 'https://www.worcester.ac.uk/courses/archaeology-heritage-studies-and-art-design-ba-hons.html':
    #         link_list = response.xpath('//*[@id="#content"]/div/div/section//a/@href')
    #         print("======================++++++++++++++++++++++++++++++++")
    #         print(link_list)
    #         print("======================++++++++++++++++++++++++++++++++")
    #         for i in link_list:
    #             link = "https://www.worcester.ac.uk" + str(i)
    #             yield scrapy.Request(link, callback=self.parse_item)
    #     else:
    #         print('错误页面')

    def parse_item(self,response):
        print('==================================',response.url)
        item = HooliItem()

        url = response.url
        print(1,url)

        university = 'University of Wales, Trinity St David'
        print(2,university)

        country = 'UK'
        city = 'NULL'
        website = 'http://www.uwtsd.ac.uk'

        department = response.xpath('/html/body/div/div/div/div/div/div/p/a/strong/text()').extract()
        department = '  '.join(department)

        print(3,department)

        # programme = response.xpath('//div[@class="section picture-nav"]/h1/text()').extract()
        programme = response.xpath('//*[@class="span12"]/h1//text()').extract()
        programme = ''.join(programme)
        print(4,programme)

        ucas_code = response.xpath('/html/body/div/div/div/div/div/div/p/strong/text()').extract()[:20]
        ucas_code = ''.join(ucas_code)
        print(5,ucas_code)

        degree_level = '1'

        # degree_type = response.xpath('//div[@class="section picture-nav"]/h1/text()').extract()
        degree_type = response.xpath('//*[@class="span12"]/h1//text()').extract()
        degree_type = ''.join(degree_type)
        # try:
        #     if "BSc" in degree_type:
        #         degree_type = 'Bsc'
        #     elif "BA" in degree_type:
        #         degree_type = 'BA'
        #     elif "MNSW" in degree_type:
        #         degree_type = 'MNSW'
        #     elif "PGCert" in degree_type:
        #         degree_type = 'PGCert'
        #     elif "MBA" in degree_type:
        #         degree_type = 'MBA'
        #     elif "MA" in degree_type:
        #         degree_type = 'MA'
        #     elif "MComp" in degree_type:
        #         degree_type = 'MComp'
        #     elif "PhD" in degree_type:
        #         degree_type = 'PhD'
        #     elif "FdA" in degree_type:
        #         degree_type =  'FdA'
        #     elif "PGCE" in degree_type:
        #         degree_type = 'PGCE'
        #     elif "IFP" in degree_type:
        #         degree_type = 'IFP'
        #     elif "LLB" in degree_type:
        #         degree_type = 'LLB'
        #     elif "MHealth Res" in degree_type:
        #         degree_type = 'MHealth Res'
        #     elif "MRes" in degree_type:
        #         degree_type = 'MRes'
        #     elif "MMed" in degree_type:
        #         degree_type = 'MMed'
        #     elif "MSci" in degree_type:
        #         degree_type = 'MSci'
        #     elif "MCh" in degree_type:
        #         degree_type = 'MCh'
        #     else:
        #         degree_type = 'Ordinary degree'
        # except:
        #     degree_type = "报错!"
        print(6,degree_type)

        degree_description = 'NULL'

        start_date_s = response.xpath('/html/body/div/div/div/div/div/div/p/em/text()').extract()
        start_date_s = ''.join(start_date_s)
        try:
            if "Start Date:" in start_date_s:
                start_date = start_date_s
            else:
                start_date = 'NULL'
        except:
            start_date = "NULL"
        print(7,start_date)

        # overview = response.xpath('//div[@class="left logo-bg"]//text()').extract()
        overview = response.xpath('//*[@class="span6"]/p//text()').extract()
        overview = ''.join(overview)
        print(8, overview)

        mode_s = response.xpath('//*[@class="span3"]/p//text()').extract()
        mode_s = ''.join(mode_s)
        if "full time" in mode_s:
            mode = 'full time'
        else:
            mode = 'NULL'
        # mode = mode.replace('\n','')
        # mode = mode.replace('      ','')
        print(9,mode)

        duration_s = response.xpath('/html/body/div/div/div/div/div/div/p/strong/text()').extract()
        duration_s = ''.join(duration_s)
        # duration = duration.replace('\n','')
        # duration = duration.replace('    ','')
        try:
            if "year" in duration_s:
                duration =  duration_s
            else:
                duration = "NULL"
        except:
            duration = "NULL"

        print(10,duration)

        modules = response.xpath('//*[@id="collapseModules"]//text()').extract()
        modules = ''.join(modules)
        # modules = modules.replace('\n','')
        print(11,modules)

        teaching = 'NULL'

        assessment = response.xpath('//*[@id="collapseAssessment"]//text()').extract()
        assessment = ''.join(assessment)
        print(12, assessment)

        career = response.xpath('//*[@id="collapseCareerOpportunities"]//text()').extract()
        career = ''.join(career)
        print(13, career)

        application_date = 'NULL'

        deadline = 'NULL'

        application_fee = 'NULL'

        tuition_fee= 'NULL'
        # tuition_fee = ''.join(tuition_fee)
        # # tuition_fee = tuition_fee.replace('\n','')
        # # tuition_fee = tuition_fee.replace('    ','')
        # print(9, tuition_fee)

        location = response.xpath('//*[@class="span3"]/p//text()').extract()
        location = ''.join(location)
        print(14,location)


        GPA = 'NULL'

        ATAS = 'NULL'

        average_score = 'NULL'

        accredited_university = 'NULL'

        Alevel = 'NULL'

        IB = 'NULL'

        IELTS = 'NULL'
        # IELTS = ''.join(IELTS)
        # # IELTS = re.findall('(IELTS:|IELTS)? (.*){0,5} \d?.\d? .{0,70}',IELTS)
        # print(10, IELTS)
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
        # how_to_apply = ''.join(how_to_apply)
        # print(11,how_to_apply)

        entry_requirements = response.xpath('//*[@id="collapseEntryCriteria"]//text()').extract()
        entry_requirements = ''.join(entry_requirements)
        # EntryRequirements = EntryRequirements.replace(' ','')
        print(15,entry_requirements)

        chinese_requirements = 'NULL'

        school_test = 'NULL'

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