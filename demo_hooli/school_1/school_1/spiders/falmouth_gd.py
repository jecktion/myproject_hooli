





import scrapy
from school_1.items import HooliItem
import datetime
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import re

class PlymouthSpider(CrawlSpider):
    name = 'falmouth_gd'
    allowed_domains = ['www.falmouth.ac.uk']
    start_urls = []
    base_url = '%s'

    Lists = ['http://flexible.falmouth.ac.uk/courses/ma-advertising-strategy-planning.htm',
'https://www.falmouth.ac.uk/communication-design-ma',
'https://www.falmouth.ac.uk/creativeadvertising',
'http://flexible.falmouth.ac.uk/courses/ma-creative-app-development.htm',
'http://flexible.falmouth.ac.uk/courses/ma-creative-events-management.htm',
'https://www.falmouth.ac.uk/film-television-ma',
'https://www.falmouth.ac.uk/illustrationma',
'https://www.falmouth.ac.uk/launchpad',
'https://www.falmouth.ac.uk/leasing-asset-finance',
'http://flexible.falmouth.ac.uk/courses/ma-photography.htm',
'http://flexible.falmouth.ac.uk/courses/pgche.htm',
'https://www.falmouth.ac.uk/professionalwriting',
'http://flexible.falmouth.ac.uk/courses/ma-writing-for-script-screen.htm',

]

    for i in Lists:
        fullurl = base_url % i
        start_urls.append(fullurl)

    rules = (
        Rule(LinkExtractor(allow=(r'.*'), restrict_xpaths=('//li[@class="item isotope-item"]/a')),follow=True),
        # Rule(LinkExtractor(allow=r''),follow=True),
        Rule(LinkExtractor(allow=r'.*'),callback='parse_item', follow=False),
    )

    def parse_item(self,response):
        print('==================================',response.url)
        item = HooliItem()

        url = response.url
        print(1,url)

        university = 'FALMOUTH UNIVERSITY'
        print(2,university)

        department = 'NULL'
        country = 'UK'
        city = 'NULL'
        website = 'https://www.falmouth.ac.uk'

        # programme = response.xpath('//div[@class="title"]/h1/text()').extract()
        programme = response.xpath('//div[@class="h1-box"]/h1/text()').extract()
        programme = ''.join(programme)
        print(3,programme)

        ucas_code = 'NULL'

        degree_level = '1'

        degree_type = response.xpath('//div[@class="h1-box"]/h1/text()').extract()
        degree_type = ''.join(degree_type)
        print(4,degree_type)

        start_date_lists = response.xpath('//div[@class="accordion"]//text()').extract()
        start_date_str = ''.join(start_date_lists)
        if "Start dates and application deadlines" in start_date_str:
            sdstart = start_date_str.find("Start dates and application deadlines")
            sdend = start_date_str.find("News and Events")
            start_date = start_date_str[sdstart:sdend]
            item["start_date"] = start_date
        else:
            start_date = 'NULL'
        print(5,start_date)

        # overview = response.xpath('//div[@class="moduleWhite smallmargin"]//text()').extract()
        overview_list = response.xpath('//div[@class="content-block-wrapper"]//text()').extract()
        overview_str = ''.join(overview_list)
        if "Benefits" in overview_str:
            Ostart = overview_str.find("Benefits")
            Oend = overview_str.find("How the course is taught")
            overview = overview_str[Ostart:Oend]
            item["overview"] = overview
        else:
            overview = response.xpath('//div[@class="content-block-wrapper"]//text()').extract()
            overview = ''.join(overview)

        print(6, overview)

        mode = response.xpath('//div[@class="content-block-wrapper"]//dl//text()').extract()
        mode = ''.join(mode)
        # mode_lists = response.xpath('//div[@class="moduleWhite smallmargin"]//text()').extract()
        # mode_str = ''.join(mode_lists)
        # # mode = mode.replace('\n','')
        # # mode = mode.replace('      ','')
        # if "Mode of study:" in mode_str:
        #     mstart = mode_str.find("Mode of study:")
        #     mend = mode_str.find("Summary")
        #     mode = mode_str[mstart:mend]
        #     item["mode"] = mode
        # else:
        #     mode = ''
        print(7,mode)

        types = ''

        # duration_lists = response.xpath('//div[@class="moduleWhite smallmargin"]//text()').extract()
        duration = response.xpath('//div[@class="content-block-wrapper"]//dl//text()').extract()
        duration = ''.join(duration)
        # duration_str = ''.join(duration_lists)
        # # duration = duration.replace('\n','')
        # # duration = duration.replace('    ','')
        # if "Mode of study:" in duration_str:
        #     dstart = duration_str.find("Mode of study:")
        #     dend = duration_str.find("Duration:")
        #     duration = duration_str[dstart:dend]
        #     item["duration"] = duration
        # else:
        #     duration = ''
        print(8,duration)

        modules = response.xpath('//div[@class="accordion ui-accordion ui-widget ui-helper-reset"]//text()').extract()
        modules = ''.join(modules)
        # modules_lists = response.xpath('//div[@class="accordion"]//text()').extract()
        # modules_str = ''.join(modules_lists)
        # if "Course content" in modules_str:
        #     mdstart = modules_str.find("Course content")
        #     mdend = modules_str.find("Assessments")
        #     modules = modules_str[mdstart:mdend]
        #     item["modules"] = modules
        # else:
        #     modules = ''
        # modules = modules.replace('\n','')
        print(9,modules)

        teaching = 'NULL'

        assessment = response.xpath('//div[@class="accordion"]//text()').extract()
        assessment = ''.join(assessment)
        # teaching_assessment_lists = response.xpath('//div[@class="accordion"]//text()').extract()
        # teaching_assessment_str = ''.join(teaching_assessment_lists)
        # if "Assessments" in teaching_assessment_str:
        #     Astart = teaching_assessment_str.find("Assessments")
        #     Aend = teaching_assessment_str.find("How you study")
        #     teaching_assessment = teaching_assessment_str[Astart:Aend]
        #     item["teaching_assessment"] = teaching_assessment
        # else:
        #     teaching_assessment = ''
        print(10,assessment)

        career = response.xpath('//div[@class="field-career-opportunities"]//text()').extract()
        career = ''.join(career)
        print(11, career)

        application_date = 'NULL'

        deadline_lists = response.xpath('//div[@class="accordion"]//text()').extract()
        deadline_str = ''.join(deadline_lists)
        if "Start dates and application deadlines" in deadline_str:
            dlstart  = deadline_str.find("Start dates and application deadlines")
            dlend = deadline_str.find("News and Events")
            deadline = deadline_str[dlstart:dlend]
            item["deadline"] = deadline
        else:
            deadline = 'NULL'
        print(11,deadline)



        application_fee = 'NULL'

        tuition_fee= 'NULL'
        # tuition_fee = ''.join(tuition_fee).replace('\r\n','')
        # tuition_fee = tuition_fee.replace('\n','')
        # tuition_fee = tuition_fee.replace('    ','')
        # print(11, tuition_fee)

        location = 'NULL'
        # location = ''.join(location)
        # print(13,location)

        ATAS = 'NULL'


        GPA = 'NULL'

        average_score = 'NULL'

        accredited_university = 'NULL'

        Alevel = 'NULL'

        IB = 'NULL'

        IELTS_lists = response.xpath('//div[@class="accordion"]//text()').extract()
        IELTS_str = ''.join(IELTS_lists)
        # IELTS = re.findall('(IELTS:|IELTS)? (.*){0,5} \d?.\d? .{0,70}',IELTS)
        if "Entry Requirements" in IELTS_str:
            Istart = IELTS_str.find("Entry Requirements")
            Iend = IELTS_str.find("Financing your studies")
            IELTS = IELTS_str[Istart:Iend]
            item["IELTS"] = IELTS
        else:
            IELTS = 'NULL'
        print(12, IELTS)

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

        interview = response.xpath('//div[@class="field-selection-process"]//text()').extract()
        interview = ''.join(interview)
        print(13,interview)

        portfolio = response.xpath('//div[@class="field-selection-process"]//text()').extract()
        portfolio = ''.join(portfolio)
        print(14,portfolio)

        application_documents = 'NULL'

        how_to_apply_lists = response.xpath('//div[@class="accordion"]//text()').extract()
        how_to_apply_str = ''.join(how_to_apply_lists)
        if "How to apply" in how_to_apply_str:
            hstart = how_to_apply_str.find("How to apply")
            hend = how_to_apply_str.find("Start dates and application deadlines")
            how_to_apply = how_to_apply_str[hstart:hend]
            item["how_to_apply"] = how_to_apply
        else:
            how_to_apply = 'NULL'
        print(13,how_to_apply)

        entry_requirements = response.xpath('//*[@id="start-of-content"]/div[2]/div[2]/div[1]//text()').extract()
        entry_requirements = ''.join(entry_requirements)
        
        # entry_requirements_lists = response.xpath('//div[@class="accordion"]//text()').extract()
        # entry_requirements_str = ''.join(entry_requirements_lists)
        # # EntryRequirements = EntryRequirements.replace(' ','')
        # if "Entry Requirements" in entry_requirements_str:
        #     Estart = entry_requirements_str.find("Entry Requirements")
        #     Eend = entry_requirements_str.find("Financing your studies")
        #     entry_requirements = entry_requirements_str[Estart:Eend]
        #     item["entry_requirements"] = entry_requirements
        # else:
        #     entry_requirements = ''
        print(14,entry_requirements)

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