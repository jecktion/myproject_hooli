



import scrapy
from school_1.items import HooliItem
import datetime
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import re

class PlymouthSpider(CrawlSpider):
    name = 'lboro_gd'
    allowed_domains = ['www.lboro.ac.uk']
    start_urls = []
    base_url = 'http://www.lboro.ac.uk/%s'

    Lists = ['/study/postgraduate/masters-degrees/a-z/advanced-chemical-engineering/',
'/study/postgraduate/masters-degrees/a-z/advanced-computer-science/',
'/study/postgraduate/masters-degrees/a-z/advanced-manufacturing-engineering-management/',
'/study/postgraduate/masters-degrees/a-z/advanced-physics/',
'/study/postgraduate/masters-degrees/a-z/advanced-process-engineering/',
'/study/postgraduate/masters-degrees/a-z/aero-auto-engineering-short-courses/',
'/study/postgraduate/masters-degrees/a-z/air-transport-management/',
'/study/postgraduate/masters-degrees/a-z/analytical-pharmaceutical-science/',
'/study/postgraduate/masters-degrees/a-z/analytical-chemistry/',
'/study/postgraduate/masters-degrees/a-z/automotive-systems-engineering/',
'/study/postgraduate/masters-degrees/a-z/banking-finance/',
'/study/postgraduate/masters-degrees/a-z/built-environment-energy-demand-studies/',
'/study/postgraduate/masters-degrees/a-z/business-analytics-consulting/',
'/study/postgraduate/masters-degrees/a-z/business-psychology/',
'/study/postgraduate/masters-degrees/a-z/certificates-automotive-engineering/',
'/study/postgraduate/masters-degrees/a-z/communication-cultural-policy/',
'/study/postgraduate/masters-degrees/a-z/construction-management/',
'/study/postgraduate/masters-degrees/a-z/construction-project-management/',
'/study/postgraduate/masters-degrees/a-z/corporate-finance/',
'/study/postgraduate/masters-degrees/a-z/creative-writing/',
'/study/postgraduate/masters-degrees/a-z/cyber-security-big-data/',
'/study/postgraduate/masters-degrees/a-z/design-culture/',
'/study/postgraduate/masters-degrees/a-z/design-additive-manufacture/',
'/study/postgraduate/masters-degrees/a-z/design-innovation/',
'/study/postgraduate/masters-degrees/a-z/design-innovation-management/',
'/study/postgraduate/masters-degrees/a-z/design-innovation-mres/',
'/study/postgraduate/masters-degrees/a-z/digital-communications-systems/',
'/study/postgraduate/masters-degrees/a-z/digital-creative-media/',
'/study/postgraduate/masters-degrees/a-z/digital-marketing/',
'/study/postgraduate/masters-degrees/a-z/digital-media-society/',
'/study/postgraduate/masters-degrees/a-z/digital-technologies/',
'/study/postgraduate/masters-degrees/a-z/diplomacy-international-governance/',
'/study/postgraduate/masters-degrees/a-z/diplomacy-business-trade/',
'/study/postgraduate/masters-degrees/a-z/diplomacy-statecraft-foreign-policy/',
'/study/postgraduate/masters-degrees/a-z/economics-business-strategy/',
'/study/postgraduate/masters-degrees/a-z/economics-finance/',
'/study/postgraduate/masters-degrees/a-z/economics-international-business/',
'/study/postgraduate/masters-degrees/a-z/electronic-electrical-engineering/',
'/study/postgraduate/masters-degrees/a-z/employment-relations-human-resource-management/',
'/study/postgraduate/masters-degrees/a-z/engineering-design/',
'/study/postgraduate/masters-degrees/a-z/entrepreneurial-design-management/',
'/study/postgraduate/masters-degrees/a-z/entrepreneurship-innovation/',
'/study/postgraduate/masters-degrees/a-z/entrepreneurship-innovation-management/',
'/study/postgraduate/masters-degrees/a-z/entrepreneurship-finance-innovation/',
'/study/postgraduate/masters-degrees/a-z/environmental-monitoring-management/',
'/study/postgraduate/masters-degrees/a-z/ergonomics-human-factors/',
'/study/postgraduate/masters-degrees/a-z/ergonomics-health-community-care/',
'/study/postgraduate/masters-degrees/a-z/european-masters-renewable-energy/',
'/study/postgraduate/masters-degrees/a-z/executive-education/',
'/study/postgraduate/masters-degrees/a-z/exercise-medicine/',
'/study/postgraduate/masters-degrees/a-z/exercise-physiology/',
'/study/postgraduate/masters-degrees/a-z/finance/',
'/study/postgraduate/masters-degrees/a-z/finance-investment/',
'/study/postgraduate/masters-degrees/a-z/finance-management/',
'/study/postgraduate/masters-degrees/a-z/global-communication-development/',
'/study/postgraduate/masters-degrees/a-z/global-media-cultural-industries/',
'/study/postgraduate/masters-degrees/a-z/global-political-communication/',
'/study/postgraduate/masters-degrees/a-z/globalization-cities/',
'/study/postgraduate/masters-degrees/a-z/graphic-design-visualisation/',
'/study/postgraduate/masters-degrees/a-z/human-factors-ergonomics-patient-safety/',
'/study/postgraduate/masters-degrees/a-z/human-factors-inclusive-design/',
'/study/postgraduate/masters-degrees/a-z/human-factors-transport/',
'/study/postgraduate/masters-degrees/a-z/human-resource-management/',
'/study/postgraduate/masters-degrees/a-z/industrial-mathematical-modelling/',
'/study/postgraduate/masters-degrees/a-z/information-management-business-technology/',
'/study/postgraduate/masters-degrees/a-z/infrastructure-emergencies/',
'/study/postgraduate/masters-degrees/a-z/integrated-industrial-design/',
'/study/postgraduate/masters-degrees/a-z/international-business/',
'/study/postgraduate/masters-degrees/a-z/international-financial-political-relations/',
'/study/postgraduate/masters-degrees/a-z/international-management/',
'/study/postgraduate/masters-degrees/a-z/international-water-sanitation-management/',
'/study/postgraduate/masters-degrees/a-z/international-water-sanitation-engineering/',
'/study/postgraduate/masters-degrees/a-z/internet-computing-network-security/',
'/study/postgraduate/masters-degrees/a-z/internet-technologies-business-management/',
'/study/postgraduate/masters-degrees/a-z/low-energy-building-services-engineering/',
'/study/postgraduate/masters-degrees/a-z/management/',
'/study/postgraduate/masters-degrees/a-z/managing-innovation-creative-organisations/',
'/study/postgraduate/masters-degrees/a-z/marketing/',
'/study/postgraduate/masters-degrees/a-z/materials-science-technology/',
'/study/postgraduate/masters-degrees/a-z/mathematical-finance/',
'/study/postgraduate/masters-degrees/a-z/mathematics-qualified-teacher-status/',
'/study/postgraduate/masters-degrees/a-z/mechanical-engineering/',
'/study/postgraduate/masters-degrees/a-z/meme-short-course/',
'/study/postgraduate/masters-degrees/a-z/media-creative-industries/',
'/study/postgraduate/masters-degrees/a-z/media-creative-industries-mres/',
'/study/postgraduate/masters-degrees/a-z/media-cultural-analysis/',
'/study/postgraduate/masters-degrees/a-z/mobile-communications/',
'/study/postgraduate/masters-degrees/a-z/musculoskeletal-sport-science-health/',
'/study/postgraduate/masters-degrees/a-z/pharmaceutical-science-medicinal-chemistry/',
'/study/postgraduate/masters-degrees/a-z/physical-education-qualified-teacher-status/',
'/study/postgraduate/masters-degrees/a-z/physics-materials/',
'/study/postgraduate/masters-degrees/a-z/polymer-science-technology/',
'/study/postgraduate/masters-degrees/a-z/renewable-energy-systems-technology-distance/',
'/study/postgraduate/masters-degrees/a-z/renewable-energy-systems-technology-full-time/',
'/study/postgraduate/masters-degrees/a-z/security-peace-building-diplomacy/',
'/study/postgraduate/masters-degrees/a-z/social-science-research-business-management/',
'/study/postgraduate/masters-degrees/a-z/social-science-research-communication-media/',
'/study/postgraduate/masters-degrees/a-z/social-science-research-social-policy/',
'/study/postgraduate/masters-degrees/a-z/social-science-research-sport-exercise-science/',
'/study/postgraduate/masters-degrees/a-z/sport-exercise-nutrition/',
'/study/postgraduate/masters-degrees/a-z/sport-exercise-psychology/',
'/study/postgraduate/masters-degrees/a-z/sport-biomechanics/',
'/study/postgraduate/masters-degrees/a-z/sport-business/',
'/study/postgraduate/masters-degrees/a-z/sport-business-innovation/',
'/study/postgraduate/masters-degrees/a-z/sport-business-leadership/',
'/study/postgraduate/masters-degrees/a-z/sport-digital-media-technologies/',
'/study/postgraduate/masters-degrees/a-z/sport-management/',
'/study/postgraduate/masters-degrees/a-z/sport-marketing/',
'/study/postgraduate/masters-degrees/a-z/systems-engineering/',
'/study/postgraduate/masters-degrees/a-z/telecommunications-engineering/',
'/study/postgraduate/masters-degrees/a-z/loughborough-mba/',
'/study/postgraduate/masters-degrees/a-z/user-experience-design/',
'/study/postgraduate/masters-degrees/a-z/water-and-environmental-management-distance-learni/',
'/study/postgraduate/masters-degrees/a-z/water-waste-engineering-distance/',
'/study/postgraduate/masters-degrees/a-z/work-psychology/']

    for i in Lists:
        fullurl = base_url % i
        start_urls.append(fullurl)

    rules = (
        Rule(LinkExtractor(allow=(r'.*'), restrict_xpaths=('//div[@class="programmes"]/ul/li/h2/@href')), follow=True),
        # Rule(LinkExtractor(allow=r''),follow=True),
        Rule(LinkExtractor(allow=r'/study/postgraduate/masters-degrees/a-z/.*'),callback='parse_item', follow=False),
    )

    def parse_item(self,response):
        print('==================================',response.url)
        item = HooliItem()

        url = response.url
        print(1,url)

        university = 'Loughborough University'
        print(2,university)

        department = 'NULL'
        country = 'UK'
        city = 'NULL'
        website = 'http://www.lboro.ac.uk'
        degree_level = '1'

        programme = response.xpath('//div[@class="programme-column programme-details"]/h1[@id="top"]//text()').extract()
        programme = ''.join(programme)
        print(3,programme)

        degree_type = response.xpath('//div[@class="programme-column programme-details"]/h1[@id="top"]/span/text()').extract()
        degree_type = ''.join(degree_type)
        print(4,degree_type)

        ucas_code = 'NULL'

        start_date = response.xpath('//div[@class="list__content icon icon--calendar"]/dd/text()').extract()
        start_date = ''.join(start_date)
        print(5,start_date)

        overview = response.xpath('//div[@class="content-type content-type--main"]/div[@class="content-type__container"]/div[@class="editor"]//text()').extract()
        overview = ''.join(overview)
        print(6, overview)

        mode = response.xpath('//div[@class="list__content icon icon--clock"]//text()').extract()
        mode = ''.join(mode).replace('\r\n','')
        mode = mode.replace('   ','')
        print(7, mode)



        duration = response.xpath('//div[@class="list__content icon icon--clock"]//text()').extract()
        duration = ''.join(duration).replace('\r\n','')
        duration = duration.replace('   ','')
        print(8,duration)

        modules_lists = response.xpath('//div[@class="container"]//text()').extract()
        modules_str = ''.join(modules_lists).replace('\r\n','')
        # modules = modules.replace('\n','')
        if "Modules" in modules_str:
            mstart = modules_str.find("Modules")
            mend = modules_str.find("How you'll be assessed")
            modules = modules_str[mstart:mend]
            # modules = ''.join(modules).replace('\r\n', '')
            # modules = modules.replace('\n', '')
            item["modules"] = modules
        else:
            modules = 'NULL'
        print(9,modules)

        teaching = 'NULL'

        assessment = response.xpath('//div[@class="content-type__container"]/div[@class="editor"]/p/span/text()').extract()
        assessment = ''.join(assessment)
        print(10, assessment)

        career_lists = response.xpath('//div[@class="container"]//text()').extract()
        career_str = ''.join(career_lists).replace('\r\n', '')
        if "Your personal and professional development" in career_str:
            cstart = career_str.find("Your personal and professional development")
            cend = career_str.find("Fees and funding")
            career = career_str[cstart:cend]
            # career = ''.join(career).replace('\r\n', '')
            item["career"] = career
        else:
            career = 'NULL'
        print(11,career)

        application_date = 'NULL'

        deadline = 'NULL'

        application_fee = 'NULL'

        tuition_fee = response.xpath('//div[@class="list__content icon icon--money"]//text()').extract()
        tuition_fee = ''.join(tuition_fee).replace('\r\n','')
        tuition_fee = tuition_fee.replace('   ','')
        print(12, tuition_fee)

        location = response.xpath('//dd[@class="list__item list__item--definition"]/a/text()').extract()
        location = ''.join(location)
        print(13,location)

        ATAS = 'NULL'

        GPA = 'NULL'

        average_score = 'NULL'

        accredited_university = 'NULL'

        Alevel = 'NULL'

        IB = 'NULL'

        IELTS = 'NULL'
        # IELTS = ''.join(IELTS).replace('\r\n','')
        # # IELTS = re.findall('(IELTS:|IELTS)? (.*){0,5} \d?.\d? .{0,70}',IELTS)
        # print(14, IELTS)

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

        entry_requirements_lists = response.xpath('//div[@class="container"]//text()').extract()
        entry_requirements_str = ''.join(entry_requirements_lists).replace('\r\n','')
        # EntryRequirements = EntryRequirements.replace(' ','')
        if "Entry requirements" in entry_requirements_str:
            erstart = entry_requirements_str.find("Who should study this programme?")
            erend = entry_requirements_str.find("English Language requirements")
            entry_requirements = entry_requirements_str[erstart:erend]

            item["entry_requirements"] = entry_requirements
        #     print('===========================')
        else:
            entry_requirements = 'NULL'
        print(15, entry_requirements,'==================================')

        chinese_requirements = 'NULL'

        school_test = 'NULL'

        degree_description = 'NULL'

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

