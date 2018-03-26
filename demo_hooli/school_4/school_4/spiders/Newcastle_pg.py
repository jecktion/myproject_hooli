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
    name = 'Newcastle_pg'
    allowed_domains = ['www.ncl.ac.uk']
    start_urls = ['http://www.ncl.ac.uk/postgraduate/courses/#subjects']


    def parse(self, response):
        # print(1,'==================',response.url)
        # print(response.text)
        for i in range(1,443):

            department = response.xpath('//*[@id="azlink"]/li[' +str(i)+ ']/@data-subject').extract()
            clear_space(department)
            department = ''.join(department)
            # print("department:",department)

            # full_links = []

            md = ['#profile','#modules','#careers','#training&skills','#fees&funding','#entryrequirements','#howtoapply','#contact']

            # links = response.xpath('//*[@id="content"]/article/div[@class="subjectcontainer contentSeparator tab containAsides tabtp"]/section[@class="course-list-section"]['+str(i)+ ']/ul/li/a/@href').extract()
            links = response.xpath('//*[@id="azlink"]/li[' +str(i)+ ']/a/@href').extract()
            # print(links)
            for link in links:
                for m in md:
                # print('m:',m)
                    url = 'http://www.ncl.ac.uk' + link + m
                    # print(2,'=================',url)
                    # full_links.append(url)
                    # print(3,'==============',full_links)
                    yield scrapy.Request(url, callback=self.parse_item, meta={"department": department})

                i += 1
        # for full_link in full_links:

    def parse_item(self, response):
        print(3, '================', response.url)
        item = HooliItem()
        url = response.url
        university = "The University of Newcastle"
        country = 'Australia'
        city = 'Newcastle'
        website = 'http://www.ncl.ac.uk'
        degree_level = "1"

        department = response.meta['department']
        print(2, department)
        # print(response.text)

        try:
            programme = response.xpath('//header[@class="introArea"]/div[@class="introTextArea"]/h1/text()').extract()
            programme = ''.join(programme)
            print(3, programme)

            ucas_code = "NULL"
            # clear_space(ucas_code_s)
            # ucas_code_s = ''.join(ucas_code_s)
            # if "UCAS Code:" in ucas_code_s:
            #     start = ucas_code_s.find("UCAS Code:")
            #     end = ucas_code_s.find("(full time:")
            #     ucas_code = ucas_code_s[start:end]
            #     ucas_code = ucas_code.lstrip("UCAS Code:")
            # elif "UCAS Code:" in ucas_code_s:
            #     start = ucas_code_s.find("UCAS Code:")
            #     end = ucas_code_s.find("(part time:")
            #     ucas_code = ucas_code_s[start:end]
            #     # ucas_code = ucas_code[:20]
            #     ucas_code = ucas_code.lstrip("UCAS Code:")
            # else:
            #     ucas_code = "NULL"
            # print(4, ucas_code)


            degree_type = response.xpath('//header[@class="introArea"]/div[@class="introTextArea"]/h1/text()').extract()
            degree_type = getDegree_type(''.join(degree_type))
            print(4, degree_type)

            start_date_s = response.xpath('//div[@class="contentSeparator containAsides textEditorArea"]//text()').extract()
            clear_space(start_date_s)
            # print('===========',start_date_s)
            start_date_s = ''.join(start_date_s)
            if "Start dates" in start_date_s:
                start = start_date_s.find("Start dates")
                end = start_date_s.find("Deposit")
                start_date = start_date_s[start:end]
                start_date = start_date.lstrip("Start dates")
                start_date = start_date[:100]
            else:
                start = start_date_s.find("Start dates")
                start_date = start_date_s[start:]
                start_date = start_date.lstrip("Start dates")
                start_date = start_date[:100]
            print(5,start_date)

            # overview = response.xpath('//div[@class="left logo-bg"]//text()').extract()
            overview_s = response.xpath('//*[@id="content"]/article//div[@class="contentSeparator tab containAsides tabtp"]//text()').extract()
            clear_space(overview_s)
            overview_s = ''.join(overview_s)
            try:
                if "Profile" in overview_s:
                    start = overview_s.find("Profile")
                    end = overview_s.find("Modules")
                    overview = overview_s[start:end]
                elif "Profile" in overview_s:
                    start = overview_s.find("Profile")
                    end = overview_s.find("Training & Skills")
                    overview = overview_s[start:end]
                else:
                    overview = "NULL"
            except:
                overview = "报错!"
            print(6, overview)

            mode = response.xpath('//div[@class="introTextArea"]/p[2]/text()').extract()
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

            duration = response.xpath('//div[@class="introTextArea"]/p[2]/text()').extract()
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

            modules_s = response.xpath('//div[@class="contentSeparator containAsides textEditorArea" or @class="contentSeparator tab containAsides tabtp"]//text()').extract()
            clear_space(modules_s)
            modules_s = ''.join(modules_s)

            try:
                if "Modules for 2017 entry" in modules_s:
                    start = modules_s.find("Modules for 2017 entry")
                    # end = modules_s.find("Fees & Funding")
                    modules = modules_s[start:]
                    item["modules"] = modules
                else:
                    modules = "NULL"
            except:
                modules = "报错!"
            print(9, modules)

            teaching = 'NULL'

            assessment = "NULL"
            # clear_space(assessment_s)
            # assessment_s = ''.join(assessment_s)
            # try:
            #     if "Assessment methods" in assessment_s:
            #         start = assessment_s.find("Assessment methods")
            #         assessment = assessment_s[start:]
            #         assessment = assessment[:1000]
            #     elif "Teaching and assessment" in assessment_s:
            #         start = assessment_s.find("Teaching and assessment")
            #         assessment = assessment_s[start:]
            #         assessment = assessment[:1000]
            #     else:
            #         assessment = "NULL"
            # except:
            #     assessment = "报错!"
            # print(10, assessment)

            career_s = response.xpath('//div[@class="tab-wrapper"]/div[@class="contentSeparator tab containAsides tabtp"]//text()').extract()
            clear_space(career_s)
            # print('===========',career_s)
            career_s = ''.join(career_s)
            try:
                if "Careers " in career_s:
                    start = career_s.find("Careers ")
                    end = career_s.find("Entry Requirements")
                    career = career_s[start:end]
                    item["career"] = career
                else:
                    career = "NULL"
            except:
                career = "报错!"
            # time.sleep(2)

            application_date = "NULL"

            deadline = 'NULL'
            # deadline = ''.join(deadline)
            # print(9,deadline)

            application_fee = 'NULL'

            #//div[@class="contentSeparator tab containAsides tabtp"]//text()
            tuition_fee_s = response.xpath('//div[@class="contentSeparator tab containAsides tabtp"]//text()').extract()
            clear_space(tuition_fee_s)
            tuition_fee_s = ''.join(tuition_fee_s)
            # # tuition_fee = tuition_fee.replace('\n','')
            # # tuition_fee = tuition_fee.replace('    ','')
            # tuition_fee = self.getTuition_fee(tuition_fee)

            try:
                if "Fees & Funding" in tuition_fee_s:
                    start = tuition_fee_s.find("Fees & Funding")
                    end = tuition_fee_s.find("Entry Requirements")
                    tuition_fee = tuition_fee_s[start:end]
                    tuition_fee = getTuition_fee(tuition_fee)

                else:
                    tuition_fee = "NULL"
            except:
                tuition_fee = "报错!"

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

            IELTS_s = response.xpath('//div[@class="answer"]/ul/li//text()').extract()
            # clear_space(IELTS_s)
            IELTS_s = ''.join(IELTS_s).replace('\r\n','')
            # print(IELTS_s)
            # IELTS = re.findall('(IELTS:|IELTS)? (.*){0,5} \d?.\d? .{0,70}',IELTS)

            if "IELTS" in IELTS_s:
                start = IELTS_s.find("IELTS")
                IELTS = IELTS_s[start:]
                # IELTS = IELTS.lstrip("English requirements")
                IELTS = IELTS[:80]
            # elif "" in IELTS_s:
            #     start = IELTS_s.find("English Language Requirements")
            #     IELTS = IELTS_s[start:]
            #     IELTS = IELTS.lstrip("English Language Requirements")
            #     IELTS = IELTS[:100]

            else:
                IELTS = " IELTS 6.5 overall (with a minimum of 5.5 in all sub-skills)."

            print(14, IELTS)

            IELTS_L = 'NULL'
            IELTS_S = 'NULL'
            IELTS_R = 'NULL'
            IELTS_W = 'NULL'

            TOEFL_s = response.xpath('//div[@class="contentSeparator tab containAsides tabtp"]//text()').extract()
            clear_space(TOEFL_s)
            TOEFL_s = ''.join(TOEFL_s)
            try:
                if "TOEFL" in TOEFL_s:
                    start = TOEFL_s.find("TOEFL")
                    TOEFL = TOEFL_s[start:]
                    TOEFL = TOEFL[:80]
                else:
                    TOEFL = "TOEFL 90 overall (with a minimum of 17 in listening, 18 in reading, 20 in speaking, and 17 in writing)."
            except:
                TOEFL = "报错!"

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

            #//div[@class="contentSeparator tab containAsides tabtp"]//text()
            how_to_apply_s = response.xpath('//div[@class="contentSeparator tab containAsides tabtp"]//text()').extract()
            clear_space(how_to_apply_s)
            how_to_apply_s = ''.join(how_to_apply_s)
            try:
                if "How to Apply" in how_to_apply_s:
                    start = how_to_apply_s.find("How to Apply")
                    end = how_to_apply_s.find("Contact")
                    how_to_apply = how_to_apply_s[start:end]

                else:
                    how_to_apply = response.xpath('//div[@class="contentSeparator tab containAsides tabtp"]//text()').extract()
                    clear_space(how_to_apply)
                    how_to_apply = ''.join(how_to_apply)
            except:
                how_to_apply = '报错!'
            print(15, how_to_apply)

            entry_requirements_s = response.xpath('//div[@class="contentSeparator tab containAsides tabtp"]//text()').extract()
            clear_space(entry_requirements_s)
            entry_requirements_s = ''.join(entry_requirements_s)

            try:
                if "Entry Requirements" in entry_requirements_s:
                    start = entry_requirements_s.find("Entry Requirements")
                    end = entry_requirements_s.find("How to Apply")
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
            with open("./error/" + item['university'] + ".txt", 'wa+', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================")
            print("异常：", str(e))
            print("报错url：", response.url)
