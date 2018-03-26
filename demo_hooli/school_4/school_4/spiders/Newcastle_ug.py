# -*- coding: utf-8 -*-
import scrapy
import re
import datetime
import time
from school_4.clearSpace import clear_space
from school_4.items import HooliItem
from school_4.getItem import get_item
from school_4.getTuition_fee import getTuition_fee
from school_4.getDegree_type import getDegree_type



class PlymouthSpider(scrapy.Spider):
    name = 'Newcastle_ug'
    allowed_domains = ['www.ncl.ac.uk']
    start_urls = ['http://www.ncl.ac.uk/undergraduate/degrees/?filterBy=undergraduate&q=&searchSubmit=Search#subject']


    def parse(self, response):
        print(1,'==================',response.url)
        # print(response.text)
        for i in range(0,61):

            department = response.xpath('//div[@id="az"]/div[@class="contentSeparator tab containAsides tabtp"]/h3[' +str(i)+ ']/text()').extract()
            clear_space(department)
            department = ''.join(department)
            print(department)

            # full_links = []

            md = ['#courseoverview','#coursedetails','#entryrequirements','#careers','Progression','#fees&funding','#apply']

            links = response.xpath('//div[@id="az"]/div[@class="contentSeparator tab containAsides tabtp"]/ul[' +str(i)+ ']/li/a/@href').extract()
            # print(links)
            for link in links:
                for m in md:
                # print('m:',m)
                    url = 'http://www.ncl.ac.uk' + link + m
                    print(2,'=================',url)
                    # full_links.append(url)
                    # print(3,'==============',full_links)
                    yield scrapy.Request(url, callback=self.parse_item, meta={"department": department})

                i += 1
        # for full_link in full_links:

    def parse_item(self, response):
        item = HooliItem()
        university = "The University of Newcastle"
        country = 'Australia'
        city = 'Newcastle'
        website = 'http://www.ncl.ac.uk'
        degree_level = "0"
        url = response.url
        print(3,'================',response.url)

        department = response.meta['department']
        print(2, department)

        try:
            programme = response.xpath('//*[@id="content"]/article/header/h1/text()').extract()
            programme = ''.join(programme)
            print(3, programme)

            ucas_code_s = response.xpath('//*[@id="content"]//header[@class="pageTitle"]/p/text()').extract()
            clear_space(ucas_code_s)
            ucas_code_s = ''.join(ucas_code_s)
            if "UCAS Code:" in ucas_code_s:
                start = ucas_code_s.find("UCAS Code:")
                end = ucas_code_s.find("(full time:")
                ucas_code = ucas_code_s[start:end]
                ucas_code = ucas_code.lstrip("UCAS Code:")
            elif "UCAS Code:" in ucas_code_s:
                start = ucas_code_s.find("UCAS Code:")
                end = ucas_code_s.find("(part time:")
                ucas_code = ucas_code_s[start:end]
                # ucas_code = ucas_code[:20]
                ucas_code = ucas_code.lstrip("UCAS Code:")
            else:
                ucas_code = "NULL"
            print(4, ucas_code)


            degree_type = response.xpath('//*[@id="content"]/article/header/h1/text()').extract()
            degree_type = getDegree_type(''.join(degree_type))
            print(5, degree_type)

            start_date = 'NULL'
            # start_date = ''.join(start_date)
            # # print(5,start_date)

            # overview = response.xpath('//div[@class="left logo-bg"]//text()').extract()
            overview_s = response.xpath('//*[@id="content"]/article//div//text()').extract()
            clear_space(overview_s)
            overview_s = ''.join(overview_s)
            try:
                if "Course Overview" in overview_s:
                    start = overview_s.find("Course Overview")
                    end = overview_s.find("Highlights of this degree")
                    overview = overview_s[start:end]
                else:
                    overview = "NULL"
            except:
                overview = "报错!"
            print(6, overview)

            mode = response.xpath('//*[@id="content"]//header[@class="pageTitle"]/p/text()').extract()
            clear_space(mode)
            mode = ''.join(mode)
            # mode = mode.replace('\n','')
            # mode = mode.replace('      ','')
            # try:
            #     if "Study Mode" in mode_s:
            #         start = mode_s.find("Study Mode")
            #         mode = mode_s[start:]
            #         mode = mode[:100]
            #         mode = mode.lstrip("Study Mode")
            #         item["mode"] = mode
            #     else:
            #         mode = "NULL"
            # except:
            #     mode = "报错!"
            print(7, mode)

            duration = response.xpath('//*[@id="content"]//header[@class="pageTitle"]/p/text()').extract()
            clear_space(duration)
            duration = ''.join(duration)
            # duration = duration.replace('\n','')
            # duration = duration.replace('    ','')
            # if "Course Duration" in duration_s:
            #     start= duration_s.find("Course Duration")
            #     duration = duration_s[start:]
            #     duration = duration[:100]
            #     duration = duration.lstrip("Course Duration")
            #     item["duration"] = duration
            # else:
            #     duration = "NULL"

            print(8, duration)

            modules_s = response.xpath('//*[@id="content"]/article//div//text()').extract()
            clear_space(modules_s)
            modules_s = ''.join(modules_s)

            try:
                if "Modules" in modules_s:
                    start = modules_s.find("Modules")
                    end = modules_s.find("Teaching and assessment")
                    modules = modules_s[start:end]
                else:
                    modules = modules_s
            except:
                modules = "报错!"
            print(9, modules)

            teaching = 'NULL'

            assessment_s = response.xpath('//*[@id="content"]/article//div//text()').extract()
            clear_space(assessment_s)
            assessment_s = ''.join(assessment_s)
            try:
                if "Assessment methods" in assessment_s:
                    start = assessment_s.find("Assessment methods")
                    assessment = assessment_s[start:]
                    assessment = assessment[:1000]
                elif "Teaching and assessment" in assessment_s:
                    start = assessment_s.find("Teaching and assessment")
                    assessment = assessment_s[start:]
                    assessment = assessment[:1000]
                else:
                    assessment = "NULL"
            except:
                assessment = "报错!"
            print(10, assessment)

            career_s = response.xpath('//div[@class="contentSeparator containAsides textEditorArea"]//text()').extract()
            clear_space(career_s)
            print('===========',career_s)
            career_s = ''.join(career_s)
            # if "Careers" in career_s:
            #     start = career_s.find("Careers")
            #     end = career_s.find("Next step:")
            #     career = career_s[start:end]
            #     item["career"] = career
            # if "Progression" in career_s:
            #     start = career_s.find("Progression")
            #     end = career_s.find("Next step:")
            #     career = career_s[start:end]

            # if "Careers and employability at Newcastle" in career_s:
            #     career_s = re.findall('',career_s)
            #     start = career_s.index("Careers and employability at Newcastle")
            #     end = career_s.index("Next step:")
            #     career = career_s[start:end]
            #     item["career"] = career

            if "Accounting and Finance careers" in career_s:
                start = career_s.find("Accounting and Finance careers")
                end = career_s.find("Next step:")
                career = career_s[start:end]

            elif "What our graduates go on to do: employment and further study choices" in career_s:
                start = career_s.find("What our graduates go on to do: employment and further study choices")
                end = career_s.find("Next step:")
                career = career_s[start:end]


            else:
                career = "NULL"

            print(11, career)
            time.sleep(2)

            application_date = "NULL"

            deadline = 'NULL'
            # deadline = ''.join(deadline)
            # print(9,deadline)

            application_fee = 'NULL'

            tuition_fee_s = response.xpath('//*[@id="content"]/article//div//text()').extract()
            clear_space(tuition_fee_s)
            tuition_fee_s = ''.join(tuition_fee_s)
            # # tuition_fee = tuition_fee.replace('\n','')
            # # tuition_fee = tuition_fee.replace('    ','')
            # tuition_fee = self.getTuition_fee(tuition_fee)

            if "Tuition Fees (International students)" in tuition_fee_s:
                start = tuition_fee_s.find("Tuition Fees (International students)")
                end = tuition_fee_s.find("Scholarships and Financial Support (UK students)")
                tuition_fee = tuition_fee_s[start:end]
                tuition_fee = getTuition_fee(tuition_fee)

            else:
                tuition_fee = getTuition_fee(tuition_fee_s)


            print(12, tuition_fee)

            location = "Newcastle"
            # location_s = ''.join(location_s).replace('\r\n','')
            # try:
            #     if "Location" in location_s:
            #         start = location_s.find("Location")
            #         location = location_s[start:]
            #         location = location[:100]
            #         location = location.lstrip("Location")
            #         item["location"] = location
            #     else:
            #         location = "NULL"
            # except:
            #     location = "报错!"
            print(13, location)

            ATAS = 'NULL'

            GPA = 'NULL'

            average_score = 'NULL'

            accredited_university = 'NULL'

            Alevel = 'NULL'

            IB = 'NULL'

            IELTS_s = response.xpath('//*[@id="content"]/article//div//text()').extract()
            # clear_space(IELTS_s)
            IELTS_s = ''.join(IELTS_s).replace('\r\n','')
            # print(IELTS_s)
            # IELTS = re.findall('(IELTS:|IELTS)? (.*){0,5} \d?.\d? .{0,70}',IELTS)

            if "English requirements" in IELTS_s:
                start = IELTS_s.find("English requirements")
                IELTS = IELTS_s[start:]
                IELTS = IELTS.lstrip("English requirements")
                IELTS = IELTS[:255]
            elif "" in IELTS_s:
                start = IELTS_s.find("English Language Requirements")
                IELTS = IELTS_s[start:]
                IELTS = IELTS.lstrip("English Language Requirements")
                IELTS = IELTS[:255]

            else:
                IELTS = "NULL"

            print(14, IELTS)

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

            how_to_apply_s = response.xpath('//*[@id="content"]/article//div//text()').extract()
            clear_space(how_to_apply_s)
            how_to_apply_s = ''.join(how_to_apply_s)
            try:
                if "Apply" in how_to_apply_s:
                    start = how_to_apply_s.find("Apply")
                    how_to_apply = how_to_apply_s[start:]

                else:
                    how_to_apply = how_to_apply_s
            except:
                how_to_apply = '报错!'
            print(15, how_to_apply)

            entry_requirements_s = response.xpath('//*[@id="content"]/article//div//text()').extract()
            clear_space(entry_requirements_s)
            entry_requirements_s = ''.join(entry_requirements_s)

            try:
                if "Entry Requirements" in entry_requirements_s:
                    start = entry_requirements_s.find("Entry Requirements")
                    end = entry_requirements_s.find("Careers")
                    entry_requirements = entry_requirements_s[start:end]

                else:
                    entry_requirements = entry_requirements_s

            except:
                entry_requirements = '报错!'

            print(16, entry_requirements)

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
            print(17, create_time)

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

        #异常报错写入日志
        except Exception as e:
            with open("./error/" + item['university'] + ".txt", 'a+', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================")
            print("异常：", str(e))
            print("报错url：", response.url)
