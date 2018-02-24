




import scrapy
from school_1.items import HooliItem
import datetime
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import re

class PlymouthSpider(CrawlSpider):
    name = 'chester_gd'
    allowed_domains = ['www1.chester.ac.uk']
    start_urls = []
    base_url = 'https://www1.chester.ac.uk%s'

    Lists = ['/study/postgraduate/advanced-computer-science/201810',
    '/study/postgraduate/advanced-practice-clinical-practice-pathway/201809',
    '/study/postgraduate/advanced-practice-mental-health-pathway/201809',
    '/study/postgraduate/applied-mental-health-practice/201901',
    '/study/postgraduate/applied-science/201810',
    '/study/postgraduate/applied-wildlife-forensics/201810',
    '/study/postgraduate/archaeology/201810',
    '/study/postgraduate/archaeology-and-heritage-practice/201910',
    '/study/postgraduate/archaeology-death-and-memory/201810',
    '/study/postgraduate/art-therapy/201809',
    '/study/postgraduate/arts-and-media/201802',
    '/study/postgraduate/autism/201809',
    '/study/postgraduate/biological-sciences-cell-and-molecular-biology-pathway/201810',
    '/study/postgraduate/biological-sciences-stem-cell-and-regenerative-biology-pathway/201810',
    '/study/postgraduate/biological-sciences-wildlife-behaviour-and-conservation-pathway/201810',
    '/study/postgraduate/biomedical-science/201810',
    '/study/postgraduate/broadcast-media/201802',
    '/study/postgraduate/cancer-care/201805',
    '/study/postgraduate/cardiovascular-disease/201810',
    '/study/postgraduate/cardiovascular-health-and-rehabilitation/201809',
    '/study/postgraduate/cbt-clinical-supervision-high-intensity/201810',
    '/study/postgraduate/clinical-bariatric-practice/201810',
    '/study/postgraduate/clinical-counselling/201809',
    '/study/postgraduate/clinical-sciences-and-nutrition-mres/201810',
    '/study/postgraduate/clinical-supervision-low-intensity/201810',
    '/study/postgraduate/coaching-and-mentoring/201809',
    '/study/postgraduate/cognitive-behavioural-therapies-high-intensity-training/201810',
    '/study/postgraduate/creative-industries-management/201810',
    '/study/postgraduate/creative-practices-education/201809',
    '/study/postgraduate/creative-writing-writing-and-publishing-fiction/201810',
    '/study/postgraduate/critical-care/201809',
    '/node/5211',
    '/study/postgraduate/cybersecurity-conversion/201810',
    '/study/postgraduate/dance/201810',
    '/study/postgraduate/diabetes/201810',
    '/study/postgraduate/digital-marketing/201810',
    '/study/postgraduate/doctor-business-administration/201810',
    '/study/postgraduate/doctor-education/201810',
    '/study/postgraduate/doctor-medicine/201810',
    '/study/postgraduate/doctor-professional-studies-counselling-and-psychotherapy-studies-psychological-0',
    '/study/postgraduate/doctor-professional-studies-dprof-negotiated-studies/201810',
    '/study/postgraduate/doctor-professional-studies-dprof-health-and-social-care/201810',
    '/study/postgraduate/doctor-professional-studies-dprof-practical-theology/201810',
    '/study/postgraduate/doctor-public-health/201810',
    '/study/postgraduate/drama/201810',
    '/study/postgraduate/dyslexia-research-and-practice/201809',
    '/study/postgraduate/early-childhood/201805',
    '/study/postgraduate/early-years-practice/201809',
    '/study/postgraduate/education-society/201805',
    '/study/postgraduate/educational-leadership/201809',
    '/study/postgraduate/endodontology/201810',
    '/study/postgraduate/engineering-management/201810',
    '/study/postgraduate/english/201809',
    '/study/postgraduate/english-language-and-linguistics/201810',
    '/study/postgraduate/exercise-and-nutrition-science/201809',
    '/study/postgraduate/exercise-and-nutrition-science-dublin/201809',
    '/study/postgraduate/exercise-medicine/201810',
    '/study/postgraduate/family-and-child-psychology/201810',
    '/study/postgraduate/fine-art/201810',
    '/study/postgraduate/food-integrity-and-innovation/201810',
    '/study/postgraduate/food-science-and-innovation/201810',
    '/study/postgraduate/food-science-and-innovation-mres/201810',
    '/study/postgraduate/gastroenterology/201810',
    '/study/postgraduate/gender-studies/201810',
    '/study/postgraduate/haematology/201810',
    '/study/postgraduate/health-services-management/201810',
    '/study/postgraduate/history/201809',
    '/study/postgraduate/history-mres/201810',
    '/study/postgraduate/human-nutrition/201809',
    '/study/postgraduate/infection-and-immunity/201809',
    '/study/postgraduate/integrated-approaches-urgent-care-across-community-settings/201809',
    '/study/postgraduate/international-business/201802',
    '/study/postgraduate/international-finance/201802',
    '/study/postgraduate/language-cultures-and-translation/201810',
    '/study/postgraduate/llm-contemporary-legal-studies/201810',
    '/study/postgraduate/management/201810',
    '/study/postgraduate/marketing-management/201802',
    '/study/postgraduate/master-nursing/201810',
    '/study/postgraduate/master-public-health/201809',
    '/study/postgraduate/maternal-and-womens-reproductive-health/201810',
    '/study/postgraduate/mathematics/201810',
    '/study/postgraduate/mathematics-enhancement-course/201810',
    '/study/postgraduate/mba-master-business-administration-full-time/201802',
    '/study/postgraduate/mba-master-business-administration-part-time/201810-0',
    '/study/postgraduate/mba-master-business-administration-part-time/201810',
    '/study/postgraduate/mba-master-business-administration-part-time-shrewsbury/201810',
    '/study/postgraduate/mba-medical-leadership-and-management/201810',
    '/study/postgraduate/medical-genetics/201810',
    '/study/postgraduate/medical-science-mres/201810',
    '/study/postgraduate/medicolegal-practice/201810',
    '/study/postgraduate/military-history/201809',
    '/study/postgraduate/modern-and-contemporary-fiction/201910',
    '/study/postgraduate/modern-language-french-enhancement-course/201810',
    '/study/postgraduate/modern-languages-mres/201810',
    '/study/postgraduate/museums-practice/201810',
    '/study/postgraduate/national-award-special-educational-needs-coordination-nasenco/201809',
    '/study/postgraduate/nineteenth-century-literature-and-culture/201810',
    '/study/postgraduate/non-medical-prescribing/201803',
    '/study/postgraduate/nutrition-and-dietetics/201809',
    '/study/postgraduate/obesity-and-weight-management/201809',
    '/study/postgraduate/oncology/201810',
    '/study/postgraduate/orthopaedics/201810',
    '/study/postgraduate/past-landscapes-and-environments/201810',
    '/study/postgraduate/physician-associate/201901',
    '/study/postgraduate/popular-music/201810',
    '/study/postgraduate/postgraduate-certificate-professional-education/201809',
    '/study/postgraduate/primary-including-school-direct-qts/201809',
    '/study/postgraduate/primaryearly-years-including-school-direct-qts/201809',
    '/study/postgraduate/professional-education/201802',
    '/study/postgraduate/professional-studies/201809',
    '/study/postgraduate/programme-and-project-management/201802',
    '/study/postgraduate/psychological-trauma/201810',
    '/study/postgraduate/psychology-conversion/201810',
    '/study/postgraduate/psychology-mres/201810',
    '/study/postgraduate/public-health-nutrition/201809',
    '/study/postgraduate/qualified-teacher-status-qts-assessment-only/201809',
    '/study/postgraduate/radio-production/201810',
    '/study/postgraduate/regeneration-practitioners/201810',
    '/study/postgraduate/religious-studies/201810',
    '/study/postgraduate/respiratory-medicine/201810',
    '/study/postgraduate/rural-health/201810',
    '/study/postgraduate/secondary-including-school-direct-qts/201809',
    '/study/postgraduate/secondary-including-school-direct-qts/201809-0',
    '/study/postgraduate/secondary-art-and-design-including-school-direct-qts/201809',
    '/study/postgraduate/secondary-biology-including-school-direct-qts/201809',
    '/study/postgraduate/secondary-business-studies-including-school-direct-qts/201809',
    '/study/postgraduate/secondary-chemistry-including-school-direct-qts/201809',
    '/study/postgraduate/secondary-computer-science-including-school-direct-qts/201809',
    '/study/postgraduate/secondary-design-and-technology-including-school-direct-qts/201809',
    '/study/postgraduate/secondary-drama-including-school-direct-qts/201809',
    '/study/postgraduate/secondary-english-including-school-direct-qts/201809',
    '/study/postgraduate/secondary-geography-including-school-direct-qts/201809',
    '/study/postgraduate/secondary-history-including-school-direct-qts/201809',
    '/study/postgraduate/secondary-mathematics-including-school-direct-qts/201809',
    '/study/postgraduate/secondary-modern-languages-including-school-direct-qts/201809',
    '/study/postgraduate/secondary-music-including-school-direct-qts/201809',
    '/study/postgraduate/secondary-physical-education-including-school-direct-qts/201809',
    '/study/postgraduate/secondary-physics-including-school-direct-qts/201809',
    '/study/postgraduate/secondary-religious-education-including-school-direct-qts/201809',
    '/study/postgraduate/social-work/201801',
    '/study/postgraduate/sociology-sport-and-exercise/201810',
    '/study/postgraduate/special-educational-needs-and-disability/201809',
    '/study/postgraduate/specialist-community-public-health-nursing-scphn/201809',
    '/study/postgraduate/specialist-practice-community/201809',
    '/study/postgraduate/sport-and-exercise-sciences-mres/201810',
    '/study/postgraduate/sport-management/201810',
    '/study/postgraduate/sports-coaching-and-development/201810',
    '/study/postgraduate/sports-sciences/201809',
    '/study/postgraduate/sports-sciences-performance-analysis-sport/201809',
    '/study/postgraduate/sports-sciences-physiology/201809',
    '/study/postgraduate/sports-sciences-sports-biomechanics/201809',
    '/study/postgraduate/sports-sciences-strength-and-conditioning/201809',
    '/study/postgraduate/stem-cells-and-regenerative-medicine/201810',
    '/study/postgraduate/storytelling/201810',
    '/study/postgraduate/sustainable-heritage-practice/201810',
    '/study/postgraduate/television-production/201802',
    '/study/postgraduate/theology/201810',
    '/study/postgraduate/therapeutic-practice-psychological-trauma/201810',
    '/study/postgraduate/war-conflict-and-society/201810',
    '/study/postgraduate/wildlife-conservation/201810',
    '/study/postgraduate/womens-health/201810',
    '/study/postgraduate/work-based-and-integrative-studies-wbis/201809',
    '/study/postgraduate/work-based-learning-facilitation-wbis/201809']

    for i in Lists:
        fullurl = base_url % i
        start_urls.append(fullurl)

    rules = (
        Rule(LinkExtractor(allow=(r'.*'), restrict_xpaths=('//td[@class="m-table__cell m-table__cell--title"]/a')), follow=True),
        # Rule(LinkExtractor(allow=r''),follow=True),
        Rule(LinkExtractor(allow=r'study/postgraduate/.*'),callback='parse_item', follow=False),
    )

    def parse_item(self,response):
        print('==================================',response.url)
        item = HooliItem()

        url = response.url
        print(1,url)

        university = 'University of Chester'
        print(2,university)

        country = 'UK'

        city = 'NULL'

        website = 'https://www1.chester.ac.uk'

        department = 'NULL'

        programme = response.xpath('//h1[@id="main-content"]//text()').extract()
        programme = ''.join(programme)
        print(3,programme)

        degree_type = response.xpath('//h1[@id="main-content"]/div/text()').extract()
        degree_type = ''.join(degree_type)
        print(4,degree_type)

        ucas_code = 'NULL'

        degree_level = '1'

        start_date = response.xpath('//div[@class="startdate m-facts__item"]//text()').extract()
        start_date = ''.join(start_date)
        print(5,start_date)

        degree_description = 'NULL'

        overview = response.xpath('//div[@class="courseajax_overview"]//text()').extract()
        overview = ''.join(overview).replace('\r\n','')
        print(6, overview)

        mode = response.xpath('//div[@class="mode m-facts__item"]//text()').extract()
        mode = ''.join(mode).replace('\r\n','')
        # mode = mode.replace('   ','')
        print(7, mode)


        duration = response.xpath('//div[@class="courseajax_duration m-facts__item"]//text()').extract()
        duration = ''.join(duration).replace('\r\n','')
        # duration = duration.replace('   ','')
        print(8,duration)

        modules = response.xpath('//*[@id="learning"]//text()').extract()
        modules = ''.join(modules).replace('\r\n','')
        modules = modules.replace('\n','').replace('\t','')
        print(9,modules)

        teaching = 'NULL'

        assessment = response.xpath('//div[@class="large-7 columns float-right m-sections__learning-section"]//text()').extract()
        assessment = ''.join(assessment).replace('\r\n','')
        print(10, assessment)

        career = 'NULL'
        # career = ''.join(career).replace('\r\n', '')
        # if "Your personal and professional development" in career_str:
        #     cstart = career_str.find("Your personal and professional development")
        #     cend = career_str.find("Fees and funding")
        #     career = career_str[cstart:cend]
        #     # career = ''.join(career).replace('\r\n', '')
        #     item["career"] = career
        # else:
        #     career = ''
        # print(11,career)

        application_date = 'NULL'

        deadline = 'NULL'

        application_fee = 'NULL'

        tuition_fee = response.xpath('//div[@class="field-fees-international"]/p/text()').extract()
        tuition_fee = ''.join(tuition_fee).replace('\n','')
        # tuition_fee = tuition_fee.replace('   ','')
        tuition_fee = self.getTuition_fee(tuition_fee)
        try:
            if tuition_fee > 0:
                tuition_fee = tuition_fee
            else:
                tuition_fee = 'NULL'
        except:
            tuition_fee = 'NULL'

        print(11, tuition_fee)

        location = response.xpath('//div[@id="edit-compulsory"]//text()').extract()
        location = ''.join(location)
        print(12,location)


        GPA = 'NULL'
        ATAS = 'NULL'

        average_score = 'NULL'

        accredited_university = 'NULL'

        Alevel = 'NULL'

        IB = 'NULL'

        IELTS_lists = response.xpath('//div[@class="courseajax_entryrequirementsint"]//text()').extract()
        IELTS_str = ''.join(IELTS_lists).replace('\r\n','')
        # IELTS = re.findall('(IELTS:|IELTS)? (.*){0,5} \d?.\d? .{0,70}',IELTS)
        if "English Language Requirements" in IELTS_str:
            Istart = IELTS_str.find("IELTS Academic:")
            Iend = IELTS_str.find("Select your country")
            IELTS = IELTS_str[Istart:Iend]
            IELTS = IELTS[:120]
            item["IELTS"] = IELTS
        else:
            IELTS = 'NULL'
        print(13, IELTS)

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

        entry_requirements = response.xpath('//div[@class="courseajax_entryrequirements"]//text()').extract()
        entry_requirements = ''.join(entry_requirements).replace('\r\n','')
        # EntryRequirements = EntryRequirements.replace(' ','')
        # if "Entry requirements" in entry_requirements_str:
        #     erstart = entry_requirements_str.find("Who should study this programme?")
        #     erend = entry_requirements_str.find("English Language requirements")
        #     entry_requirements = entry_requirements_str[erstart:erend]
        #
        #     item["entry_requirements"] = entry_requirements
        # #     print('===========================')
        # else:
        #     entry_requirements = ''
        print(14, entry_requirements)

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

    def getTuition_fee(self,tuition_fee):
        allfee = re.findall(r'\d+,\d+',tuition_fee)
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
