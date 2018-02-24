
import scrapy
from school_1.items import HooliItem
import datetime
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import re

class PlymouthSpider(CrawlSpider):
    name = 'exeter_gd'
    allowed_domains = ['www.exeter.ac.uk']
    start_urls = []
    base_url = 'https://www.exeter.ac.uk/%s'

    Lists = ['/postgraduate/research-degrees/accounting/',
    '/postgraduate/taught/accounting/accounting_finance/',
    '/postgraduate/taught/accounting/accounting_tax/',
    '/postgraduate/taught/mathematics/advdmathsmsc/',
    '/postgraduate/taught/politics/aqm_mres/',
    '/postgraduate/research-degrees/politics/mphil-aqm/',
    '/postgraduate/taught/english/english-ma/americanatlantic/',
    '/postgraduate/taught/classics/classicsma/ancient_philosophy/',
    '/postgraduate/taught/classics/classicsma/ancient_politics/',
    '/postgraduate/taught/psychology/animal/',
    '/postgraduate/research-degrees/sociology/mares_anthropology/',
    '/postgraduate/research-degrees/sociology/mphil-phd_anthropology/',
    '/postgraduate/taught/sociology/anthrozoology/',
    '/postgraduate/research-degrees/sociology/mphil-phd_anthrozoology/',
    '/postgraduate/taught/geology/applied-geotechnics-msc/',
    '/postgraduate/taught/medicine/health-services-research-msc/',
    '/postgraduate/taught/psychology/alp/',
    '/postgraduate/taught/politics/applied-security-strategy/',
    '/postgraduate/research-degrees/arabislamic/mphil-phd_arabandislamic/',
    '/postgraduate/taught/archaeology/archma/',
    '/postgraduate/research-degrees/archaeology/archmabyres/',
    '/postgraduate/research-degrees/archaeology/archmphilphd/',
    '/postgraduate/research-degrees/arthistory/arthistmphilphd/',
    '/postgraduate/taught/economics/behavioural_economics/',
    '/postgraduate/taught/archaeology/bioarch/',
    '/postgraduate/research-degrees/biosciences/mphilphdpenryn/',
    '/postgraduate/research-degrees/biosciences/mphilphdstreatham/',
    '/postgraduate/research-degrees/biosciences/masterspenryn/',
    '/postgraduate/research-degrees/biosciences/mastersstreatham/',
    '/postgraduate/research-degrees/modlang/chinesemphilphd/',
    '/postgraduate/taught/engineering/civil-engineering-msc/',
    '/postgraduate/taught/engineering/civil-engineering-management-msc/',
    '/postgraduate/taught/classics/classicsma/classical_receptions/',
    '/postgraduate/taught/classics/classicsma/',
    '/postgraduate/research-degrees/classics/clasmabyres/',
    '/postgraduate/research-degrees/classics/clasmphilphd/',
    '/postgraduate/taught/medicine/clinicaledcert/',
    '/postgraduate/taught/medicine/clinical-pharmacy-pgcert/',
    '/postgraduate/research-degrees/psychology/dclinprac/',
    '/postgraduate/research-degrees/psychology/dclinpsy/',
    '/postgraduate/research-degrees/psychology/dclinres/',
    '/postgraduate/research-degrees/computerscience/computer-science/',
    '/postgraduate/taught/computerscience/compscimsc/',
    '/postgraduate/research-degrees/computerscience/computer-science-msc-research/',
    '/postgraduate/taught/computerscience/compscibusmsc/',
    '/postgraduate/taught/politics/conflict-security-development/',
    '/postgraduate/taught/geography/conservationsci/',
    '/postgraduate/taught/geography/conservationsci/',
    '/postgraduate/taught/biosciences/conservation/',
    '/postgraduate/research-degrees/history/cornish/',
    '/postgraduate/taught/education/educationma/creativearts/',
    '/postgraduate/taught/english/creative-ma/',
    '/postgraduate/research-degrees/english/creativewritingmphilphd/',
    '/postgraduate/taught/geography/mreschg/',
    '/postgraduate/taught/english/english-ma/criticismtheory/',
    '/postgraduate/taught/classics/classicsma/cultural_histories/',
    '/postgraduate/taught/sociology/culturalsociologyma/',
    '/postgraduate/taught/education/dedpsych/',
    '/postgraduate/taught/datascience/msc-data-science/',
    '/postgraduate/taught/datascience/datascimsc/',
    '/postgraduate/taught/datascience/datascibusinessmsc/',
    '/postgraduate/research-degrees/drama/mabyres/',
    '/postgraduate/research-degrees/drama/mphil-phd/',
    '/postgraduate/taught/history/econhistmres/',
    '/postgraduate/research-degrees/economics/',
    '/postgraduate/taught/economics/mres_economics/',
    '/postgraduate/taught/economics/economics/',
    '/postgraduate/taught/economics/economics_econometrics/',
    '/postgraduate/research-degrees/education/eddoctoral/',
    '/postgraduate/taught/education/dedpsych/',
    '/postgraduate/taught/education/educationma/',
    '/postgraduate/research-degrees/education/phd/',
    '/postgraduate/taught/education/edresearchmsc/',
    '/postgraduate/taught/engineering/engmanagemsc/',
    '/postgraduate/research-degrees/engineering/engd-engineering/',
    '/postgraduate/research-degrees/engineering/mphil-phd/',
    '/postgraduate/research-degrees/engineering/mbyres/',
    '/postgraduate/taught/english/english-ma/',
    '/postgraduate/research-degrees/english/englishmphilphd/',
    '/postgraduate/research-degrees/english/engmabyres/',
    '/postgraduate/taught/english/english-ma/enlightenmentromanticism/',
    '/postgraduate/taught/medicine/environment-health-msc/',
    '/postgraduate/research-degrees/geography/sustainablefutures/',
    '/postgraduate/research-degrees/arabislamic/mphil-phd_ethnopolitical/',
    '/postgraduate/taught/law/masteroflaws/european/',
    '/postgraduate/taught/politics/europolma/',
    '/postgraduate/research-degrees/politics/mphil-phd_eurpolitics/',
    '/postgraduate/taught/biosciences/evolutionary/',
    '/postgraduate/taught/archaeology/experimentma/',
    '/postgraduate/taught/geology/explorationgeologymsc/',
    '/postgraduate/taught/medicine/extrememedicinemsc/',
    '/postgraduate/research-degrees/film/mphil-phd/',
    '/postgraduate/taught/english/english-ma/film_studies/',
    '/postgraduate/research-degrees/finance/',
    '/postgraduate/taught/finance/finance_investment/',
    '/postgraduate/taught/finance/finance_management/',
    '/postgraduate/taught/finance/marketing_financial/',
    '/postgraduate/taught/finance/fafm/',
    '/postgraduate/taught/economics/financial_economics/',
    '/postgraduate/taught/mathematics/finmathsmsc/',
    '/postgraduate/taught/biosciences/foodsecurity/',
    '/postgraduate/taught/sociology/food-studies-ma/',
    '/postgraduate/research-degrees/modlang/frenchmphilphd/',
    '/postgraduate/research-degrees/education/eddoctoral/generic/',
    '/postgraduate/taught/medicine/genomicmsc/',
    '/postgraduate/research-degrees/geography/mphilphdgeog/',
    '/postgraduate/research-degrees/geography/masters/',
    '/postgraduate/research-degrees/geology/geology/',
    '/postgraduate/research-degrees/geology/geology-msc-research/',
    '/postgraduate/taught/geology/geotechnicalengineeringmsc/',
    '/postgraduate/research-degrees/modlang/germmphilphd/',
    '/postgraduate/taught/languages/global-literature/',
    '/postgraduate/taught/business/globaleconomy/',
    '/postgraduate/taught/into/graduatediploma/',
    '/postgraduate/taught/medicine/healthservicesimprovementpgcert/',
    '/postgraduate/research-degrees/sport/healthwellbeing/',
    '/postgraduate/taught/sport/healthwellbeing/',
    '/postgraduate/taught/medicine/healthcare-leadership-management-pgcert/',
    '/postgraduate/research-degrees/modlang/hisapmphilphd/',
    '/postgraduate/taught/history/historyma/',
    '/postgraduate/research-degrees/history/histmabyresexe/',
    '/postgraduate/research-degrees/history/histmabyres/',
    '/postgraduate/research-degrees/history/mphil-phdexe/',
    '/postgraduate/taught/business/hrm/',
    '/postgraduate/taught/law/masteroflaws/insurance/',
    '/postgraduate/taught/law/masteroflaws/property/',
    '/postgraduate/research-degrees/modlang/intermphilphd/',
    '/postgraduate/taught/law/masteroflaws/commercial/',
    '/postgraduate/taught/film/film-business-ma/',
    '/postgraduate/taught/history/int-heritage-ma/',
    '/postgraduate/taught/history/int-heritage-mres/',
    '/postgraduate/taught/history/int-heritage-pgcert/',
    '/postgraduate/taught/history/int-heritage-pgdip/',
    '/postgraduate/taught/law/masteroflaws/humanrights/',
    '/postgraduate/taught/law/masteroflaws/internationalconflictsecurity/',
    '/postgraduate/taught/business/international_management/',
    '/postgraduate/taught/politics/intrelma/',
    '/postgraduate/taught/engineering/supplymanagementmsc/',
    '/postgraduate/taught/business/international-tourism-msc/',
    '/postgraduate/taught/arabislamic/islamicstudiesma/',
    '/postgraduate/research-degrees/modlang/italmphilphd/',
    '/postgraduate/research-degrees/arabislamic/mphil-phd_kurdish/',
    '/postgraduate/taught/law/masteroflaws/',
    '/postgraduate/taught/education/educationma/languageliteracy/',
    '/postgraduate/research-degrees/law/mbyreslaw/',
    '/postgraduate/research-degrees/law/mphil-phd/',
    '/postgraduate/research-degrees/business/leadership/',
    '/postgraduate/research-degrees/law/legal/',
    '/postgraduate/taught/classics/classicsma/literary_interactions/',
    '/postgraduate/research-degrees/modlang/lusophone-mphilphd/',
    '/postgraduate/taught/sociology/food-studies-ma/',
    '/postgraduate/taught/business/exeter-mba/',
    '/postgraduate/taught/politics/public-administration/',
    '/postgraduate/research-degrees/business/management/',
    '/postgraduate/taught/business/managementmres/',
    '/postgraduate/research-degrees/history/maritime/',
    '/postgraduate/taught/law/masteroflaws/maritime/',
    '/postgraduate/taught/business/marketing/',
    '/postgraduate/taught/engineering/materialsmsc/',
    '/postgraduate/taught/engineering/materials-management-msc/',
    '/postgraduate/taught/education/educationma/mathematics/',
    '/postgraduate/research-degrees/mathematics/mathematics-phd/',
    '/postgraduate/research-degrees/mathematics/mathematics-mbyres/',
    '/postgraduate/taught/engineering/mechanicalmsc/',
    '/postgraduate/taught/engineering/mechanical-management-msc/',
    '/postgraduate/research-degrees/history/medical/',
    '/postgraduate/taught/medicine/medicalimagingmsc/',
    '/postgraduate/research-degrees/medicine/mscbyres-medical-imaging/',
    '/postgraduate/research-degrees/medicine/phd-md-ms/',
    '/postgraduate/research-degrees/medicine/mscbyres-medical-studies/',
    '/postgraduate/taught/history/medievalma/',
    '/postgraduate/research-degrees/history/medieval/',
    '/postgraduate/taught/medicine/methods-applied-health-services-pgcert/',
    '/postgraduate/research-degrees/arabislamic/mphil-phd_mepolitics/',
    '/postgraduate/taught/arabislamic/mideastmres/',
    '/postgraduate/taught/arabislamic/mideastislamicma/',
    '/postgraduate/taught/mining-engineering/msc-mining-engineering-professional/',
    '/postgraduate/taught/mining-engineering/msc-mining-engineering/',
    '/postgraduate/taught/geology/mining-geology-msc/',
    '/postgraduate/taught/mining-engineering/pgcert-mining-professional/',
    '/postgraduate/research-degrees/mining-engineering/mining-minerals-engineering/',
    '/postgraduate/research-degrees/modlang/mabyres/',
    '/postgraduate/taught/english/english-ma/moderncontemporary/',
    '/postgraduate/taught/economics/money_banking/',
    '/postgraduate/research-degrees/renewable-energy/offshore-renewable-energy/',
    '/postgraduate/taught/sport/paediatric/',
    '/postgraduate/research-degrees/arabislamic/mphil-phd_palestine/',
    '/postgraduate/research-degrees/drama/performance/',
    '/postgraduate/taught/sociology/philosophyma/',
    '/postgraduate/research-degrees/sociology/mares_philosophy/',
    '/postgraduate/research-degrees/sociology/mphil-phd_philosophy/',
    '/postgraduate/taught/sociology/philsocscima/',
    '/postgraduate/research-degrees/physics/',
    '/postgraduate/taught/politics/policyanalyticsmsc/',
    '/postgraduate/taught/politics/polthoughtma/',
    '/postgraduate/research-degrees/politics/mbyrespolitics/',
    '/postgraduate/research-degrees/politics/mbyrespolitics_cornwall/',
    '/postgraduate/research-degrees/politics/mphil-phd_pol/',
    '/postgraduate/taught/politics/politicsmres/',
    '/postgraduate/taught/politics/politics-international-relations-middle-east/',
    '/postgraduate/taught/education/professional_development/',
    '/postgraduate/taught/education/educationma/individual/',
    '/postgraduate/taught/psychology/psychological/',
    '/postgraduate/research-degrees/psychology/mphilphdpsy/',
    '/postgraduate/research-degrees/psychology/masters/',
    '/postgraduate/taught/politics/public-administration/',
    '/postgraduate/taught/english/english-ma/renaissancestudies/',
    '/postgraduate/taught/engineering/renewableenergyengineeringmsc/',
    '/postgraduate/research-degrees/renewable-energy/phd-masters-research/',
    '/postgraduate/taught/archaeology/romarchma/',
    '/postgraduate/research-degrees/modlang/russmphilphd/',
    '/postgraduate/research-degrees/education/eddoctoral/snie/',
    '/postgraduate/taught/education/educationma/science/',
    '/postgraduate/taught/sociology/scitechmres/',
    '/postgraduate/taught/politics/applied-security-strategy/',
    '/postgraduate/taught/politics/securitymres/',
    '/postgraduate/research-degrees/politics/mphil-pd_security/',
    '/postgraduate/taught/psychology/social/',
    '/postgraduate/taught/law/sociolegalmres/',
    '/postgraduate/taught/sociology/sociologyma/',
    '/postgraduate/research-degrees/sociology/mphil-phd_sociology/',
    '/postgraduate/taught/education/educationma/sen/',
    '/postgraduate/research-degrees/sport/mphilphdshs/',
    '/postgraduate/taught/sport/sporthealth/',
    '/postgraduate/research-degrees/sport/masters/',
    '/postgraduate/research-degrees/politics/mbyres_strategysecurity/',
    '/postgraduate/research-degrees/politics/mphil-pd_strategy_security/',
    '/postgraduate/taught/engineering/structuralmsc/',
    '/postgraduate/taught/engineering/structural-management-msc/',
    '/postgraduate/taught/mining-engineering/msc-surveying-environmental/',
    '/postgraduate/taught/geography/sustdev/',
    '/postgraduate/taught/geography/sustdev/',
    '/postgraduate/research-degrees/geography/sustainablefutures/',
    '/postgraduate/taught/geography/mressf/',
    '/postgraduate/research-degrees/education/eddoctoral/tesoldubai/',
    '/postgraduate/taught/education/tesolsummer/',
    '/postgraduate/research-degrees/education/eddoctoral/tesol/',
    '/postgraduate/taught/education/pgce/',
    '/postgraduate/taught/education/tesolmed/',
    '/postgraduate/taught/education/educationma/tct/',
    '/postgraduate/taught/drama/theatrema/',
    '/postgraduate/taught/theology/theologyma/',
    '/postgraduate/research-degrees/theology/marestheolrel/',
    '/postgraduate/research-degrees/theology/threlmmphilphd/',
    '/postgraduate/taught/languages/translation/',
    '/postgraduate/taught/languages/translation/',
    '/postgraduate/research-degrees/modlang/transmphilphd/',
    '/postgraduate/taught/mining-engineering/msc-tunnel-engineering/',
    '/postgraduate/taught/english/english-ma/victorianstudies/',
    '/postgraduate/taught/engineering/water-engineering/',
    '/postgraduate/taught/engineering/water-engineering-management-msc/',]

    for i in Lists:
        fullurl = base_url % i
        start_urls.append(fullurl)

    rules = (
        Rule(LinkExtractor(allow=r'https://www.exeter.ac.uk/postgraduate/all-courses/'), follow=True),
        Rule(LinkExtractor(allow=r'/postgraduate/taught/.*'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        print('==================================', response.url)

        item = HooliItem()

        url = response.url
        print(1, url)

        university = "EXETER postgraduate study and research"
        print(2, university)

        department = 'NULL'

        country = 'UK'
        city = 'NULL'
        website = 'https://www.exeter.ac.uk'

        programme = response.xpath('//div[@id="left-col"]//h1//text()').extract()
        programme = ''.join(programme)
        # Course = Course.replace('\r\n', '')
        print(3,programme)

        ucas_code = 'NULL'
        degree_level = '1'

        degree_type = response.xpath('//div[@id="left-col"]/h1/text()').extract()
        degree_type = ''.join(degree_type)
        print(4,degree_type)

        duration = response.xpath('//div[@class="panel-padding"]/table/tbody/tr/td/span[1]/text()').extract()
        duration = ''.join(duration)
        print(5, duration)

        start_date = response.xpath('//div[@class="panel-padding"]//table//tbody//tr[4]//td//text()').extract()
        start_date = ''.join(start_date).replace('\r\n', '')
        print(6,start_date)

        location = response.xpath('//div[@class="panel-padding"]//text()').extract()
        location = ''.join(location).replace('\r\n', '')
        print(7,location)

        ATAS = 'NULL'

        overview = response.xpath('//div[@id="Overview"]//text()').extract()
        overview = ''.join(overview).replace('\r\n', '')
        overview = overview.replace('\n','')
        print(8,overview)

        mode = response.xpath('//td[@class="exeter-course-duration"]/span/text()').extract()
        mode = ''.join(mode)
        print(9,mode)


        modules = response.xpath('//div[@id="myTabContent"]//text()').extract()
        modules = ''.join(modules).replace('\r\n','')
        modules = modules.replace('\n','')
        print(10,modules)

        teaching = 'NULL'

        assessment = response.xpath('//div[@id="Learning"]//text()').extract()
        assessment = ''.join(assessment).replace('\r\n','')
        # teaching_assessment = teaching_assessment.replace('\n', '')
        print(11,assessment)

        career = response.xpath('//div[@id="Careers"]//text()').extract()
        career = ''.join(career).replace('\r\n', '')
        career =  career.replace('\n', '')
        print(12,career)

        application_date = 'NULL'

        deadline = 'NULL'

        application_fee = 'NULL'

        entry_requirements = response.xpath('//div[@id="Entry-requirements"]//p[1]//text()').extract()
        entry_requirements = ''.join(entry_requirements)
        print(13,entry_requirements)

        chinese_requirements = 'NULL'

        TOEFL = response.xpath('//div[@id="Entry-requirements"]//p[6]//text()').extract()
        TOEFL = ''.join(TOEFL)
        print(14,TOEFL)

        TOEFL_L = 'NULL'
        TOEFL_S = 'NULL'
        TOEFL_R = 'NULL'
        TOEFL_W = 'NULL'

        IELTS = response.xpath('//div[@id="Entry-requirements"]//p[5]//text()').extract()
        IELTS = ''.join(IELTS)
        print(15,IELTS)

        IELTS_L = 'NULL'
        IELTS_S = 'NULL'
        IELTS_R = 'NULL'
        IELTS_W = 'NULL'

        tuition_fee = response.xpath('//div[@class="highlight-panel-fees"]//ul//li[2]//text()').extract()
        tuition_fee = ''.join(tuition_fee).replace('\r\n','')
        print(16,tuition_fee)

        Alevel = 'NULL'

        IB = 'NULL'

        # crawltime = datetime.datetime.now().strftime('%Y-%m-%d')
        # print(16,crawltime)


        GPA = 'UNLL'
        average_score = 'NULL'
        accredited_university = 'NULL'
        GRE = 'NULL'
        GMAT = 'NULL'
        LSAT = 'NULL'
        MCAT = 'NULL'
        working_experience = 'NULL'
        interview = 'NULL'
        portfolio = 'NULL'
        application_documents = 'NULL'
        how_to_apply = 'NULL'
        school_test = 'NULL'
        SATII = 'NULL'
        degree_description = 'NULL'
        SATI = 'NULL'
        SAT_code = 'NULL'
        ACT = 'NULL'
        ACT_code = 'NULL'
        other = response.xpath('//div[@class="span9"]//text()').extract()
        other = ''.join(other).replace('\r\n','')
        other = other.replace('\n','')
        print(17,other)

        create_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(18, create_time)

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