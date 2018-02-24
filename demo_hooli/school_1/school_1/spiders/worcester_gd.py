





import scrapy
from school_1.items import HooliItem
import datetime
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import re

class PlymouthSpider(CrawlSpider):
    name = 'worcester_gd'
    allowed_domains = ['www.worcester.ac.uk']
    start_urls = []
    base_url = 'https://www.worcester.ac.uk%s'

    Lists = ['/journey/advancing-practice-msc.html',
'/courses/allied-health-studies-mphil-phd.html',
'/courses/animal-biology-mphil-phd.html',
'/courses/applied-sports-performance-analysis-msc.html',
'/journey/applied-sport-science-msc.html',
'/courses/archaeology-mphil-phd.html',
'/courses/master-research-archaeology.html',
'/courses/art-and-design-mphil-phd.html',
'/courses/atmospheric-sciences-mphil-phd.html',
'/courses/biochemistry-mphil-phd.html',
'/courses/master-research-biology.html',
'/courses/business-mphil-phd.html',
'/journey/business-psychology-msc-occupational-psychology-msc.html',
'/courses/mres-clinical-education.html',
'/courses/computing-mphil-phd.html',
'/journey/counselling-msc.html',
'/courses/creative-media-ma.html',
'/courses/creative-digital-media-mphil-phd.html',
'/courses/criminology-mphil-phd.html',
'/courses/dementia-studies-mphil-phd.html',
'/courses/design-mres.html',
'/discover/doctor-of-education-edD.html',
'/courses/drama-and-performance-mphil-phd.html',
'/journey/drama-performance-ma.html',
'/courses/early-modern-studies-mres.html',
'/courses/mres-ecology-environmental-management.html',
'/courses/ecology-mphil-phd.html',
'/journey/education-ma.html',
'/courses/education-mphil-phd.html',
'/courses/mres-education.html',
'/courses/msc-emdr-therapy.html',
'/courses/english-literature-and-language-mphil-phd.html',
'/courses/environmental-studies-science-mphil-phd.html',
'/courses/film-studies-mphil-phd.html',
'/courses/fine-art-mres.html',
'/courses/green-media-mres.html',
'/journey/higher-education-mapgdippgcert.html',
'/courses/history-mphil-phd.html',
'/courses/history-mres.html',
'/courses/human-biology-mphil-phd.html',
'/courses/huma-geography-mphil-phd.html',
'/journey/human-resource-management-ma.html',
'/courses/management-human-resources-msc.html',
'/journey/management-msc.html',
'/courses/international-sport-management-msc.html',
'/courses/leading-culture-change-in-safeguarding-pgcert.html',
'/journey/leading-early-years-practice-pgcert.html',
'/journey/teaching-and-learning-in-higher-education-pg-cert.html',
'/courses/mathematics-mphil-phd.html',
'/courses/master-of-business-administration-mba.html',
'/courses/mba-executive-leadership-and-management-part-time.html',
'/courses/media-and-cultural-studies-mphil-phd.html',
'/journey/mentoring-in-early-childhood-pgcert.html',
'/courses/midwifery-mphil-phd.html',
'/courses/national-award-senco-nasc-special-educational-needs-coordination-pg-cert.html',
'/courses/nursing-mphil-phd.html',
'/courses/nutrition-and-health-access-module.html',
'/journey/nutritional-therapy-msc.html',
'/journey/business-psychology-msc-occupational-psychology-msc.html',
'/courses/occupational-therapy-mphil-phd.html',
'/courses/outdoor-education-ma.html',
'/journey/postgraduate-certificate-in-education-pgce-primary.html',
'/journey/postgraduate-certificate-in-education-pgce-secondary.html',
'/courses/pgce-school-direct-primary.html',
'/courses/pgce-school-direct-secondary.html',
'/courses/physical-geography-mphil-phd.html',
'/courses/physician-associate-msc.html',
'/courses/plant-biology-mphil-phd.html',
'/courses/positive-psychology-coaching-pgcert.html',
'/courses/psychology-mphil-phd.html',
'/journey/psychology-msc.html',
'/courses/public-health-msc.html',
'/courses/master-research-river-science.html',
'/courses/social-work-social-policy-mphil-phd.html',
'/journey/social-work-ma.html',
'/courses/master-research-socio-cultural-studies-sport-exercise.html',
'/courses/sociology-mphil-phd.html',
'/courses/sport-exercise-science-mphil-phd.html',
'/journey/sports-coaching-msc.html',
'/courses/supervision-pgcert.html',
'/courses/theatre-performance-mres.html',
'/courses/understanding-domestic-and-sexual-violence-ma.html']

    for i in Lists:
        fullurl = base_url % i
        start_urls.append(fullurl)

    rules = (
        Rule(LinkExtractor(allow=(r'.*'), restrict_xpaths=('//div[@class="body-copy"]/ul/li/a')),callback='parse_item', follow=True),
        # Rule(LinkExtractor(allow=r''),follow=True),
        Rule(LinkExtractor(allow=r'/courses|journey|discover/.*'),callback='parse_item', follow=False),
    )

    def parse_item(self,response):
        print('==================================',response.url)
        item = HooliItem()

        url = response.url
        print(1,url)

        university = 'University of Worcester'
        print(2,university)

        department = 'NULL'

        country = 'UK'
        city = "NULL"
        website = 'NULL'
        degree_level = '1'

        # programme = response.xpath('//div[@class="section picture-nav"]/h1/text()').extract()
        programme = response.xpath('//section[@class="pageHead"]//text()').extract()
        programme = ''.join(programme)
        print(3,programme)

        ucas_code = 'NULL'

        # degree_type = response.xpath('//div[@class="section picture-nav"]/h1/text()').extract()
        degree_type = response.xpath('//section[@class="pageHead"]/h1/text()').extract()
        degree_type = ''.join(degree_type)
        degree_type = self.getDegree_type(degree_type)
        print(4,degree_type)

        start_date = 'NULL'
        # start_date = ''.join(start_date)
        # print(5,start_date)

        # overview = response.xpath('//div[@class="left logo-bg"]//text()').extract()
        overview = response.xpath('//div[@class="body-copy"]/p//text()').extract()
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

        modules_s = response.xpath('//div[@class="columns__column"]//text()').extract()
        modules_s = ''.join(modules_s)
        # modules = modules.replace('\n','')
        try:
            if "Modules" in modules_s:
                start = modules_s.find("Modules")
                end = modules_s.find("Assessment")
                modules = modules_s[start:end]
                item["modules"] = modules
            else:
                modules = modules_s
        except:
            modules = modules_s
        print(6,modules)

        teaching = 'NULL'

        assessment_s = response.xpath('//div[@class="columns__column"]//text()').extract()
        assessment_s = ''.join(assessment_s)
        try:
            if "Assessment" in assessment_s:
                start = assessment_s.find("Assessment")
                assessment = assessment_s[start:]
                item["assessment"] = assessment
            else:
                assessment = assessment_s
        except:
            assessment = assessment_s
        print(7, assessment)

        career = response.xpath('//dd[@class="accordion__content rte"]//text()').extract()
        career = ''.join(career)
        print(8, career)

        application_date = 'NULL'

        deadline = 'NULL'

        application_fee = 'NULL'

        tuition_fee_s= response.xpath('//div[@class="columns"]//text()').extract()
        tuition_fee_s = ''.join(tuition_fee_s)
        # tuition_fee = tuition_fee.replace('\n','')
        # tuition_fee = tuition_fee.replace('    ','')
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

        ATAS = 'NULL'

        GPA = 'NULL'

        average_score = 'NULL'

        accredited_university = 'NULL'

        Alevel = 'NULL'

        IB = 'NULL'

        IELTS_s = response.xpath('//div[@class="right equal-height"]//text()').extract()
        IELTS_s = ''.join(IELTS_s)
        # IELTS = re.findall('(IELTS:|IELTS)? (.*){0,5} \d?.\d? .{0,70}',IELTS)
        try:
            if "IELTS" in IELTS_s:
                start = IELTS_s.find("IELTS")
                IELTS = IELTS_s[:100]
                item["IELTS"] = IELTS
            else:
                IELTS = "NULL"
        except:
            IELTS = "报错!"
        print(10, IELTS)

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

        how_to_apply_s = response.xpath('//dd[@class="accordion__content rte"]//text()').extract()
        how_to_apply_s = ''.join(how_to_apply_s)
        try:
            if "How to Apply" in how_to_apply_s:
                start = how_to_apply_s.find("How to Apply")
                end = how_to_apply_s.find("Entry requirements")
                how_to_apply = how_to_apply_s[start:end]
                item["how_to_apply"] = how_to_apply
            else:
                how_to_apply = how_to_apply_s
        except:
            how_to_apply = '报错!'
        print(11,how_to_apply)

        entry_requirements_s = response.xpath('//dd[@class="accordion__content rte"]//text()').extract()
        entry_requirements_s = ''.join(entry_requirements_s)
        # EntryRequirements = EntryRequirements.replace(' ','')
        try:
            if "Entry requirements" in entry_requirements_s:
                start = entry_requirements_s.find("Entry requirements")
                end = entry_requirements_s.find("Study options")
                entry_requirements = entry_requirements_s[start:end]
                item["entry_requirements"] = entry_requirements
            else:
                entry_requirements = entry_requirements_s

        except:
            entry_requirements = '报错!'

        print(12,entry_requirements)

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

