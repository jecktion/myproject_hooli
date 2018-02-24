
import scrapy
from school_2.items import HooliItem
import datetime
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import re
from w3lib.html import remove_tags


class PlymouthSpider(CrawlSpider):
    name = 'mastersportal_USA'
    allowed_domains = ['www.mastersportal.com']
    start_urls = ['https://www.mastersportal.com/ranking-country/82/united-states.html']

    rules = (
        Rule(LinkExtractor(allow=(r'.*'), restrict_xpaths=('//*[@id="RankingXCountryChart"]/table/tbody/tr/td/a')),callback='parse_item',follow=False),
        # Rule(LinkExtractor(allow=(r'.*'), restrict_xpaths=('')), follow=True),
        # Rule(LinkExtractor(allow=(r'.*'), restrict_xpaths=('//*[@id="LinkTrail"]/ul/li[4]/a')), callback='parse_item', follow=False),
    )

    def parse_item(self,response):
        print('==================================',response.url)
        item = HooliItem()

        url = response.url
        print(1,url)

        university = response.xpath('//*[@id="OrganisationHeader"]//h1').extract()[0]
        university = remove_tags(university)
        # university = ''.join(university)
        print(2,university)

        country = response.xpath('//*[@id="OrganisationHeader"]/article/header/div/span/span//text()').extract()[5:6]
        country = ''.join(country)
        print(3,country)

        city = response.xpath('//*[@id="OrganisationHeader"]/article/header/div/span/span//text()').extract()[1:4]
        city = ''.join(city)
        print(4,city)

        overview = response.xpath('//*[@id="ShortDescription"]//text()').extract()
        overview = ''.join(overview)
        print(5,overview)
        history_s = response.xpath('//*[@id="About"]//*[@class="RowWrapper"]//text()').extract()
        history_s = ''.join(history_s)
        try:
            if "History" in history_s:
                start = history_s.find("History")
                end = history_s.find("Education")
                history = history_s[start:end]
                item["history"] = history
            else:
                history = "NULL"
        except:
            history = '报错!'
        print(6,history)

        education_s = response.xpath('//*[@id="About"]//*[@class="RowWrapper"]//text()').extract()
        education_s = ''.join(education_s)
        try:
            if "Education" in education_s:
                start = education_s.find("Education")
                end = education_s.find("Research")
                education = education_s[start:end]
                item["education"] = education
            else:
                education = "NULL"
        except:
            education = '报错!'
        print(7,education)

        research_s = response.xpath('//*[@id="About"]//*[@class="RowWrapper"]//text()').extract()
        research_s = ''.join(research_s)
        try:
            if "Research" in research_s:
                start = research_s.find("Research")
                end = research_s.find("Career")
                research = research_s[start:end]
                item["research"] = research
            else:
                research = "NULL"
        except:
            research = '报错!'
        print(8,research)

        career_s = response.xpath('//*[@id="About"]//*[@class="RowWrapper"]//text()').extract()
        career_s = ''.join(career_s)
        try:
            if "Career" in career_s:
                start = career_s.find("Career")
                career = career_s[start:]
                item["career"] = career
            else:
                career = "NULL"
        except:
            career = "报错!"
        print(9,career)

        student_services_s = response.xpath('//*[@id="Services"]/*[@class="RowWrapper"]//text()').extract()
        student_services_s = ''.join(student_services_s)
        try:
            if "Student services" in student_services_s:
                start = student_services_s.find("Student services")
                end =  student_services_s.find("Housing services")
                student_services = student_services_s[start:end]
                item["student_services"] = student_services
            elif len(student_services_s) == 0:
                student_services = 'NULL'
            else:
                student_services = "NULL"
        except:
            student_services = '报错!'
        print(10,student_services)

        housing_services_s = response.xpath('//*[@id="Services"]/*[@class="RowWrapper"]//text()').extract()
        housing_services_s = ''.join(housing_services_s)
        try:
            if "Housing services" in housing_services_s:
                start = housing_services_s.find("Housing services")
                end = housing_services_s.find("Library services")
                housing_services = housing_services_s[start:end]
                item["housing_services"] = housing_services
            elif len(housing_services_s) == 0:
                housing_services = 'NULL'

            else:
                housing_services = "NULL"
        except:
            housing_services = '报错!'
        print(11,housing_services)

        library_services_s = response.xpath('//*[@id="Services"]/*[@class="RowWrapper"]//text()').extract()
        library_services_s = ''.join(library_services_s)
        try:
            if "Library services" in library_services_s:
                start = library_services_s.find("Library services")
                end = library_services_s.find("ICT services")
                library_services = library_services_s[start:end]
                item["library_services"] = library_services
            elif len(library_services_s) == 0:
                library_services = "NULL"
            else:
                library_services = "NULL"
        except:
            library_services = '报错!'
        print(12,library_services)


        ICT_services_s = response.xpath('//*[@id="Services"]/*[@class="RowWrapper"]//text()').extract()
        ICT_services_s = ''.join(ICT_services_s)
        try:
            if "ICT services" in ICT_services_s:
                start = ICT_services_s.find("ICT services")
                end = ICT_services_s.find("Medical services")
                ICT_services = ICT_services_s[start:end]
                item["ICT_services"] = ICT_services
            elif len(ICT_services_s) == 0:
                ICT_services = 'NULL'
            else:
                ICT_services = "NULL"
        except:
            ICT_services = '报错!'
        print(13,ICT_services)

        medical_services_s = response.xpath('//*[@id="Services"]/*[@class="RowWrapper"]//text()').extract()
        medical_services_s = ''.join(medical_services_s)
        try:
            if "Medical services" in medical_services_s:
                start = medical_services_s.find("Medical services")
                medical_services = medical_services_s[start:]
                item["medical_services"] = medical_services
            elif len(medical_services_s) == 0:
                medical_services = "NULL"
            else:
                medical_services = "NULL"
        except:
            medical_services = '报错!'
        print(14,medical_services)

        campus_life_s = response.xpath('//*[@id="StudentLife"]//text()').extract()
        campus_life_s = ''.join(campus_life_s)
        try:
            if "Campus life" in campus_life_s:
                start = campus_life_s.find("Campus life")
                end = campus_life_s.find("Sports facilities")
                campus_life = campus_life_s[start:end]
                item["campus_life"] = campus_life
            elif len(campus_life_s) == 0:
                campus_life = "NULL"
            else:
                campus_life = 'NULL'
        except:
            campus_life = '报错!'
        print(15,campus_life)

        sports_facilities_s = response.xpath('//*[@id="StudentLife"]/div//text()').extract()
        sports_facilities_s = ''.join(sports_facilities_s)
        try:
            if "Sports facilities " in sports_facilities_s:
                start = sports_facilities_s.find("Sports facilities ")
                end = sports_facilities_s.find("Student clubs ")
                sports_facilities = sports_facilities_s[start:end]
                item["sports_facilities"] = sports_facilities
            elif len(sports_facilities_s) == 0:
                sports_facilities = "NULL"
            else:
                sports_facilities = "NULL"
        except:
            sports_facilities = '报错!'

        print(16,sports_facilities)

        student_clubs_s = response.xpath('//*[@id="StudentLife"]/div//text()').extract()
        student_clubs_s = ''.join(student_clubs_s)
        try:
            if "Student clubs" in student_clubs_s:
                start = student_clubs_s.find("Student clubs")
                student_clubs = student_clubs_s[start:]
                item["student_clubs"] = student_clubs
            elif len(student_clubs_s) == 0:
                student_clubs = 'NULL'
            else:
                student_clubs = "NULL"
        except:
            student_clubs = '报错!'
        print(17,student_clubs)

        students_number_s = response.xpath('//*[@id="QuickFacts"]//span//text()').extract()
        students_number_s = ''.join(students_number_s)
        try:
            if "Students" in students_number_s:
                students_number = re.findall(r'\d+,\d+',students_number_s)
                students_number = ''.join(students_number)
            else:
                students_number = "NULL"
        except:
            students_number = "报错!"
        print(18,students_number)

        masters_s = response.xpath('//*[@id="QuickFacts"]//span//text()').extract()[2:4]
        masters_s = ''.join(masters_s)
        try:
            if "Masters" in masters_s:
                masters = re.findall('\d+',masters_s)
                masters = ''.join(masters)
            else:
                masters = "NULL"
        except:
            masters = "报错!"
        print(19,masters)

        rank_W_s = response.xpath('//*[@id="OrganisationRanking"]/div/div//text()').extract()
        rank_W_s = ''.join(rank_W_s)
        try:
            if "World University Rankings by Times Higher Education" in rank_W_s:
                rank_W = re.findall(r'#\d+ World University Rankings by Times Higher Education',rank_W_s)
                rank_W = ''.join(rank_W)
                rank_W = re.findall(r'#\d+',rank_W)
                rank_W = ''.join(rank_W)
            else:
                rank_W = "NULL"
        except:
            rank_W = "报错!"
        print(20,rank_W)

        rank_A_s = response.xpath('//*[@id="OrganisationRanking"]/div/div//text()').extract()
        rank_A_s = ''.join(rank_A_s)
        try:
            if "Academic Ranking of World Universities by Shanghai Jiao Tong University" in rank_A_s:
                rank_A = re.findall(r'#\d+ Academic Ranking of World Universities by Shanghai Jiao Tong University',rank_A_s)
                rank_A = ''.join(rank_A)
                rank_A = re.findall(r'#\d+',rank_A)
                rank_A = ''.join(rank_A)
            else:
                rank_A = "NULL"
        except:
            rank_A = "报错!"
        print(21,rank_A)

        other = 'NULL'

        create_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(22, create_time)

        item["url"] = url
        item["university"] = university
        item["country"] = country
        item["city"] = city
        item["overview"] = overview
        item["history"] = history
        item["education"] = education
        item["rank_W"] = rank_W
        item["rank_A"] = rank_A
        item["masters"] = masters
        item["research"] = research
        item["career"] = career
        item["student_services"] = student_services
        item["housing_services"] = housing_services
        item["library_services"] = library_services
        item["ICT_services"] = ICT_services
        item["medical_services"] = medical_services
        item["campus_life"] = campus_life
        item["sports_facilities"] = sports_facilities
        item["student_clubs"] = student_clubs
        item["students_number"] = students_number
        item["other"] = other
        item["create_time"] = create_time

        yield item

