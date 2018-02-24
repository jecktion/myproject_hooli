


import scrapy
from school_1.items import HooliItem
import datetime
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import re

class PlymouthSpider(CrawlSpider):
    name = 'bath_gd'
    allowed_domains = ['www.bath.ac.uk']
    start_urls = []
    base_url = 'http://www.bath.ac.uk/%s'

    Lists = ['/courses/postgraduate-2018/taught-postgraduate-courses/msc-accounting-and-finance',
'/courses/postgraduate-2018/taught-postgraduate-courses/mres-advanced-quantitive-methods-in-social-science-part-time',
'/courses/postgraduate-2018/taught-postgraduate-courses/mres-advanced-quantitive-methods-in-social-science',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-applied-clinical-psychology-part-time',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-applied-clinical-psychology',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-applied-economics',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-applied-economics-with-banking-and-financial-markets',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-applied-economics-with-behavioural-science',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-applied-economics-with-environmental-policy',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-applied-economics-with-public-policy',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-applied-psychology-and-economic-behaviour',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-architectural-engineering-environmental-design',
'/courses/postgraduate-2018/taught-postgraduate-courses/march-architecture',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-automotive-engineering',
'/courses/postgraduate-2018/taught-postgraduate-courses/mres-biosciences',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-biosciences',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-business-analytics',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-civil-engineering-innovative-structural-materials',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-computer-science',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-conservation-of-historic-buildings-part-time-4-years',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-conservation-of-historic-buildings-part-time-2-years',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-conservation-of-historic-buildings',
'/courses/postgraduate-2018/taught-postgraduate-courses/ma-contemporary-european-studies-euromasters',
'/courses/postgraduate-2018/taught-postgraduate-courses/ma-contemporary-european-studies-euromasters-with-transatlantic-track',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-data-science',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-data-science-including-placement-year',
'/courses/postgraduate-2018/taught-postgraduate-courses/mres-developmental-biology',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-developmental-biology',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-digital-entertainment-including-placement-year',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-digital-entertainment',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-drug-discovery',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-economics-and-finance',
'/courses/postgraduate-2018/taught-postgraduate-courses/mres-economics-part-time',
'/courses/postgraduate-2018/taught-postgraduate-courses/mres-economics',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-economics',
'/courses/postgraduate-2018/taught-postgraduate-courses/ma-education',
'/courses/postgraduate-2018/taught-postgraduate-courses/ma-education-educational-leadership-and-management',
'/courses/postgraduate-2018/taught-postgraduate-courses/ma-education-international-education',
'/courses/postgraduate-2018/taught-postgraduate-courses/ma-education-learning-and-teaching',
'/courses/postgraduate-2018/taught-postgraduate-courses/mres-education-part-time',
'/courses/postgraduate-2018/taught-postgraduate-courses/mres-education',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-electrical-power-systems',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-electronic-systems-design',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-engineering-business-management',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-engineering-design',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-entrepreneurship-and-management',
'/courses/postgraduate-2018/taught-postgraduate-courses/mres-european-social-policy-part-time',
'/courses/postgraduate-2018/taught-postgraduate-courses/mres-european-social-policy',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-evolutionary-and-population-biology',
'/courses/postgraduate-2018/taught-postgraduate-courses/mres-evolutionary-biology',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-finance',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-finance-with-banking',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-finance-with-risk-management',
'/courses/postgraduate-2018/taught-postgraduate-courses/mres-global-political-economy-part-time',
'/courses/postgraduate-2018/taught-postgraduate-courses/mres-global-political-economy',
'/courses/postgraduate-2018/taught-postgraduate-courses/mres-health-and-wellbeing-part-time',
'/courses/postgraduate-2018/taught-postgraduate-courses/mres-health-and-wellbeing',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-health-psychology-part-time',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-health-psychology',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-human-computer-interaction-including-placement-year',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-human-computer-interaction',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-human-resource-management-and-consulting',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-humanitarianism-conflict-and-development-part-time',
'/courses/postgraduate-2018/taught-postgraduate-courses/innovation-and-technology-management',
'/courses/postgraduate-2018/taught-postgraduate-courses/mres-international-development-part-time',
'/courses/postgraduate-2018/taught-postgraduate-courses/mres-international-development',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-international-development-part-time',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-international-development',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-international-development-with-conflict-and-humanitarian-action-part-time',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-international-development-with-conflict-and-humanitarian-action',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-international-development-with-economics-part-time',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-international-development-with-economics',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-international-development-social-justice-and-sustainability-part-time',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-international-development-social-justice-and-sustainability',
'/courses/postgraduate-2018/taught-postgraduate-courses/ma-international-education-and-globalisation',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-international-management',
'/courses/postgraduate-2018/taught-postgraduate-courses/ma-international-relations-part-time',
'/courses/postgraduate-2018/taught-postgraduate-courses/ma-international-relations',
'/courses/postgraduate-2018/taught-postgraduate-courses/ma-international-relations-and-european-politics-part-time',
'/courses/postgraduate-2018/taught-postgraduate-courses/ma-international-relations-and-european-politics',
'/courses/postgraduate-2018/taught-postgraduate-courses/ma-international-security-part-time',
'/courses/postgraduate-2018/taught-postgraduate-courses/ma-international-security',
'/courses/postgraduate-2018/taught-postgraduate-courses/ma-interpreting-and-translating-french-and-german',
'/courses/postgraduate-2018/taught-postgraduate-courses/ma-interpreting-and-translating-french-and-italian',
'/courses/postgraduate-2018/taught-postgraduate-courses/ma-interpreting-and-translating-french-and-russian',
'/courses/postgraduate-2018/taught-postgraduate-courses/ma-interpreting-and-translating-french-and-spanish',
'/courses/postgraduate-2018/taught-postgraduate-courses/ma-interpreting-and-translating-german-and-spanish',
'/courses/postgraduate-2018/taught-postgraduate-courses/ma-interpreting-and-translating-italian-and-german',
'/courses/postgraduate-2018/taught-postgraduate-courses/ma-interpreting-and-translating-italian-and-spanish',
'/courses/postgraduate-2018/taught-postgraduate-courses/ma-interpreting-and-translating-russian-and-german',
'/courses/postgraduate-2018/taught-postgraduate-courses/ma-interpreting-and-translating-russian-and-italian',
'/courses/postgraduate-2018/taught-postgraduate-courses/ma-interpreting-and-translating-russian-and-spanish',
'/courses/postgraduate-2018/taught-postgraduate-courses/ma-interpreting-and-translating-chinese',
'/courses/postgraduate-2018/taught-postgraduate-courses/ma-interpreting-and-translating-russian',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-machine-learning-and-autonomous-systems-including-placement-year',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-machine-learning-and-autonomous-systems',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-management',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-marketing',
'/courses/postgraduate-2018/taught-postgraduate-courses/mba-full-time',
'/courses/postgraduate-2018/taught-postgraduate-courses/mba-part-time-executive',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-mechatronics',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-medical-biosciences',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-modern-applications-of-mathematics',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-modern-applications-of-mathematics-plus-6-month-placement-project',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-modern-building-design',
'/courses/postgraduate-2018/taught-postgraduate-courses/mres-molecular-microbiology',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-molecular-microbiology',
'/courses/postgraduate-2018/taught-postgraduate-courses/mres-molecular-plant-sciences',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-molecular-plant-sciences',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-operations-logistics-and-supply-chain-management',
'/courses/postgraduate-2018/taught-postgraduate-courses/mres-politics-and-international-studies-part-time',
'/courses/postgraduate-2018/taught-postgraduate-courses/mres-politics-and-international-studies-full-time',
'/courses/postgraduate-2018/taught-postgraduate-courses/pg-cert-professional-practice',
'/courses/postgraduate-2018/taught-postgraduate-courses/mres-protein-structure-and-function',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-protein-structure-and-function',
'/courses/postgraduate-2018/taught-postgraduate-courses/mres-psychology-part-time',
'/courses/postgraduate-2018/taught-postgraduate-courses/mres-psychology-full-time',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-public-policy-part-time',
'/courses/postgraduate-2018/taught-postgraduate-courses/mres-regenerative-medicine',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-research-in-health-practice',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-robotics-and-autonomous-systems-including-three-month-placement',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-robotics-and-autonomous-systems',
'/courses/postgraduate-2018/taught-postgraduate-courses/mres-security-conflict-and-human-rights-part-time',
'/courses/postgraduate-2018/taught-postgraduate-courses/mres-security-conflict-and-human-rights',
'/courses/postgraduate-2018/taught-postgraduate-courses/mres-social-policy-part-time',
'/courses/postgraduate-2018/taught-postgraduate-courses/mres-social-policy',
'/courses/postgraduate-2018/taught-postgraduate-courses/mres-social-work-part-time',
'/courses/postgraduate-2018/taught-postgraduate-courses/mres-social-work',
'/courses/postgraduate-2018/taught-postgraduate-courses/mres-sociology-part-time',
'/courses/postgraduate-2018/taught-postgraduate-courses/mres-sociology',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-software-systems-including-placement-year',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-software-systems',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-sport-and-exercise-medicine',
'/courses/postgraduate-2018/taught-postgraduate-courses/pg-dip-sport-and-exercise-medicine',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-sports-physiotherapy',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-sustainability-and-management',
'/courses/postgraduate-2018/taught-postgraduate-courses/msc-sustainable-chemical-engineering',
'/courses/postgraduate-2018/taught-postgraduate-courses/mres-sustainable-futures-part-time',
'/courses/postgraduate-2018/taught-postgraduate-courses/mres-sustainable-futures-full-time',
'/courses/postgraduate-2018/taught-postgraduate-courses/ma-teaching-english-to-speakers-of-other-languages',
'/courses/postgraduate-2018/taught-postgraduate-courses/ma-translation-and-professional-language-skills-french',
'/courses/postgraduate-2018/taught-postgraduate-courses/ma-translation-and-professional-language-skills-french-and-german',
'/courses/postgraduate-2018/taught-postgraduate-courses/ma-translation-and-professional-language-skills-french-and-italian',
'/courses/postgraduate-2018/taught-postgraduate-courses/ma-translation-and-professional-language-skills-french-and-russian',
'/courses/postgraduate-2018/taught-postgraduate-courses/ma-translation-and-professional-language-skills-french-and-spanish',
'/courses/postgraduate-2018/taught-postgraduate-courses/ma-translation-and-professional-language-skills-german',
'/courses/postgraduate-2018/taught-postgraduate-courses/ma-translation-and-professional-language-skills-german-and-spanish',
'/courses/postgraduate-2018/taught-postgraduate-courses/ma-translation-and-professional-language-skills-italian',
'/courses/postgraduate-2018/taught-postgraduate-courses/ma-translation-and-professional-language-skills-italian-and-german',
'/courses/postgraduate-2018/taught-postgraduate-courses/ma-translation-and-professional-language-skills-italian-and-spanish',
'/courses/postgraduate-2018/taught-postgraduate-courses/ma-translation-and-professional-language-skills-russian',
'/courses/postgraduate-2018/taught-postgraduate-courses/ma-translation-and-professional-language-skills-russian-and-german',
'/courses/postgraduate-2018/taught-postgraduate-courses/ma-translation-and-professional-language-skills-russian-and-italian',
'/courses/postgraduate-2018/taught-postgraduate-courses/ma-translation-and-professional-language-skills-russian-and-spanish',
'/courses/postgraduate-2018/taught-postgraduate-courses/ma-translation-and-professional-language-skills-spanish',
'/courses/postgraduate-2018/taught-postgraduate-courses/ma-translation-with-business-interpreting-chinese',]

    for i in Lists:
        fullurl = base_url % i
        start_urls.append(fullurl)

    rules = (
        Rule(LinkExtractor(allow=(r'.*'), restrict_xpaths=('//ul[@class="action-list black"]/li/a/@href')),follow=True),
        # Rule(LinkExtractor(allow=r'www.gold.ac.uk/course-finder/results/\?collection=goldsmiths-courses&sort=Title&f.Level%7Clevel=Postgraduate&start_rank=\d+'), follow=True),
        # Rule(LinkExtractor(allow=(r'.*'), restrict_xpaths=('//div[@class="teaser__body media__body"]/h3/a')),follow=True),
        Rule(LinkExtractor(allow=r'/courses/postgraduate-2018/taught-postgraduate-courses/.*'),callback='parse_item', follow=False),
    )

    def parse_item(self,response):
        print('==================================',response.url)
        item = HooliItem()

        url = response.url
        print(1,url)

        university = 'BATH UNIVERSITY'
        print(2,university)

        department = 'NULL'
        # department = ''.join(department)
        # print(3,department)

        country = 'UK'

        city= 'NULL'
        website = 'http://www.bath.ac.uk'

        programme = response.xpath('//h1[@class="page-heading text-center reverse"]/text()').extract()
        programme = ''.join(programme)
        print(3,programme)

        ucas_code = response.xpath('//div[@class="sidebar"]/dl/dd/text()').extract()
        ucas_code = ''.join(ucas_code).replace('\n', '')
        print(4,ucas_code)

        degree_level = "1"

        degree_type = response.xpath('//h1[@class="page-heading text-center reverse"]/span/text()').extract()
        degree_type = ''.join(degree_type).replace('\n', '')
        print(5,degree_type)

        start_date = response.xpath('//h2[@class="page-subheading text-center reverse"]/text()').extract()
        start_date = ''.join(start_date)
        print(6,start_date)

        degree_description = 'NULL'

        overview = response.xpath('//div[@class="column medium-15 end"]/p/text()').extract()
        overview = ''.join(overview).replace('\n', '')
        print(7, overview)

        mode = response.xpath('//h2[@class="page-subheading text-center reverse"]/text()').extract()
        mode = ''.join(mode).replace('\n', '')
        print(8,mode)

        duration = response.xpath('//h2[@class="page-subheading text-center reverse"]/text()').extract()
        duration = ''.join(duration).replace('\n','')
        # duration = duration.replace('   ','')
        print(9,duration)

        modules = response.xpath('//div[@class="row medium-up-2"]//text()').extract()
        modules = ''.join(modules).replace('\n','')
        # modules = modules.replace('\n','')
        print(10,modules)

        teaching = 'NULL'

        assessment = response.xpath('//div[@class="column medium-12"]//text()').extract()
        assessment = ''.join(assessment).replace('\n','')
        print(11,assessment)

        career = response.xpath('//div[@class="column medium-15 end"]/p/text()').extract()
        career = ''.join(career).replace('\n', '')
        print(12, career)

        application_date = 'NULL'

        deadline = response.xpath('//div[@class="aside style-dark-red key-information"]/ul/li/p/text()').extract()
        deadline = ''.join(deadline)
        print(13,deadline)

        application_fee = 'NULL'

        tuition_fee = response.xpath('//div[@class="aside style-dark-red key-information"]/ul/li[3]/p[2]/text()').extract()
        tuition_fee = ''.join(tuition_fee).replace('\r\n','')
        # tuition_fee = tuition_fee.replace('   ','')
        tuition_fee = self.getTuition_fee(tuition_fee)
        try:
            if tuition_fee > 0:
                tuition_fee = tuition_fee
            else:
                tuition_fee = 'NULL'
        except:
            tuition_fee = 'NULL'
        print(14, tuition_fee)

        location = response.xpath('//div[@class="sidebar"]/dl/dd/a/text()').extract()
        location = ''.join(location)
        print(15,location)


        GPA = 'NULL'
        ATAS = 'NULL'

        average_score = 'NULL'
        # average_score = ''.join(average_score)
        # print(16,average_score)


        accredited_university = 'NULL'

        Alevel = 'NULL'

        IB = 'NULL'

        IELTS_str = response.xpath('//div[@class="sidebar seperator reverse"]//text()').extract()
        IELTS_str = ''.join(IELTS_str)
        # IELTS = re.findall('(IELTS:|IELTS)? (.*){0,5} \d?.\d? .{0,70}',IELTS)
        if "English language requirements" in IELTS_str:
            Istart = IELTS_str.find("IELTS:")
            Iend = IELTS_str.find("The Pearson Test of English Academic (PTE Academic):")
            IELTS = IELTS_str[Istart:Iend]
            item["IELTS"] = IELTS
        else:
            IELTS = 'NULL'
        print(17,IELTS)

        IELTS_L = 'NULL'
        IELTS_S = 'NULL'
        IELTS_R = 'NULL'
        IELTS_W = 'NULL'

        TOEFL_str = response.xpath('//div[@class="sidebar seperator reverse"]//text()').extract()
        TOEFL_str = ''.join(TOEFL_str)
        if "English language requirements" in TOEFL_str:
            Istart = TOEFL_str.find("TOEFL IBT:")
            # Iend = IELTS_str.find("The Pearson Test of English Academic (PTE Academic):")
            TOEFL = TOEFL_str[Istart:]
            TOEFL = TOEFL[:100]
            item["TOEFL"] = TOEFL
        else:
            TOEFL = 'NULL'
        print(18,TOEFL)

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

        entry_requirements = response.xpath('//div[@class="column medium-15 end"]/p//text()').extract()
        entry_requirements = ''.join(entry_requirements)
        print(19,entry_requirements)

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

        # yield item

    def getTuition_fee(self, tuition_fee):
        allfee = re.findall(r'\d+,\d+', tuition_fee)
        # print(allfee)
        for index in range(len(allfee)):
            print(index)
            fee = allfee[index].split(",")
            allfee[index] = ''.join(fee)
            print(allfee[index])
        # print(allfee)
        maxfee = 0
        for fee in allfee:
            if int(fee) >= maxfee:
                maxfee = int(fee)
        return maxfee


