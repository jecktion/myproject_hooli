







import scrapy
from school_1.items import HooliItem
import datetime
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import re

class PlymouthSpider(CrawlSpider):
    name = 'uwtsd'
    allowed_domains = ['www.uwtsd.ac.uk']
    start_urls = []
    base_url = 'http://www.uwtsd.ac.uk%s'

    Lists = ['/undergraduate/applied-computing/meng-computer-systems-electronics-applied-environmental-engineering/',
'/bsc-architecture/',
'/beng-automotive-engineering/',
'/beng-automotive-engineering-4-yr/',
'/ba-accounting/',
'/ba-applied-drama/',
'/ba-business-and-management/',
'/ba-business-management/',
'/ba-performing-arts-contemporary-performance/',
'/ba-cultural-industries-management/',
'/ba-design-crafts/',
'/ba-architectural-glass-arts/',
'/ba-international-business/',
'/ba-law-and-business/',
'/ba-rural-enterprise-management/',
'/ba-3d-computer-animation/',
'/ba-acting/',
'/ba-adventure-filmmaking/',
'/ba-advertising-brand-design/',
'/ba-advocacy/',
'/ba-ancient-civilisations/',
'/ba-ancient-history/',
'/ba-ancient-history-archaeology/',
'/ba-ancient-history-history/',
'/ba-ancient-history-ancient-egyptian-culture/',
'/ba-ancient-history-education-studies/',
'/ba-ancient-history-latin/',
'/ba-anthropology/',
'/ba-anthropology-psychology/',
'/ba-archaeology/',
'/ba-archaeology-anthropology/',
'/ba-art-gallery-museum-studies/',
'/ba-automotive-design/',
'/ba-business-management-events-festivals/',
'/ba-business-management-finance/',
'/ba-business-management-human-resource-management/',
'/ba-business-management-marketing/',
'/ba-celtic-studies/',
'/ba-chinese-civilisation-and-medieval-studies/',
'/ba-chinese-studies/',
'/ba-chinese-studies-education-studies/',
'/ba-classical-civilisation/',
'/ba-classical-studies-heritage-studies/',
'/ba-classical-studies-archaeology/',
'/ba-classical-studies-creative-writing/',
'/ba-classical-studies-theology/',
'/ba-classical-studies-ancient-egyptian-culture/',
'/ba-classical-studies-with-education-studies/',
'/undergraduate/classics/ba-classical-civilisation-with-greek/',
'/ba-english-classical-studies/',
'/ba-classical-studies-religious-studies/',
'/ba-classical-studies-heritage-management/',
'/ba-conflict-and-war/',
'/ba-counselling-studies-psychology/',
'/ba-creative-computer-games-design/',
'/ba-creative-writing/',
'/ba-dance/',
'/ba-digital-marketing/',
'/ba-early-years-education-and-care/',
'/ba-early-years-education-and-care-early-years-practitioner/',
'/undergraduate/early-years/ba-early-years-education-and-care-early-years-practitioner---2-years/',
'/ba-early-years-education-and-care-early-years-practitioner-2-years/',
'/ba-education-studies/',
'/ba-education-studies-additional-learning-needs-inclusion/',
'/ba-education-studies-contemporary-learners-learning/',
'/ba-education-studies-international-perspectives/',
'/ba-primary-education-studies/',
'/ba-english/',
'/ba-english-classical-studies/',
'/ba-english-education-studies/',
'/ba-english-tefl/',
'/ba-ethical-political-studies/',
'/ba-event-management/',
'/ba-film-tv/',
'/ba-film-visual-culture/',
'/ba-filmmaking/',
'/ba-fine-art-site-context/',
'/ba-graphic-design/',
'/ba-heritage-studies/',
'/ba-heritage-studies-digital-humanities/',
'/ba-history/',
'/ba-history-education-studies/',
'/ba-humanistic-counselling/',
'/ba-illustration/',
'/ba-international-development-and-global-politics/',
'/ba-international-hotel-management/',
'/ba-international-sports-management/',
'/ba-international-travel-and-tourism-management/',
'/ba-law-criminology/',
'/ba-law-policing/',
'/ba-law-and-public-service/',
'/ba-management-skills-for-the-workplace/',
'/ba-leisure-management/',
'/ba-humanities/',
'/ba-medieval-studies/',
'/ba-medieval-studies-classical-studies/',
'/ba-medieval-studies-modern-historical-studies/',
'/ba-medieval-studies-latin/',
'/ba-modern-historical-studies-heritage-management/',
'/ba-modern-historical-studies/',
'/ba-music-performance-production/',
'/bsc-music-technology/',
'/ba-new-media-production/',
'/ba-outdoor-education/',
'/cbc/ba-perfformio/',
'/ba-philosophy/',
'/ba-philosophy-classical-studies/',
'/ba-philosophy-psychology/',
'/ba-philosophy-education-studies/',
'/undergraduate/politics--economics/ba-philosophy-politics-and-economics/',
'/ba-philosophy-religion-applied-psychology/',
'/ba-photography-in-the-arts/',
'/ba-photojournalism/',
'/ba-physical-education/',
'/undergraduate/ecology/ba-political-ecology/',
'/ba-primary-education-qts/',
'/ba-product-design/',
'/ba-public-services/',
'/ba-religion-ethics-applied-psychology/',
'/ba-religion-philosophy-ethics/',
'/ba-religion-theology-ethics/',
'/ba-religion-theology-philosophy/',
'/ba-religious-studies/',
'/ba-religious-studies-theology/',
'/ba-religious-studies-psychology/',
'/ba-religious-studies-education-studies/',
'/ba-religious-studies-islamic-studies/',
'/ba-set-design/',
'/ba-sinology/',
'/ba-social-studies-additional-needs/',
'/ba-social-studies-advocacy/',
'/ba-social-studies-communities-families-individuals/',
'/ba-social-studies-health-social-care/',
'/ba-sport-health/',
'/ba-sports-management/',
'/ba-stadium-sports-facility-management/',
'/ba-surface-pattern-design-fashion-object/',
'/ba-surface-pattern-design-contemporary-applied-arts-practice/',
'/ba-surface-pattern-design-textiles-for-fashion/',
'/ba-surface-pattern-design-textiles-for-interiors/',
'/ba-theatre-design-production/',
'/ba-theology-education-studies/',
'/ba-theology-philosophy-ethics/',
'/ba-tourism-management/',
'/ba-transport-design/',
'/ba-vocal-studies/',
'/ba-watersports-management/',
'/ba-youth-community-work/',
'/beng-electrical-electronic-engineering/',
'/bsc-psychology/',
'/bsc-applied-psychology/',
'/bsc-health-care-children-young-people/',
'/bsc-health-social-care/',
'/bsc-health-management/',
'/bsc-health-nutrition-lifestyle/',
'/bsc-mental-health/',
'/bsc-police-sciences/',
'/bsc-policing-criminology/',
'/bsc-product-design-technology/',
'/bsc-public-health/',
'/bsc-sports-exercise-science/',
'/bsc-sports-exercise-science-clinical-exercise-physiology/',
'/bsc-outdoor-fitness/',
'/bsc-personal-training/',
'/bsc-sports-exercise-science-sports-nutrition/',
'/bsc-sport-therapy/',
'/courses/welsh-learners/certificate-in-practical-welsh-advanced/',
'/cert-he-art-and-design-foundation/',
'/cert-he/certificate-of-higher-education-in-advocacy/',
'/cert-he-chinese/',
'/cert-he/certificate-of-higher-education-in-playwork/',
'/cert-he/certificate-of-higher-education-in-stem/',
'/certhe-young-peoples-health-wellbeing/',
'/certificate-of-higher-education-skills-for-the-workplace/',
'/ba-chinese-studies-history/',
'/level6-advanced-diploma-logistics-transport/',
'/intermediate-certificate-in-human-resource-management/',
'/bsc-computing/',
'/bsc-computer-networks/',
'/bsc-computing-information-systems-foundation/',
'/bsc-computer-games-development/',
'/bsc-software-engineering/',
'/bsc-web-development/',
'/bsc-web-development-foundation/',
'/bsc-applied-computing-foundation/',
'/hnd-electronics-engineering/',
'/beng-energy-environmental-engineering-4-year/',
'/beng-energy-environmental-engineering/',
'/bsc-environmental-conservation/',
'/beng-extreme-sports-engineering-4-year/',
'/beng-extreme-sports-engineering/',
'/fdsc-health-care-children-young-people/',
'/fda-early-childhood/',
'/fda-events-management/',
'/ba-social-inclusion-inclusive-education/',
'/fda-inclusive-studies-for-teaching-assistants/',
'/fda-learning-support/',
'/fda-sports-management/',
'/fda-tourism-management/',
'/foundation-year-for-computing-electronics/',
'/cert-he/gateway-to-the-humanities/',
'/graduate-diploma-bible-theology/',
'/hnc-business-management/',
'/hnd-business-finance/',
'/hnd-business-management/',
'/hnd-events-management/',
'/hnd-health-social-care/',
'/hnd-health-informatics/',
'/hnd-health-management/',
'/hnd-public-services/',
'/hnd-sports-management/',
'/hnd-tourism-management/',
'/wiwbl/courses-we-offer/human-factors-in-the-workplace/',
'/integrated-masters-advocacy/',
'/integrated-masters-humanistic-counselling/',
'/msocstud-social-studies-additional-needs/',
'/msocstud-social-studies-health-social-care/',
'/wiwbl/courses-we-offer/introduction-to-marketing/',
'/wiwbl/courses-we-offer/introduction-to-process-safety/',
'/bsc-logistics-supply-chain-management/',
'/mtour-tourism-management/',
'/wiwbl/courses-we-offer/managing-teams/',
'/marts-ancient-civilisations/',
'/marts-3d-computer-animation/',
'/marts-art-gallery-museum-studies/',
'/marts-classical-languages/',
'/marts-creative-computer-games-design/',
'/marts-digital-film-television-production/',
'/mart-fine-art/',
'/undergraduate/international-development-and-global-politics/marts-international-development-humanitarianism-and-law/',
'/marts-photography-in-the-arts/',
'/marts-photojournalism/',
'/mdes-advertising-brand-design/',
'/mdes-automotive-design/',
'/mdes-graphic-design/',
'/mdes-illustration/',
'/mdes-product-design/',
'/mdes-product-design-technology/',
'/mdes-set-design/',
'/mdes-surface-pattern-design-fashion-object/',
'/mdes-surface-pattern-design-maker/',
'/mdes-surface-pattern-design-textile-for-interiors/',
'/mdes-surface-pattern-design-textile-for-fashion/',
'/mdes-transport-design/',
'/meach-early-childhood/',
'/beng-mechanical-manufacturing-engineering-4-year/',
'/beng-mechanical-engineering-four-year-including-foundation-entry/',
'/beng-mechanical-engineering/',
'/marts-music-technology/',
'/beng-motorcycle-engineering/',
'/beng-motorcycle-engineering-4yr/',
'/beng-motorsport-engineering/',
'/beng-motorsport-engineering-4yrs/',
'/bsc-motorsport-management/',
'/dip-he-nursing-studies-health/',
'/wiwbl/courses-we-offer/process-safety-risk-analysis/',
'/wiwbl/courses-we-offer/process-safety-risk-management/',
'/wiwbl/courses-we-offer/project-management/',
'/wiwbl/courses-we-offer/promoting-bilingualism/',
'/wiwbl/courses-we-offer/recruitment-and-selection/',
'/wiwbl/courses-we-offer/research-methods-for-work-based-learning/',
'/wiwbl/courses-we-offer/stress-in-the-workplace/',
'/certhe-health-and-wellbeing-for-carers/',
'/cert-he/certificate-of-higher-education-workplace-health-and-wellbeing/',
'/wiwbl/courses-we-offer/training-the-trainers/',
'/wiwbl/courses-we-offer/workplace-coaching/']

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

        department = response.xpath('/html/body/div/div/div/div/div/div/p/a/strong//text()').extract()
        department = ''.join(department)
        print(3,department)

        # programme = response.xpath('//div[@class="section picture-nav"]/h1/text()').extract()
        programme = response.xpath('//h1[@class="t4-course-title"]/text()').extract()
        programme = ''.join(programme)
        print(4,programme)

        ucas_code = response.xpath('//div[@class="span3"]/p//text()').extract()[:7]
        ucas_code = ''.join(ucas_code)
        print(5,ucas_code)

        degree_level = '0'

        # degree_type = response.xpath('//div[@class="section picture-nav"]/h1/text()').extract()
        degree_type = response.xpath('//h1[@class="t4-course-title"]/text()').extract()
        degree_type = ''.join(degree_type)
        print(6,degree_type)

        start_date = 'NULL'
        # start_date = ''.join(start_date)
        # print(7,start_date)

        degree_description = 'NULL'

        # overview = response.xpath('//div[@class="left logo-bg"]//text()').extract()
        overview = response.xpath('//div[@class="span6"]//text()').extract()
        overview = ''.join(overview)
        print(8, overview)

        mode_s = response.xpath('//div[@class="span3"]/p//text()').extract()
        mode_s = ''.join(mode_s)
        try:
            if "Full Time" in mode_s:
                mode = "Full Time"
            else:
                mode = "Full Time"
        except:
            mode = "Part Time"
        # mode = mode.replace('\n','')
        # mode = mode.replace('      ','')
        print(9,mode)


        duration = response.xpath('//div[@class="span3"]/p//text()').extract()[1:30]
        duration = ''.join(duration)
        # duration = duration.replace('\n','')
        # duration = duration.replace('    ',''

        print(10,duration)

        modules = response.xpath('//*[@id="collapseModules"]//text()').extract()
        modules = ''.join(modules)
        # modules = modules.replace('\n','')
        print(11,modules)

        teaching = 'NULL'

        assessment = response.xpath('//*[@id="collapseAssessment"]//text()').extract()
        assessment = ''.join(assessment)
        print(12,assessment)

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

        location = response.xpath('//div[@class="span3"]/p//text()').extract()
        location = ''.join(location)
        print(14,location)

        ATAS = 'NULL'

        GPA = 'NULL'

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