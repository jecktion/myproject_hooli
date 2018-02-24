

import scrapy
from school_1.items import HooliItem
import datetime
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import re

class PlymouthSpider(CrawlSpider):
    name = 'gold_gd'
    allowed_domains = ['www.gold.ac.uk']
    start_urls = []
    base_url = 'https://www.gold.ac.uk/pg/%s'

    Lists = ['/cert-humanistic-counselling/',
'/ma-advanced-social-work/',
'/ma-anthropology-cultural-politics/',
'/ma-anthropology-museum-practice/',
'/ma-applied-anthropology-community-youth-work/',
'/ma-applied-anthropology-community-arts/',
'/ma-applied-anthropology-community-development/',
'/ma-applied-theatre/',
'/ma-art-politics/',
'/ma-art-psychotherapy/',
'/ma-artists-film/',
'/ma-arts-admin-cultural-policy/',
'/ma-arts-admin-cultural-policy-music-pathway/',
'/ma-arts-learning/',
'/ma-black-british-writing/',
'/ma-brands-communication-culture/',
'/ma-childrens-literature/',
'/ma-childrens-literature-illustration/',
'/ma-cities-society/',
'/ma-computational-arts/',
'/ma-computer-games-art-design/',
'/ma-contemporary-art-theory/',
'/ma-counselling/',
'/ma-creative-cultural-entrepreneurship/',
'/ma-creative-cultural-entrepreneurship-comp/',
'/ma-creative-cultural-entrepreneurship-design/',
'/ma-creative-cultural-entrepreneurship-fashion/',
'/ma-creative-cultural-entrepreneurship-leadership/',
'/ma-creative-cultural-entrepreneurship-media/',
'/ma-creative-cultural-entrepreneurship-music/',
'/ma-creative-cultural-entrepreneurship-theatre/',
'/ma-creative-life-writing/',
'/ma-creative-writing-education/',
'/ma-critical-creative-analysis/',
'/ma-cultural-policy-relations/',
'/ma-cultural-studies/',
'/ma-culture-industry/',
'/ma-dance-movement-psychotherapy/',
'/ma-design-expanded-practice/',
'/ma-digital-media-technology-cultural-form/',
'/ma-dramaturgy-writing-performance/',
'/ma-education-culture-language-identity/',
'/ma-events-experience-management/',
'/ma-film-screen-studies/',
'/ma-filmmaking-cinematography/',
'/ma-filmmaking-directing-fiction/',
'/ma-filmmaking-editing/',
'/ma-filmmaking-producing/',
'/ma-filmmaking-screen-documentary/',
'/ma-filmmaking-sound-recording-design/',
'/ma-filmmaking/',
'/ma-gender-media-culture/',
'/ma-global-media-transnational-communications/',
'/ma-history/',
'/ma-human-rights/',
'/ma-independent-games-design/',
'/ma-international-relations/',
'/ma-journalism/',
'/ma-literary-studies/',
'/ma-literary-studies/american-literature-and-culture/',
'/ma-literary-studies/comparative-literature-and-criticism/',
'/ma-literary-studies/critical-theory/',
'/ma-literary-studies/literature-of-the-caribbean-and-its-diasporas/',
'/ma-literary-studies/modern-literature/',
'/ma-literary-studies/romantic-and-victorian-literature-and-culture/',
'/ma-literary-studies/shakespeare-early-modern/',
'/ma-luxury-brand-management/',
'/ma-media-communications/',
'/ma-multilingualism-linguistics-education/',
'/ma-music-contemporary-music-studies/',
'/ma-music-ethnomusicology/',
'/ma-music-general/',
'/ma-music-historical-musicology/',
'/ma-music-popular-music-research/',
'/ma-music/',
'/ma-musical-theatre/',
'/ma-performance-culture/',
'/ma-performance-making/',
'/ma-photography-urban-cultures/',
'/ma-photography-electronic-arts/',
'/ma-political-communications/',
'/ma-politics-development-global-south/',
'/ma-postcolonial-culture-global-policy/',
'/ma-practice-education/',
'/ma-promotional-media/',
'/ma-queer-history/',
'/ma-race-media-social-justice/',
'/ma-radio/',
'/ma-research-architecture/',
'/ma-script-writing/',
'/ma-social-anthropology/',
'/ma-social-entrepreneurship/',
'/ma-social-research/',
'/ma-social-work/',
'/ma-sociocultural-linguistics/',
'/ma-tv-journalism/',
'/ma-tourism-cultural-policy/',
'/ma-translation/',
'/ma-understanding-domestic-violence-and-sexual-abuse/',
'/cpd-understanding-domestic-violence-and-sexual-abuse/',
'/ma-visual-anthropology/',
'/ma-visual-sociology/',
'/ma-world-theatres/',
'/cpd-practice-education/',
'/ma-digital-journalism/',
'/mfa-computational-arts/',
'/mfa-curating/',
'/mfa-fine-art/',
'/mmus-composition/',
'/mmus-creative-practice/',
'/mmus-performance/',
'/mmus-popular-music/',
'/mmus-sonic-arts/',
'/mphil-phd-anthropology/',
'/mphil-phd-art-practice-learning/',
'/mphil-phd-art-psychotherapy/',
'/mphil-phd-art/',
'/mphil-phd-arts-computational-tech/',
'/mphil-phd-community-youth-work/',
'/mphil-phd-computer-science/',
'/mphil-phd-creative-writing/',
'/mphil-phd-cultural-studies/',
'/mphil-phd-curating/',
'/mphil-phd-curatorial-knowledge/',
'/mphil-phd-design/',
'/mphil-phd-drama/',
'/mphil-phd-education/',
'/mphil-phd-english-comparative-literature/',
'/mphil-phd-history/',
'/mphil-phd-intelligent-games/',
'/mphil-phd-management/',
'/mphil-phd-media-communications/',
'/mphil-phd-music/',
'/mphil-phd-politics/',
'/mphil-phd-psychology-ims/',
'/mphil-phd-psychology/',
'/mphil-phd-religious-studies/',
'/mphil-phd-research-architecture/',
'/mphil-phd-social-work/',
'/mphil-phd-sociology/',
'/mphil-phd-creative-cultural-entrepreneurship/',
'/mphil-phd-visual-anthropology/',
'/mphil-phd-visual-culture/',
'/mphil-phd-visual-sociology/',
'/mphil-phd-counselling-psychotherapy/',
'/mres-anthropology/',
'/mres-curatorial-knowledge/',
'/mres-english/',
'/mres-filmmaking-photography-electronic-arts/',
'/mres-history/',
'/mres-media-communications/',
'/mres-research-methods-psychology/',
'/mres-visual-anthropology/',
'/mres-visual-cultures/',
'/msc-cognitive-clinical-neuroscience/',
'/msc-computational-cognitive-neuroscience/',
'/msc-consumer-behaviour/',
'/msc-data-science/',
'/msc-forensic-psychology/',
'/msc-clinical-psychology-health-services/',
'/msc-management-innovation/',
'/msc-marketing-technology/',
'/msc-music-mind-brain/',
'/msc-occupational-psychology/',
'/msc-psychology-arts-neuroaesthetics-creativity/',
'/msc-psychology-social-relations/',
'/msc-cognitive-behavioural-therapy/',
'/pgcert-museums-galleries-entrepreneurship/',
'/phd-by-publication/',
]

    for i in Lists:
        fullurl = base_url % i
        start_urls.append(fullurl)

    rules = (
        Rule(LinkExtractor(allow=(r'.*'), restrict_xpaths=('//div[@class="wrapper clearfix"]/footer/nav/ul/li/a')), follow=True),
        # Rule(LinkExtractor(allow=r'www.gold.ac.uk/course-finder/results/\?collection=goldsmiths-courses&sort=Title&f.Level%7Clevel=Postgraduate&start_rank=\d+'), follow=True),
        # Rule(LinkExtractor(allow=(r'.*'), restrict_xpaths=('//div[@class="teaser__body media__body"]/h3/a')),follow=True),
        Rule(LinkExtractor(allow=r'pg/.*'),callback='parse_item', follow=False),
    )

    def parse_item(self,response):
        print('==================================',response.url)
        item = HooliItem()

        url = response.url
        print(1,url)

        university = 'Goldsmiths UNIVERSITY OF LONDON'
        print(2,university)

        department_str = response.xpath('//div[@class="hero__content"]/ul[@class="split-list split-list--hero"]/li//text()').extract()
        department_str = ''.join(department_str)
        try:
            if "Department" in department_str:
                start = department_str.find("Department")
                department = department_str[start:]
                department = department[:50]
                item["department"] = department
            else:
                department = "NULL"
        except:
            department = "报错"
        print(3,department)

        country = 'UK'
        city = 'NULL'

        programme = response.xpath('//div[@class="hero__content"]/h1/text()').extract()
        Programme = ''.join(programme)
        print(4,Programme)

        ucas_code = 'NULL'
        # Master = ''.join(Master)

        degree_type = response.xpath('//div[@class="hero__content"]/h1/text()').extract()
        degree_type = ''.join(degree_type)
        print(5,degree_type)
        degree_level = '1'

        website = 'https://www.gold.ac.uk/pg'

        start_date = 'NULL'
        # start_date = response.xpath('//div[@class="rich-content rich-content-section full-wrap"]/p[6]/text()').extract()
        # start_date = ''.join(start_date)
        # print(5,start_date)

        overview = response.xpath('//div[@class="rich-content rich-content-section full-wrap"]//text()').extract()
        overview = ''.join(overview).replace('\r\n', '')
        print(6, overview)

        mode = 'NULL'






        duration = response.xpath('//div[@class="hero__content"]/ul[@class="split-list split-list--hero"]/li/text()').extract()
        duration = ''.join(duration).replace('\r\n','')
        # Duration = Duration.replace('   ','')
        print(7,duration)

        modules = response.xpath('//div[@class="rich-content rich-content-section full-wrap"]//text()').extract()
        modules = ''.join(modules).replace('\r\n','')
        modules = modules.replace('\n','')
        print(8,modules)

        teaching = 'NULL'

        assessment = response.xpath('//div[@class="rich-content rich-content-section full-wrap"]//text()').extract()
        assessment = ''.join(assessment).replace('\r\n','')
        print(9, assessment)

        career = response.xpath('//div[@class="rich-content rich-content-section full-wrap"]//text()').extract()
        career = ''.join(career).replace('\r\n', '')
        print(10, career)

        application_date = 'NULL'

        deadline = 'NULL'

        application_fee = 'NULL'

        tuition_fee= 'NULL'
        # tuition_fee = ''.join(tuition_fee).replace('\r\n','')
        # tuition_fee = tuition_fee.replace('   ','')
        # print(12, Tuition_Fee)

        location = 'NULL'
        # location = ''.join(location)
        # print(13,location)

        accredited_university = 'NULL'
        ATAS = 'NULL'

        GPA = 'NULL'


        IELTS_str = response.xpath('//div[@class="rich-content rich-content-section full-wrap"]/p//text()').extract()
        IELTS_str = ''.join(IELTS_str).replace('\r\n','')
        # IELTS = re.findall('(IELTS:|IELTS)? (.*){0,5} \d?.\d? .{0,70}',IELTS)
        try:
            if "IELTS" in IELTS_str:
                start = IELTS_str.find("IELTS")
                end = IELTS_str.find("If you need")
                IELTS = IELTS_str[start:end]
                # IELTS = IELTS[:80]
                item["IELTS"] = IELTS

            else:
                IELTS = 'NULL'
        except:
            IELTS = '报错'
        print(11, IELTS)

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

        average_score = 'NULL'

        Alevel = 'NULL'

        IB = 'NULL'

        working_experience = 'NULL'

        interview = 'NULL'

        portfolio = 'NULL'

        application_documents = 'NULL'

        how_to_apply = 'NULL'

        entry_requirements = response.xpath('//div[@class="rich-content rich-content-section full-wrap"]/ul/li/text()').extract()
        entry_requirements = ''.join(entry_requirements).replace('\n','')
        # EntryRequirements = EntryRequirements.replace(' ','')
        print(12,entry_requirements)

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




