

import scrapy
from school_1.items import HooliItem
import datetime
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import re

class PlymouthSpider(CrawlSpider):
    name = 'exeter'
    allowed_domains = ['www.exeter.ac.uk']
    start_urls = []
    base_url = 'https://www.exeter.ac.uk/%s'

    Lists = ['/undergraduate/degrees/accounting/accountfin/',
    '/undergraduate/degrees/accounting/accountfineu/',
    '/undergraduate/degrees/accounting/accountfinexp/',
    '/undergraduate/degrees/accounting/accountfinint/',
    '/undergraduate/degrees/classics/ancient/',
    '/undergraduate/degrees/classics/ancientarch/',
    '/undergraduate/degrees/classics/ancientarch-employment/',
    '/undergraduate/degrees/classics/ancientarch-abroad/',
    '/undergraduate/degrees/classics/ancient-history-employment/',
    '/undergraduate/degrees/classics/ancient-abroad/',
    '/undergraduate/degrees/biosciences/animal/',
    '/undergraduate/degrees/biosciences/animalmsci/',
    '/undergraduate/degrees/biosciences/animalwpp/',
    '/undergraduate/degrees/biosciences/animalwsa/',
    '/undergraduate/degrees/anthropology/anthropologyba/',
    '/undergraduate/degrees/anthropology/anthropologyba-abroad/',
    '/undergraduate/degrees/geology/applied/',
    '/undergraduate/degrees/geology/appliedmgeol/',
    '/undergraduate/degrees/psychology/msciapppsy/',
    '/undergraduate/degrees/arabislamic/marabic/',
    '/undergraduate/degrees/archaeology/arch/',
    '/undergraduate/degrees/archaeology/archanth/',
    '/undergraduate/degrees/archaeology/archanth-experience/',
    '/undergraduate/degrees/archaeology/archanth-abroad/',
    '/undergraduate/degrees/archaeology/arch-employment/',
    '/undergraduate/degrees/archaeology/forensic/',
    '/undergraduate/degrees/archaeology/forensic-experience/',
    '/undergraduate/degrees/archaeology/forensic-abroad/',
    '/undergraduate/degrees/archaeology/arch-abroad/',
    '/undergraduate/degrees/art/arthist/',
    '/undergraduate/degrees/art/arthistclassics/',
    '/undergraduate/degrees/art/arthistclassics-abroad/',
    '/undergraduate/degrees/drama/dramavc/',
    '/undergraduate/degrees/drama/dramavc-abroad/',
    '/undergraduate/degrees/art/arthistenglish/',
    '/undergraduate/degrees/art/arthistenglish-abroad/',
    '/undergraduate/degrees/art/arthisthistory/',
    '/undergraduate/degrees/art/arthisthistory-abroad/',
    '/undergraduate/degrees/art/arthistmodlang/',
    '/undergraduate/degrees/art/classics-employment/',
    '/undergraduate/degrees/art/drama-employment/',
    '/undergraduate/degrees/art/arthist-employment/',
    '/undergraduate/degrees/art/english-employment/',
    '/undergraduate/degrees/art/history-employment/',
    '/undergraduate/degrees/art/arthist-abroad/',
    '/undergraduate/degrees/biosciences/biochem/',
    '/undergraduate/degrees/biosciences/biochemexp/',
    '/undergraduate/degrees/biosciences/biochemwsa/',
    '/undergraduate/degrees/biosciences/biosci/',
    '/undergraduate/degrees/biosciences/biosciprof/',
    '/undergraduate/degrees/biosciences/biosciwsa/',
    '/undergraduate/degrees/biosciences/biomed/',
    '/undergraduate/degrees/biosciences/biomedexp/',
    '/undergraduate/degrees/biosciences/biomedwsa/',
    '/undergraduate/degrees/business/businessbsc/',
    '/undergraduate/degrees/economics/busecon/',
    '/undergraduate/degrees/economics/buseconeu/',
    '/undergraduate/degrees/economics/buseconexp/',
    '/undergraduate/degrees/economics/buseconint/',
    '/undergraduate/degrees/accounting/businessacc/',
    '/undergraduate/degrees/accounting/businessacceu/',
    '/undergraduate/degrees/accounting/businessaccexp/',
    '/undergraduate/degrees/accounting/businessaccint/',
    '/undergraduate/degrees/business/businessman/',
    '/undergraduate/degrees/business/businessmaneu/',
    '/undergraduate/degrees/business/businessmanexp/',
    '/undergraduate/degrees/business/businessmanint/',
    '/undergraduate/degrees/business/businesseu/',
    '/undergraduate/degrees/business/businessexp/',
    '/undergraduate/degrees/business/businessint/',
    '/undergraduate/degrees/languages/modlang/chinese/',
    '/undergraduate/degrees/engineering/civil/',
    '/undergraduate/degrees/engineering/civilmeng/',
    '/undergraduate/degrees/engineering/civil-engineering/',
    '/undergraduate/degrees/engineering/environmental/',
    '/undergraduate/degrees/classics/classical/',
    '/undergraduate/degrees/classics/classics-english/',
    '/undergraduate/degrees/classics/classics-english-employment/',
    '/undergraduate/degrees/classics/classics-english-abroad/',
    '/undergraduate/degrees/classics/classics-modlang/',
    '/undergraduate/degrees/classics/classics-philosophy/',
    '/undergraduate/degrees/classics/classics-philosophy-employment/',
    '/undergraduate/degrees/classics/classics-philosophy-abroad/',
    '/undergraduate/degrees/classics/classics-theology/',
    '/undergraduate/degrees/classics/classics-theology-employment/',
    '/undergraduate/degrees/classics/classics-theology-abroad/',
    '/undergraduate/degrees/classics/classical-employment/',
    '/undergraduate/degrees/classics/classical-abroad/',
    '/undergraduate/degrees/classics/classics/',
    '/undergraduate/degrees/classics/classics-employment/',
    '/undergraduate/degrees/classics/classics-abroad/',
    '/undergraduate/degrees/computerscience/comsci/',
    '/undergraduate/degrees/computerscience/comscimsci/',
    '/undergraduate/degrees/computerscience/comscimaths/',
    '/undergraduate/degrees/computerscience/comscimathsmsci/',
    '/undergraduate/degrees/computerscience/comscimaths-placement/',
    '/undergraduate/degrees/computerscience/comsci-placement/',
    '/undergraduate/degrees/biosciences/conservation/',
    '/undergraduate/degrees/biosciences/conservationmsci/',
    '/undergraduate/degrees/biosciences/conservationwpp/',
    '/undergraduate/degrees/biosciences/conservationwsa/',
    '/undergraduate/degrees/politics/cornwall/',
    '/undergraduate/degrees/sociology/criminologybsc/',
    '/undergraduate/degrees/sociology/criminologybsc-abroad/',
    '/undergraduate/degrees/computerscience/digital-technology-apprenticeship/',
    '/undergraduate/degrees/drama/drama/',
    '/undergraduate/degrees/drama/drama-employment/',
    '/undergraduate/degrees/drama/dramawsa/',
    '/undergraduate/degrees/economics/economics/',
    '/undergraduate/degrees/economics/finance/',
    '/undergraduate/degrees/economics/financeeu/',
    '/undergraduate/degrees/economics/financeexp/',
    '/undergraduate/degrees/economics/financeint/',
    '/undergraduate/degrees/economics/politics/',
    '/undergraduate/degrees/economics/politicseu/',
    '/undergraduate/degrees/economics/politicsexp/',
    '/undergraduate/degrees/economics/politicsint/',
    '/undergraduate/degrees/economics/econometrics/',
    '/undergraduate/degrees/economics/econometricseu/',
    '/undergraduate/degrees/economics/econometricsexp/',
    '/undergraduate/degrees/economics/econometricsint/',
    '/undergraduate/degrees/economics/economicseu/',
    '/undergraduate/degrees/economics/economicsexp/',
    '/undergraduate/degrees/economics/economicsint/',
    '/undergraduate/degrees/engineering/electronic/',
    '/undergraduate/degrees/engineering/electronicmeng/',
    '/undergraduate/degrees/engineering/eleccomp/',
    '/undergraduate/degrees/engineering/eleccompmeng/',
    '/undergraduate/degrees/engineering/engineering/',
    '/undergraduate/degrees/geology/engineering/',
    '/undergraduate/degrees/geology/engineeringmgeol/',
    '/undergraduate/degrees/engineering/engineeringmeng/',
    '/undergraduate/degrees/engineering/engineering-entrepreneurship/',
    '/undergraduate/degrees/engineering/management/',
    '/undergraduate/degrees/engineering/managementmeng/',
    '/undergraduate/degrees/english/english/',
    '/undergraduate/degrees/english/baenglish/',
    '/undergraduate/degrees/english/engdrama/',
    '/undergraduate/degrees/english/englishdrama-employment/',
    '/undergraduate/degrees/english/engdrama-abroad/',
    '/undergraduate/degrees/english/film/',
    '/undergraduate/degrees/english/film-employment/',
    '/undergraduate/degrees/english/film-abroad/',
    '/undergraduate/degrees/english/history/',
    '/undergraduate/degrees/english/history-abroad/',
    '/undergraduate/degrees/english/english-modlang/',
    '/undergraduate/degrees/english/english-employment/',
    '/undergraduate/degrees/english/english-abroad/',
    '/undergraduate/degrees/english/baenglish-abroad/',
    '/undergraduate/degrees/english/englishna/',
    '/undergraduate/degrees/envsci/envscimsci/',
    '/undergraduate/degrees/envsci/envsci/',
    '/undergraduate/degrees/envsci/envsciwpp/',
    '/undergraduate/degrees/envsci/envsciwsa/',
    '/undergraduate/degrees/biosciences/evobiology/',
    '/undergraduate/degrees/biosciences/evobiologymsci/',
    '/undergraduate/degrees/biosciences/evobiologywpp/',
    '/undergraduate/degrees/biosciences/evobiologywsa/',
    '/undergraduate/degrees/sport/exsport/',
    '/undergraduate/degrees/sport/exsportmsci/',
    '/undergraduate/degrees/sport/exsportwsa/',
    '/undergraduate/degrees/film/film/',
    '/undergraduate/degrees/film/film-modlang/',
    '/undergraduate/degrees/film/film-employment/',
    '/undergraduate/degrees/film/film-abroad/',
    '/undergraduate/degrees/flexible/cornwall/',
    '/undergraduate/degrees/flexible/exeter/',
    '/undergraduate/degrees/flexible/cornwall-abroad/',
    '/undergraduate/degrees/flexible/exeter-abroad/',
    '/undergraduate/degrees/flexible/cornwall-experience/',
    '/undergraduate/degrees/flexible/exeter-experience/',
    '/undergraduate/degrees/flexible/cornwall-work-abroad/',
    '/undergraduate/degrees/flexible/exeter-work-abroad/',
    '/undergraduate/degrees/foundation/foundation/',
    '/undergraduate/degrees/languages/modlang/french/',
    '/undergraduate/degrees/geography/exegeogba/',
    '/undergraduate/degrees/geography/corngeogbabsc/',
    '/undergraduate/degrees/geography/exegeogbsc/',
    '/undergraduate/degrees/geography/exegeogba-abroad/',
    '/undergraduate/degrees/geography/exegeogbsc-abroad/',
    '/undergraduate/degrees/geography/corngeogbabscwpp/',
    '/undergraduate/degrees/geography/exegeogbawsa/',
    '/undergraduate/degrees/geography/corngeogbabscwsa/',
    '/undergraduate/degrees/geography/exegeogbscwsa/',
    '/undergraduate/degrees/geology/geology/',
    '/undergraduate/degrees/geology/geologymgeol/',
    '/undergraduate/degrees/languages/modlang/german/',
    '/undergraduate/degrees/law/gradllb/',
    '/undergraduate/degrees/history/historyexe/',
    '/undergraduate/degrees/history/bahistory/',
    '/undergraduate/degrees/history/history-ancient/',
    '/undergraduate/degrees/history/history-ancient-employment/',
    '/undergraduate/degrees/history/history-ancient-abroad/',
    '/undergraduate/degrees/history/hist-arch/',
    '/undergraduate/degrees/history/history-arch-employment/',
    '/undergraduate/degrees/history/hist-arch-abroad/',
    '/undergraduate/degrees/history/history-intrel/',
    '/undergraduate/degrees/history/intrel-corn/',
    '/undergraduate/degrees/history/intrel-employment/',
    '/undergraduate/degrees/history/intrel-abroad/',
    '/undergraduate/degrees/history/intrel-corn-abroad/',
    '/undergraduate/degrees/history/history-modlang/',
    '/undergraduate/degrees/history/history-politics-corn/',
    '/undergraduate/degrees/history/histpol-abroad-corn/',
    '/undergraduate/degrees/history/historyexe-employment/',
    '/undergraduate/degrees/history/historyexeabroad/',
    '/undergraduate/degrees/history/bahistoryabroad/',
    '/undergraduate/degrees/sport/humanbio/',
    '/undergraduate/degrees/humansciences/humansciences/',
    '/undergraduate/degrees/humansciences/humansciwpp/',
    '/undergraduate/degrees/humansciences/humansciwsa/',
    '/undergraduate/degrees/politics/intrelations/',
    '/undergraduate/degrees/politics/cornwallir/',
    '/undergraduate/degrees/politics/intlrel_modlang/',
    '/undergraduate/degrees/politics/intrelations-abroad/',
    '/undergraduate/degrees/politics/cornwallir-abroad/',
    '/undergraduate/degrees/foundation/internationalyearone/',
    '/undergraduate/degrees/languages/modlang/italian/',
    '/undergraduate/degrees/law/master1/',
    '/undergraduate/degrees/law/law/',
    '/undergraduate/degrees/law/laweurostudy/',
    '/undergraduate/degrees/libarts/liberal/',
    '/undergraduate/degrees/libarts/liberal-employment/',
    '/undergraduate/degrees/libarts/liberal-abroad/',
    '/undergraduate/degrees/business/marketing/',
    '/undergraduate/degrees/business/marketingeu/',
    '/undergraduate/degrees/business/marketingexp/',
    '/undergraduate/degrees/business/marketingint/',
    '/undergraduate/degrees/biosciences/marinebio/',
    '/undergraduate/degrees/biosciences/marinebiomsci/',
    '/undergraduate/degrees/biosciences/marinebiowpp/',
    '/undergraduate/degrees/biosciences/marinebiowsa/',
    '/undergraduate/degrees/engineering/materials/',
    '/undergraduate/degrees/engineering/materialsmeng/',
    '/undergraduate/degrees/mathematics/mathsmsci-ecology/',
    '/undergraduate/degrees/mathematics/mathsmsci-energy/',
    '/undergraduate/degrees/mathematics/mathsmsci-environment/',
    '/undergraduate/degrees/mathematics/mathematical-sciences-bsc/',
    '/undergraduate/degrees/mathematics/mathsmsci-climate/',
    '/undergraduate/degrees/mathematics/mathssci-geophysical/',
    '/undergraduate/degrees/mathematics/mathsmsci-biology/',
    '/undergraduate/degrees/mathematics/mathsbsc/',
    '/undergraduate/degrees/mathematics/mathsmm/',
    '/undergraduate/degrees/mathematics/maths-physics/',
    '/undergraduate/degrees/mathematics/mathsaccounting/',
    '/undergraduate/degrees/mathematics/mathsaccountingmsci/',
    '/undergraduate/degrees/mathematics/mathseconomics/',
    '/undergraduate/degrees/mathematics/mathseconomicsmsci/',
    '/undergraduate/degrees/mathematics/mathsfinance/',
    '/undergraduate/degrees/mathematics/mathsfinancemsci/',
    '/undergraduate/degrees/mathematics/internationalmm/',
    '/undergraduate/degrees/mathematics/mathsmanage/',
    '/undergraduate/degrees/mathematics/mathsmanagemsci/',
    '/undergraduate/degrees/mathematics/professionalmm/',
    '/undergraduate/degrees/engineering/mechanical/',
    '/undergraduate/degrees/engineering/mechanicalmeng/',
    '/undergraduate/degrees/medical-imaging/imaging/',
    '/undergraduate/degrees/medicalsci/medicalsci/',
    '/undergraduate/degrees/medicalsci/medicalscipty/',
    '/undergraduate/degrees/medicine/medicine/',
    '/undergraduate/degrees/arabislamic/mideast/',
    '/undergraduate/degrees/engineering/miningb/',
    '/undergraduate/degrees/mining/miningb/',
    '/undergraduate/degrees/mining/miningm/',
    '/undergraduate/degrees/engineering/miningm/',
    '/undergraduate/degrees/languages/modlang/',
    '/undergraduate/degrees/languages/modlang-arabic/',
    '/undergraduate/degrees/languages/latin/',
    '/undergraduate/degrees/natural-sciences/bsc/',
    '/undergraduate/degrees/natural-sciences/msci/',
    '/undergraduate/degrees/neuroscience/neurosciencebsc/',
    '/undergraduate/degrees/philosophy/philosophy/',
    '/undergraduate/degrees/philosophy/combined/',
    '/undergraduate/degrees/philosophy/history/',
    '/undergraduate/degrees/philosophy/history-abroad/',
    '/undergraduate/degrees/philosophy/modlang/',
    '/undergraduate/degrees/philosophy/politics/',
    '/undergraduate/degrees/philosophy/politics-abroad/',
    '/undergraduate/degrees/philosophy/sociology/',
    '/undergraduate/degrees/philosophy/sociology-abroad/',
    '/undergraduate/degrees/philosophy/theology/',
    '/undergraduate/degrees/philosophy/theology-abroad/',
    '/undergraduate/degrees/philosophy/philosophy-abroad/',
    '/undergraduate/degrees/physics/physicbsc/',
    '/undergraduate/degrees/physics/physicsmphys/',
    '/undergraduate/degrees/physics/astrobsc/',
    '/undergraduate/degrees/physics/astromphys/',
    '/undergraduate/degrees/physics/physicsusa/',
    '/undergraduate/degrees/physics/professional/',
    '/undergraduate/degrees/physics/physicsaustrmphys/',
    '/undergraduate/degrees/physics/physicsnz/',
    '/undergraduate/degrees/politics/politics/',
    '/undergraduate/degrees/politics/combined/',
    '/undergraduate/degrees/politics/cornwallpolir/',
    '/undergraduate/degrees/politics/politicsir/',
    '/undergraduate/degrees/politics/cornwallpolir-abroad/',
    '/undergraduate/degrees/politics/politicsir-abroad/',
    '/undergraduate/degrees/politics/modlang/',
    '/undergraduate/degrees/politics/sociology/',
    '/undergraduate/degrees/politics/sociology-abroad/',
    '/undergraduate/degrees/politics/politics-abroad/',
    '/undergraduate/degrees/politics/ppe/',
    '/undergraduate/degrees/politics/ppe-abroad/',
    '/undergraduate/degrees/languages/modlang/portuguese/',
    '/undergraduate/degrees/accounting/exemptions/',
    '/undergraduate/degrees/psychology/psychbsc/',
    '/undergraduate/degrees/psychology/psychsport/',
    '/undergraduate/degrees/psychology/psycbsc-abroad/',
    '/undergraduate/degrees/energy/energybsc/',
    '/undergraduate/degrees/engineering/energy-engineering-beng/',
    '/undergraduate/degrees/energy/energy-engineering-beng/',
    '/undergraduate/degrees/energy/energy-engineering-meng/',
    '/undergraduate/degrees/engineering/energy-engineering-meng/',
    '/undergraduate/degrees/energy/energy-engineering-ind-meng/',
    '/undergraduate/degrees/engineering/energy-engineering-ind-meng/',
    '/undergraduate/degrees/languages/modlang/russian/',
    '/undergraduate/degrees/sociology/sociology/',
    '/undergraduate/degrees/sociology/sociologybsc/',
    '/undergraduate/degrees/sociology/combined/',
    '/undergraduate/degrees/sociology/anthropology/',
    '/undergraduate/degrees/sociology/anthropology-abroad/',
    '/undergraduate/degrees/sociology/criminology/',
    '/undergraduate/degrees/sociology/criminology-abroad/',
    '/undergraduate/degrees/sociology/modlang/',
    '/undergraduate/degrees/sociology/sociology-abroad/',
    '/undergraduate/degrees/sociology/sociologybsc-abroad/',
    '/undergraduate/degrees/languages/modlang/spanish/',
    '/undergraduate/degrees/medicalsci/sport-exercise/',
    '/undergraduate/degrees/medicalsci/sport-exercisepty/',
    '/undergraduate/degrees/theology/theology/',
    '/undergraduate/degrees/theology/theology-employment/',
    '/undergraduate/degrees/theology/theology-abroad/',
    '/undergraduate/degrees/biosciences/zoology/',
    '/undergraduate/degrees/biosciences/zoologymsci/',
    '/undergraduate/degrees/biosciences/zoologywpp/',
    '/undergraduate/degrees/biosciences/zoologywsa/',]

    for i in Lists:
        fullurl = base_url % i
        start_urls.append(fullurl)

    rules = (
        Rule(LinkExtractor(allow=(r'.*'),restrict_xpaths=('//li[@class="course"]/a')), follow=True),
        Rule(LinkExtractor(allow=r'/undergraduate/degrees/.*'), callback='parse_item', follow=False),
    )


    def parse_item(self,response):
        print('==================================',response.url)

        item = HooliItem()

        url = response.url
        print(1, url)

        university = "EXETER UNDERGRADUATE STUDY"
        print(2, university)

        department = 'NULL'
        country = 'UK'
        city = 'NULL'
        website = 'https://www.exeter.ac.uk'

        programme = response.xpath('//div[@id="left-col"]/h1//text()').extract()
        programme = ''.join(programme)
        # Course = Course.replace('\r\n', '')
        print(3,programme)

        ucas_code = response.xpath('//td[@class="exeter-course-ucascode"]//text()').extract()
        ucas_code = ''.join(ucas_code)
        print(4,ucas_code)

        degree_level = '0'

        degree_type = response.xpath('//div[@id="left-col"]/h1/text()').extract()
        degree_type = ''.join(degree_type)
        print(5,degree_type)

        start_date = 'NULL'

        degree_description = 'NULL'

        overview = response.xpath('//div[@id="Overview"]//text()').extract()
        overview = ''.join(overview)
        print(6,overview)

        mode = 'NULL'

        duration = response.xpath('//td[@class="exeter-course-duration"]//text()').extract()
        duration = ''.join(duration)
        print(7,duration)

        Alevel = response.xpath('//td[@class="exeter-course-typicaloffer"]//text()').extract()
        Alevel = ''.join(Alevel)
        print(8,Alevel)

        IB = response.xpath('//td[@class="exeter-course-typicaloffer"]//text()').extract()
        IB = ''.join(IB)
        print(9,IB)

        IELTS = 'NULL'
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

        location = response.xpath('//td[@class="exeter-course-location"]//text()').extract()
        location = ''.join(location)
        print(10,location)

        ATAS = 'NULL'

        modules = response.xpath('//div[@class="container"]//text()').extract()
        modules = ''.join(modules).replace('\n', '')
        modules = modules.replace('\r', '')
        modules = modules.replace('\t', '')
        modules = str(modules)
        print(11, modules)

        teaching = 'NULL'

        assessment = response.xpath('//div[@id="Learning"]//text()').extract()
        assessment = ''.join(assessment)
        assessment = assessment.replace('\r\n', '')
        assessment = assessment.replace('\n', '')
        assessment = assessment.replace('\r', '')
        print(12, assessment)

        career = response.xpath('//div[@id="Careers"]//text()').extract()
        career = ''.join(career).replace('\r\n', '')
        career = career.replace('\n', '')
        print(13, career)

        application_date = 'NULL'

        deadline = 'NULL'

        application_fee = 'NULL'

        tuition_fee = 'NULL'

        GPA = 'NULL'

        average_score = 'NULL'

        accredited_university = 'NULL'

        working_experience = 'NULL'

        interview = 'NULL'

        portfolio = 'NULL'

        application_documents = 'NULL'

        how_to_apply = 'NULL'

        entry_requirements = response.xpath('//div[@id="Entry-requirements"]//text()').extract()
        entry_requirements = ''.join(entry_requirements).replace('\r\n', '')
        print(14, entry_requirements)

        chinese_requirements = 'NULL'

        school_test = 'NULL'


        SATI = 'NULL'

        SATII = 'NULL'

        SAT_code = 'NULL'

        ACT = 'NULL'

        ACT_code = 'NULL'

        other = response.xpath('//div[@id="course-synopsis"]//text()').extract()
        other = ''.join(other).replace('\r\n', '')
        other = other.replace('\n', '')
        other = other.replace('\t', '')
        print(15,other)

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









