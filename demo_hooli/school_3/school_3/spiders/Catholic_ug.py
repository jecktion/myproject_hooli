

# -*- coding: utf-8 -*-






import scrapy
from school_3.items import HooliItem
import datetime
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import re

class PlymouthSpider(scrapy.Spider):
    name = 'Catholic_ug'
    allowed_domains = ['www.acu.edu.au']
    start_urls = []
    base_url = '%s'

    Lists = ['http://www.acu.edu.au/courses/undergraduate/education/inclusive_education_and_disability_studies/associate_degree_in_inclusive_education_and_disability_studies',
'http://www.acu.edu.au/courses/undergraduate/business/accounting/bachelor_of_accounting_and_finance',
'http://www.acu.edu.au/courses/undergraduate/health/public_health/bachelor_of_applied_public_health',
'http://www.acu.edu.au/courses/undergraduate/health/public_health/bachelor_of_applied_public_health_honours',
'http://www.acu.edu.au/courses/undergraduate/business/business_administration/bachelor_of_applied_public_healthbachelor_of_business_administration',
'http://www.acu.edu.au/courses/undergraduate/health/public_health/bachelor_of_applied_public_healthbachelor_of_global_studies',
'http://www.acu.edu.au/courses/undergraduate/arts/literature,_creative_and_visual_arts/bachelor_of_arts',
'http://www.acu.edu.au/courses/undergraduate/arts/history_and_politics/bachelor_of_arts_business_and_communication_studies',
'http://www.acu.edu.au/courses/undergraduate/arts/history_and_politics/bachelor_of_arts_honours',
'http://www.acu.edu.au/courses/undergraduate/psychology_and_counselling/psychology/bachelor_of_arts_psychology',
'http://www.acu.edu.au/courses/undergraduate/arts/history_and_politics/bachelor_of_arts_bachelor_of_commerce',
'http://www.acu.edu.au/courses/undergraduate/arts/history_and_politics/bachelor_of_artsbachelor_of_global_studies',
'http://www.acu.edu.au/courses/undergraduate/law/law/bachelor_of_artsbachelor_of_laws',
'http://www.acu.edu.au/courses/undergraduate/science/biomedical_science/bachelor_of_biomedical_science',
'http://www.acu.edu.au/courses/undergraduate/science/biomedical_science/bachelor_of_biomedical_sciencebachelor_of_applied_public_health',
'http://www.acu.edu.au/courses/undergraduate/science/biomedical_science/bachelor_of_biomedical_sciencebachelor_of_business_administration',
'http://www.acu.edu.au/courses/undergraduate/science/biomedical_science/bachelor_of_biomedical_sciencebachelor_of_laws',
'http://www.acu.edu.au/courses/undergraduate/business/business_administration/bachelor_of_business_administration',
'http://www.acu.edu.au/courses/undergraduate/business/business_administration/bachelor_of_business_administrationbachelor_of_global_studies',
'http://www.acu.edu.au/courses/undergraduate/law/law/bachelor_of_business_administrationbachelor_of_laws',
'http://www.acu.edu.au/courses/undergraduate/business/commerce/bachelor_of_commerce',
'http://www.acu.edu.au/courses/undergraduate/business/commerce/bachelor_of_commerce_atsi',
'http://www.acu.edu.au/courses/undergraduate/business/commerce/bachelor_of_commercebachelor_of_business_administration',
'http://www.acu.edu.au/courses/undergraduate/business/commerce/bachelor_of_commercebachelor_of_global_studies',
'http://www.acu.edu.au/courses/undergraduate/law/law/bachelor_of_commercebachelor_of_laws',
'http://www.acu.edu.au/courses/undergraduate/psychology_and_counselling/counselling/bachelor_of_counselling',
'http://www.acu.edu.au/courses/undergraduate/arts/literature,_creative_and_visual_arts/bachelor_of_creative_arts',
'http://www.acu.edu.au/courses/undergraduate/education/early_childhood_education/bachelor_of_early_childhood_education_birth_to_five_years',
'http://www.acu.edu.au/courses/undergraduate/education/primary_teaching/bachelor_of_education_early_childhood_and_primary_pass_and_honours',
'http://www.acu.edu.au/courses/undergraduate/education/primary_teaching/bachelor_of_education_fourth_year_upgrade',
'http://www.acu.edu.au/courses/undergraduate/education/primary_teaching/bachelor_of_education_primary',
'http://www.acu.edu.au/courses/undergraduate/education/primary_teaching/bachelor_of_education_primary_away_from_base',
'http://www.acu.edu.au/courses/undergraduate/business/business_administration/bachelor_of_exercise_sciencebachelor_of_business_administration',
'http://www.acu.edu.au/courses/undergraduate/health/public_health/bachelor_of_exercise_sciencebachelor_of_public_health2',
'http://www.acu.edu.au/courses/undergraduate/exercise_science/exercise_science/bachelor_of_exercise_and_health_science_honours',
'http://www.acu.edu.au/courses/undergraduate/exercise_science/exercise_science/bachelor_of_exercise_and_sports_science',
'http://www.acu.edu.au/courses/undergraduate/exercise_science/exercise_science/bachelor_of_exercise_and_sports_science_honours',
'http://www.acu.edu.au/courses/undergraduate/education/inclusive_education_and_disability_studies/bachelor_of_inclusive_education_and_disability_studies',
'http://www.acu.edu.au/courses/undergraduate/information_technology/bachelor_of_information_technology',
'http://www.acu.edu.au/courses/undergraduate/business/information_technology/b_of_information_technology_b_of_business_administration',
'http://www.acu.edu.au/courses/undergraduate/arts/international_development_and_global_studies/bachelor_of_international_development_studies',
'http://www.acu.edu.au/courses/undergraduate/law/law/bachelor_of_laws',
'http://www.acu.edu.au/courses/undergraduate/law/law/bachelor_of_laws_graduate_entry',
'http://www.acu.edu.au/courses/undergraduate/law/law/bachelor_of_lawsbachelor_of_global_studies',
'http://www.acu.edu.au/courses/undergraduate/arts/media_and_digital_journalism/bachelor_of_media_production',
'http://www.acu.edu.au/courses/undergraduate/nursing_and_midwifery/midwifery/bachelor_of_midwifery',
'http://www.acu.edu.au/courses/undergraduate/nursing_and_midwifery/midwifery/bachelor_of_midwifery_graduate_entry',
'http://www.acu.edu.au/courses/undergraduate/nursing_and_midwifery/midwifery/bachelor_of_midwifery_honours',
'http://www.acu.edu.au/courses/undergraduate/nursing_and_midwifery/midwifery/bachelor_of_midwifery_indigenous_program',
'http://www.acu.edu.au/courses/undergraduate/nursing_and_midwifery/nursing/bachelor_of_nursing',
'http://www.acu.edu.au/courses/undergraduate/nursing_and_midwifery/nursing/bachelor_of_nursing_enrolled_nurses',
'http://www.acu.edu.au/courses/undergraduate/nursing_and_midwifery/nursing/bachelor_of_nursing_honours',
'http://www.acu.edu.au/courses/undergraduate/nursing_and_midwifery/nursing/bachelor_of_nursingbachelor_of_business_administration',
'http://www.acu.edu.au/courses/undergraduate/nursing_and_midwifery/nursing/bachelor_of_nursingbachelor_of_counselling',
'http://www.acu.edu.au/courses/undergraduate/health/paramedicine/bachelor_of_nursingbachelor_of_paramedicine',
'http://www.acu.edu.au/courses/undergraduate/exercise_science/nutrition_science/bachelor_of_nutrition_science',
'http://www.acu.edu.au/courses/undergraduate/business/business_administration/bachelor_of_nutrition_sciencebachelor_of_business_administration',
'http://www.acu.edu.au/courses/undergraduate/allied_health/occupational_therapy/bachelor_of_occupational_therapy',
'http://www.acu.edu.au/courses/undergraduate/health/paramedicine/bachelor_of_paramedicine',
'http://www.acu.edu.au/courses/undergraduate/health/paramedicine/bachelor_of_paramedicine_honours',
'http://www.acu.edu.au/courses/undergraduate/health/paramedicine/bachelor_of_paramedicine_professional_entry',
'http://www.acu.edu.au/courses/undergraduate/exercise_science/exercise_science/bachelor_of_physical_activity_and_health_science',
'http://www.acu.edu.au/courses/undergraduate/allied_health/physiotherapy/bachelor_of_physiotherapy',
'http://www.acu.edu.au/courses/undergraduate/psychology_and_counselling/psychology/bachelor_of_psychological_science',
'http://www.acu.edu.au/courses/undergraduate/psychology_and_counselling/psychology/bachelor_of_psychological_science_honours',
'http://www.acu.edu.au/courses/undergraduate/law/law/bachelor_of_psychological_sciencebachelor_of_laws',
'http://www.acu.edu.au/courses/undergraduate/science/science/bachelor_of_science',
'http://www.acu.edu.au/courses/undergraduate/science/science/bachelor_of_science_environment',
'http://www.acu.edu.au/courses/undergraduate/business/business_administration/bachelor_of_science_environmentbachelor_of_business_administration',
'http://www.acu.edu.au/courses/undergraduate/business/business_administration/bachelor_of_sciencebachelor_of_business_administration',
'http://www.acu.edu.au/courses/undergraduate/social_work/bachelor_of_social_work',
'http://www.acu.edu.au/courses/undergraduate/allied_health/speech_pathology/bachelor_of_speech_pathology',
'http://www.acu.edu.au/courses/undergraduate/exercise_science/exercise_science/bachelor_of_sport_and_outdoor_education',
'http://www.acu.edu.au/courses/undergraduate/exercise_science/exercise_science/bachelor_of_sport_and_outdoor_education',
'http://www.acu.edu.au/courses/undergraduate/arts/history_and_politics/bachelor_of_teachingbachelor_of_arts_humanities',
'http://www.acu.edu.au/courses/undergraduate/arts/history_and_politics/bachelor_of_teachingbachelor_of_arts_mathematics',
'http://www.acu.edu.au/courses/undergraduate/arts/history_and_politics/bachelor_of_teachingbachelor_of_arts_technology',
'http://www.acu.edu.au/courses/undergraduate/arts/history_and_politics/bachelor_of_teachingbachelor_of_arts_visual_arts',
'http://www.acu.edu.au/courses/undergraduate/education/secondary_teaching/bachelor_of_teachingbachelor_of_exercise_science',
'http://www.acu.edu.au/courses/undergraduate/education/secondary_teaching/bachelor_of_teachingbachelor_of_science',
'http://www.acu.edu.au/courses/undergraduate/theology/theology/bachelor_of_theology',
'http://www.acu.edu.au/courses/undergraduate/theology/theology/bachelor_of_theology_honours',
'http://www.acu.edu.au/courses/undergraduate/arts/international_development_and_global_studies/bachelor_of_theologybachelor_of_global_studies',
'http://www.acu.edu.au/courses/undergraduate/law/law/bachelor_of_theologybachelor_of_laws',
'http://www.acu.edu.au/courses/undergraduate/theology/theology/bachelor_of_theology_bachelor_of_philosophy',
'http://www.acu.edu.au/courses/undergraduate/arts/literature,_creative_and_visual_arts/bachelor_of_visual_arts_and_design',
'http://www.acu.edu.au/courses/undergraduate/arts/society_and_youth/bachelor_of_youth_work',
'http://www.acu.edu.au/courses/other_courses/pathway/diploma_in_business_information_systems',
'http://www.acu.edu.au/courses/other_courses/pathway/diploma_in_commerce',
'http://www.acu.edu.au/courses/undergraduate/education/education/diploma_in_educational_studies_tertiary_preparation',
'http://www.acu.edu.au/courses/undergraduate/arts/languages/diploma_in_languages',
'http://www.acu.edu.au/courses/other_courses/pathway/diploma_in_liberal_studies',
'http://www.acu.edu.au/courses/other_courses/pathway/diploma_in_visual_arts_and_design',
'http://www.acu.edu.au/courses/other_courses/pathway/diploma_in_youth_work',]

    for i in Lists:
        fullurl = base_url % i
        start_urls.append(fullurl)

    #rules = (
    #     # Rule(LinkExtractor(allow=(r'.*'), restrict_xpaths=('')),callback='parse_item', follow=True),
    #     # Rule(LinkExtractor(allow=r'https://www.usq.edu.au/extrafiles/templates/gsa/search.htm\?q=undergraduate&proxystylesheet=USQ_Search&site=USQ_Degrees&d=1519805530929&page=[0-45]'),follow=True),
    #     # Rule(LinkExtractor(allow=(r'.*'),restrict_xpaths=('//*[@id="course-lists"]/ul/li/a')), follow=False),
        #Rule(LinkExtractor(allow=r'.*'),callback='parse_item', follow=False),
    #)

    def parse(self,response):
        print('==================================', response.url)
        item = HooliItem()
        url = response.url
        print(1,url)

        university = 'Australian Catholic University'
        print(2,university)

        department = "NULL"
        # department_s = ''.join(department_s).replace('\n','')
        # try:
        #     if "Offered by:" in department_s:
        #         start = department_s.find("Offered by:")
        #         department = department_s[start:]
        #         department = department[:80]
        #         department = department.lstrip("Offered by:")
        #         item["department"] = department
        #     else:
        #         department = "NULL"
        #
        # except:
        #     department = "报错!"

        # print(3,department)

        country = 'Australia'
        city = "NULL"
        website = 'http://www.acu.edu.au'
        degree_level = '0'

        # programme = response.xpath('//div[@class="section picture-nav"]/h1/text()').extract()
        programme = response.xpath('//*[@id="main-content"]/section/div/h1/text()').extract()
        programme = ''.join(programme)
        print(4,programme)

        ucas_code = response.xpath('//*[@id="new_content_container_1346001"]/text()').extract()
        ucas_code = ''.join(ucas_code)
        # try:
        #     if "VU course code:" in ucas_code_s:
        #         start = ucas_code_s.find("VU course code:")
        #         ucas_code = ucas_code_s[start:]
        #         ucas_code = ucas_code[:50]
        #         ucas_code = ucas_code.lstrip("VU course code:")
        #         item["ucas_code"] = ucas_code
        #     else:
        #         ucas_code = "NULL"
        # except:
        #     ucas_code = "报错!"
        print(5,ucas_code)

        # degree_type = response.xpath('//div[@class="section picture-nav"]/h1/text()').extract()
        degree_type = response.xpath('//*[@id="main-content"]/section/div/h1/text()').extract()
        degree_type = ''.join(degree_type)
        # degree_type = self.getDegree_type(degree_type)
        try:
            if "Bachelor" in degree_type:
                degree_type = "Bachelor"
            elif "Master" in degree_type:
                degree_type = "Master"
            else:
                degree_type = "NULL"
        except:
            degree_type = "报错!"
        print(6,degree_type)

        start_date = response.xpath('//*[@id="collapseSeven"]/div//text()').extract()
        start_date = ''.join(start_date)
        # try:
        #     if " Start" in start_date_s:
        #         start = start_date_s.find(" Start")
        #         start_date = start_date_s[start:]
        #         start_date = start_date[:100]
        #         item["start_date"] = start_date
        #     else:
        #         start_date = "NULL"
        # except:
        #     start_date = "报错!"
        print(7,start_date)

        # overview = response.xpath('//div[@class="left logo-bg"]//text()').extract()
        overview = response.xpath('//*[@id="collapseOne"]//text()').extract()
        overview = ''.join(overview)
        print(7, overview)

        mode = response.xpath('//*[@id="collapseTwo"]/div/p/text()').extract()
        mode = ''.join(mode)
        # try:
        #     if " Study Mode" in mode_s:
        #         start = mode_s.find(" Study Mode")
        #         mode = mode_s[start:]
        #         mode = mode[:80]
        #         mode = mode.lstrip(" Study Mode")
        #         item["mode"] = mode
        #     else:
        #         mode = "NULL"
        # except:
        #     mode = "报错!"
        print(8,mode)



        duration = response.xpath('//*[@id="collapseTwo"]/div/p/text()').extract()
        duration = ''.join(duration)
        # duration = duration.replace('\n','')
        # duration = duration.replace('    ','')
        # try:
        #     if "Duration" in duration_s:
        #         start = duration_s.find("Duration")
        #         # end = duration_s.find("Location:")
        #         duration = duration_s[start:]
        #         duration = duration[:100]
        #         duration = duration.lstrip("Duration")
        #         item["duration"] = duration
        #     else:
        #         duration = "NULL"
        # except:
        #     duration = "报错!"
        print(9,duration)

        modules = response.xpath('//*[@id="collapseEntryPathways"]/div//text()').extract()
        modules = ''.join(modules)
        modules = modules.replace('\n','')
        # try:
        #     if "Modules" in modules_s:
        #         start = modules_s.find("Modules")
        #         end = modules_s.find("Assessment")
        #         modules = modules_s[start:end]
        #         item["modules"] = modules
        #     else:
        #         modules = modules_s
        # except:
        #     modules = modules_s
        print(10,modules)

        teaching = 'NULL'

        assessment = 'NULL'
        # assessment_s = ''.join(assessment_s).replace("\r\n","").replace('      ','').replace('\n','')
        # try:
        #     if "Admission & pathways" in assessment_s:
        #         start = assessment_s.find("Admission & pathways")
        #         end = assessment_s.find("How to apply")
        #         assessment = assessment_s[start:end]
        #         item["assessment"] = assessment
        #     else:
        #         assessment = "NULL"
        # except:
        #     assessment = "报错!"
        print(11, assessment)

        career = response.xpath('//*[@id="collapseEleven"]//text()').extract()
        career = ''.join(career)

        # try:
        #     if "Career opportunities" in career_s:
        #         start = career_s.find("Career opportunities")
        #         end = career_s.find("Course specific information")
        #         career = career_s[start:end]
        #         item["career"] = career
        #     else:
        #         career = "NULL"
        # except:
        #     career = "报错!"
        print(12, career)

        application_date = "NULL"

        deadline = 'NULL'
        # deadline = ''.join(deadline)
        # print(9,deadline)

        application_fee = 'NULL'

        tuition_fee_s = response.xpath('//*[@id="collapseEight"]/div/ul/li/text()').extract()
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

        print(13, tuition_fee)

        location_s = response.xpath('//*[@id="main-content"]//div[@class="col-xs-12 col-sm-6 col-md-6 col-lg-6"]//text()').extract()
        location_s = ''.join(location_s)
        try:
            if "Location:" in location_s:
                start = location_s.find("Location:")
                location = location_s[start:]
                location = location[:100]
                location = location.lstrip("Location:")
                item["location"] = location
            else:
                location = "NULL"
        except:
            location = "报错!"
        print(14,location)

        ATAS = 'NULL'

        GPA = 'NULL'

        average_score = 'NULL'

        accredited_university = 'NULL'

        Alevel = 'NULL'

        IB = 'NULL'

        IELTS_s = response.xpath('//*[@id="collapseSeventeen"]/div/p//text()').extract()
        IELTS_s = ''.join(IELTS_s)
        # # IELTS = re.findall('(IELTS:|IELTS)? (.*){0,5} \d?.\d? .{0,70}',IELTS)
        try:
            if "IELTS" in IELTS_s:
                start = IELTS_s.find("IELTS")
                # end = IELTS_s.find("TOEFL")
                IELTS = IELTS_s[start:]
                IELTS = IELTS[:200]
                item["IELTS"] = IELTS
            else:
                IELTS = "NULL"
        except:
            IELTS = "报错!"
        print(11, IELTS)

        IELTS_L = 'NULL'
        IELTS_S = 'NULL'
        IELTS_R = 'NULL'
        IELTS_W = 'NULL'


        TOEFL_s = response.xpath('//*[@id="collapseSeventeen"]/div/p//text()').extract()
        TOEFL_s = ''.join(TOEFL_s)
        # # IELTS = re.findall('(IELTS:|IELTS)? (.*){0,5} \d?.\d? .{0,70}',IELTS)
        try:
            if "IELTS" in TOEFL_s:
                start = TOEFL_s.find("IELTS")
                # end = TOEFL_s.find("TOEFL")
                TOEFL = TOEFL_s[start:]
                TOEFL = TOEFL[:200]
                item["TOEFL"] = TOEFL
            else:
                TOEFL = "NULL"
        except:
            TOEFL = "报错!"
        print(12, TOEFL)

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

        how_to_apply = response.xpath('//*[@id="collapseTen"]/div//text()').extract()
        how_to_apply = ''.join(how_to_apply)
        # try:
        #     if "How to Apply" in how_to_apply_s:
        #         start = how_to_apply_s.find("How to Apply")
        #         end = how_to_apply_s.find("Entry requirements")
        #         how_to_apply = how_to_apply_s[start:end]
        #         item["how_to_apply"] = how_to_apply
        #     else:
        #         how_to_apply = how_to_apply_s
        # except:
        #     how_to_apply = '报错!'
        print(15,how_to_apply)

        entry_requirements = response.xpath('//*[@id="collapseNine"]/div//text()').extract()
        entry_requirements = ''.join(entry_requirements)
        # # EntryRequirements = EntryRequirements.replace(' ','')
        # # try:
        # #     if "Entry requirements" in entry_requirements_s:
        # #         start = entry_requirements_s.find("Entry requirements")
        # #         end = entry_requirements_s.find("Study options")
        # #         entry_requirements = entry_requirements_s[start:end]
        # #         item["entry_requirements"] = entry_requirements
        # #     else:
        # #         entry_requirements = entry_requirements_s
        # #
        # # except:
        # #     entry_requirements = '报错!'
        #
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
        print(16, create_time)

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

        #yield item

    def getTuition_fee(self, tuition_fee):
        allfee = re.findall(r'\d+', tuition_fee)
        # print(allfee)
        for index in range(len(allfee)):
            fee = allfee[index]
            allfee[index] = ''.join(fee)
            # print(allfee[index])
        # print(allfee)
        maxfee = 0
        for fee in allfee:
            if int(fee) >= maxfee:
                maxfee = int(fee)
        return maxfee

