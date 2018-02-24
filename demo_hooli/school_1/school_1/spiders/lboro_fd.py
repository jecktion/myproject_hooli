


import scrapy
from school_1.items import HooliItem
import datetime
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import re

class PlymouthSpider(CrawlSpider):
    name = 'lboro_fd'
    allowed_domains = ['www.lboro.ac.uk']
    start_urls = []
    base_url = 'http://www.lboro.ac.uk/%s'

    Lists = ['/study/postgraduate/research-degrees/funded/3d-data-capture/',
'/study/postgraduate/research-degrees/funded/3d-printed-chemical-reactors/',
'/study/postgraduate/research-degrees/funded/bioresorbable-medical-devices/',
'/study/postgraduate/research-degrees/funded/forecasting-global-hydrological-extremes/',
'/study/postgraduate/research-degrees/funded/beam-steering-antenna-arrays/',
'/study/postgraduate/research-degrees/funded/action-event-detection/',
'/study/postgraduate/research-degrees/funded/manufacturing-digital-revolution/',
'/study/postgraduate/research-degrees/funded/amorphous-solids-analytic-description/',
'/study/postgraduate/research-degrees/funded/channel-vegetation-impact/',
'/study/postgraduate/research-degrees/funded/cyber-physical-systems/',
'/study/postgraduate/research-degrees/funded/automorphic-lie-algebras/',
'/study/postgraduate/research-degrees/funded/storm-surge-catastrophe-modelling/',
'/study/postgraduate/research-degrees/funded/human-aging-biomarkers/',
'/study/postgraduate/research-degrees/funded/underwater-vehicle-navigation/',
'/study/postgraduate/research-degrees/funded/low-inertia-systems/',
'/study/postgraduate/research-degrees/funded/cyber-human-integration/',
'/study/postgraduate/research-degrees/funded/high-entropy-alloys/',
'/study/postgraduate/research-degrees/funded/mild-slope-computational-models/',
'/study/postgraduate/research-degrees/funded/golf-swing-analysis/',
'/study/postgraduate/research-degrees/funded/advanced-sensing-manufacturing-systems/',
'/study/postgraduate/research-degrees/funded/dust-fluxes/',
'/study/postgraduate/research-degrees/funded/synthetic-inertia-control/',
'/study/postgraduate/research-degrees/funded/circular-economy-principles/',
'/study/postgraduate/research-degrees/funded/energy-demand-london-lboro/',
'/study/postgraduate/research-degrees/funded/energy-harvesting/',
'/study/postgraduate/research-degrees/funded/manufacturing-corneal-tissues/',
'/study/postgraduate/research-degrees/funded/community-based-geohazard-response-schemes/',
'/study/postgraduate/research-degrees/funded/fjord-meltwater-delivery/',
'/study/postgraduate/research-degrees/funded/fractal-structures/',
'/study/postgraduate/research-degrees/funded/mechatronic-rail-vehicle-development/',
'/study/postgraduate/research-degrees/funded/complex-functional-molecules-synthesis/',
'/study/postgraduate/research-degrees/funded/hybrid-additive-manufacturing/',
'/study/postgraduate/research-degrees/funded/hybrid-deep-learning-accelerators/',
'/study/postgraduate/research-degrees/funded/hyperbolic-equations/',
'/study/postgraduate/research-degrees/funded/spatial-mapping-accuracy/',
'/study/postgraduate/research-degrees/funded/golf-equipment-construction/',
'/study/postgraduate/research-degrees/funded/trackbed-construction-quality/',
'/study/postgraduate/research-degrees/funded/diamond-structures-laser-modification/',
'/study/postgraduate/research-degrees/funded/laser-surface-treatments/',
'/study/postgraduate/research-degrees/funded/nuclear-graphite-radiation-damage/',
'/study/postgraduate/research-degrees/funded/low-carbon-district-heating/',
'/study/postgraduate/research-degrees/funded/telecommunication-networks-machine-learning/',
'/study/postgraduate/research-degrees/funded/ultra-dense-networks/',
'/study/postgraduate/research-degrees/funded/metal-alloys-material-instability/',
'/study/postgraduate/research-degrees/funded/droplets-on-surfaces-modelling/',
'/study/postgraduate/research-degrees/funded/modular-metabolic-engineering/',
'/study/postgraduate/research-degrees/funded/multi-scale-remote-sensing/',
'/study/postgraduate/research-degrees/funded/multidimensional-integrable-systems/',
'/study/postgraduate/research-degrees/funded/multidimensional-quasilinear-systems/',
'/study/postgraduate/research-degrees/funded/nano-particle-transport/',
'/study/postgraduate/research-degrees/funded/software-defined-networks/',
'/study/postgraduate/research-degrees/funded/nonlinear-internal-waves/',
'/study/postgraduate/research-degrees/funded/ultra-low-engine-emissions/',
'/study/postgraduate/research-degrees/funded/politics-international-relations/',
'/study/postgraduate/research-degrees/funded/phd-architecture-building-civil-engineering/',
'/study/postgraduate/research-degrees/funded/social-political-geographical-sciences/',
'/study/postgraduate/research-degrees/funded/science-phd-studentships/',
'/study/postgraduate/research-degrees/funded/arts-english-drama/',
'/study/postgraduate/research-degrees/funded/post-fire-dunefield-ecological-recovery/',
'/study/postgraduate/research-degrees/funded/pgta-physiology/',
'/study/postgraduate/research-degrees/funded/teaching-assistant-biomechanics/',
'/study/postgraduate/research-degrees/funded/power-electronic-converters/',
'/study/postgraduate/research-degrees/funded/powertrain-resource-optimisation/',
'/study/postgraduate/research-degrees/funded/preschool-children-mathematics/',
'/study/postgraduate/research-degrees/funded/unique-tracking-information/',
'/study/postgraduate/research-degrees/funded/spin-caloritronic-device-applications/',
'/study/postgraduate/research-degrees/funded/transfer-operator-techniques/',
'/study/postgraduate/research-degrees/funded/rational-interaction-autonomous-systems/',
'/study/postgraduate/research-degrees/funded/resilient-network-policy-enforcement/',
'/study/postgraduate/research-degrees/funded/railway-infrastructure-autonomy/',
'/study/postgraduate/research-degrees/funded/mechatronic-rail-vehicles/',
'/study/postgraduate/research-degrees/funded/special-purpose-networks/',
'/study/postgraduate/research-degrees/funded/thermal-magnetic-currents/',
'/study/postgraduate/research-degrees/funded/mapping-vegetation-patterns/',
'/study/postgraduate/research-degrees/funded/spectral-correlations-random-matrices/',
'/study/postgraduate/research-degrees/funded/string-logic-query-languages/',
'/study/postgraduate/research-degrees/funded/symbol-grounding-problem/',
'/study/postgraduate/research-degrees/funded/tribological-contacts-nanoparticles/',
'/study/postgraduate/research-degrees/funded/tailorable-heterogenous-catalysts/',
'/study/postgraduate/research-degrees/funded/virtual-railway-network/',
'/study/postgraduate/research-degrees/funded/pv-systems-operational-environment/',
'/study/postgraduate/research-degrees/funded/phase-field-crystal-model/',
'/study/postgraduate/research-degrees/funded/deep-learning-networks/',
'/study/postgraduate/research-degrees/funded/hybrid-electric-vehicles-powertrains/',
'/study/postgraduate/research-degrees/funded/electromechanical-actuators-uncertainty/',
'/study/postgraduate/research-degrees/funded/advanced-xray-characterisation/',
'/study/postgraduate/research-degrees/funded/variations-pattern-languages/',
'/study/postgraduate/research-degrees/funded/evolutionary-response-to-tropical-lake-disruption/',
'/study/postgraduate/research-degrees/funded/complex-sos-environments/',]

    for i in Lists:
        fullurl = base_url % i
        start_urls.append(fullurl)

    rules = (
        Rule(LinkExtractor(allow=(r'.*'), restrict_xpaths=('//h2[@class="list__heading heading"]/a/@href')), follow=True),
        # Rule(LinkExtractor(allow=r'www.gold.ac.uk/course-finder/results/\?collection=goldsmiths-courses&sort=Title&f.Level%7Clevel=Postgraduate&start_rank=\d+'), follow=True),
        # Rule(LinkExtractor(allow=(r'.*'), restrict_xpaths=('//div[@class="teaser__body media__body"]/h3/a')),follow=True),
        Rule(LinkExtractor(allow=r'/study/postgraduate/research-degrees/funded/.*'),callback='parse_item', follow=False),
    )

    def parse_item(self,response):
        print('==================================',response.url)
        item = HooliItem()

        url = response.url
        print(1,url)

        university = 'Loughborough University'
        print(2,university)

        department = response.xpath('//dd[@class="list__item--definition"]/text()').extract()
        department = ''.join(department)
        print(3,department)

        country = 'UK'
        city = 'NULL'
        website = 'http://www.lboro.ac.uk'
        degree_level = '1'

        programme = response.xpath('//h1[@id="top"]//text()').extract()
        programme = ''.join(programme)
        print(4,programme)

        ucas_code = 'NULL'
        # Master = ''.join(Master)

        degree_type = response.xpath('//h1[@id="top"]/span/text()').extract()
        degree_type = ''.join(degree_type)
        print(5,degree_type)

        start_date_str = response.xpath('//div[@class="list__content icon icon--calendar"]//text()').extract()
        start_date_str = ''.join(start_date_str)
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
        print(6,start_date)

        overview = response.xpath('//div[@class="content-type content-type--main"]//text()').extract()
        overview = ''.join(overview)
        print(7, overview)

        mode = response.xpath('//div[@class="list__content icon icon--clock"]//text()').extract()
        mode = ''.join(mode)
        print(8,mode)



        duration = response.xpath('//div[@class="list__content icon icon--clock"]//text()').extract()
        duration = ''.join(duration)
        # Duration = Duration.replace('   ','')
        print(9,duration)

        modules = 'NULL'
        # modules = ''.join(modules).replace('\n','')
        # modules = modules.replace('\n','')
        # print(8,modules)

        teaching = 'NULL'

        assessment = 'NULL'
        # teaching_assessment = ''.join(teaching_assessment).replace('\n','')
        # print(9, teaching_assessment)

        career = 'NULL'
        # career = ''.join(career).replace('\n', '')
        # print(10, career)

        application_date = 'NULL'

        deadline_str = response.xpath('//div[@class="list__content icon icon--calendar"]//text()').extract()
        deadline_str = ''.join(deadline_str)
        try:
            if "Application deadline:" in deadline_str:
                start = deadline_str.find("Application deadline:")
                deadline = deadline_str[start:]
                item["deadline"] = deadline
            else:
                deadline = "NULL"
        except:
            deadline = "报错!"
        print(10,deadline)

        application_fee = 'NULL'

        tuition_fee= response.xpath('//div[@class="list__content icon icon--money"]//text()').extract()
        tuition_fee = ''.join(tuition_fee)
        # tuition_fee = tuition_fee.replace('   ','')
        print(11,tuition_fee)

        location_str = response.xpath('//dl[@class="list list--definition list--pg-programme"]//text()').extract()
        location_str = ''.join(location_str).replace('\r\n','')
        location_str = location_str.replace('    ','')
        try:
            if "Location:" in location_str:
                start = location_str.find("Location:")
                end = location_str.find("Application deadline:")
                location = location_str[start:end]
                item["location"] = location
            else:
                location = "NULL"
        except:
            location = "报错!"
        print(12,location)

        ATAS = 'NULL'
        GPA = 'NULL'

        accredited_university = 'NULL'

        IELTS = 'NULL'
        # IELTS = ''.join(IELTS).replace('\n','')
        # # IELTS = re.findall('(IELTS:|IELTS)? (.*){0,5} \d?.\d? .{0,70}',IELTS)
        # print(11, IELTS)

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
        LSAT= 'NULL'
        MCAT= 'NULL'

        average_score = 'NULL'

        Alevel = 'NULL'

        IB = 'NULL'

        working_experience = 'NULL'

        interview = 'NULL'

        portfolio = 'NULL'

        application_documents = 'NULL'

        how_to_apply = response.xpath('//div[@class="editor"]//text()').extract()
        how_to_apply = ''.join(how_to_apply)
        print(13,how_to_apply)

        entry_requirements = response.xpath('//div[@class="editor"]//text()').extract()
        entry_requirements = ''.join(entry_requirements)
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

