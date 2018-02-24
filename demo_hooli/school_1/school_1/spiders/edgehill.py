








import scrapy
from school_1.items import HooliItem
import datetime
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import re

class PlymouthSpider(CrawlSpider):
    name = 'edgehill'
    allowed_domains = ['www.edgehill.ac.uk']
    start_urls = []
    base_url = '%s'


    Lists = ['https://www.edgehill.ac.uk/courses/accountancy/',
'https://www.edgehill.ac.uk/courses/adult-nursing-and-social-work/',
'https://www.edgehill.ac.uk/courses/advanced-computer-networking/',
'https://www.edgehill.ac.uk/courses/advanced-critical-care/',
'https://www.edgehill.ac.uk/courses/advanced-fertility-practice/',
'https://www.edgehill.ac.uk/courses/advanced-practice/',
'https://www.edgehill.ac.uk/courses/advertising/',
'https://www.edgehill.ac.uk/courses/animation/',
'https://www.edgehill.ac.uk/courses/applied-clinical-nutrition/',
'https://www.edgehill.ac.uk/courses/behaviour-analysis-and-intervention/',
'https://www.edgehill.ac.uk/courses/big-data-analytics/',
'https://www.edgehill.ac.uk/courses/big-data-analytics-pgcert/',
'https://www.edgehill.ac.uk/courses/biology/',
'https://www.edgehill.ac.uk/courses/biology-ske/',
'https://www.edgehill.ac.uk/courses/biotechnology/',
'https://www.edgehill.ac.uk/courses/master-of-business-administration/',
'https://www.edgehill.ac.uk/courses/master-of-business-administration-finance/',
'https://www.edgehill.ac.uk/courses/master-of-business-administration-hrm/',
'https://www.edgehill.ac.uk/courses/master-of-business-administration-information-technology/',
'https://www.edgehill.ac.uk/courses/master-of-business-administration-marketing/',
'https://www.edgehill.ac.uk/courses/business-and-economics/',
'https://www.edgehill.ac.uk/courses/business-and-management/',
'https://www.edgehill.ac.uk/courses/business-and-management-with-accounting-and-finance/',
'https://www.edgehill.ac.uk/courses/business-and-management-with-human-resource-management/',
'https://www.edgehill.ac.uk/courses/business-and-management-with-leisure-and-tourism/',
'https://www.edgehill.ac.uk/courses/business-and-management-with-logistics-and-supply-chain-management/',
'https://www.edgehill.ac.uk/courses/business-and-management-with-marketing/',
'https://www.edgehill.ac.uk/courses/business-information-systems/',
'https://www.edgehill.ac.uk/courses/business-innovation-and-enterprise/',
'https://www.edgehill.ac.uk/courses/cardiothoracic-practice/',
'https://www.edgehill.ac.uk/courses/child-and-adolescent-mental-health-and-wellbeing/',
'https://www.edgehill.ac.uk/courses/child-and-adolescent-mental-health-and-wellbeing-msc/',
'https://www.edgehill.ac.uk/courses/child-health-and-wellbeing/',
'https://www.edgehill.ac.uk/courses/childhood-youth-studies-and-criminology/',
'https://www.edgehill.ac.uk/courses/childhood-youth-studies-and-sociology/',
'https://www.edgehill.ac.uk/courses/childhood-and-youth-studies/',
'https://www.edgehill.ac.uk/courses/children-and-young-people-s-learning-and-development/',
'https://www.edgehill.ac.uk/courses/childrens-nursing-and-social-work/',
'https://www.edgehill.ac.uk/courses/clinical-and-professional-cardiothoracic-care/',
'https://www.edgehill.ac.uk/courses/clinical-and-professional-palliative-practice/',
'https://www.edgehill.ac.uk/courses/clinical-and-professional-paramedic-practice/',
'https://www.edgehill.ac.uk/courses/clinical-and-professional-perioperative-practice/',
'https://www.edgehill.ac.uk/courses/clinical-and-professional-practice/',
'https://www.edgehill.ac.uk/courses/clinical-education/',
'https://www.edgehill.ac.uk/courses/clinical-reproductive-medicine/',
'https://www.edgehill.ac.uk/courses/coaching-and-mentoring-for-wellbeing/',
'https://www.edgehill.ac.uk/courses/computer-science/',
'https://www.edgehill.ac.uk/courses/computer-science-bsc/',
'https://www.edgehill.ac.uk/courses/computer-science-and-mathematics/',
'https://www.edgehill.ac.uk/courses/computer-security-and-networks/',
'https://www.edgehill.ac.uk/courses/computing-mcomp/',
'https://www.edgehill.ac.uk/courses/computing/',
'https://www.edgehill.ac.uk/courses/computing-msc/',
'https://www.edgehill.ac.uk/courses/computing-games-programming/',
'https://www.edgehill.ac.uk/courses/computing-networking-security-and-forensics/',
'https://www.edgehill.ac.uk/courses/conservation-management/',
'https://www.edgehill.ac.uk/courses/counselling-and-psychotherapy/',
'https://www.edgehill.ac.uk/courses/creative-and-cultural-education/',
'https://www.edgehill.ac.uk/courses/creative-performance/',
'https://www.edgehill.ac.uk/courses/creative-writing/',
'https://www.edgehill.ac.uk/courses/creative-writing-ma/',
'https://www.edgehill.ac.uk/courses/creative-writing-and-drama/',
'https://www.edgehill.ac.uk/courses/creative-writing-and-english-literature/',
'https://www.edgehill.ac.uk/courses/creative-writing-and-film-studies/',
'https://www.edgehill.ac.uk/courses/criminology-ba/',
'https://www.edgehill.ac.uk/courses/criminology-and-law/',
'https://www.edgehill.ac.uk/courses/criminology-and-psychology/',
'https://www.edgehill.ac.uk/courses/criminology-and-sociology/',
'https://www.edgehill.ac.uk/courses/critical-screen-practice/',
'https://www.edgehill.ac.uk/courses/cyber-security/',
'https://www.edgehill.ac.uk/courses/dance/',
'https://www.edgehill.ac.uk/courses/dance-and-drama/',
'https://www.edgehill.ac.uk/courses/data-science/',
'https://www.edgehill.ac.uk/courses/dental-implantology/',
'https://www.edgehill.ac.uk/courses/phd/',
'https://www.edgehill.ac.uk/courses/drama/',
'https://www.edgehill.ac.uk/courses/drama-and-english-literature/',
'https://www.edgehill.ac.uk/courses/drama-and-film-studies/',
'https://www.edgehill.ac.uk/courses/early-childhood-studies/',
'https://www.edgehill.ac.uk/courses/early-childhood-studies-and-sociology/',
'https://www.edgehill.ac.uk/courses/early-years-education-and-leadership/',
'https://www.edgehill.ac.uk/courses/early-years-education-with-qts/',
'https://www.edgehill.ac.uk/courses/pgce-early-years/',
'https://www.edgehill.ac.uk/courses/early-years-leadership-fda/',
'https://www.edgehill.ac.uk/courses/early-years-leadership/',
'https://www.edgehill.ac.uk/courses/early-years-practice-ba/',
'https://www.edgehill.ac.uk/courses/early-years-practice/',
'https://www.edgehill.ac.uk/courses/ecology-and-conservation/',
'https://www.edgehill.ac.uk/courses/education-ba/',
'https://www.edgehill.ac.uk/courses/education-dyscalculia/',
'https://www.edgehill.ac.uk/courses/education-inclusion-sen/',
'https://www.edgehill.ac.uk/courses/education-and-english/',
'https://www.edgehill.ac.uk/courses/education-and-history/',
'https://www.edgehill.ac.uk/courses/education-and-religion/',
'https://www.edgehill.ac.uk/courses/education-and-sociology/',
'https://www.edgehill.ac.uk/courses/educational-enquiry-and-professional-learning/',
'https://www.edgehill.ac.uk/courses/educational-psychology/',
'https://www.edgehill.ac.uk/courses/emergency-services-management/',
'https://www.edgehill.ac.uk/courses/employment-enterprise-and-entrepreneurship-development/',
'https://www.edgehill.ac.uk/courses/pre-sessional-english/',
'https://www.edgehill.ac.uk/courses/english-ske/',
'https://www.edgehill.ac.uk/courses/english/',
'https://www.edgehill.ac.uk/courses/english-ma/',
'https://www.edgehill.ac.uk/courses/english-and-film-studies/',
'https://www.edgehill.ac.uk/courses/english-language/',
'https://www.edgehill.ac.uk/courses/english-language-with-creative-writing/',
'https://www.edgehill.ac.uk/courses/english-literature/',
'https://www.edgehill.ac.uk/courses/english-literature-and-history/',
'https://www.edgehill.ac.uk/courses/english-literature-with-creative-writing/',
'https://www.edgehill.ac.uk/courses/english-with-creative-writing/',
'https://www.edgehill.ac.uk/courses/environmental-science/',
'https://www.edgehill.ac.uk/courses/fastrack-preparation-for-higher-education/',
'https://www.edgehill.ac.uk/courses/film-and-media/',
'https://www.edgehill.ac.uk/courses/film-and-television-production/',
'https://www.edgehill.ac.uk/courses/film-studies/',
'https://www.edgehill.ac.uk/courses/film-studies-with-film-production/',
'https://www.edgehill.ac.uk/courses/food-science/',
'https://www.edgehill.ac.uk/courses/further-education-and-training-pgce/',
'https://www.edgehill.ac.uk/courses/games-programming-and-visual-computing/',
'https://www.edgehill.ac.uk/courses/genetics/',
'https://www.edgehill.ac.uk/courses/geoenvironmental-hazards/',
'https://www.edgehill.ac.uk/courses/geography-ske/',
'https://www.edgehill.ac.uk/courses/geography-ba/',
'https://www.edgehill.ac.uk/courses/geography-bsc/',
'https://www.edgehill.ac.uk/courses/geology-with-physical-geography/',
'https://www.edgehill.ac.uk/courses/global-public-health/',
'https://www.edgehill.ac.uk/courses/health-and-social-care-leadership-and-management/',
'https://www.edgehill.ac.uk/courses/health-and-social-wellbeing/',
'https://www.edgehill.ac.uk/courses/history/',
'https://www.edgehill.ac.uk/courses/history-and-culture/',
'https://www.edgehill.ac.uk/courses/history-with-politics/',
'https://www.edgehill.ac.uk/courses/human-biology/',
'https://www.edgehill.ac.uk/courses/human-geography/',
'https://www.edgehill.ac.uk/courses/information-security-and-it-management/',
'https://www.edgehill.ac.uk/courses/information-technology-management-for-business/',
'https://www.edgehill.ac.uk/courses/integrated-children-and-young-people-s-practice/',
'https://www.edgehill.ac.uk/courses/international-business/',
'https://www.edgehill.ac.uk/courses/international-foundation-programme/',
'https://www.edgehill.ac.uk/courses/law/',
'https://www.edgehill.ac.uk/courses/law-with-criminology/',
'https://www.edgehill.ac.uk/courses/law-with-politics/',
'https://www.edgehill.ac.uk/courses/leadership-and-management-development/',
'https://www.edgehill.ac.uk/courses/leadership-development/',
'https://www.edgehill.ac.uk/courses/learning-disabilities-and-nursing-social-work/',
'https://www.edgehill.ac.uk/courses/making-performance/',
'https://www.edgehill.ac.uk/courses/marketing/',
'https://www.edgehill.ac.uk/courses/marketing-communications-and-branding/',
'https://www.edgehill.ac.uk/courses/marketing-with-advertising/',
'https://www.edgehill.ac.uk/courses/marketing-with-digital-communications/',
'https://www.edgehill.ac.uk/courses/clinical-research/',
'https://www.edgehill.ac.uk/courses/health-research/',
'https://www.edgehill.ac.uk/courses/mres/',
'https://www.edgehill.ac.uk/courses/mathematics/',
'https://www.edgehill.ac.uk/courses/media-management/',
'https://www.edgehill.ac.uk/courses/media-film-and-television/',
'https://www.edgehill.ac.uk/courses/media-music-and-sound/',
'https://www.edgehill.ac.uk/courses/medical-leadership/',
'https://www.edgehill.ac.uk/courses/master-of-medicine/',
'https://www.edgehill.ac.uk/courses/mental-health-law-and-ethics/',
'https://www.edgehill.ac.uk/courses/mental-health-nursing-and-social-work/',
'https://www.edgehill.ac.uk/courses/midwifery/',
'https://www.edgehill.ac.uk/courses/midwifery-msc/',
'https://www.edgehill.ac.uk/courses/music/',
'https://www.edgehill.ac.uk/courses/music-production/',
'https://www.edgehill.ac.uk/courses/musical-theatre/',
'https://www.edgehill.ac.uk/courses/nursing-adult/',
'https://www.edgehill.ac.uk/courses/nursing-children/',
'https://www.edgehill.ac.uk/courses/nursing-learning-disabilities/',
'https://www.edgehill.ac.uk/courses/nursing-mental-health/',
'https://www.edgehill.ac.uk/courses/nursing-adult-msc/',
'https://www.edgehill.ac.uk/courses/nursing-child-msc/',
'https://www.edgehill.ac.uk/courses/nursing-learning-disabilities-msc/',
'https://www.edgehill.ac.uk/courses/nursing-mental-health-msc/',
'https://www.edgehill.ac.uk/courses/nutrition-msci/',
'https://www.edgehill.ac.uk/courses/nutrition-and-health/',
'https://www.edgehill.ac.uk/courses/operating-department-practice-bsc/',
'https://www.edgehill.ac.uk/courses/paramedic-practice-bsc/',
'https://www.edgehill.ac.uk/courses/physical-education-and-school-sport/',
'https://www.edgehill.ac.uk/courses/physical-geography/',
'https://www.edgehill.ac.uk/courses/physical-geography-and-geology/',
'https://www.edgehill.ac.uk/courses/plant-science/',
'https://www.edgehill.ac.uk/courses/policing/',
'https://www.edgehill.ac.uk/courses/politics-and-criminology/',
'https://www.edgehill.ac.uk/courses/politics-and-history/',
'https://www.edgehill.ac.uk/courses/politics-and-media/',
'https://www.edgehill.ac.uk/courses/politics-and-sociology/',
'https://www.edgehill.ac.uk/courses/popular-culture/',
'https://www.edgehill.ac.uk/courses/pre-masters-programme/',
'https://www.edgehill.ac.uk/courses/pgce-primary/',
'https://www.edgehill.ac.uk/courses/primary-education-with-qts/',
'https://www.edgehill.ac.uk/courses/primary-education-with-qts-school-based-route/',
'https://www.edgehill.ac.uk/courses/pgce-primary-mathematics-specialist/',
'https://www.edgehill.ac.uk/courses/primary-physical-education-specialist/',
'https://www.edgehill.ac.uk/courses/professional-clinical-practice/',
'https://www.edgehill.ac.uk/courses/professional-development-ba/',
'https://www.edgehill.ac.uk/courses/professional-development-business-leadership-and-management/',
'https://www.edgehill.ac.uk/courses/psychology/',
'https://www.edgehill.ac.uk/courses/psychology-msc/',
'https://www.edgehill.ac.uk/courses/psychology-and-criminology/',
'https://www.edgehill.ac.uk/courses/psychosocial-analysis-of-offending-behaviour/',
'https://www.edgehill.ac.uk/courses/public-health-nutrition/',
'https://www.edgehill.ac.uk/courses/robotics-and-artificial-intelligence/',
'https://www.edgehill.ac.uk/courses/pgce-secondary-computer-science-and-information-technology/',
'https://www.edgehill.ac.uk/courses/pgce-secondary-english/',
'https://www.edgehill.ac.uk/courses/secondary-english-education-with-qts/',
'https://www.edgehill.ac.uk/courses/pgce-secondary-geography/',
'https://www.edgehill.ac.uk/courses/pgce-secondary-history/',
'https://www.edgehill.ac.uk/courses/pgce-secondary-mathematics/',
'https://www.edgehill.ac.uk/courses/secondary-mathematics-education-with-qts/',
'https://www.edgehill.ac.uk/courses/pgce-secondary-physical-education/',
'https://www.edgehill.ac.uk/courses/pgce-secondary-religious-education/',
'https://www.edgehill.ac.uk/courses/secondary-religious-education-with-qts/',
'https://www.edgehill.ac.uk/courses/pgce-secondary-science-biology/',
'https://www.edgehill.ac.uk/courses/simulation-and-clinical-learning/',
'https://www.edgehill.ac.uk/courses/social-work-ma/',
'https://www.edgehill.ac.uk/courses/social-work/',
'https://www.edgehill.ac.uk/courses/sociology/',
'https://www.edgehill.ac.uk/courses/sociology-with-politics/',
'https://www.edgehill.ac.uk/courses/software-application-development/',
'https://www.edgehill.ac.uk/courses/software-engineering/',
'https://www.edgehill.ac.uk/courses/special-educational-needs-coordination/',
'https://www.edgehill.ac.uk/courses/specialist-primary-mathematics-practice/',
'https://www.edgehill.ac.uk/courses/spld-dyslexia/',
'https://www.edgehill.ac.uk/courses/sport-and-exercise-psychology/',
'https://www.edgehill.ac.uk/courses/sport-and-exercise-science-msci/',
'https://www.edgehill.ac.uk/courses/sport-and-exercise-science/',
'https://www.edgehill.ac.uk/courses/sport-physical-activity-and-mental-health/',
'https://www.edgehill.ac.uk/courses/sports-coaching-and-development-msci/',
'https://www.edgehill.ac.uk/courses/sports-coaching-and-development/',
'https://www.edgehill.ac.uk/courses/sports-development-and-management/',
'https://www.edgehill.ac.uk/courses/sports-management-and-coaching/',
'https://www.edgehill.ac.uk/courses/sports-therapy-msci/',
'https://www.edgehill.ac.uk/courses/sports-therapy/',
'https://www.edgehill.ac.uk/courses/supporting-pre-hospital-care/',
'https://www.edgehill.ac.uk/courses/master-of-surgery/',
'https://www.edgehill.ac.uk/courses/surgical-care-practice/',
'https://www.edgehill.ac.uk/courses/teaching-and-learning-in-clinical-practice/',
'https://www.edgehill.ac.uk/courses/teaching-learning-and-child-development/',
'https://www.edgehill.ac.uk/courses/television-production-management/',
'https://www.edgehill.ac.uk/courses/tesol/',
'https://www.edgehill.ac.uk/courses/web-design-and-development-mcomp/',
'https://www.edgehill.ac.uk/courses/web-design-and-development/',
'https://www.edgehill.ac.uk/courses/working-and-teaching-in-the-early-years/',
'https://www.edgehill.ac.uk/courses/working-with-children-5-11/',
'https://www.edgehill.ac.uk/courses/workplace-based-postgraduate-medical-education/']

    for i in Lists:
        fullurl = base_url % i
        start_urls.append(fullurl)

    rules = (
        # Rule(LinkExtractor(allow=(r'/courses/.*'), restrict_xpaths=('//div[@id="content"]/div/a')),callback='parse_item',follow=True),
        # Rule(LinkExtractor(allow=r''),follow=True),
        Rule(LinkExtractor(allow=(r'/courses/.*'), restrict_xpaths=('//ul[@id="tabs"]/li/h2/a')),callback='parse_item',follow=False),
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

        university = 'Edge Hill University'
        print(2,university)

        country = 'UK'
        city = 'NULL'
        website = 'https://www.edgehill.ac.uk'

        department = response.xpath('//*[@id="overview"]//tr//text()').extract()[6:8]
        department = '  '.join(department)
        print(3,department)

        programme = response.xpath('//*[@id="primary"]/header/h1//text()').extract()
        # programme = response.xpath('//section[@class="pageHead"]/h1/text()').extract()
        programme = ''.join(programme)

        print(4,programme)

        ucas_code_s = response.xpath('//*[@id="overview"]//text()').extract()
        ucas_code_s = ''.join(ucas_code_s)
        try:
            if " Code:" in ucas_code_s:
                start = ucas_code_s.find("Code:")
                end = ucas_code_s.find("Course Length:")
                ucas_code = ucas_code_s[start:end]
                item["ucas_code"] = ucas_code
            else:
                ucas_code = 'NULL'
        except:
            ucas_code = '报错!'
        print(5,ucas_code)

        degree_level = '1'

        degree_type = response.xpath('//*[@id="primary"]/header/h1//text()').extract()
        # degree_type = response.xpath('//section[@class="pageHead"]/h1/text()').extract()
        degree_type = ''.join(degree_type)
        try:
            if "BSc" in degree_type:
                degree_type = 'Bsc'
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
                degree_type =  'FdA'
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
            else:
                degree_type = 'Ordinary degree'
        except:
            degree_type = "N/A"
        print(5,degree_type)

        start_date_s = response.xpath('//*[@id="overview"]//text()').extract()
        start_date_s = ''.join(start_date_s)
        try:
            if "Start Dates:" in start_date_s:
                start = start_date_s.find("Start Dates:")
                end = start_date_s.find("Department:")
                start_date = start_date_s[start:end]
                item["start_date"] = start_date
            else:
                start_date = 'NULL'
        except:
            start_date = '报错!'
        print(6,start_date)

        degree_description = 'NULL'

        overview = response.xpath('//*[@id="overview"]//text()').extract()
        # overview = response.xpath('//div[@class="body-copy"]/ul/li/text()').extract()
        overview = ''.join(overview)
        print(7, overview)

        mode_s = response.xpath('//*[@id="overview"]//tr//text()').extract()
        mode_s = ''.join(mode_s)
        # mode = mode.replace('\n','')
        # mode = mode.replace('      ','')
        try:
            if "Full-Time" in mode_s:
                mode = "Full-Time"
            else:
                mode = "Part-Time"
        except:
            mode = "报错!"
        print(8,mode)


        duration_s = response.xpath('//*[@id="overview"]//text()').extract()
        duration_s = ''.join(duration_s)
        # duration = duration.replace('\n','')
        # duration = duration.replace('    ','')
        try:
            if "Length:" in duration_s:
                start = duration_s.find("Length:")
                end = duration_s.find("Start Dates:")
                duration = duration_s[start:end]
                item["duration"] = duration
            else:
                duration = "NULL"
        except:
            duration = "报错!"

        print(9,duration)

        modules = response.xpath('//*[@id="modules"]//text()').extract()
        modules = ''.join(modules)
        # modules = modules.replace('\n','')
        print(10,modules)

        teaching = 'NULL'

        assessment = response.xpath('//*[@id="course-in-depth"]//text()').extract()
        assessment = ''.join(assessment)
        print(11, assessment)

        career = response.xpath('//*[@id="careers-and-employability"]//text()').extract()
        career = ''.join(career)
        print(12, career)

        application_date = 'NULL'

        deadline = 'NULL'

        application_fee = 'NULL'

        # tuition_fee= response.xpath('//*[@id="finance"]//text()').extract()[3:9]
        tuition_fee = '£12,750'
        # tuition_fee = ''.join(tuition_fee)

        # tuition_fee = tuition_fee.replace('\n','')
        # tuition_fee = tuition_fee.replace('    ','')
        print(13, tuition_fee)

        location = response.xpath('//*[@id="overview"]//tr//text()').extract()
        location = ''.join(location)
        print(14,location)

        ATAS = 'NULL'
        GPA = 'NULL'
        MCAT = 'NULL'

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

        working_experience = 'NULL'

        interview = 'NULL'

        portfolio = 'NULL'

        application_documents = 'NULL'

        how_to_apply = response.xpath('//*[@id="next-steps"]//text()').extract()
        how_to_apply = ''.join(how_to_apply)
        print(15,how_to_apply)

        entry_requirements = response.xpath('//*[@id="entry-criteria"]//text()').extract()
        entry_requirements = ''.join(entry_requirements)
        # EntryRequirements = EntryRequirements.replace(' ','')
        print(16,entry_requirements)

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