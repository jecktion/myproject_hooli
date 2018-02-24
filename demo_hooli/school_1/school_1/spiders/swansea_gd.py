




import scrapy
from school_1.items import HooliItem
import datetime
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import re

class PlymouthSpider(CrawlSpider):
    name = 'swansea_gd'
    allowed_domains = ['www.swansea.ac.uk']
    start_urls = []
    base_url = '%s'

    Lists = ['http://www.swansea.ac.uk/postgraduate/taught/humanandhealthsciences/abnormal-and-clinical-psychology/',
'http://www.swansea.ac.uk/postgraduate/taught/som/mscaccountingandfinance/',
'http://www.swansea.ac.uk/postgraduate/taught/science/msc-advanced-computer-science/',
'http://www.swansea.ac.uk/postgraduate/taught/humanandhealthsciences/advanced-critical-care-practice/',
'http://www.swansea.ac.uk/postgraduate/taught/humanandhealthsciences/advanced-practice-in-healthcare/',
'http://www.swansea.ac.uk/postgraduate/taught/science/msc-advanced-software-technology/',
'http://www.swansea.ac.uk/postgraduate/taught/humanandhealthsciences/mscpgdippgcertadvancedspecialistbloodtransfusion/',
'http://www.swansea.ac.uk/postgraduate/taught/engineering/msc-aerospace-engineering/',
'http://www.swansea.ac.uk/postgraduate/taught/artsandhumanities/ma-ancient-egyptian-culture/',
'http://www.swansea.ac.uk/postgraduate/taught/artsandhumanities/ma-ancient-history-classical-civilisation/',
'http://www.swansea.ac.uk/postgraduate/taught/artsandhumanities/ma-ancient-narrative-literature/',
'http://www.swansea.ac.uk/postgraduate/taught/medicine/msc-applied-analytical-science-(lcms)/',
'http://www.swansea.ac.uk/postgraduate/taught/law/maappliedcriminaljusticecriminology/',
'http://www.swansea.ac.uk/postgraduate/taught/medicine/pg-certificate-in-applied-lcms/',
'http://www.swansea.ac.uk/postgraduate/taught/humanandhealthsciences/approved-mental-health-professional/',
'http://www.swansea.ac.uk/postgraduate/taught/medicine/msc-autism/',
'http://www.swansea.ac.uk/postgraduate/taught/humanandhealthsciences/blood-transfusion/',
'http://www.swan.ac.uk/elts/teacher-training/',
'http://www.swansea.ac.uk/postgraduate/taught/engineering/msc-chemical-engineering/',
'http://www.swansea.ac.uk/postgraduate/taught/humanandhealthsciences/msc-child-public-health/',
'http://www.swansea.ac.uk/postgraduate/taught/humanandhealthsciences/childhood-studies/',
'http://www.swansea.ac.uk/postgraduate/taught/artsandhumanities/ma-chinese-english-translation-language-teaching/',
'http://www.swansea.ac.uk/postgraduate/taught/engineering/msc-civil-engineering/',
'http://www.swansea.ac.uk/postgraduate/taught/artsandhumanities/ma-classics/',
'http://www.swansea.ac.uk/postgraduate/taught/medicine/clinicalmedicine/',
'http://www.swansea.ac.uk/postgraduate/taught/medicine/msc-clinical-science-medical-physics-part-time/',
'http://www.swansea.ac.uk/postgraduate/taught/artsandhumanities/ma-communication-media-practice-pr/',
'http://www.swansea.ac.uk/postgraduate/taught/engineering/msc-communication-engineering/',
'http://www.swan.ac.uk/postgraduate/taught/humanandhealthsciences/community-and-primary-healthcare-practice/',
'http://www.swansea.ac.uk/postgraduate/taught/engineering/erasmus-mundus-msc-computational-mechanics/',
'http://www.swansea.ac.uk/postgraduate/taught/engineering/msc-computer-modelling-and-finite-elements/',
'http://www.swansea.ac.uk/postgraduate/taught/science/msc-computer-science/',
'http://www.swansea.ac.uk/postgraduate/taught/science/msc-computer-science-informatique/',
'http://www.swansea.ac.uk/postgraduate/taught/artsandhumanities/ma-creative-writing/',
'http://www.swansea.ac.uk/postgraduate/taught/artsandhumanities/macreativewritingextended/',
'http://www.swansea.ac.uk/postgraduate/taught/science/mscdatascience/',
'http://www.swansea.ac.uk/postgraduate/taught/artsandhumanities/ma-development-and-human-rights/',
'http://www.swansea.ac.uk/postgraduate/taught/artsandhumanities/madevelopmentandhumanrightsextended/',
'http://www.swansea.ac.uk/postgraduate/taught/humanandhealthsciences/developmental-and-therapeutic-play/',
'http://www.swansea.ac.uk/postgraduate/taught/medicine/diabetespractice/',
'http://www.swansea.ac.uk/postgraduate/taught/artsandhumanities/ma-digital-media/',
'http://www.swansea.ac.uk/postgraduate/taught/artsandhumanities/ma-early-modern-history/',
'http://www.swansea.ac.uk/postgraduate/taught/som/msceconomics/',
'http://www.swansea.ac.uk/postgraduate/taught/som/msceconomicsandfinance/',
'http://www.swansea.ac.uk/postgraduate/taught/humanandhealthsciences/education-for-the-health-professions/',
'http://www.swansea.ac.uk/postgraduate/taught/engineering/msc-electrical-and-electronic-engineering/',
'http://www.swansea.ac.uk/postgraduate/taught/engineering/msc-engineering-leadership/',
'http://www.swansea.ac.uk/postgraduate/taught/artsandhumanities/ma-english-literature/',
'http://www.swansea.ac.uk/postgraduate/taught/humanandhealthsciences/pgcertenhancedneonatalcare/',
'http://www.swansea.ac.uk/postgraduate/taught/humanandhealthsciences/msc-enhanced-professional-midwifery-practice/',
'http://www.swansea.ac.uk/postgraduate/taught/humanandhealthsciences/msc_pgdip_pgcert_enhanced_professional_practice/',
'http://www.swansea.ac.uk/postgraduate/taught/science/msc-environmental-biology-conservation-and-resource-management/',
'http://www.swansea.ac.uk/postgraduate/taught/science/msc-environmental-dynamics-and-climate-change/',
'http://www.swansea.ac.uk/postgraduate/taught/som/mscfinance/',
'http://www.swansea.ac.uk/postgraduate/taught/som/mscfinanceandbusinessanalytics/',
'http://www.swansea.ac.uk/postgraduate/taught/som/mscfinancialmanagement/',
'http://www.swansea.ac.uk/postgraduate/taught/artsandhumanities/ma-gender-and-culture/',
'http://www.swansea.ac.uk/postgraduate/taught/artsandhumanities/magenderandcultureextended/',
'http://www.swansea.ac.uk/postgraduate/taught/science/msc-geographic-information-and-climate-change/',
'http://www.swansea.ac.uk/postgraduate/taught/humanandhealthsciences/gerontology-and-ageing/',
'http://www.swansea.ac.uk/postgraduate/taught/law/graduatediplomainlaw/',
'http://www.swansea.ac.uk/postgraduate/taught/humanandhealthsciences/mschealthcaremanagement/',
'http://www.swansea.ac.uk/postgraduate/taught/medicine/msc-health-data-science/',
'http://www.swansea.ac.uk/postgraduate/taught/medicine/msc-health-informatics/',
'http://www.swansea.ac.uk/postgraduate/taught/science/msc-high-performance-and-scientific-computing/',
'http://www.swansea.ac.uk/postgraduate/taught/artsandhumanities/ma-history/',
'http://www.swansea.ac.uk/postgraduate/taught/law/llminhumanrights/',
'http://www.swansea.ac.uk/postgraduate/taught/law/llminintellectualpropertyandcommercialpractice/',
'http://www.swansea.ac.uk/postgraduate/taught/som/mscinternationalbankingandfinance/',
'http://www.swansea.ac.uk/postgraduate/taught/law/llmininternationalcommerciallaw/',
'http://www.swansea.ac.uk/postgraduate/taught/law/llmininternationalcommercialandmaritimelaw/',
'http://www.swansea.ac.uk/postgraduate/taught/humanandhealthsciences/international-gerontology-and-ageing-studies/',
'http://www.swansea.ac.uk/postgraduate/taught/artsandhumanities/ma-comparative-journalism/',
'http://www.swansea.ac.uk/postgraduate/taught/law/llmininternationalmaritimelaw/',
'http://www.swansea.ac.uk/postgraduate/taught/artsandhumanities/ma-international-relations/',
'http://www.swansea.ac.uk/postgraduate/taught/artsandhumanities/mainternationalrelationsextended/',
'http://www.swansea.ac.uk/postgraduate/taught/artsandhumanities/ma-international-security-development/',
'http://www.swansea.ac.uk/postgraduate/taught/artsandhumanities/maininternationalsecurityanddevelopmentextended/',
'http://www.swansea.ac.uk/postgraduate/taught/law/llmininternationaltradelaw/',
'http://www.swansea.ac.uk/postgraduate/taught/som/mscinvestmentmanagement/',
'http://www.swansea.ac.uk/postgraduate/taught/artsandhumanities/ma-erasmus-mundus-journalism/',
'http://www.swansea.ac.uk/postgraduate/taught/medicine/msc-leadership-health-professions/',
'http://www.swansea.ac.uk/postgraduate/taught/medicine/msc-leadership-health-professions-distance-learning/',
'http://www.swansea.ac.uk/postgraduate/taught/humanandhealthsciences/mscleadershipmanagementandinnovationinhealthcare/',
'http://www.swansea.ac.uk/postgraduate/taught/law/legalpracticecourselpc/',
'http://www.swansea.ac.uk/postgraduate/taught/law/llminlegalpracticeandadvanceddrafting/',
'http://www.swansea.ac.uk/postgraduate/taught/humanandhealthsciences/long-term-chronic-conditions-management/',
'http://www.swansea.ac.uk/postgraduate/taught/som/mscmanagement/',
'http://www.swansea.ac.uk/postgraduate/taught/som/mscmanagementbusinessanalytics/',
'http://www.swansea.ac.uk/postgraduate/taught/som/mscmanagemententrepreneurship/',
'http://www.swansea.ac.uk/postgraduate/taught/som/mscmanagementfinance/',
'http://www.swansea.ac.uk/postgraduate/taught/som/mscmanagementhumanresourcemanagement/',
'http://www.swansea.ac.uk/postgraduate/taught/som/mscmanagementinternationalmanagement/',
'http://www.swansea.ac.uk/postgraduate/taught/som/mscmanagementinternationalstandards/',
'http://www.swansea.ac.uk/postgraduate/taught/som/mscmanagementmarketing/',
'http://www.swansea.ac.uk/postgraduate/taught/som/mscmanagementoperationsandsupplymanagement/',
'http://www.swansea.ac.uk/postgraduate/taught/som/mscmanagementtourism/',
'http://www.swansea.ac.uk/postgraduate/taught/som/mscmanagemente-business/',
'http://www.swansea.ac.uk/postgraduate/taught/engineering/msc-materials-engineering/',
'http://www.swansea.ac.uk/postgraduate/taught/science/mscmathematics/',
'http://www.swansea.ac.uk/postgraduate/taught/science/msc-mathematics-and-computing-for-finance/',
'http://www.swansea.ac.uk/postgraduate/taught/engineering/msc-mechanical-engineering/',
'http://www.swansea.ac.uk/postgraduate/taught/humanandhealthsciences/medical-law-and-ethics/',
'http://www.swansea.ac.uk/postgraduate/taught/medicine/msc-medical-radiation-physics/',
'http://www.swansea.ac.uk/undergraduate/courses/medicine/mbbchgraduateentrymedicine/',
'http://www.swansea.ac.uk/postgraduate/taught/artsandhumanities/ma-medieval-studies/',
'http://www.swansea.ac.uk/postgraduate/taught/artsandhumanities/ma-modern-history/',
'http://www.swan.ac.uk/postgraduate/taught/medicine/msc_nanomedicine/',
'http://www.swansea.ac.uk/postgraduate/taught/engineering/msc-nanoscience-to-nanotechnology/',
'http://www.swansea.ac.uk/postgraduate/taught/humanandhealthsciences/pgcertnon-medicalprescribing/',
'http://www.swansea.ac.uk/postgraduate/taught/humanandhealthsciences/pgcertnon-medicalprescribingforalliedhealthprofessionals/',
'http://www.swansea.ac.uk/postgraduate/taught/humanandhealthsciences/pgcertnon-medicalprescribing/',
'http://www.swansea.ac.uk/postgraduate/taught/humanandhealthsciences/pgcertnon-medicalprescribingforpharmacists/',
'http://www.swansea.ac.uk/postgraduate/taught/humanandhealthsciences/adult-nursing/',
'http://www.swansea.ac.uk/postgraduate/taught/humanandhealthsciences/child-nursing/',
'http://www.swansea.ac.uk/postgraduate/taught/humanandhealthsciences/mental-health-nursing/',
'http://www.swansea.ac.uk/postgraduate/taught/law/llminoilgasandrenewableenergylaw/',
'http://www.swansea.ac.uk/postgraduate/taught/medicine/pg_dip_physician_associate_studies/',
'http://www.swansea.ac.uk/postgraduate/taught/artsandhumanities/ma-politics/',
'http://www.swansea.ac.uk/postgraduate/taught/artsandhumanities/mapoliticsextended/',
'http://www.swansea.ac.uk/postgraduate/taught/engineering/msc-power-engineering-and-sustainable-energy/',
'http://www.swansea.ac.uk/postgraduate/taught/artsandhumanities/ma-translation-language-technology/',
'http://www.swansea.ac.uk/postgraduate/taught/artsandhumanities/ma-translation-language-technology-2-years/',
'http://www.swansea.ac.uk/postgraduate/taught/humanandhealthsciences/public-health-and-health-promotion/',
'http://www.swansea.ac.uk/postgraduate/taught/artsandhumanities/mapublichistoryandheritage/',
'http://www.swansea.ac.uk/postgraduate/taught/artsandhumanities/mapublichistoryandheritageextended/',
'http://www.swansea.ac.uk/postgraduate/taught/artsandhumanities/ma-public-policy/',
'http://www.swansea.ac.uk/postgraduate/taught/artsandhumanities/mapublicpolicyextended/',
'http://www.swansea.ac.uk/postgraduate/taught/humanandhealthsciences/research-methods-in-psychology/',
'http://www.swansea.ac.uk/postgraduate/taught/humanandhealthsciences/research-methods-in-psychology-and-cognitive-neuroscience/',
'http://www.swansea.ac.uk/postgraduate/taught/humanandhealthsciences/social-research-methods/',
'http://www.swansea.ac.uk/postgraduate/taught/humanandhealthsciences/social-work/',
'http://www.swansea.ac.uk/postgraduate/taught/engineering/erasmus-mundus-ma-sports-ethics-integrity/',
'http://www.swansea.ac.uk/postgraduate/taught/som/mscstrategicaccounting/',
'http://www.swansea.ac.uk/postgraduate/taught/som/mscstrategicmarketing/',
'http://www.swansea.ac.uk/postgraduate/taught/engineering/msc-sustainable-engineering/',
'http://www.swansea.ac.uk/postgraduate/taught/artsandhumanities/ma-teaching-english-as-a-foreign-language/',
'http://www.swansea.ac.uk/postgraduate/taught/artsandhumanities/postgraduatecertificateintranslationtechnology/',
'http://www.swansea.ac.uk/postgraduate/taught/artsandhumanities/ma-translation-interpreting/',
'http://www.swansea.ac.uk/postgraduate/taught/artsandhumanities/ma-translation-interpreting-2-years/',
'http://www.swansea.ac.uk/postgraduate/taught/artsandhumanities/ma-war-and-society/',
'http://www.swansea.ac.uk/postgraduate/taught/artsandhumanities/ma-welsh-writing-in-english/']

    for i in Lists:
        fullurl = base_url % i
        start_urls.append(fullurl)

    rules = (
        Rule(LinkExtractor(allow=(r'.*'), restrict_xpaths=('//div[@class="widget--course--a-to-z"]//li//a')), follow=True),
        # Rule(LinkExtractor(allow=r''),follow=True),
        Rule(LinkExtractor(allow=r'postgraduate/taught/.*'),callback='parse_item', follow=False),
    )

    def parse_item(self,response):
        print('==================================',response.url)
        item = HooliItem()

        url = response.url
        print(1,url)

        university = 'Swansea University Prifysgol Abertawe'
        print(2,university)

        department = 'NULL'

        country = 'UK'
        city = "NULL"
        website = 'NULL'

        programme = response.xpath('//div[@id="contentHeader"]/h1/text()').extract()
        programme = ''.join(programme)
        print(3,programme)

        ucas_code = 'NULL'
        degree_level = '1'

        degree_type = response.xpath('//div[@id="contentHeader"]/h1/text()').extract()
        degree_type = ''.join(degree_type)
        degree_type = self.getDegree_type(degree_type)
        print(4,degree_type)

        start_date = 'NULL'
        # start_date = ''.join(start_date)
        # print(5,start_date)

        overview = response.xpath('//div[@id="description-contents"]/p/text()').extract()
        overview = ''.join(overview).replace('\n', '')
        print(6, overview)

        mode_s = response.xpath('//div[@id="tuition-fees-contents"]//text()').extract()
        mode_s = ''.join(mode_s).replace('\r\n','')
        mode_s = mode_s.replace('\n','')
        mode_s = mode_s.replace('      ','')
        try:
            if "Full-time" in mode_s:
                mode = "Full-time"
            else:
                mode = "Part-time"
        except:
            mode = "报错!"

        print(7,mode)


        duration = response.xpath('//div[@id="content-items"]/div/div/ol/li//text()').extract()
        duration = ''.join(duration).replace('\r\n','')
        duration = duration.replace('\n','')
        duration = duration.replace('    ','')
        print(8,duration)

        modules = response.xpath('//div[@id="modules"]/div[@id="modules-contents"]//text()').extract()
        modules = ''.join(modules).replace('\r\n','')
        # modules = modules.replace('\n','')
        print(9,modules)

        teaching = 'NULL'

        assessment = response.xpath('//*[@id="teaching-assessment"]//text()').extract()
        assessment = ''.join(assessment)
        print(10, assessment)

        career = 'NULL'
        # career = ''.join(career).replace('\n', '')
        # print(11, career)

        application_date = 'NULL'

        deadline = 'NULL'

        application_fee = 'NULL'

        tuition_fee_s = response.xpath('//div[@id="tuition-fees-contents"]//text()').extract()
        tuition_fee_s = ''.join(tuition_fee_s).replace('\r\n','')
        tuition_fee_s = tuition_fee_s.replace('\n','')
        tuition_fee_s = tuition_fee_s.replace('    ','')
        tuition_fee_s = self.getTuition_fee(tuition_fee_s)
        try:
            if tuition_fee_s >0:
                tuition_fee = tuition_fee_s
            else:
                tuition_fee = 'NULL'
        except:
            tuition_fee = '报错!'

        print(11, tuition_fee)

        location = 'NULL'
        # location = ''.join(location)
        # print(13,location)

        ATAS = 'NULL'

        GPA = 'NULL'

        average_score = 'NULL'

        accredited_university = 'NULL'

        Alevel = 'NULL'

        IB = 'NULL'

        IELTS_s = response.xpath('//div[@id="entry-requirements-contents"]//text()').extract()
        IELTS_s = ''.join(IELTS_s).replace('\r\n','')
        # IELTS = re.findall('(IELTS:|IELTS)? (.*){0,5} \d?.\d? .{0,70}',IELTS)
        try:
            if "IELTS" in IELTS_s:
                start = IELTS_s.find("IELTS")
                IELTS = IELTS_s[start:]
                IELTS = IELTS[:100]
            else:
                IELTS = 'NULL'
        except:
            IELTS = '报错!'
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

        interview = 'NULL'

        portfolio = 'NULL'

        application_documents = 'NULL'

        how_to_apply = response.xpath('//div[@id="how-to-apply"]//text()').extract()
        how_to_apply = ''.join(how_to_apply).replace('\n','')
        print(13,how_to_apply)

        entry_requirements = response.xpath('//div[@id="entry-requirements-contents"]//text()').extract()
        entry_requirements = ''.join(entry_requirements).replace('\n','')
        # EntryRequirements = EntryRequirements.replace(' ','')
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

    def getDegree_type(self,degree_type):
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
        return degree_type

