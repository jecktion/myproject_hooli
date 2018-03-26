from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import scrapy
import re
import datetime
from school_3.clearSpace import clear_space, clear_space_str
from school_3.getItem import get_item
from school_3.getTuition_fee import getTuition_fee
from school_3.items import HooliItem
from school_3.getDegree_type import getDegree_type

class DeakinBenSchoolSpider(CrawlSpider):
    name = "deakinBen_ug"
    allowed_domains = ['www.deakin.edu.au']
    start_urls = ["http://www.deakin.edu.au/courses/find-a-course/results?dkncoursestudent=International&dkncoursequal=under_bachelor_degree&dkncoursequal=under_bachelor_honours&q=&dknpagetype=Course&startrow=0"]

    rules = (
        # Rule(page_link, callback='get_programme_link', follow=True),
        Rule(LinkExtractor(allow=r'startrow=\d+'), follow=True),
        Rule(LinkExtractor(restrict_xpaths="//div[@class='module_search-item']/div[@class='module_search-item--content']/div[@class='module_search-text']/p[1]/a"), follow=True, callback='text1'),
        # Rule(LinkExtractor(restrict_xpaths='//ul[@class="no-list-bullets"]/li/a'), follow=False, callback='text2'),
    )
    # def text(self, response):
    #     print(response.url)

    def text1(self, response):
        item = HooliItem()
        university = "Deakin University"

        city = "NULL"
        country = 'Australia'

        website = 'http://www.deakin.edu.au'

        url = response.url

        print("===========================",response.url)

        try:
            programme = response.xpath("//div[@class='module__hero-banner--content--inner']/h1//text()").extract()
            clear_space(programme)
            programme = ''.join(programme)
            # print("item['programme']: ", item['programme'])
            degree_type = response.xpath("//div[@class='module__hero-banner--content--inner']/h1//text()").extract()
            clear_space(degree_type)
            degree_type = ''.join(degree_type)
            # degree_type = getDegree_type(''.join(degree_type))
            print(degree_type)
            # try:
            #     if "Associate Degree" in degree_type:
            #         degree_type = "Associate Degree"
            #     elif "Bachelor" in degree_type:
            #         degree_type = "Bachelor"
            #     elif "Master" in degree_type:
            #         degree_type = "Master"
            #     else:
            #         degree_type = "NULL"
            # except:
            #     degree_type = "报错!"


            # //div[@class='module__summary--items']/div[1]/div[2]
            IELTS = response.xpath("//div[@class='module__summary--items']/div[1]/div[2]//text()").extract()
            clear_space(IELTS)
            IELTS = ''.join(IELTS)
            # print("item['IELTS']: ", item['IELTS'])

            duration = response.xpath("//div[@class='module__summary--items']/div[2]/div[2]//text()").extract()
            clear_space(duration)
            duration = ''.join(duration)
            # print("item['duration']: ", item['duration'])

            # location = response.xpath("//div[@class='module__summary--items']/div[3]/div[2]//text()").extract()
            # clear_space(location)
            # location = ''.join(location)
            # print("item['location']: ", item['location'])

            mode_s = response.xpath('//*[@id="main-content"]//div[@class="module__summary--item"]//text()').extract()
            mode_s = ''.join(mode_s).replace('\n', '').strip().replace('   ', '')
            # mode = mode.replace('\n','')
            # mode = mode.replace('      ','')
            try:
                if "Duration" in mode_s:
                    start = mode_s.find("Duration")
                    mode = mode_s[start:]
                    mode = mode[:50]
                    mode = mode.lstrip("Duration")
                    item["mode"] = mode
                else:
                    mode = "NULL"
            except:
                mode = "报错!"

            location_s = response.xpath(
                '//*[@id="main-content"]//div[@class="module__summary--item"]//text()').extract()
            location_s = ''.join(location_s).replace('\n', '')
            try:
                if "Campuses" in location_s:
                    start = location_s.find("Campuses ")
                    location = location_s[start:]
                    location = location[:150]
                    location = location.lstrip("Campuses")
                    location= location.strip()
                    item["location"] = location
                else:
                    location = "NULL"
            except:
                location = "报错!"

            # //div[@id='navigation__course']/following-sibling::div
            overview = response.xpath("//div[@id='navigation__course']/following-sibling::div[1]//text()").extract()
            clear_space(overview)
            overview = ''.join(overview)
            # print("item['overview']: ", item['overview'])

            modules = response.xpath("//div[@id='module__course-structure']//text()").extract()
            clear_space(modules)
            modules = ''.join(modules)
            # print("item['modules']: ", item['modules'])

            # //div[@id='main-content']/div[@class='module__content-panel module__key-information module__no-divider']
            ucascodeContent = response.xpath("//div[@id='main-content']/div[@class='module__content-panel module__key-information module__no-divider']//text()").extract()
            clear_space(ucascodeContent)
            # print("ucascodeContent: ", ucascodeContent)
            if "Deakin code" in ucascodeContent:
                ucascodeIndex = ucascodeContent.index("Deakin code")
                if "CRICOS" in ucascodeContent:
                    ucascodeIndexEnd = ucascodeContent.index("CRICOS")
                else:
                    ucascodeIndexEnd = -1
                ucascode = ucascodeContent[ucascodeIndex+1:ucascodeIndexEnd]
                ucas_code = ''.join(ucascode).strip()
            # print("item['ucas_code']: ", item['ucas_code'])

            # //div[@data-section='entry requirements']
            entry_requirements = response.xpath("//div[@data-section='entry requirements']//text()").extract()
            clear_space(entry_requirements)
            entry_requirements = ''.join(entry_requirements)
            # print("item['entry_requirements']: ", item['entry_requirements'])

            # //div[@data-section='fees and scholarships']
            tuition_fee = response.xpath("//div[@data-section='fees and scholarships']//text()").extract()
            clear_space(tuition_fee)
            tuition_fee = getTuition_fee(''.join(tuition_fee))

            # print("item['tuition_fee']: ", item['tuition_fee'])

            career1 = response.xpath("//div[@data-section='graduate outcomes']//text()").extract()
            career2= response.xpath("//div[@data-section='graduate outcomes']/following-sibling::div[1]//text()").extract()
            clear_space(career1)
            clear_space(career2)
            career = ''.join(career1) + ''.join(career2)

            # print("item['career']: ", item['career'])

            # //div[@data-section='application information']/following-sibling::div[2]
            how_to_apply = response.xpath(
                "//div[@data-section='application information']/following-sibling::div[2]//text()").extract()
            clear_space(how_to_apply)
            how_to_apply = ''.join(how_to_apply)
            # print("item['how_to_apply']: ", item['how_to_apply'])

            # print(item)
            department = "NULL"
            degree_level = "0"
            start_date = "NULL"
            degree_description = "NULL"
            teaching = 'NULL'
            assessment = "NULL"
            application_date = "NULL"
            deadline = "NULL"
            application_fee = "NULL"
            ATAS = "NULL"
            GPA = "NULL"
            average_score = "NULL"
            accredited_university = "NULL"
            Alevel = 'NULL'
            IB = "NULL"
            IELTS_L = "NULL"
            IELTS_S = "NULL"
            IELTS_R = 'NULL'
            IELTS_W = 'NULL'
            TOEFL = "NULL"
            TOEFL_L = 'NULL'
            TOEFL_S = "NULL"
            TOEFL_R = 'NULL'
            TOEFL_W = 'NULL'
            GRE = "NULL"
            GMAT = 'NULL'
            LSAT = "NULL"
            MCAT = "NULL"
            working_experience = 'NULL'
            interview = 'NULL'
            portfolio = 'NULL'
            application_documents = 'NULL'
            chinese_requirements = 'NULL'
            school_test = 'NULL'
            SATI = 'NULL'
            SATII = 'NULL'
            SAT_code = 'NULL'
            ACT = 'NULL'
            ACT_code = 'NULL'
            other = 'NULL'
            create_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


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

        except Exception as e:
            with open("./error/"+item['university']+item['degree_level']+".txt", 'w', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================")
            print("异常：", str(e))
            print("报错url：", response.url)

    # def parse(self, response):
    #     item = get_item(SchoolItem)
    #     item['university'] = "University"
    #     item['country'] = 'Australia'
    #     item['website'] = ''
    #     item['url'] = response.url
    #     print("===========================")
    #     print(response.url)
    #     try:
    #
    #         yield item
    #     except Exception as e:
    #         with open("./error/"+item['university']+item['degree_level']+".txt", 'w', encoding="utf-8") as f:
    #             f.write(str(e) + "\n" + response.url + "\n========================")
    #         print("异常：", str(e))
    #         print("报错url：", response.url)

