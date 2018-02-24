







import scrapy
from school_1.items import HooliItem
import datetime
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import re

class PlymouthSpider(CrawlSpider):
    name = 'worcester_s'
    allowed_domains = ['www.worcester.ac.uk']
    start_urls = []
    base_url = 'https://www.worcester.ac.uk%s'

    Lists = ['/journey/uwic-programme-accountancy-business-marketing.html',
'/journey/accounting-and-finance-ba-hons-wbs.html',
'/journey/advancing-practice-msc.html',
'/journey/allied-health-studies-mphil-phd.html',
'/journey/animal-biology-bsc-hons.html',
'/journey/animal-biology-mbiol-integrated-masters.html',
'/journey/animal-biology-mphil-phd.html',
'/journey/animal-biology-degrees.html',
'/journey/animation-ba-hons.html',
'/journey/animation-degrees.html',
'/journey/applied-health-social-care-ba-top-up.html',
'/journey/applied-sport-science-msc.html',
'/journey/applied-sports-performance-analysis-msc.html',
'/journey/arabic-module.html',
'/journey/archaeology-heritage-studies-degrees.html',
'/journey/archaeology-mphil-phd.html',
'/journey/master-research-archaeology.html',
'/journey/archaeology-and-heritage-studies-ba-hons.html',
'/journey/art-and-design-mphil-phd.html',
'/journey/uwic-programme-art-design-creative-media.html',
'/journey/atmospheric-sciences-mphil-phd.html',
'/journey/biochemistry-bsc-hons.html',
'/journey/biochemistry-mbiol-integrated-masters.html',
'/journey/biochemistry-mphil-phd.html',
'/journey/biology-degrees.html',
'/journey/biology-bsc-hons.html',
'/journey/biology-mbiol-integrated-masters.html',
'/journey/master-research-biology.html',
'/journey/biomedical-sciences-bsc-hons.html',
'/journey/birth-and-beyond-ba-top-up.html',
'/journey/birth-beyond-fda.html',
'/journey/business-and-accountancy-ba-hons.html',
'/journey/business-and-digital-communications-ba-hons.html',
'/journey/business-and-enterprise-ba-hons.html',
'/journey/business-and-finance-ba-hons.html',
'/journey/business-and-human-resource-management-ba-hons.html',
'/journey/business-and-marketing-ba-hons.html',
'/journey/uwic-programme-pg-business.html',
'/journey/business-administration-ba-hons.html',
'/journey/business-information-technology-bsc-hons.html',
'/journey/business-mphil-phd.html',
'/journey/business-management-ba-hons-top-up.html',
'/journey/business-management-ba-hons-wbs.html',
'/journey/business-management-hnd.html',
'/journey/business-management-degrees.html',
'/journey/business-psychology-bsc-hons.html',
'/journey/business-studies-ba-hons.html',
'/journey/business-economics-finance-ba-hons-wbs.html',
'/journey/online-celta-course.html',
'/journey/chartered-manager-degree-apprenticeship.html',
'/journey/child-adolescent-mental-health-fdsc.html',
'/journey/child-adolescent-mental-health-bsc-hons-top-up.html',
'/journey/mres-clinical-education.html',
'/journey/clinical-psychology-bsc-hons.html',
'/journey/collaborative-working-with-children-young-people-families-fda.html',
'/journey/computer-games-design-development-bsc-hons.html',
'/journey/computing-bsc-hons.html',
'/journey/computing-hnd.html',
'/journey/computing-mphil-phd.html',
'/journey/computing-degrees.html',
'/journey/counselling-fdsc.html',
'/journey/counselling-msc.html',
'/journey/counselling-psychology-bsc-hons.html',
'/journey/creative-professional-writing-ba-hons.html',
'/journey/creative-professional-writing-degrees.html',
'/journey/creative-digital-media-mphil-phd.html',
'/journey/creative-digital-media-degrees.html',
'/journey/creative-digital-media-ba-hons.html',
'/journey/creative-media-ma.html',
'/journey/cricket-coaching-management-bsc-hons.html',
'/journey/criminology-ba-hons.html',
'/journey/criminology-mphil-phd.html',
'/journey/criminology-with-policing-ba-hons.html',
'/journey/dance-hnd.html',
'/journey/dance-and-community-practice-ba-hons.html',
'/journey/dementia-studies-mphil-phd.html',
'/journey/dental-technology-fdsc.html',
'/journey/design-mres.html',
'/journey/developmental-psychology-bsc-hons.html',
'/journey/diploma-in-education-and-training.html',
'/journey/doctor-business-administration-dba.html',
'/journey/doctor-education-edd.html',
'/journey/drama-performance-degrees.html',
'/journey/drama-performance-ma.html',
'/journey/drama-performance-ba-hons.html',
'/journey/drama-and-performance-mphil-phd.html',
'/journey/msc-emdr-therapy.html',
'/journey/early-childhood-professional-practice-ba-hons.html',
'/journey/early-modern-studies-mres.html',
'/journey/early-years-foundation-degree-flexible-distributed-learning-pathway.html',
'/journey/early-years-sector-endorsed-fda.html',
'/journey/ecology-bsc-hons.html',
'/journey/ecology-mphil-phd.html',
'/journey/mres-ecology-environmental-management.html',
'/journey/ecology-degrees.html',
'/journey/education-ma.html',
'/journey/education-mphil-phd.html',
'/journey/mres-education.html',
'/journey/education-studies-ba-hons.html',
'/journey/education-studies-degrees.html',
'/journey/english-language-studies-ba-hons.html',
'/journey/english-language-degrees.html',
'/journey/english-literature-ba-hons.html',
'/journey/english-literature-and-language-mphil-phd.html',
'/journey/english-literature-degrees.html',
'/journey/entrepreneurship-ba-hons-wbs.html',
'/journey/environmental-science-bsc-hons.html',
'/journey/environmental-science-degrees.html',
'/journey/environmental-studies-science-mphil-phd.html',
'/journey/film-production-ba-hons.html',
'/journey/film-production-degrees.html',
'/journey/film-studies-ba-hons.html',
'/journey/film-studies-mphil-phd.html',
'/journey/film-studies-degrees.html',
'/journey/fine-art-practice-ba-hons.html',
'/journey/fine-art-mres.html',
'/journey/fine-art-degrees.html',
'/journey/football-business-management-coaching-fdsc.html',
'/journey/forensic-psychology-bsc-hons.html',
'/journey/forensic-and-applied-biology-bsc-hons.html',
'/journey/free-general-english-classes.html',
'/journey/french-module.html',
'/journey/game-art-ba-hons.html',
'/journey/game-art-degrees.html',
'/journey/general-english-classes-advanced.html',
'/journey/general-english-classes-english-foreign-language.html',
'/journey/geography-bsc-hons.html',
'/journey/geography-degrees.html',
'/journey/german-module.html',
'/journey/graphic-design-ba-hons.html',
'/journey/graphic-design-multimedia-degrees.html',
'/journey/green-media-mres.html',
'/journey/health-sciences-bsc-hons.html',
'/journey/health-and-social-care-fdsc.html',
'/journey/higher-education-mapgdippgcert.html',
'/journey/history-ba-hons.html',
'/journey/history-mphil-phd.html',
'/journey/history-mres.html',
'/journey/history-degrees.html',
'/journey/human-biology-bsc-hons.html',
'/journey/human-biology-mbiol-integrated-masters.html',
'/journey/human-biology-mphil-phd.html',
'/journey/human-biology-degrees.html',
'/journey/human-geography-ba-hons.html',
'/journey/huma-geography-mphil-phd.html',
'/journey/human-nutrition-bsc-hons.html',
'/journey/human-nutrition-degrees.html',
'/journey/human-resource-management-ma.html',
'/journey/management-human-resources-msc.html',
'/journey/ielts-preparation-classes-english-foreign-language.html',
'/journey/illustration-ba-hons.html',
'/journey/illustration-degrees.html',
'/journey/language-module-improving-english-in-academic-language.html',
'/journey/language-module-improving-english-in-academic-writing-non-native-speakers.html',
'/journey/integrated-working-children-families-ba-hons-top-up-degree.html',
'/journey/integrative-counselling-ba-hons.html',
'/journey/integrative-counselling-fda.html',
'/journey/international-business-management-ba-hons-wbs.html',
'/journey/international-finance-ba-hons-top-up-wbs.html',
'/journey/management-msc.html',
'/journey/international-sport-management-msc.html',
'/journey/introduction-to-teaching-english-foreign-language.html',
'/journey/intro-teaching-english-as-a-foreign-language-lang1001.html',
'/journey/introduction-to-tefl-language-awareness-lang1012.html',
'/journey/introduction-to-tefl-lang1013.html',
'/journey/italian-module.html',
'/journey/japanese-module.html',
'/journey/journalism-ba-hons.html',
'/journey/journalism-degrees.html',
'/journey/21020.html',
'/journey/language-awareness-and-analysis-tefl-module.html',
'/journey/uwic-programme-law.html',
'/journey/law-llb-hons.html',
'/journey/law-with-criminology-llb-hons.html',
'/journey/law-with-forensic-psychology-llb-hons.html',
'/journey/leadership-and-management-fda-ba.html',
'/journey/leading-culture-change-in-safeguarding-pgcert.html',
'/journey/leading-early-years-practice-pgcert.html',
'/journey/learning-support-fda.html',
'/journey/learning-and-development-early-years-to-adolescence-fda.html',
'/journey/teaching-and-learning-in-higher-education-pg-cert.html',
'/journey/master-of-business-administration-mba.html',
'/journey/mba-executive-leadership-and-management-part-time.html',
'/journey/marketing-ba-hons-wbs.html',
'/journey/marketing-advertising-and-public-relations-ba-hons-wbs.html',
'/journey/mathematics-mphil-phd.html',
'/journey/mathematics-bsc-hons.html',
'/journey/media-and-cultural-studies-ba-hons.html',
'/journey/media-culture-degrees.html',
'/journey/media-and-cultural-studies-mphil-phd.html',
'/journey/mental-health-fdsc.html',
'/journey/mentoring-in-early-childhood-pgcert.html',
'/journey/midwifery-bsc-hons.html',
'/journey/midwifery-mphil-phd.html',
'/journey/music-education-ba-mmus.html',
'/journey/national-award-senco-nasc-special-educational-needs-coordination-pg-cert.html',
'/journey/nursing-bsc-hons.html',
'/journey/nursing-mphil-phd.html',
'/journey/nursing-studies-bsc-hons.html',
'/journey/nutrition-and-health-access-module.html',
'/journey/nutritional-therapy-msc.html',
'/journey/occupational-therapy-bsc-hons.html',
'/journey/occupational-therapy-mphil-phd.html',
'/journey/business-psychology-msc-occupational-psychology-msc.html',
'/journey/open-short-language-courses.html',
'/journey/outdoor-adventure-leadership-management-bsc-hons.html',
'/journey/outdoor-education-ma.html',
'/journey/supervision-pgcert.html',
'/journey/postgraduate-certificate-in-education-pgce-primary.html',
'/journey/pgce-primary-mathematics.html',
'/journey/pgce-primary-physical-education.html',
'/journey/pgce-school-direct-primary.html',
'/journey/pgce-school-direct-secondary.html',
'/journey/postgraduate-certificate-in-education-pgce-secondary.html',
'/journey/paramedic-science-bsc-hons.html',
'/journey/pharmacology-bsc-hons.html',
'/journey/physical-education-bsc-hons.html',
'/journey/physical-education-and-dance-ba-hons.html',
'/journey/physical-education-and-outdoor-education-bsc-hons.html',
'/journey/physical-education-degrees.html',
'/journey/physical-geography-bsc-hons.html',
'/journey/physical-geography-mphil-phd.html',
'/journey/physician-associate-msc.html',
'/journey/physiotherapy-bsc-hons.html',
'/journey/plant-biology-mphil-phd.html',
'/journey/politics-ba-hons.html',
'/journey/positive-psychology-coaching-pgcert.html',
'/journey/primary-initial-teacher-education-ba-hons.html',
'/journey/primary-outdoor-education-ba-hons.html',
'/journey/professional-practice-ba-hons-top-up-degree .html',
'/journey/psychology-bsc-hons.html',
'/journey/psychology-mphil-phd.html',
'/journey/psychology-msc.html',
'/journey/psychology-degrees.html',
'/journey/public-health-msc.html',
'/journey/religion-philosophy-and-values-in-education-ba-hons.html',
'/journey/master-research-river-science.html',
'/journey/uwic-programme-science-health-social-science.html',
'/journey/screenwriting-ba-hons.html',
'/journey/screenwriting-degrees.html',
'/journey/social-work-social-policy-mphil-phd.html',
'/journey/social-work-ba-hons.html',
'/journey/social-work-ma.html',
'/journey/master-research-socio-cultural-studies-sport-exercise.html',
'/journey/sociology-ba-hons.html',
'/journey/sociology-mphil-phd.html',
'/journey/sociology-degrees.html',
'/journey/special-educational-needs-disabilities-inclusion-ba-hons.html',
'/journey/sport-exercise-psychology-bsc-hons.html',
'/journey/uwic-programme-sport-exercise-science.html',
'/journey/sport-exercise-science-bsc-hons.html',
'/journey/sport-exercise-science-mphil-phd.html',
'/journey/sport-business-management-bsc-hons.html',
'/journey/sport-development-coaching-ba-hons.html',
'/journey/sport-coaching-physical-education-hnd.html',
'/journey/sports-coaching-msc.html',
'/journey/sports-coaching-science-bsc-hons.html',
'/journey/sports-coaching-science-degrees.html',
'/journey/sports-coaching-science-with-disability-sport-bsc-hons.html',
'/journey/sports-studies-bsc-hons.html',
'/journey/sports-studies-degrees.html',
'/journey/sports-therapy-bsc-hons.html',
'/journey/subject-knowledge-enhancement-ske.html',
'/journey/teaching-english-celta-course.html',
'/journey/teaching-and-learning-fda.html',
'/journey/theatre-performance-mres.html',
'/journey/mtheatre-touring-theatre-integrated-masters.html',
'/journey/understanding-domestic-and-sexual-violence-ma.html',
'/journey/university-diploma-in-leadership-and-management.html',
'/journey/university-diploma-in-academic-tutoring.html',
'/journey/web-development-bsc-hons.html']

    for i in Lists:
        fullurl = base_url % i
        start_urls.append(fullurl)

    rules = (
        Rule(LinkExtractor(allow=(r'.*'), restrict_xpaths=('//*[@id="aToZ"]/ul/li/a')),callback='parse_item',follow=True),
        # Rule(LinkExtractor(allow=r'/courses/.*'),callback='parse_item',follow=True),
        Rule(LinkExtractor(allow=(r'.*'), restrict_xpaths=('//*[@class="box__inner box__inner--purple"]//a')),callback='parse_item',follow=False),
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

        university = 'University of Worcester'
        print(2,university)

        country = 'UK'

        city = 'NULL'

        website = 'https://www.worcester.ac.uk'

        department = 'NULL'

        programme_s = response.xpath('//*[@id="content"]/div/h1//text()').extract()
        # programme = response.xpath('//section[@class="pageHead"]/h1/text()').extract()
        programme_s = ''.join(programme_s)
        if len(programme_s) > 0:
            programme = programme_s
        else:
            programme = 'NULL'
        print(3,programme)

        ucas_code = 'NULL'

        degree_level = ''

        degree_type = response.xpath('//*[@id="content"]/div/h1//text()').extract()
        # degree_type = response.xpath('//section[@class="pageHead"]/h1/text()').extract()
        degree_type = ''.join(degree_type)
        degree_type = self.getDegree_type(degree_type)
        print(4,degree_type)

        start_date = 'NULL'
        # start_date = ''.join(start_date)
        # print(5,start_date)

        degree_description = 'NULL'

        overview = response.xpath('//div[@class="left logo-bg"]//text()').extract()
        # overview = response.xpath('//div[@class="body-copy"]/ul/li/text()').extract()
        overview = ''.join(overview)
        print(5, overview)

        mode = 'NULL'
        # mode = ''.join(mode).replace('\r\n','')
        # mode = mode.replace('\n','')
        # mode = mode.replace('      ','')
        # print(7,mode)


        duration = 'NULL'
        # duration = ''.join(duration).replace('\r\n','')
        # duration = duration.replace('\n','')
        # duration = duration.replace('    ','')
        # print(8,duration)

        modules = response.xpath('//*[@id="section-3"]/div/table/tbody//text()').extract()
        modules = ''.join(modules)
        # modules = modules.replace('\n','')
        print(6,modules)

        teaching = response.xpath('//*[@id="section-4"]/div/div//text()').extract()
        teaching = ''.join(teaching)
        print(7.7,teaching)

        assessment = response.xpath('//*[@id="section-4"]/div/div//text()').extract()
        assessment = ''.join(assessment)
        print(7,assessment)

        career = response.xpath('//*[@id="section-5"]/div/div//text()').extract()
        career = ''.join(career)
        print(8, career)

        application_date = 'NULL'

        deadline = 'NULL'

        application_fee = 'NULL'

        tuition_fee_s= response.xpath('//*[@id="section-6"]//text()').extract()[33:37]
        tuition_fee_s = ''.join(tuition_fee_s)
        tuition_fee_s = tuition_fee_s.replace('\r\n','')
        tuition_fee_s = tuition_fee_s.replace('    ','')
        tuition_fee_s = self.getTuition_fee(tuition_fee_s)
        try:
            if tuition_fee_s > 0:
                tuition_fee = tuition_fee_s
            else:
                tuition_fee = "NULL"
        except:
            tuition_fee = "报错!"

        print(9, tuition_fee)

        location = 'worcester'
        # location = ''.join(location)
        # print(13,location)

        GPA = 'NULL'

        ATAS = 'NULL'

        average_score = 'NULL'

        accredited_university = 'NULL'

        Alevel = 'NULL'

        IB = 'NULL'

        IELTS_s = response.xpath('//*[@id="section-2"]//p/text()').extract()
        IELTS_s = ''.join(IELTS_s)
        # IELTS = re.findall('(IELTS:|IELTS)? (.*){0,5} \d?.\d? .{0,70}',IELTS)
        try:
            if " IELTS" in IELTS_s:
                start = IELTS_s.find(" IELTS")
                IELTS = IELTS_s[start:]
                IELTS = IELTS[:100]
                item["IELTS"] = IELTS
            else:
                IELTS = "NULL"
        except:
            IELTS = "报错!"
        print(10, IELTS)

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

        LSAT= 'NULL'

        MCAT = 'NULL'

        working_experience = 'NULL'

        interview = 'NULL'

        portfolio = 'NULL'

        application_documents = 'NULL'

        how_to_apply = response.xpath('//*[@id="section-7"]//text()').extract()
        how_to_apply = ''.join(how_to_apply)
        print(11,how_to_apply)

        entry_requirements = response.xpath('//*[@id="section-2"]/div//text()').extract()
        entry_requirements = ''.join(entry_requirements)
        print(12,entry_requirements)

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

