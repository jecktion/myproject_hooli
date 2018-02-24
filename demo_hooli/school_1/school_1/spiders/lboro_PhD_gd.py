




import scrapy
from school_1.items import HooliItem
import datetime
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import re

class PlymouthSpider(CrawlSpider):
    name = 'lboro_PhD_gd'
    allowed_domains = ['www.lboro.ac.uk']
    start_urls = []
    base_url = 'http://www.lboro.ac.uk/%s'

    Lists = ['/study/postgraduate/research-degrees/unfunded/complex-systems-environments/',
'/study/postgraduate/research-degrees/unfunded/synthesis-hydroxy-enones/',
'/study/postgraduate/research-degrees/unfunded/rehabilitation-non-union-fractures/',
'/study/postgraduate/research-degrees/unfunded/advanced-agile-architecture/',
'/study/postgraduate/research-degrees/unfunded/agent-based-cyber-physical-devices/',
'/study/postgraduate/research-degrees/unfunded/alloys-by-design/',
'/study/postgraduate/research-degrees/unfunded/composite-materials-damage-identification/',
'/study/postgraduate/research-degrees/unfunded/non-proteinogenic-amino-acids/',
'/study/postgraduate/research-degrees/unfunded/social-capacity-workplace-communities/',
'/study/postgraduate/research-degrees/unfunded/deep-learning-intelligence/',
'/study/postgraduate/research-degrees/unfunded/boron-sub-dyes/',
'/study/postgraduate/research-degrees/unfunded/electric-field-assisted-machining/',
'/study/postgraduate/research-degrees/unfunded/embroidered-ground-plane/',
'/study/postgraduate/research-degrees/unfunded/gas-plasma-technologies/',
'/study/postgraduate/research-degrees/unfunded/encapsulated-tadf-molecules/',
'/study/postgraduate/research-degrees/unfunded/circular-economy-for-leather-products/',
'/study/postgraduate/research-degrees/unfunded/executable-systems-architectures/',
'/study/postgraduate/research-degrees/unfunded/dietary-nitrate-metabolism/',
'/study/postgraduate/research-degrees/unfunded/finite-element-modelling/',
'/study/postgraduate/research-degrees/unfunded/fracture-problems-microstructured-materials/',
'/study/postgraduate/research-degrees/unfunded/high-data-rate-communications-interconnects-for-bo/',
'/study/postgraduate/research-degrees/unfunded/impact-performance-sports-balls/',
'/study/postgraduate/research-degrees/unfunded/integrable-systems-hydrodynamic-type/',
'/study/postgraduate/research-degrees/unfunded/altering-childrens-eating-behaviour/',
'/study/postgraduate/research-degrees/unfunded/cervical-cancer-acceptability/',
'/study/postgraduate/research-degrees/unfunded/business-solutions-business-economy/',
'/study/postgraduate/research-degrees/unfunded/kinesemiotics-wearable-sensor-technology/',
'/study/postgraduate/research-degrees/unfunded/cash-voucher-distribution-humanitarian-aid/',
'/study/postgraduate/research-degrees/unfunded/mechanics-advanced-materials/',
'/study/postgraduate/research-degrees/unfunded/mechanics-biometrials/',
'/study/postgraduate/research-degrees/unfunded/mega-sports-events/',
'/study/postgraduate/research-degrees/unfunded/dislocation-microstructure-interaction/',
'/study/postgraduate/research-degrees/unfunded/motivation-health-behaviours/',
'/study/postgraduate/research-degrees/unfunded/modelling-bone-fracture/',
'/study/postgraduate/research-degrees/unfunded/3d-prinitng-for-medical-modelling/',
'/study/postgraduate/research-degrees/unfunded/multiscale-modelling-deformation-twinning/',
'/study/postgraduate/research-degrees/unfunded/network-security-in-software-defined-networks/',
'/study/postgraduate/research-degrees/unfunded/novel-passive-microwave-devices/',
'/study/postgraduate/research-degrees/unfunded/cold-recycling-sheet-metals/',
'/study/postgraduate/research-degrees/unfunded/coach-leadership-athlete-relationship/',
'/study/postgraduate/research-degrees/unfunded/on-fabric-wearable-computers/',
'/study/postgraduate/research-degrees/unfunded/smart-prosthetic-lower-limb/',
'/study/postgraduate/research-degrees/unfunded/small-manufacturing-firms-process-monitoring/',
'/study/postgraduate/research-degrees/unfunded/successful-athletic-performance/',
'/study/postgraduate/research-degrees/unfunded/external-fire-spread-mechanism/',
'/study/postgraduate/research-degrees/unfunded/polycrystalline-laser-simulation/',
'/study/postgraduate/research-degrees/unfunded/single-material-multi-functional-products/',
'/study/postgraduate/research-degrees/unfunded/stunting-short-stature-cardiovascular-health/',
'/study/postgraduate/research-degrees/unfunded/cranial-plates-surgeon-led-design/',
'/study/postgraduate/research-degrees/unfunded/sustainable-energy-rural-off-grid-communities/',
'/study/postgraduate/research-degrees/unfunded/protective-equipment-performance/',
'/study/postgraduate/research-degrees/unfunded/health-and-physical-activity-knowledge/',
'/study/postgraduate/research-degrees/unfunded/cardiovascular-health-altered-menstrual-cycle/',
'/study/postgraduate/research-degrees/unfunded/implementation-of-eu-sports-policy/',
'/study/postgraduate/research-degrees/unfunded/lived-experience-concussion-injuries/',
'/study/postgraduate/research-degrees/unfunded/cricket-management-development-china/',
'/study/postgraduate/research-degrees/unfunded/fibroblasts-role-skeletal-muscle-ageing/',
'/study/postgraduate/research-degrees/unfunded/physical-education-addressing-childhood-obesity/',
'/study/postgraduate/research-degrees/unfunded/thermoregulatory-behaviour-in-humans/',
'/study/postgraduate/research-degrees/unfunded/recreating-neuromuscular-junction-formation/',
'/study/postgraduate/research-degrees/unfunded/tissue-engineered-joint-model/',
'/study/postgraduate/research-degrees/unfunded/traumatic-brain-injury/',
'/study/postgraduate/research-degrees/unfunded/ultraprecision-machining-silicon-carbide/',
'/study/postgraduate/research-degrees/unfunded/physical-performance-3d-protective-clothin/',
'/study/postgraduate/research-degrees/unfunded/skeletal-muscle-disuse-atrophy/',
'/study/postgraduate/research-degrees/unfunded/third-generation-artificial-turf/',
'/study/postgraduate/research-degrees/unfunded/cancer-cell-metabolic-flux-maps/',
'/study/postgraduate/research-degrees/unfunded/cancer-growth-mechanistic-effects/',
'/study/postgraduate/research-degrees/unfunded/engineered-complex-systems/',
'/study/postgraduate/research-degrees/unfunded/wearable-technology-robot-interaction/',]

    for i in Lists:
        fullurl = base_url % i
        start_urls.append(fullurl)

    rules = (
        Rule(LinkExtractor(allow=(r'.*'), restrict_xpaths=('//h2[@class="list__heading heading"]/a')), follow=True),
        # Rule(LinkExtractor(allow=r''),follow=True),
        Rule(LinkExtractor(allow=r'/study/postgraduate/research-degrees/unfunded/.*'),callback='parse_item', follow=False)
    )

    def parse_item(self,response):
        print('==================================',response.url)
        item = HooliItem()

        url = response.url
        print(1,url)

        university = 'Loughborough University PhD'
        print(2,university)

        department = 'NULL'
        # department = ''.join(department)
        # print(3,department)
        country = 'UK'
        city = "NULL"
        website = 'http://www.lboro.ac.uk'
        degree_level = '1'


        programme = response.xpath('//h1[@id="top"]//text()').extract()
        programme = ''.join(programme)
        print(3,programme)

        ucas_code = 'NULL'



        degree_type = response.xpath('//h1[@id="top"]/span/text()').extract()
        degree_type = ''.join(degree_type)
        print(4,degree_type)

        start_date_str = response.xpath('//div[@class="list__content icon icon--calendar"]//text()').extract()
        start_date_str = ''.join(start_date_str).replace('\r\n', '')
        try:
            if "Start date:" in start_date_str:
                start = start_date_str.find("Start date:")
                end = start_date_str.find("Application deadline:")
                start_date = start_date_str[start:end]
                item["start_date"] = start_date
            else:
                start_date = "NULL"
        except:
            start_date = "报错"
        print(5,start_date)

        overview = response.xpath('//div[@class="editor"]/p/text()').extract()
        overview = ''.join(overview).replace('\n', '')
        print(6, overview)

        mode = response.xpath('//div[@class="list__content icon icon--clock"]//text()').extract()
        mode = ''.join(mode).replace('\r\n','')
        mode = mode.replace('   ','')
        print(7, mode)


        duration = response.xpath('//div[@class="list__content icon icon--clock"]//text()').extract()
        duration = ''.join(duration).replace('\r\n','')
        print(8,duration)

        modules = ''
        # modules = ''.join(modules).replace('\r\n','')
        # modules = modules.replace('\n','')
        # print(9,modules)

        teaching = 'NULL'

        assessment = 'NULL'
        # teaching_assessment = ''.join(teaching_assessment)
        # print(10, teaching_assessment)

        career = 'NULL'
        # career = ''.join(career).replace('\n', '')
        # print(11, career)

        application_date = 'NULL'

        deadline = response.xpath('//div[@class="list__content icon icon--calendar"]//text()').extract()
        deadline = ''.join(deadline).replace('\r\n', '')
        print(12,deadline)

        application_fee = 'NULL'

        tuition_fee = response.xpath('//div[@class="list__content icon icon--money"]//text()').extract()
        tuition_fee = ''.join(tuition_fee).replace('\r\n', '')
        tuition_fee = tuition_fee.replace('   ','')
        print(13, tuition_fee)

        location = response.xpath('//div[@class="list__content  icon icon--location"]/dd/a/text()').extract()
        location = ''.join(location)
        print(14,location)


        GPA = 'NULL'
        ATAS = 'NULL'

        average_score = 'NULL'

        accredited_university = 'NULL'

        Alevel = 'NULL'

        IB = 'NULL'

        IELTS = 'NULL'
        # IELTS = ''.join(IELTS).replace('\r\n','')
        # # IELTS = re.findall('(IELTS:|IELTS)? (.*){0,5} \d?.\d? .{0,70}',IELTS)
        # print(14, IELTS)

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

        how_to_apply = response.xpath('//div[@class="intro"]/p/text()').extract()
        how_to_apply = ''.join(how_to_apply)
        print(15,how_to_apply)

        entry_requirements = response.xpath('//div[@class="toggle__content-container"]//text()').extract()
        entry_requirements = ''.join(entry_requirements).replace('\r\n','')
        # EntryRequirements = EntryRequirements.replace(' ','')
        print(16,entry_requirements)

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