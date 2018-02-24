

import scrapy
from school_1.items import HooliItem
import datetime
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import re

class PlymouthSpider(CrawlSpider):
    name = 'royalholloway'
    allowed_domains = ['www.royalholloway.ac.uk']
    # start_urls = ['https://www.royalholloway.ac.uk/courses/undergraduate/home.aspx']
    start_urls = []
    base_url = 'https://www.royalholloway.ac.uk/%s'

    Lists = ['/courses/undergraduate/management/accounting-and-finance.aspx',
'/courses/undergraduate/management/accounting-and-finance-year-in-business.aspx',
'/courses/undergraduate/english/american-literature-and-creative-writing.aspx',
'/courses/2018/undergraduate/english/american-literature-and-creative-writing.aspx',
'/courses/undergraduate/classics/ancient-and-medieval-history.aspx',
'/courses/undergraduate/classics/ancient-history.aspx',
'/courses/2018/undergraduate/classics/ancient-history.aspx',
'/courses/undergraduate/classics/ancient-history-and-philosophy.aspx',
'/courses/undergraduate/classics/ancient-history-with-philosophy.aspx',
'/courses/undergraduate/psychology/applied-psychology.aspx',
'/courses/undergraduate/physics/astrophysics-msci.aspx',
'/courses/undergraduate/physics/astrophysics-bsc.aspx',
'/courses/undergraduate/biological-sciences/biochemistry.aspx',
'/courses/undergraduate/biological-sciences/biology.aspx',
'/courses/undergraduate/biological-sciences/biomedical-sciences.aspx',
'/courses/undergraduate/management/business-and-management.aspx',
'/courses/undergraduate/management/business-and-management-year-in-business.aspx',
'/courses/undergraduate/classics/classical-archaeology-and-ancient-history.aspx',
'/courses/undergraduate/classics/classical-studies.aspx',
'/courses/undergraduate/classics/classical-studies-and-comparative-literature-and-culture.aspx',
'/courses/undergraduate/classics/classical-studies-and-drama.aspx',
'/courses/undergraduate/classics/classical-studies-and-philosophy.aspx',
'/courses/undergraduate/classics/classical-studies-with-philosophy.aspx',
'/courses/undergraduate/classics/classics.aspx',
'/courses/undergraduate/classics/classics-and-philosophy.aspx',
'/courses/undergraduate/classics/classics-with-philosophy.aspx',
'/courses/undergraduate/mllc/comparative-literature-and-culture.aspx',
'/courses/undergraduate/mllc/comparative-literature-and-culture-and-drama.aspx',
'/courses/undergraduate/mllc/comparative-literature-and-culture-and-english.aspx',
'/courses/undergraduate/mllc/comparative-literature-and-culture-and-philosophy.aspx',
'/courses/undergraduate/mllc/comparative-literature-and-culture-with-history-of-art-and-visual-culture.aspx',
'/courses/undergraduate/mllc/comparative-literature-and-culture-with-international-film.aspx',
'/courses/undergraduate/mllc/comparative-literature-and-culture-with-philosophy.aspx',
'/courses/undergraduate/computer-science/computer-science-bsc.aspx',
'/courses/undergraduate/computer-science/computer-science-msci.aspx',
'/courses/undergraduate/computer-science/computer-science-artificial-intelligence-msci.aspx',
'/courses/undergraduate/computer-science/computer-science-artificial-intelligence.aspx',
'/courses/undergraduate/computer-science/computer-science-artificial-intelligence-with-a-year-in-industry-msci.aspx',
'/courses/undergraduate/computer-science/computer-science-artificial-intelligence-with-a-year-in-industry.aspx',
'/courses/undergraduate/computer-science/computer-science-distributed-networked-systems-msci.aspx',
'/courses/undergraduate/computer-science/computer-science-distributed-networked-systems.aspx',
'/courses/undergraduate/computer-science/computer-science-distributed-networked-systems-with-a-year-in-industry-msci.aspx',
'/courses/undergraduate/computer-science/computer-science-distributed-networked-systems-with-a-year-in-industry.aspx',
'/courses/undergraduate/computer-science/computer-science-information-security.aspx',
'/courses/undergraduate/computer-science/computer-science-information-security-msci.aspx',
'/courses/undergraduate/computer-science/computer-science-information-security-with-a-year-in-industry.aspx',
'/courses/undergraduate/computer-science/computer-science-information-security-with-a-year-in-industry-msci.aspx',
'/courses/undergraduate/computer-science/computer-science-software-engineering.aspx',
'/courses/undergraduate/computer-science/computer-science-software-engineering-msci.aspx',
'/courses/undergraduate/computer-science/computer-science-software-engineering-with-a-year-in-industry-msci.aspx',
'/courses/undergraduate/computer-science/computer-science-software-engineering-with-a-year-in-industry.aspx',
'/courses/undergraduate/computer-science/computer-science-and-mathematics.aspx',
'/courses/undergraduate/computer-science/computer-science-year-in-industry.aspx',
'/courses/undergraduate/computer-science/computer-science-year-in-industry-msci.aspx',
'/courses/undergraduate/law/criminology-and-psychology.aspx',
'/courses/undergraduate/law/criminology-and-psychology-with-a-year-in-industry.aspx',
'/courses/undergraduate/law/criminology-and-sociology.aspx',
'/courses/undergraduate/law/criminology-and-sociology-with-a-year-in-industry.aspx',
'/courses/undergraduate/drama-theatre/dance.aspx',
'/courses/undergraduate/earth-sciences/digital-geosciences.aspx',
'/courses/undergraduate/media-arts/digital-media-culture-technology-ba.aspx',
'/courses/undergraduate/media-arts/digital-media-culture-technology-bsc.aspx',
'/courses/undergraduate/drama-theatre/drama-and-creative-writing.aspx',
'/courses/undergraduate/drama-theatre/drama-and-dance.aspx',
'/courses/undergraduate/drama-theatre/drama-and-music.aspx',
'/courses/undergraduate/drama-theatre/drama-and-philosophy.aspx',
'/courses/undergraduate/drama-theatre/drama-and-theatre-studies.aspx',
'/courses/undergraduate/drama-theatre/drama-with-film.aspx',
'/courses/undergraduate/drama-theatre/drama-with-philosophy.aspx',
'/courses/undergraduate/biological-sciences/ecology-and-conservation.aspx',
'/courses/undergraduate/economics/economics.aspx',
'/courses/undergraduate/economics/economics-and-management.aspx',
'/courses/undergraduate/economics/economics-and-management-with-a-year-in-business.aspx',
'/courses/undergraduate/economics/economics-and-mathematics.aspx',
'/courses/undergraduate/economics/economics-and-mathematics-with-a-year-in-business.aspx',
'/courses/undergraduate/economics/economics-with-a-year-in-business.aspx',
'/courses/undergraduate/economics/economics-with-french.aspx',
'/courses/undergraduate/economics/economics-with-german.aspx',
'/courses/undergraduate/economics/economics-with-italian.aspx',
'/courses/undergraduate/economics/economics-with-music.aspx',
'/courses/undergraduate/economics/economics-with-political-studies.aspx',
'/courses/undergraduate/economics/economics-with-political-studies-with-a-year-in-business.aspx',
'/courses/undergraduate/economics/economics-with-spanish.aspx',
'/courses/undergraduate/economics/economics-politics-and-international-relations.aspx',
'/courses/undergraduate/economics/economics-politics-and-international-relations-with-a-year-in-business.aspx',
'/courses/undergraduate/electronic-engineering/electronic-engineering-beng.aspx',
'/courses/undergraduate/electronic-engineering/electronic-engineering-meng.aspx',
'/courses/undergraduate/electronic-engineering/electronic-engineering-with-a-year-in-industry-beng.aspx',
'/courses/undergraduate/electronic-engineering/electronic-engineering-with-a-year-in-industry-meng.aspx',
'/courses/undergraduate/english/english.aspx',
'/courses/undergraduate/english/english-and-american-literature.aspx',
'/courses/undergraduate/english/english-and-classical-studies.aspx',
'/courses/undergraduate/english/english-and-creative-writing.aspx',
'/courses/undergraduate/english/english-and-drama.aspx',
'/courses/undergraduate/english/english-and-film-studies.aspx',
'/courses/undergraduate/english/english-and-history.aspx',
'/courses/undergraduate/english/english-and-latin.aspx',
'/courses/undergraduate/english/english-and-philosophy.aspx',
'/courses/undergraduate/english/english-with-philosophy.aspx',
'/courses/undergraduate/earth-sciences/environmental-geology.aspx',
'/courses/undergraduate/earth-sciences/environmental-geology-with-a-year-in-industry.aspx',
'/courses/undergraduate/earth-sciences/environmental-geoscience.aspx',
'/courses/undergraduate/earth-sciences/environmental-geoscience-with-a-year-in-industry.aspx',
'/courses/undergraduate/earth-sciences/environmental-geoscience-with-an-international-year.aspx',
'/courses/undergraduate/pir/european-and-international-studies-french.aspx',
'/courses/undergraduate/pir/european-and-international-studies-german.aspx',
'/courses/undergraduate/pir/european-and-international-studies-italian.aspx',
'/courses/undergraduate/pir/european-and-international-studies-spanish.aspx',
'/courses/undergraduate/physics/experimental-physics-msci.aspx',
'/courses/undergraduate/physics/experimental-physics-bsc.aspx',
'/courses/undergraduate/media-arts/film-studies.aspx',
'/courses/undergraduate/media-arts/film-studies-with-philosophy.aspx',
'/courses/undergraduate/media-arts/film-television-and-digital-production.aspx',
'/courses/undergraduate/economics/finance-and-mathematics.aspx',
'/courses/undergraduate/economics/finance-and-mathematics-with-a-year-in-business.aspx',
'/courses/undergraduate/economics/financial-and-business-economics.aspx',
'/courses/undergraduate/economics/financial-and-business-economics-with-a-year-in-business.aspx',
'/courses/undergraduate/geography/geography-bsc.aspx',
'/courses/undergraduate/geography/geography-ba.aspx',
'/courses/undergraduate/earth-sciences/geology.aspx',
'/courses/undergraduate/earth-sciences/geology-with-a-year-in-industry.aspx',
'/courses/undergraduate/earth-sciences/geoscience.aspx',
'/courses/undergraduate/earth-sciences/geoscience-with-a-year-in-industry.aspx',
'/courses/undergraduate/earth-sciences/geoscience-with-a-year-of-international-study.aspx',
'/courses/undergraduate/classics/greek.aspx',
'/courses/undergraduate/history/history.aspx',
'/courses/undergraduate/history/history-and-music.aspx',
'/courses/undergraduate/history/history-and-philosophy.aspx',
'/courses/undergraduate/mllc/history-of-art-and-visual-culture-and-comparative-literature-and-culture.aspx',
'/courses/undergraduate/history/history-politics-and-international-relations.aspx',
'/courses/undergraduate/geography/human-geography.aspx',
'/courses/undergraduate/pir/international-relations.aspx',
'/courses/undergraduate/classics/latin.aspx',
'/courses/undergraduate/law/law.aspx',
'/courses/undergraduate/law/law-senior-status.aspx',
'/courses/undergraduate/law/law-with-a-year-in-industry.aspx',
'/courses/undergraduate/law/law-with-criminology.aspx',
'/courses/undergraduate/law/law-with-criminology-with-a-year-in-industry.aspx',
'/courses/undergraduate/law/law-with-sociology.aspx',
'/courses/undergraduate/law/law-with-sociology-with-a-year-in-industry.aspx',
'/courses/undergraduate/mllc/liberal-arts.aspx',
'/courses/undergraduate/mllc/liberal-arts-with-a-language-year-abroad.aspx',
'/courses/undergraduate/mllc/liberal-arts-with-an-international-year.aspx',
'/courses/undergraduate/management/management-with-accounting.aspx',
'/courses/undergraduate/management/management-with-accounting-year-in-business.aspx',
'/courses/undergraduate/management/management-with-sustainability.aspx',
'/courses/undergraduate/management/management-with-sustainability-year-in-business.aspx',
'/courses/undergraduate/management/management-with-digital-innovation.aspx',
'/courses/undergraduate/management/management-with-digital-innovation-year-in-business.aspx',
'/courses/undergraduate/management/management-with-entrepreneurship.aspx',
'/courses/undergraduate/management/management-with-entrepreneurship-year-in-business.aspx',
'/courses/undergraduate/management/management-with-human-resources.aspx',
'/courses/undergraduate/management/management-with-human-resources-year-in-business.aspx',
'/courses/undergraduate/management/management-with-international-business.aspx',
'/courses/undergraduate/management/management-with-international-business-year-in-business.aspx',
'/courses/undergraduate/management/management-with-marketing.aspx',
'/courses/undergraduate/management/management-with-marketing-year-in-business.aspx',
'/courses/undergraduate/management/management-with-mathematics.aspx',
'/courses/undergraduate/mathematics/mathematical-studies.aspx',
'/courses/undergraduate/mathematics/mathematics-msci.aspx',
'/courses/undergraduate/mathematics/mathematics.aspx',
'/courses/undergraduate/mathematics/mathematics-and-management.aspx',
'/courses/undergraduate/mathematics/mathematics-and-music.aspx',
'/courses/undergraduate/mathematics/mathematics-and-physics.aspx',
'/courses/undergraduate/mathematics/mathematics-and-physics-msci.aspx',
'/courses/undergraduate/mathematics/mathematics-with-french.aspx',
'/courses/undergraduate/mathematics/mathematics-with-german.aspx',
'/courses/undergraduate/mathematics/mathematics-with-italian.aspx',
'/courses/undergraduate/mathematics/mathematics-with-management.aspx',
'/courses/undergraduate/mathematics/mathematics-with-philosophy.aspx',
'/courses/undergraduate/mathematics/mathematics-with-spanish.aspx',
'/courses/undergraduate/mathematics/mathematics-with-statistics.aspx',
'/courses/undergraduate/biological-sciences/medical-biochemistry.aspx',
'/courses/undergraduate/history/modern-and-contemporary-history.aspx',
'/courses/undergraduate/mllc/modern-languages.aspx',
'/courses/undergraduate/mllc/modern-languages-and-classical-studies.aspx',
'/courses/undergraduate/mllc/modern-languages-and-comparative-literature-and-culture.aspx',
'/courses/undergraduate/mllc/modern-languages-and-drama.aspx',
'/courses/undergraduate/mllc/modern-languages-and-english.aspx',
'/courses/undergraduate/mllc/modern-languages-and-greek.aspx',
'/courses/undergraduate/mllc/modern-languages-and-history.aspx',
'/courses/undergraduate/mllc/modern-languages-and-history-of-art-and-visual-culture.aspx',
'/courses/undergraduate/mllc/modern-languages-and-latin.aspx',
'/courses/undergraduate/mllc/modern-languages-and-management.aspx',
'/courses/undergraduate/mllc/modern-languages-and-music.aspx',
'/courses/undergraduate/mllc/modern-languages-and-philosophy.aspx',
'/courses/undergraduate/mllc/modern-languages-and-translation-studies.aspx',
'/courses/undergraduate/mllc/modern-languages-with-history-of-art-and-visual-culture.aspx',
'/courses/undergraduate/mllc/modern-languages-with-international-film.aspx',
'/courses/undergraduate/mllc/modern-languages-with-international-relations.aspx',
'/courses/undergraduate/mllc/modern-languages-with-mathematics.aspx',
'/courses/undergraduate/mllc/modern-languages-with-music.aspx',
'/courses/undergraduate/mllc/modern-languages-with-philosophy.aspx',
'/courses/undergraduate/mllc/modern-languages-with-translation-studies.aspx',
'/courses/undergraduate/biological-sciences/molecular-biology.aspx',
'/courses/undergraduate/music/music.aspx',
'/courses/undergraduate/music/music-and-english.aspx',
'/courses/undergraduate/music/music-and-philosophy.aspx',
'/courses/undergraduate/music/music-with-french.aspx',
'/courses/undergraduate/music/music-with-german.aspx',
'/courses/undergraduate/music/music-with-italian.aspx',
'/courses/undergraduate/music/music-with-philosophy.aspx',
'/courses/undergraduate/music/music-with-political-studies.aspx',
'/courses/undergraduate/music/music-with-spanish.aspx',
'/courses/undergraduate/earth-sciences/petroleum-geology.aspx',
'/courses/undergraduate/philosophy/philosophy.aspx',
'/courses/undergraduate/geography/physical-geography.aspx',
'/courses/undergraduate/physics/physics-msci.aspx',
'/courses/undergraduate/physics/physics-bsc.aspx',
'/courses/undergraduate/physics/physics-with-music.aspx',
'/courses/undergraduate/physics/physics-with-particle-physics-msci.aspx',
'/courses/undergraduate/physics/physics-with-particle-physics-bsc.aspx',
'/courses/undergraduate/physics/physics-with-philosophy.aspx',
'/courses/undergraduate/pir/politics.aspx',
'/courses/undergraduate/pir/politics-and-international-relations.aspx',
'/courses/undergraduate/pir/politics-and-international-relations-and-philosophy.aspx',
'/courses/undergraduate/pir/politics-with-philosophy.aspx',
'/courses/undergraduate/economics/politics-philosophy-and-economics.aspx',
'/courses/undergraduate/psychology/psychology-msci.aspx',
'/courses/undergraduate/psychology/psychology.aspx',
'/courses/undergraduate/psychology/psychology-clinical-and-cognitive-neuroscience.aspx',
'/courses/undergraduate/psychology/psychology-clinical-psychology-and-mental-health.aspx',
'/courses/undergraduate/psychology/psychology-development-and-developmental-disorders.aspx',
'/courses/undergraduate/physics/theoretical-physics-bsc.aspx',
'/courses/undergraduate/physics/theoretical-physics-msci.aspx',
'/courses/undergraduate/mllc/translation-studies.aspx',
'/courses/undergraduate/mllc/translation-studies-with-a-year-abroad.aspx',
'/courses/undergraduate/mllc/translation-studies-and-comparative-literature-and-culture.aspx',
'/courses/undergraduate/mllc/translation-studies-and-comparative-literature-and-culture-with-a-year-abroad.aspx',
'/courses/undergraduate/mllc/translation-studies-and-history-of-art-and-visual-culture.aspx',
'/courses/undergraduate/mllc/translation-studies-and-history-of-art-and-visual-culture-with-a-year-abroad.aspx',
'/courses/undergraduate/mllc/translation-studies-with-history-of-art-and-visual-culture.aspx',
'/courses/undergraduate/mllc/translation-studies-with-history-of-art-and-visual-culture-with-a-year-abroad.aspx',
'/courses/undergraduate/mllc/translation-studies-with-international-film.aspx',
'/courses/undergraduate/mllc/translation-studies-with-international-film-with-a-year-abroad.aspx',
'/courses/undergraduate/biological-sciences/zoology.aspx',]

    for i in Lists:
        fullurl = base_url % i
        start_urls.append(fullurl)

    rules = (
        Rule(LinkExtractor(allow=r'www.royalholloway.ac.uk/courses/undergraduate/home.aspx\?GenericList_AtoZLetter=[A-Z]'),follow=True),
        Rule(LinkExtractor(allow=r'/courses/undergraduate/.*\.aspx'), callback='parse_item', follow=False),
    )

    def parse_item(self,response):
        print('==================================',response.url)
        item = HooliItem()

        url = response.url
        print(1,url)
        university = "royalholloway"
        print(2,university)

        department = response.xpath('//div[@id="details"]//a/div/text()').extract()
        department = ''.join(department)
        print(3,department)

        country = 'UK'
        city = 'NULL'
        website = 'https://www.royalholloway.ac.uk'

        programme = response.xpath('//div[@class="sys_large-col"]/h1/text()').extract()
        programme = ''.join(programme)
        print(4,programme)

        ucas_code = response.xpath('//div[@id="details"]/table/tbody/tr/td/div/text()').extract()
        ucas_code = ' '.join(ucas_code)
        print(5, ucas_code)

        degree_level = '0'

        degree_type = response.xpath('//div[@class="sys_large-col"]/h1/text()').extract()
        degree_type = ''.join(degree_type)
        try:
            if "BSc" in degree_type:
                degree_type = 'Bsc'
            elif "MSc" in degree_type:
                degree_type = "MSc"
            elif "BA" in degree_type:
                degree_type = 'BA'
            elif "MNSW" in degree_type:
                degree_type = 'MNSW'
            elif "PGCert" in degree_type:
                degree_type = 'PGCert'
            elif "MBA" in degree_type:
                degree_type = 'MBA'
            elif "MA" in degree_type:
                degree_type = 'MA'
            elif "MComp" in degree_type:
                degree_type = 'MComp'
            elif "PhD" in degree_type:
                degree_type = 'PhD'
            elif "FdA" in degree_type:
                degree_type = 'FdA'
            elif "PGCE" in degree_type:
                degree_type = 'PGCE'
            elif "IFP" in degree_type:
                degree_type = 'IFP'
            elif "LLB" in degree_type:
                degree_type = 'LLB'
            elif "MHealth Res" in degree_type:
                degree_type = 'MHealth Res'
            elif "MRes" in degree_type:
                degree_type = 'MRes'
            elif "MMed" in degree_type:
                degree_type = 'MMed'
            elif "MSci" in degree_type:
                degree_type = 'MSci'
            elif "MCh" in degree_type:
                degree_type = 'MCh'
            elif "LLM" in degree_type:
                degree_type = "LLM"
            elif "Y2QF" in degree_type:
                degree_type = "Y2QF"
            elif "Y2QG" in degree_type:
                degree_type = "Y2QG"
            else:
                degree_type = 'Ordinary degree'
        except:
            degree_type = "NULL"
        print(6,degree_type)

        start_date = response.xpath('//div[@id="details"]/table/tbody/tr/td/div/text()').extract()
        start_date = ' '.join(start_date)
        print(7, start_date)

        overview = response.xpath('//div[@id="tab-1"]/p/text()').extract()
        overview = ' '.join(overview)
        print(8, overview)

        mode = 'NULL'


        duration = response.xpath('//div[@id="details"]/table/tbody/tr/td/div/text()').extract()
        duration = ' '.join(duration)
        print(9, duration)

        modules = response.xpath('//div[@id="tab-2"]//text()').extract()
        modules = ' '.join(modules).replace('\n', '')
        print(10,modules)

        teaching = 'NULL'

        assessment = response.xpath('//div[@id="tab-3"]//text()').extract()
        assessment = ' '.join(assessment).replace('\n', '')
        assessment = str(assessment)
        print(11, assessment)

        career = response.xpath('//div[@id="tab-5"]//text()').extract()
        career = ''.join(career).replace('\n', '')
        career = str(career)
        print(12, career)

        application_date = 'NULL'

        deadline = 'NULL'

        application_fee = 'NULL'

        tuition_fee_s = response.xpath('//div[@id="tab-6"]/p[2]/text()').extract()
        tuition_fee_s = ''.join(tuition_fee_s)
        tuition_fee_s = self.getTuition_fee(tuition_fee_s)
        try:
            if tuition_fee_s > 0:
                tuition_fee = tuition_fee_s
            else:
                tuition_fee = 'NULL'
        except:
            tuition_fee = '报错!'

        print(13, tuition_fee)

        location = 'NULL'

        ATAS = 'NULL'
        GPA = 'NULL'

        average_score = 'NULL'

        accredited_university = 'NULL'

        Alevel = response.xpath('//div[@id="year1"]/div/table/tbody/tr/td/p/text()').extract()
        Alevel = ' '.join(Alevel)
        Alevel = re.findall('[A-Z+?]{3}-[A-Z+?]{3}|[A-Z+?]{3}',Alevel)
        Alevel = ''.join(Alevel)
        print(14,Alevel)

        IB = 'NULL'
        
        IELTS_s = response.xpath('//div[@id="intsubtext"]//p/text()').extract()
        IELTS_s = ' '.join(IELTS_s)
        try:
            if "IELTS" in IELTS_s:
                start = IELTS_s.find("IELTS")
                IELTS = IELTS_s[start:]
                IELTS = IELTS[:100]
                item["IELTS"] = IELTS
            else:
                IELTS = "NULL"
        except:
            IELTS = "报错!"

        print(15,IELTS)

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

        entry_requirements = 'NULL'
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
