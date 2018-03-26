# -*- coding: utf-8 -*-






import scrapy
from school_3.items import HooliItem
import datetime
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import re
import time
from lxml import etree
import requests
from school_3.getDegree_type import getDegree_type
from school_3.clearSpace import clear_space
from school_3.getItem import get_item

class PlymouthSpider(scrapy.Spider):
    name = 'murdoch_ug'
    allowed_domains = ['www.murdoch.edu.au']
    start_urls = []

    # url = 'http://www.murdoch.edu.au/course-search-results/'
    # endurl = '?searchQuery=undergraduate&studyLevel=undergraduate&indexCatalogue=rses&wordsMode=AllWords&studyLevel_radio=undergraduate&atarMin=60&atarMax=100&studyMode=all&schools=all'
    # offset = 1
    # start_urls = [url + str(offset) + endurl]
    # print(start_urls)

    base_url = 'http://www.murdoch.edu.au%s'

    Lists = ['/study/courses/course-details/Banking-(BBus)',
'/study/courses/course-details/Hospitality-and-Tourism-Management-(BBus)',
'/study/courses/course-details/Marketing-(BBus)',
'/study/courses/course-details/Human-Resources-Management-(BBus)',
'/study/courses/course-details/Business-Law-(BBus)',
'/study/courses/course-details/Accounting-(BBus)',
'/study/courses/course-details/Finance-(BBus)',
'/study/courses/course-details/Management-(BBus)',
'/study/courses/course-details/Economics-(BBus)',
'/study/courses/course-details/Secondary-Teaching-(Arts-Combined-English)-(BEd)(BA)',
'/study/courses/course-details/Electrical-Power-Engineering-Honours-(BE(Hons))',
'/study/courses/course-details/Games-Art-and-Design-(BCrMedia)',
'/study/courses/course-details/Psychology-(BA)',
'/study/courses/course-details/Secondary-Teaching-(Combined-Science-Degrees)-(BEd)(BSc)',
'/study/courses/course-details/law-(llb-llb(hons))',
'/study/courses/course-details/Games-Technology-(BSc)',
'/study/courses/course-details/Chiropractic-Science--Clinical-Chiropractic-(BSc)(BClinChiro)',
'/study/courses/course-details/Global-Media-and-Communication-(BCommun)',
'/study/courses/course-details/Sound-(BCrMedia)',
'/study/courses/course-details/Conservation-and-Wildlife-Biology-(BSc)',
'/study/courses/course-details/Sustainable-Development-(BA)',
'/study/courses/course-details/Mobile-and-Web-Application-Development-(BSc)',
'/study/courses/course-details/Theatre-and-Drama-(BA)',
'/study/courses/course-details/Crime-Science-(BCrim)',
'/study/courses/course-details/Forensic-Biology-and-Toxicology-(BSc)',
'/study/courses/course-details/Communication--Creative-Media-(Combined)-(BCrMedia)(BCommun)',
'/study/courses/course-details/Philosophy-(BA)',
'/study/courses/course-details/Secondary-Teaching-(Arts-Combined-History)-(BEd)(BA)',
'/study/courses/course-details/Security-Terrorism-and-Counterterrorism-Studies-(BA)',
'/study/courses/course-details/Laboratory-Medicine-(BScBLabMed)',
'/study/courses/course-details/Games-Software-Design-and-Production-(BSc)',
'/study/courses/course-details/Engineering-Technology-(BSc)',
'/study/courses/course-details/Japanese-(BA)',
'/study/courses/course-details/Computer-Science-(BSc)',
'/study/courses/course-details/Photography-(BCrMedia)',
'/study/courses/course-details/Sport-and-Exercise-Science--Psychology-(BSportExSc)(BSc)',
'/study/courses/course-details/law-communication-combined-(bcommun-llb)',
'/study/courses/course-details/Law--Business-(Combined)-(LLB)(BBus)',
'/study/courses/course-details/Criminal-Behaviour-(BCrim)',
'/study/courses/course-details/Clinical-Laboratory-Science-(BSc)',
'/study/courses/course-details/Sociology-(BA)',
'/study/courses/course-details/Law--Science-(Combined)-(LLB)(BSc)',
'/study/courses/course-details/English-and-Creative-Writing-(BA)',
'/study/courses/course-details/Psychology-(BSc)',
'/study/courses/course-details/law-psychology-combined-(llb-bsc)',
'/study/courses/course-details/Criminology--Psychology-(Combined)-(BCrim)(BA)',
'/study/courses/course-details/Internetworking-and-Network-Security-(BSc)',
'/study/courses/course-details/criminology-communication-combined-(bcrim-bcommun)',
'/study/courses/course-details/Screen-Production-(BCrMedia)',
'/study/courses/course-details/Community-Development-(BA)',
'/study/courses/course-details/History-(BA)',
'/study/courses/course-details/Biomedical-Science-(BSc)',
'/study/courses/course-details/Journalism-(BCommun)',
'/study/courses/course-details/Law--Arts-(Combined)-(LLB)(BA)',
'/study/courses/course-details/Secondary-Teaching-(Science-Combined-Sport-and-Health-Science)-(BEd)(BSc)',
'/study/courses/course-details/Environmental-Science-(BSc)',
'/study/courses/course-details/Legal-Studies-(BCrim)',
'/study/courses/course-details/Law-(LLB-LLB(Hons))',
'/study/courses/course-details/Indonesian-(BA)',
'/study/courses/course-details/Graphic-Design-(BCrMedia)',
'/study/courses/course-details/Law--Criminology-(Combined)-(BCrim)(LLB)',
'/study/courses/course-details/Primary-Teaching-(BEd)',
'/study/courses/course-details/Veterinary-Science-(BSc)(DVM)',
'/study/courses/course-details/Global-Politics-and-Policy-(BA)',
'/study/courses/course-details/Business-Information-Systems-(BSc)',
'/study/courses/course-details/Instrumentation-and-Control-Engineering-Honours-(BE(Hons))',
'/study/courses/course-details/criminology-forensic-biology-and-toxicology-combined',
'/study/courses/course-details/Mathematics-and-Statistics-(BSc)',
'/study/courses/course-details/Environmental-Engineering-Honours-(BE(Hons))',
'/study/courses/course-details/law-psychology-combined-(llb-ba)',
'/study/courses/course-details/Animal-Health-(BSc)',
'/study/courses/course-details/Genetics-and-Molecular-Biology-(BSc)',
'/study/courses/course-details/Mineral-Science-(BSc)',
'/study/courses/course-details/Tourism-and-Events-(BA)',
'/study/courses/course-details/Renewable-Energy-Engineering-Honours-(BE(Hons))',
'/study/courses/course-details/marine-biology-(bsc)',
'/study/courses/course-details/Chemical-and-Metallurgical-Engineering-Honours-(BE(Hons))',
'/study/courses/course-details/sport-and-health-science-(bsc)',
'/study/courses/course-details/Sport-and-Exercise-Science-(BSportExSc)',
'/study/courses/course-details/Environmental-Management-and-Sustainability-(BSc)',
'/study/courses/course-details/Secondary-Teaching-(Science-Combined-Mathematics)-(BEd)(BSc)',
'/study/courses/course-details/Animal-Science-(BSc)',
'/study/courses/course-details/International-Aid-and-Development-(BA)',
'/study/courses/course-details/Primary-1-10-Health-and-Physical-Education-(BEd)',
'/study/courses/course-details/Marine-Science-(BSc)',
'/study/courses/course-details/Crop-and-Pasture-Science-(BSc)',
'/study/courses/course-details/Sport-and-Exercise-Science--Clinical-Exercise-Physiology-(BSportExSc)(GradDipClinExPhys)',
'/study/courses/course-details/Cyber-Security-and-Forensics-(BSc)',
'/study/courses/course-details/Biological-Sciences-(BSc)',
'/study/courses/course-details/Physics-and-Nanotechnology-(BSc)',
'/study/courses/course-details/Industrial-Computer-Systems-Engineering-Honours-(BE(Hons))',
'/study/courses/course-details/Chemistry-(BSc)',
'/study/courses/course-details/Strategic-Communication-(BCommun)',
'/study/courses/course-details/Early-Childhood-and-Primary-Teaching-(BEd)',
'/study/courses/course-details/Nursing-(BNurs)']



    for i in Lists:
        fullurl = base_url % i
        start_urls.append(fullurl)


    def parse(self,response):
        print(1,'==================================',response.url)
        item = get_item(HooliItem)


        department_s = response.xpath('//*[@id="course-description-and-structure"]//ul[@class="list-col-2-sm list-col-top-border"]/li[3]//text()').extract()
        department_s = ''.join(department_s).replace('\r\n','')
        try:
            if "School" in department_s:
                start = department_s.find("School")
                department = department_s[start:]
                # department = department[:]
                department = department.lstrip("School").strip()

            else:
                department = "NULL"

        except:
            department = "报错!"
        print('department:',department)
        time.sleep(0.2)

        # programme = response.xpath('//div[@class="section picture-nav"]/h1/text()').extract()
        programme = response.xpath('//*[@id="course-overview"]//div[@class="article article--row"]/h1/text()').extract()
        programme = ''.join(programme)
        print('programme:',programme)
        #
        ucas_code_s = response.xpath('//*[@id="main"]//div[@data-student-origin="international"]//text()').extract()
        ucas_code_s = ''.join(ucas_code_s).replace('\r\n','')
        try:
            if "Course Code" in ucas_code_s:
                start = ucas_code_s.find("Course Code")
                ucas_code = ucas_code_s[start:]
                ucas_code = ucas_code[:100]
                ucas_code = ucas_code.lstrip("Course Code")

            else:
                ucas_code = "NULL"
        except:
            ucas_code = "报错!"

        # # print(5,ucas_code)
        #
        # degree_type = response.xpath('//div[@class="section picture-nav"]/h1/text()').extract()
        degree_type = response.xpath('//*[@id="course-overview"]//div[@class="article article--row"]/h3/text()').extract()
        degree_type = ''.join(degree_type)
        degree_type = getDegree_type(degree_type)


        # overview = response.xpath('//div[@class="left logo-bg"]//text()').extract()
        overview = response.xpath('//*[@id="course-description-and-structure"]//div[@class="article article--row"]/p/text()').extract()
        overview = ''.join(overview)

        mode_s = response.xpath('//*[@id="main"]//div[@data-student-origin="international"]//text()').extract()
        mode_s = ''.join(mode_s).replace('\r\n','')
        try:
            if "Study Mode" in mode_s:
                start = mode_s.find("Study Mode")
                mode = mode_s[start:]
                mode = mode[:100]
                mode = mode.lstrip("Study Mode")
            else:
                mode = "NULL"
        except:
            mode = "报错!"

        duration_s = response.xpath('//*[@id="main"]//div[@data-student-origin="international"]//text()').extract()
        duration_s = ''.join(duration_s).replace('\r\n','')
        if "Course Duration" in duration_s:
            start= duration_s.find("Course Duration")
            duration = duration_s[start:]
            duration = duration[:100]
            duration = duration.lstrip("Course Duration")

        else:
            duration = "NULL"

        location_s = response.xpath('//*[@id="course-description-and-structure"]//ul[@class="list-col-2-sm list-col-top-border"]/li//text()').extract()
        location_s = ''.join(location_s).replace('\r\n','')
        try:
            if "Location" in location_s:
                start = location_s.find("Location")
                location = location_s[start:]
                location = location[:100]
                location = location.lstrip("Location")

            else:
                location = "NULL"
        except:
            location = "报错!"
        # print(11,location)

        how_to_apply = response.xpath('//*[@id="how-to-apply"]//div[@class="article article--row"]//text()').extract()
        how_to_apply = ''.join(how_to_apply).replace('\r\n','').replace('\n','')

        create_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(15, create_time)

        modules_s = response.xpath('//*[@id="course-description-and-structure"]//p/a/@href').extract()[-1]
        print(modules_s, '============')
        modules_s = ''.join(modules_s)
        #http://goto.murdoch.edu.au
        #http://www.murdoch.edu.au
        if "http" in modules_s:
            modules_links = modules_s
        else:
            modules_links = 'http://www.murdoch.edu.au' + modules_s
        print("modules_links:", modules_links)
        self.parse_modules(modules_links, item)

        entry_requirements_url = response.xpath('//div[@id="entry-content"]/@data-url').extract()
        entry_requirements_url = ''.join(entry_requirements_url)
        dates = {"Accounting (BBus)": "ACCBCOMM",
                 "Accounting Honours (BBus(Hons))": "ACCBCOMH2",
                 "Animal Health (BSc)": "91384",
                 "Animal Health Honours (BSc(Hons))": "23000",
                 "Animal Science (BSc)": "60856M",
                 "Animal Science Honours (BSc(Hons))": "62307",
                 "Applied Psychology + Doctor of Philosophy (MAppPsych)+(PhD)": "71156",
                 "Applied Psychology [Clinical Psychology] (MAppPsych)": "11767",
                 "Applied Psychology [Organisational Psychology] (MAppPsych + PhD)": "71156",
                 "Applied Psychology [Organisational Psychology] (MAppPsych)": "89177",
                 "Applied Psychology [Professional] (MAppPsych(Professional))": "56356",
                 "Asian Language [In-Country] (GradDipAsianLangIn-Country)": "82755",
                 "Asian Studies (BA)": "ASSTBM",
                 "Asian Studies (GradCertAsianSt)": "13713",
                 "Asian Studies Honours (BA(Hons))": "ASSTBH",
                 "Australian Indigenous Studies (BA)": "AISBM",
                 "Australian Indigenous Studies Honours (BA(Hons))": "AISBH",
                 "Banking (BBus)": "BANKBCOMM",
                 "Banking Honours (BBus(Hons))": "BANKBCOMH2",
                 "Biological Sciences (BSc)": "BSBM",
                 "Biological Sciences Honours (BSc(Hons))": "BSBH",
                 "Biomedical Science (BSc)": "BIOMSCBM",
                 "Biomedical Science Honours (BSc(Hons))": "BIOMSCBH",
                 "Biosecurity (MBiosec)": "21380",
                 "Biotechnology Honours (BSc(Hons))": "BIOTBSCH",
                 "Business Administration (GradCertBusAdmin)": "BAPC",
                 "Business Administration (GradDipBusAdmin)": "BAPD",
                 "Business Administration (MBA)": "26871",
                 "Business Administration Professional Practice (MBA(PP))": "96933",
                 "Business Administration [MasterClass] (GradCertBusAdmin)": "95187",
                 "Business Administration [Offshore] (MBA)": "BAM",
                 "Business Information Systems (BSc)": "BISBSCM",
                 "Business Information Systems Honours (BSc(Hons))": "41032",
                 "Business Law (BBus)": "BUSLAWBCOMM",
                 "Business Law Honours (BBus(Hons))": "BUSLAWBCOMH2",
                 "Chaplaincy (GradDipChap)": "11699",
                 "Chaplaincy (MChap)": "57569",
                 "Chemical and Metallurgical Engineering Honours (BE(Hons))": "ENG10011M2",
                 "Chemistry (BSc)": "CHEBM",
                 "Chemistry Honours (BSc(Hons))": "CHEBH",
                 "Chiropractic Honours (BSc(Hons))": "CHIROH",
                 "Chiropractic Science + Clinical Chiropractic (BSc)+(BClinChiro)": "59021",
                 "Clinical Exercise Physiology (GradDipClinExPhys)": "79542",
                 "Clinical Laboratory Science (BSc)": "1637",
                 "Cognitive Neuroscience and Health Psychology (BSc)": "78925",
                 "Communication + Creative Media [Combined] (BCrMedia)+(BCommun)": "66243",
                 "Communication Honours (BCommun(Hons))": "75974",
                 "Communication Management (MCommM)": "9414",
                 "Communication and Media Studies Honours (BA(Hons))": "COMUNMED",
                 "Community Development (BA)": "COMMDEVBM",
                 "Community Development (GradCertCommDev)": "80005",
                 "Community Development (GradDipCommDev)": "58193",
                 "Community Development (MCommDev)": "99647",
                 "Community Development Honours (BA(Hons))": "COMMDEVBH",
                 "Computer Science (BSc)": "COMPSCM",
                 "Computer Science Honours (BSc(Hons))": "74320",
                 "Conservation and Wildlife Biology (BSc)": "CBBSCM",
                 "Conservation and Wildlife Biology Honours (BSc(Hons))": "CBBSCH",
                 "Consultancy Psychology (GradDipConsultPsych)": "49662",
                 "Counselling (GradCertCounsel)": "36509",
                 "Counselling (GradDipCounsel)": "10627",
                 "Counselling (MCounsel)": "23267",
                 "Creative Media Honours (BCrMedia(Hons))": "72001",
                 "Crime Science (BCrim)": "23788",
                 "Criminal Behaviour (BCrim)": "47454",
                 "Criminology + Communication [Combined]": "98717",
                 "Criminology + Forensic Biology and Toxicology [Combined]": "99288",
                 "Criminology + Psychology [Combined] (BCrim)+(BA)": "54244",
                 "Crop and Pasture Science (BSc)": "79087",
                 "Crop and Pasture Science Honours (BSc(Hons))": "7865",
                 "Cyber Forensics and Information Security (BSc)": "12046M",
                 "Cyber Forensics and Information Security Honours (BSc(Hons))": "30838",
                 "Development Studies (GradCertDS)": "85232",
                 "Development Studies (MDS)": "16059",
                 "Divinity (MDiv)": "37662",
                 "Doctor of Philosophy (PhD)": "PHILD",
                 "Doctor of Psychology (Clinical Psychology) (DPsych)": "67205",
                 "Early Childhood Education (GradCertEarlyChildEd)": "ECEDGC",
                 "Early Childhood and Primary Teaching (BEd)": "EDECPTBM",
                 "Economics (BBus)": "ECONBM",
                 "Economics Honours (BBus(Hons))": "ECONBH2",
                 "Education (EdD)": "EDD",
                 "Education [Coursework] (MEd)": "EDM2",
                 "Education [Primary] (MTeachPrim)": "22721",
                 "Education [Research] (MEd(Res))": "10079",
                 "Education [Secondary] (GradDipEd)": "EDSGD",
                 "Education [Tertiary and Adult] (GradCertTerAdEd)": "TAEDGC",
                 "Education [Tertiary and Adult] (GradDipEd)": "ETAGD",
                 "Electrical Power Engineering Honours (BE(Hons))": "ENGPOWM2",
                 "Energy Studies (GradCertEnSt)": "54978",
                 "Energy Studies (GradDipEnSt)": "73302",
                 "Energy and the Environment (GradDipEnEnv)": "EEPD",
                 "Engineering (GradDipEng)": "47788",
                 "Engineering (ME)": "ENGM",
                 "Engineering Technology (BSc)": "ENGTBM",
                 "English and Creative Writing (BA)": "ENGLBM",
                 "English and Creative Writing Honours (BA(Hons))": "ENGLBH",
                 "Environmental Assessment and Management (GradCertEnvAsstMan)": "EMPC",
                 "Environmental Engineering Honours (BE(Hons))": "97999M2",
                 "Environmental Management and Sustainability (BSc)": "33427M",
                 "Environmental Management and Sustainability Honours (BSc(Hons))": "40976",
                 "Environmental Science (BSc)": "ENVSCBENVSCM",
                 "Environmental Science (GradCertEnvSc)": "41299",
                 "Environmental Science (GradDipEnv)": "EMPD",
                 "Environmental Science (MEnvSc)": "SESM",
                 "Environmental Science Honours (BSc(Hons))": "ENVSCBENVSCH",
                 "Executive Master in Leadership Strategy and Innovation (EMLeadershipStratInnov)": "20279",
                 "Exercise Physiology Honours (BSc(Hons))": "66027",
                 "Extractive Metallurgy (GradDipExtMet)": "EXTMETGD",
                 "Finance (BBus)": "FINBCOMM",
                 "Finance Honours (BBus(Hons))": "FINBCOMH2",
                 "Food Security (MFoodSec)": "33878",
                 "Forensic Biology and Toxicology (BSc)": "FORBTSBM",
                 "Forensic Biology and Toxicology Honours (BSc(Hons))": "87039",
                 "Forensic Science [Professional Practice] (GradCertForSc(ProfessionalPractice))": "84200",
                 "Forensic Science [Professional Practice] (MForSc(ProfessionalPractice))": "73699",
                 "Games Art and Design (BCrMedia)": "63895",
                 "Games Software Design and Production (BSc)": "96690M",
                 "Games Software Design and Production Honours (BSc(Hons))": "43944",
                 "Games Technology (BSc)": "GAMTECMJM",
                 "Games Technology Honours (BSc(Hons))": "57223",
                 "Games and Apps Production (GradDipGamesAppsProd)": "95857",
                 "Global Media and Communication (BCommun)": "23781",
                 "Graduate Certificate in Education (International Education) (GradCertEdIntlEd)": "51909",
                 "Graduate Certificate in Education (Secondary Mathematics 7-10) (GradCertEd(SecMaths))": "21432",
                 "Graduate Certificate in Education (Secondary Science 7-10) (GradCertEd(SecSci))": "99768",
                 "Graduate Certificate in Energy and Carbon Studies (GradCertEnCbSt)": "39651",
                 "Graduate Certificate in Media Production (GradCertMedProd)": "16062",
                 "Graduate Certificate in Public Administration (GradCertPAdmin)": "30257",
                 "Graduate Diploma in Asian Studies (GradDipAsianSt)": "ASPD",
                 "Graduate Diploma in Australian Migration Law and Practice (GradDipAusMigLaw)": "85750",
                 "Graduate Diploma in Creative Arts Therapies (GradDipArtTherapy)": "2898",
                 "Graduate Diploma in Energy and Carbon Studies (GradDipEnCbSt)": "22879",
                 "Graphic Design (BCrMedia)": "7776",
                 "Health Care Management (GradCertHCM)": "15044",
                 "Health Care Management (MHCM)": "89061",
                 "Health Communication (GradDip)": "49127",
                 "Health Policy and Leadership (GradCertHPL)": "53250",
                 "Health Policy and Leadership (MHPL)": "16882",
                 "History (BA)": "HISTBM",
                 "History Honours (BA(Hons))": "HISTBH",
                 "Hospitality and Tourism Management (BBus)": "51088M",
                 "Human Resource Management [Offshore] (MHRM)": "HRMM",
                 "Human Resources Management (BBus)": "HRMBCOMM",
                 "Human Resources Management (GradCertHRM)": "32088",
                 "Human Resources Management (GradDipHRM)": "54559",
                 "Human Resources Management (MHRM)": "HTMMM",
                 "Human Resources and Safety (GradCertHRS)": "OHRSGC",
                 "Indonesian (BA)": "ASSTSPBM",
                 "Industrial Computer Systems Engineering Honours (BE(Hons))": "ENGICSM2",
                 "Information Technology (DIT)": "ITD",
                 "Information Technology (GradCertIT)": "58125",
                 "Information Technology (MIT)": "ITMS",
                 "Information Technology Management (GradDipITMan)": "23176",
                 "Instrumentation and Control Engineering Honours (BE(Hons))": "ENGICOM2",
                 "International Affairs (MIA)": "84778",
                 "International Aid and Development (BA)": "60600M",
                 "International Marketing (GradCertIM)": "15551",
                 "Internetworking and Network Security (BSc)": "TMBCOMM",
                 "Internetworking and Network Security Honours (BSc(Hons))": "56404",
                 "Internetworking and Security (GradDipIntwkSecur)": "13066",
                 "Japanese (BA)": "ASSTSPBM2",
                 "Journalism (BCommun)": "44055",
                 "Laboratory Medicine (BSc)": "7585",
                 "Law + Arts [Combined] (LLB)+(BA)": "LAWJOINTM",
                 "Law + Business [Combined] (LLB)+(BBus)": "LAWJOINTM2",
                 "Law + Communication [Combined]": "27383",
                 "Law + Criminology [Combined] (BCrim)+(LLB)": "34305",
                 "Law + Psychology (BA) [Combined]": "19529",
                 "Law + Psychology (BSc) [Combined]": "1884",
                 "Law + Science [Combined] (LLB)+(BSc)": "LAWJOINTM3",
                 "Law - Graduate Entry (LLB)": "43797",
                 "Law Honours (LLB(Hons))": "54313",
                 "Law [Four-Year Degree] (LLB)+(LLB(Hons))": "LAW4YRM",
                 "Laws by Research (LLM(Res))": "LAWRESM",
                 "Legal Practice (GradCertLP)": "25786",
                 "Legal Studies (BCrim)": "89398",
                 "Legal Studies Honours (BA(Hons))": "LEGSTBH2",
                 "Management (BBus)": "MGMTBCOMM",
                 "Management Honours (BBus(Hons))": "MGMTBCOMH2",
                 "Marine Biology (BSc)": "16057",
                 "Marine Science (BSc)": "MARSM",
                 "Marine Science Honours (BSc(Hons))": "MARSH",
                 "Marketing (BBus)": "MKTGBCOMM",
                 "Marketing Honours (BBus(Hons))": "MKTGBCOMH2",
                 "Master of Asian Studies (MAsianSt)": "ASMA",
                 "Master of Exercise Science (Research) (MExSc)": "23583",
                 "Master of Professional Accounting (Advanced) (MPA(Adv))": "32292",
                 "Master of Professional Accounting (MPA)": "55039",
                 "Master of Renewable and Sustainable Energy (MRenSusEn)": "87570",
                 "Master of Veterinary Studies (Small Animal Practice) (MVS)": "VSM",
                 "Mathematics and Statistics (BSc)": "MASTM",
                 "Mathematics and Statistics Honours (BSc(Hons))": "710",
                 "Media Production (GradDipMedProd)": "65936",
                 "Mineral Science (BSc)": "EXTMETBM",
                 "Mineral Science Honours (BSc(Hons))": "EXTMETBH",
                 "Mobile and Web Application Development (BSc)": "INCOBM",
                 "Mobile and Web Application Development Honours (BSc(Hons))": "63651",
                 "Molecular Biology (BSc)": "MOLBIOLM",
                 "Molecular Biology Honours (BSc(Hons))": "MOLBIOLH",
                 "Movement Science Honours (BSc(Hons))": "52486",
                 "Nursing (BNurs)": "98277",
                 "Nursing Honours (BNurs(Hons))": "NURSBH",
                 "Philosophy (BA)": "PHILBM",
                 "Philosophy Honours (BA(Hons))": "PHILBH",
                 "Photography (BCrMedia)": "80392",
                 "Physics and Nanotechnology (BSc)": "PHYM",
                 "Physics and Nanotechnology Honours (BSc(Hons))": "98362",
                 "Plant Biosecurity (GradCertPlantBiosec)": "90689",
                 "Plant Biosecurity (GradDipPlantBiosec)": "85684",
                 "Politics and International Studies (BA)": "POLINTSTBM",
                 "Politics and International Studies Honours (BA(Hons))": "POLINTSTBH",
                 "Primary Teaching (BEd)": "EDPTBM",
                 "Primary, 1-10 Health and Physical Education (BEd)": "21207M",
                 "Professional Accounting [Offshore] (MPA)": "68946",
                 "Protected Area Administration (GradCertPAAdmin)": "78647",
                 "Psychology (BPsych)/(BA)": "PSYB",
                 "Psychology (GradDipPsych)": "54632",
                 "Psychology Honours (BA(Hons))": "PSYHONBA",
                 "Psychology Honours (BSc(Hons))": "PSYHONBSC",
                 "Psychology [Clinical Psychology] (DPsych)": "54599",
                 "Psychology [Organisational Psychology] (DPsych)": "7649",
                 "Public Policy and Management (GradCertPPM)": "45180",
                 "Public Policy and Management (MPPM)": "89395",
                 "Religion (BA)": "66308",
                 "Religion Honours (BA(Hons))": "RELIGION",
                 "Renewable Energy (MRenEn)": "RETMS",
                 "Renewable Energy Engineering Honours (BE(Hons))": "ENGREM2",
                 "Safety Science (GradDipSafeSc)": "20522",
                 "Screen Production (BCrMedia)": "57264",
                 "Secondary Teaching [Arts Combined English] (BEd)+(BA)": "EDSTBM",
                 "Secondary Teaching [Arts Combined History] (BEd)+(BA)": "EDSTBM2",
                 "Secondary Teaching [Combined Science Degrees] (BEd)+(BSc)": "EDSTBM13",
                 "Secondary Teaching [Science Combined Mathematics] (BEd)+(BSc)": "EDSTBM4",
                 "Secondary Teaching [Science Combined Sport and Health Science] (BEd)+(BSc)": "EDSTBM5",
                 "Security, Terrorism and Counterterrorism Studies (BA)": "SECTERBAM",
                 "Social and Developmental Psychology (BA)": "PSYBM",
                 "Sociology (BA)": "SOCBM",
                 "Sociology Honours (BA(Hons))": "SOCBH",
                 "Sound (BCrMedia)": "3281",
                 "Sport and Exercise Science (BSportExSc)": "95532",
                 "Sport and Exercise Science + Clinical Exercise Physiology (BSportExSc)+(GradDipClinExPhys)": "35809",
                 "Sport and Exercise Science + Psychology (BSportExSc)+(BSc)": "17760",
                 "Sport and Exercise Science Honours (BSportExSc(Hons))": "36346",
                 "Sport and Health Science Honours (BSc(Hons))": "8668",
                 "Strategic Communication (BCommun)": "86448",
                 "Sustainable Development (BA)": "SUSDEVBM",
                 "Sustainable Development (MSustDev)": "ESDMA",
                 "Sustainable Development Honours (BA(Hons))": "SUSDEVBH",
                 "Teaching [Primary] (MTeachPrim)": "22721",
                 "Tertiary and Adult Education (GradCertTerAdEd)": "TAEDGC",
                 "Theatre and Drama  (BA)": "5774M",
                 "Theatre and Drama Honours (BA(Hons))": "35182",
                 "Theology (GradCertTheol)": "21443",
                 "Theology (GradDipTheol)": "58348",
                 "Tourism and Events (BA)": "46074M",
                 "Tourism and Events Honours (BA(Hons))": "TOUEVENTS",
                 "Tourism and Events Management (BA)": "46074",
                 "Veterinary Biology Honours (BSc(Hons))": "VSTH",
                 "Veterinary Medical Science (DVetMedSc)": "36336",
                 "Veterinary Science (BSc)+(DVM)": "VSTM",
                 "Veterinary Studies [Conservation Medicine] (MVS)": "VETCMM",
                 "Veterinary Studies [Veterinary Surveillance] (MVS)": "VETSVM",
                 "Water Treatment and Desalination (GradDipWatTrmt)": "96594",
                 "Water Treatment and Desalination (MWatTrmt)": "99079",
                 "Web Communication (GradDipWebComm)": "11998",
                 "Wildlife Health and Conservation (MWildlifeHth)": "98704",
                 "Please select a course": "",
                 "FlexiTrack": "FlexiTrack",
                 "OnTrack": "OnTrack",
                 "OnTrack & FlexiTrack": "OnTrack & FlexiTrack",
                 "OnTrack Sprint": "OnTrack Sprint",
                 "Please select a course": "",
                 "International Bridging Unit": "International Bridging Unit",
                 "Please select a course": "",
                 "Accounting (BBus)": "ACCBCOMM",
                 "Animal Health (BSc)": "91384",
                 "Animal Science (BSc)": "60856M",
                 "Asian Studies (BA)": "ASSTBM",
                 "Australian Indigenous Studies (BA)": "AISBM",
                 "Banking (BBus)": "BANKBCOMM",
                 "Biological Sciences (BSc)": "BSBM",
                 "Biomedical Science (BSc)": "BIOMSCBM",
                 "Business Information Systems (BSc)": "BISBSCM",
                 "Business Law (BBus)": "BUSLAWBCOMM",
                 "Chemical and Metallurgical Engineering Honours (BE(Hons))": "ENG10011M2",
                 "Chemistry (BSc)": "CHEBM",
                 "Chiropractic Science + Clinical Chiropractic (BSc)+(BClinChiro)": "59021",
                 "Clinical Laboratory Science (BSc)": "1637",
                 "Cognitive Neuroscience and Health Psychology (BSc)": "78925",
                 "Communication + Creative Media [Combined] (BCrMedia)+(BCommun)": "66243",
                 "Community Development (BA)": "COMMDEVBM",
                 "Computer Science (BSc)": "COMPSCM",
                 "Conservation and Wildlife Biology (BSc)": "CBBSCM",
                 "Crime Science (BCrim)": "23788",
                 "Criminal Behaviour (BCrim)": "47454",
                 "Criminology + Communication [Combined]": "98717",
                 "Criminology + Forensic Biology and Toxicology [Combined]": "99288",
                 "Criminology + Psychology [Combined] (BCrim)+(BA)": "54244",
                 "Crop and Pasture Science (BSc)": "79087",
                 "Cyber Forensics and Information Security (BSc)": "12046M",
                 "Early Childhood and Primary Teaching (BEd)": "EDECPTBM",
                 "Economics (BBus)": "ECONBM",
                 "Electrical Power Engineering Honours (BE(Hons))": "ENGPOWM2",
                 "Engineering Technology (BSc)": "ENGTBM",
                 "English and Creative Writing (BA)": "ENGLBM",
                 "Environmental Engineering Honours (BE(Hons))": "97999M2",
                 "Environmental Management and Sustainability (BSc)": "33427M",
                 "Environmental Science (BSc)": "ENVSCBENVSCM",
                 "Finance (BBus)": "FINBCOMM",
                 "Forensic Biology and Toxicology (BSc)": "FORBTSBM",
                 "Games Art and Design (BCrMedia)": "63895",
                 "Games Software Design and Production (BSc)": "96690M",
                 "Games Technology (BSc)": "GAMTECMJM",
                 "Global Media and Communication (BCommun)": "23781",
                 "Graphic Design (BCrMedia)": "7776",
                 "History (BA)": "HISTBM",
                 "Hospitality and Tourism Management (BBus)": "51088M",
                 "Human Resources Management (BBus)": "HRMBCOMM",
                 "Indonesian (BA)": "ASSTSPBM",
                 "Industrial Computer Systems Engineering Honours (BE(Hons))": "ENGICSM2",
                 "Instrumentation and Control Engineering Honours (BE(Hons))": "ENGICOM2",
                 "International Aid and Development (BA)": "60600M",
                 "Internetworking and Network Security (BSc)": "TMBCOMM",
                 "Japanese (BA)": "ASSTSPBM2",
                 "Journalism (BCommun)": "44055",
                 "Laboratory Medicine (BSc)": "7585",
                 "Law + Arts [Combined] (LLB)+(BA)": "LAWJOINTM",
                 "Law + Business [Combined] (LLB)+(BBus)": "LAWJOINTM2",
                 "Law + Communication [Combined]": "27383",
                 "Law + Criminology [Combined] (BCrim)+(LLB)": "34305",
                 "Law + Psychology (BA) [Combined]": "19529",
                 "Law + Psychology (BSc) [Combined]": "1884",
                 "Law + Science [Combined] (LLB)+(BSc)": "LAWJOINTM3",
                 "Law [Four-Year Degree] (LLB)+(LLB(Hons))": "LAW4YRM",
                 "Legal Studies (BCrim)": "89398",
                 "Management (BBus)": "MGMTBCOMM",
                 "Marine Biology (BSc)": "16057",
                 "Marine Science (BSc)": "MARSM",
                 "Marketing (BBus)": "MKTGBCOMM",
                 "Mathematics and Statistics (BSc)": "MASTM",
                 "Mineral Science (BSc)": "EXTMETBM",
                 "Mobile and Web Application Development (BSc)": "INCOBM",
                 "Molecular Biology (BSc)": "MOLBIOLM",
                 "Nursing (BNurs)": "98277",
                 "Philosophy (BA)": "PHILBM",
                 "Photography (BCrMedia)": "80392",
                 "Physics and Nanotechnology (BSc)": "PHYM",
                 "Politics and International Studies (BA)": "POLINTSTBM",
                 "Primary Teaching (BEd)": "EDPTBM",
                 "Primary, 1-10 Health and Physical Education (BEd)": "21207M",
                 "Psychology (BPsych)/(BA)": "PSYB",
                 "Religion (BA)": "66308",
                 "Renewable Energy Engineering Honours (BE(Hons))": "ENGREM2",
                 "Screen Production (BCrMedia)": "57264",
                 "Secondary Teaching [Arts Combined English] (BEd)+(BA)": "EDSTBM",
                 "Secondary Teaching [Arts Combined History] (BEd)+(BA)": "EDSTBM2",
                 "Secondary Teaching [Combined Science Degrees] (BEd)+(BSc)": "EDSTBM13",
                 "Secondary Teaching [Science Combined Mathematics] (BEd)+(BSc)": "EDSTBM4",
                 "Secondary Teaching [Science Combined Sport and Health Science] (BEd)+(BSc)": "EDSTBM5",
                 "Security, Terrorism and Counterterrorism Studies (BA)": "SECTERBAM",
                 "Social and Developmental Psychology (BA)": "PSYBM",
                 "Sociology (BA)": "SOCBM",
                 "Sound (BCrMedia)": "3281",
                 "Sport and Exercise Science (BSportExSc)": "95532",
                 "Sport and Exercise Science + Psychology (BSportExSc)+(BSc)": "17760",
                 "Strategic Communication (BCommun)": "86448",
                 "Sustainable Development (BA)": "SUSDEVBM",
                 "Theatre and Drama  (BA)": "5774M",
                 "Tourism and Events (BA)": "46074M",
                 "Tourism and Events Management (BA)": "46074",
                 "Veterinary Science (BSc)+(DVM)": "VSTM",
                 "Please select a course": "",
                 "Accounting Honours (BBus(Hons))": "ACCBCOMH2",
                 "Animal Health Honours (BSc(Hons))": "23000",
                 "Animal Science Honours (BSc(Hons))": "62307",
                 "Asian Studies Honours (BA(Hons))": "ASSTBH",
                 "Australian Indigenous Studies Honours (BA(Hons))": "AISBH",
                 "Banking Honours (BBus(Hons))": "BANKBCOMH2",
                 "Biological Sciences Honours (BSc(Hons))": "BSBH",
                 "Biomedical Science Honours (BSc(Hons))": "BIOMSCBH",
                 "Biotechnology Honours (BSc(Hons))": "BIOTBSCH",
                 "Business Information Systems Honours (BSc(Hons))": "41032",
                 "Business Law Honours (BBus(Hons))": "BUSLAWBCOMH2",
                 "Chemistry Honours (BSc(Hons))": "CHEBH",
                 "Chiropractic Honours (BSc(Hons))": "CHIROH",
                 "Communication Honours (BCommun(Hons))": "75974",
                 "Communication and Media Studies Honours (BA(Hons))": "COMUNMED",
                 "Community Development Honours (BA(Hons))": "COMMDEVBH",
                 "Computer Science Honours (BSc(Hons))": "74320",
                 "Conservation and Wildlife Biology Honours (BSc(Hons))": "CBBSCH",
                 "Creative Media Honours (BCrMedia(Hons))": "72001",
                 "Crop and Pasture Science Honours (BSc(Hons))": "7865",
                 "Cyber Forensics and Information Security Honours (BSc(Hons))": "30838",
                 "Economics Honours (BBus(Hons))": "ECONBH2",
                 "English and Creative Writing Honours (BA(Hons))": "ENGLBH",
                 "Environmental Management and Sustainability Honours (BSc(Hons))": "40976",
                 "Environmental Science Honours (BSc(Hons))": "ENVSCBENVSCH",
                 "Exercise Physiology Honours (BSc(Hons))": "66027",
                 "Finance Honours (BBus(Hons))": "FINBCOMH2",
                 "Forensic Biology and Toxicology Honours (BSc(Hons))": "87039",
                 "Games Software Design and Production Honours (BSc(Hons))": "43944",
                 "Games Technology Honours (BSc(Hons))": "57223",
                 "History Honours (BA(Hons))": "HISTBH",
                 "Internetworking and Network Security Honours (BSc(Hons))": "56404",
                 "Law Honours (LLB(Hons))": "54313",
                 "Legal Studies Honours (BA(Hons))": "LEGSTBH2",
                 "Management Honours (BBus(Hons))": "MGMTBCOMH2",
                 "Marine Science Honours (BSc(Hons))": "MARSH",
                 "Marketing Honours (BBus(Hons))": "MKTGBCOMH2",
                 "Mathematics and Statistics Honours (BSc(Hons))": "710",
                 "Mineral Science Honours (BSc(Hons))": "EXTMETBH",
                 "Mobile and Web Application Development Honours (BSc(Hons))": "63651",
                 "Molecular Biology Honours (BSc(Hons))": "MOLBIOLH",
                 "Movement Science Honours (BSc(Hons))": "52486",
                 "Nursing Honours (BNurs(Hons))": "NURSBH",
                 "Philosophy Honours (BA(Hons))": "PHILBH",
                 "Physics and Nanotechnology Honours (BSc(Hons))": "98362",
                 "Politics and International Studies Honours (BA(Hons))": "POLINTSTBH",
                 "Psychology Honours (BA(Hons))": "PSYHONBA",
                 "Psychology Honours (BSc(Hons))": "PSYHONBSC",
                 "Religion Honours (BA(Hons))": "RELIGION",
                 "Sociology Honours (BA(Hons))": "SOCBH",
                 "Sport and Exercise Science Honours (BSportExSc(Hons))": "36346",
                 "Sport and Health Science Honours (BSc(Hons))": "8668",
                 "Sustainable Development Honours (BA(Hons))": "SUSDEVBH",
                 "Theatre and Drama Honours (BA(Hons))": "35182",
                 "Tourism and Events Honours (BA(Hons))": "TOUEVENTS",
                 "Veterinary Biology Honours (BSc(Hons))": "VSTH",
                 "Please select a course": "",
                 "Applied Psychology + Doctor of Philosophy (MAppPsych)+(PhD)": "71156",
                 "Applied Psychology [Clinical Psychology] (MAppPsych)": "11767",
                 "Applied Psychology [Organisational Psychology] (MAppPsych + PhD)": "71156",
                 "Applied Psychology [Organisational Psychology] (MAppPsych)": "89177",
                 "Applied Psychology [Professional] (MAppPsych(Professional))": "56356",
                 "Asian Language [In-Country] (GradDipAsianLangIn-Country)": "82755",
                 "Asian Studies (GradCertAsianSt)": "13713",
                 "Biosecurity (MBiosec)": "21380",
                 "Business Administration (GradCertBusAdmin)": "BAPC",
                 "Business Administration (GradDipBusAdmin)": "BAPD",
                 "Business Administration (MBA)": "26871",
                 "Business Administration Professional Practice (MBA(PP))": "96933",
                 "Business Administration [MasterClass] (GradCertBusAdmin)": "95187",
                 "Business Administration [Offshore] (MBA)": "BAM",
                 "Chaplaincy (GradDipChap)": "11699",
                 "Chaplaincy (MChap)": "57569",
                 "Clinical Exercise Physiology (GradDipClinExPhys)": "79542",
                 "Communication Management (MCommM)": "9414",
                 "Community Development (GradCertCommDev)": "80005",
                 "Community Development (GradDipCommDev)": "58193",
                 "Community Development (MCommDev)": "99647",
                 "Consultancy Psychology (GradDipConsultPsych)": "49662",
                 "Counselling (GradCertCounsel)": "36509",
                 "Counselling (GradDipCounsel)": "10627",
                 "Counselling (MCounsel)": "23267",
                 "Development Studies (GradCertDS)": "85232",
                 "Development Studies (MDS)": "16059",
                 "Divinity (MDiv)": "37662",
                 "Doctor of Philosophy (PhD)": "PHILD",
                 "Doctor of Psychology (Clinical Psychology) (DPsych)": "67205",
                 "Early Childhood Education (GradCertEarlyChildEd)": "ECEDGC",
                 "Education (EdD)": "EDD",
                 "Education [Coursework] (MEd)": "EDM2",
                 "Education [Primary] (MTeachPrim)": "22721",
                 "Education [Research] (MEd(Res))": "10079",
                 "Education [Secondary] (GradDipEd)": "EDSGD",
                 "Education [Tertiary and Adult] (GradCertTerAdEd)": "TAEDGC",
                 "Education [Tertiary and Adult] (GradDipEd)": "ETAGD",
                 "Energy Studies (GradCertEnSt)": "54978",
                 "Energy Studies (GradDipEnSt)": "73302",
                 "Energy and the Environment (GradDipEnEnv)": "EEPD",
                 "Engineering (GradDipEng)": "47788",
                 "Engineering (ME)": "ENGM",
                 "Environmental Assessment and Management (GradCertEnvAsstMan)": "EMPC",
                 "Environmental Science (GradCertEnvSc)": "41299",
                 "Environmental Science (GradDipEnv)": "EMPD",
                 "Environmental Science (MEnvSc)": "SESM",
                 "Executive Master in Leadership Strategy and Innovation (EMLeadershipStratInnov)": "20279",
                 "Extractive Metallurgy (GradDipExtMet)": "EXTMETGD",
                 "Food Security (MFoodSec)": "33878",
                 "Forensic Science [Professional Practice] (GradCertForSc(ProfessionalPractice))": "84200",
                 "Forensic Science [Professional Practice] (MForSc(ProfessionalPractice))": "73699",
                 "Games and Apps Production (GradDipGamesAppsProd)": "95857",
                 "Graduate Certificate in Education (International Education) (GradCertEdIntlEd)": "51909",
                 "Graduate Certificate in Education (Secondary Mathematics 7-10) (GradCertEd(SecMaths))": "21432",
                 "Graduate Certificate in Education (Secondary Science 7-10) (GradCertEd(SecSci))": "99768",
                 "Graduate Certificate in Energy and Carbon Studies (GradCertEnCbSt)": "39651",
                 "Graduate Certificate in Media Production (GradCertMedProd)": "16062",
                 "Graduate Certificate in Public Administration (GradCertPAdmin)": "30257",
                 "Graduate Diploma in Asian Studies (GradDipAsianSt)": "ASPD",
                 "Graduate Diploma in Australian Migration Law and Practice (GradDipAusMigLaw)": "85750",
                 "Graduate Diploma in Creative Arts Therapies (GradDipArtTherapy)": "2898",
                 "Graduate Diploma in Energy and Carbon Studies (GradDipEnCbSt)": "22879",
                 "Health Care Management (GradCertHCM)": "15044",
                 "Health Care Management (MHCM)": "89061",
                 "Health Communication (GradDip)": "49127",
                 "Health Policy and Leadership (GradCertHPL)": "53250",
                 "Health Policy and Leadership (MHPL)": "16882",
                 "Human Resource Management [Offshore] (MHRM)": "HRMM",
                 "Human Resources Management (GradCertHRM)": "32088",
                 "Human Resources Management (GradDipHRM)": "54559",
                 "Human Resources Management (MHRM)": "HTMMM",
                 "Human Resources and Safety (GradCertHRS)": "OHRSGC",
                 "Information Technology (DIT)": "ITD",
                 "Information Technology (GradCertIT)": "58125",
                 "Information Technology (MIT)": "ITMS",
                 "Information Technology Management (GradDipITMan)": "23176",
                 "International Affairs (MIA)": "84778",
                 "International Marketing (GradCertIM)": "15551",
                 "Internetworking and Security (GradDipIntwkSecur)": "13066",
                 "Law - Graduate Entry (LLB)": "43797",
                 "Laws by Research (LLM(Res))": "LAWRESM",
                 "Legal Practice (GradCertLP)": "25786",
                 "Master of Asian Studies (MAsianSt)": "ASMA",
                 "Master of Exercise Science (Research) (MExSc)": "23583",
                 "Master of Professional Accounting (Advanced) (MPA(Adv))": "32292",
                 "Master of Professional Accounting (MPA)": "55039",
                 "Master of Renewable and Sustainable Energy (MRenSusEn)": "87570",
                 "Master of Veterinary Studies (Small Animal Practice) (MVS)": "VSM",
                 "Media Production (GradDipMedProd)": "65936",
                 "Plant Biosecurity (GradCertPlantBiosec)": "90689",
                 "Plant Biosecurity (GradDipPlantBiosec)": "85684",
                 "Professional Accounting [Offshore] (MPA)": "68946",
                 "Protected Area Administration (GradCertPAAdmin)": "78647",
                 "Psychology (GradDipPsych)": "54632",
                 "Psychology [Clinical Psychology] (DPsych)": "54599",
                 "Psychology [Organisational Psychology] (DPsych)": "7649",
                 "Public Policy and Management (GradCertPPM)": "45180",
                 "Public Policy and Management (MPPM)": "89395",
                 "Renewable Energy (MRenEn)": "RETMS",
                 "Safety Science (GradDipSafeSc)": "20522",
                 "Sport and Exercise Science + Clinical Exercise Physiology (BSportExSc)+(GradDipClinExPhys)": "35809",
                 "Sustainable Development (MSustDev)": "ESDMA",
                 "Teaching [Primary] (MTeachPrim)": "22721",
                 "Tertiary and Adult Education (GradCertTerAdEd)": "TAEDGC",
                 "Theology (GradCertTheol)": "21443",
                 "Theology (GradDipTheol)": "58348",
                 "Veterinary Medical Science (DVetMedSc)": "36336",
                 "Veterinary Studies [Conservation Medicine] (MVS)": "VETCMM",
                 "Veterinary Studies [Veterinary Surveillance] (MVS)": "VETSVM",
                 "Water Treatment and Desalination (GradDipWatTrmt)": "96594",
                 "Water Treatment and Desalination (MWatTrmt)": "99079",
                 "Web Communication (GradDipWebComm)": "11998",
                 "Wildlife Health and Conservation (MWildlifeHth)": "98704"
                 }
        url = response.url
        keys = url.lstrip('http://www.murdoch.edu.au/study/courses/course-details/').replace('-', ' ')
        print('keys:', keys)
        Dates = dates.get(keys)
        print('valus:',Dates)
        # print(22,type(Dates))
        # for d in Dates:
        entry_requirements_fullurl = entry_requirements_url + '?country=China&study_level=Undergrad&course=' + str(Dates)
        print('entry_requirements_fullurl:',entry_requirements_fullurl)
        self.parse_entry_requirements(entry_requirements_fullurl,item)



        url = response.url
        university = 'Murdoch University'
        country = 'Australia'
        city = "Murdoch Perth campus"
        website = 'http://www.murdoch.edu.au'
        degree_level = '0'
        start_date = "NULL"
        degree_description = "NULL"
        teaching = 'NULL'
        assessment = "NULL"
        career = "NULL"
        application_date = "NULL"
        deadline = "NULL"
        application_fee = "NULL"
        tuition_fee = 'NULL'
        ATAS = "NULL"
        GPA = "NULL"
        average_score = "NULL"
        accredited_university = "NULL"
        Alevel = "NULL"
        IB = "NULL"
        # IELTS = "NULL"
        IELTS_L = "NULL"
        IELTS_S = "NULL"
        IELTS_R = "NULL"
        IELTS_W = "NULL"
        # TOEFL = "NULL"
        TOEFL_L = "NULL"
        TOEFL_S = "NULL"
        TOEFL_R = "NULL"
        TOEFL_W = "NULL"
        GRE = "NULL"
        GMAT = "NULL"
        LSAT = "NULL"
        MCAT = "NULL"
        working_experience = "NULL"
        interview = "NULL"
        portfolio = "NULL"
        application_documents = "NULL"
        chinese_requirements = "NULL"
        school_test = "NULL"
        SATI = "NULL"
        SATII = "NULL"
        SAT_code = "NULL"
        ACT = "NULL"
        ACT_code = "NULL"
        other = "NULL"




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
        # item["modules"] = modules
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
        # item["IELTS"] = IELTS
        item["IELTS_L"] = IELTS_L
        item["IELTS_S"] = IELTS_S
        item["IELTS_R"] = IELTS_R
        item["IELTS_W"] = IELTS_W
        # item["TOEFL"] = TOEFL
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
        # item["entry_requirements"] = entry_requirements
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

    def parse_modules(self,modules_links, item):
        # print(2,'=====================',response.url)
        data = requests.get(modules_links)
        response = etree.HTML(data.text)
        modules_url = response.xpath('//*[@id="course-description-and-structure"]/div[@class="row-wrap"]/div[@class="row page__row"]//div[@class="article article--row"]/div[@class="request-html"]/iframe/@src')
        modules_url = ''.join(modules_url)
        print('modules_url:===========',modules_url)
        self.parse_modules_s(modules_url,item)

        # print(22222222222222222222222222)

    def parse_modules_s(self,modules_url,item):
        # print(111111111111111111111111111)

        modules_s = requests.get(modules_url)
        print('modules_s:========',modules_s)
        response = etree.HTML(modules_s.text)
        modules = response.xpath('//div[@class="structure"]/p/text()')
        # print('modules:',modules)
        modules = ''.join(modules)
        print('modules:',modules)
        item["modules"] = modules

    def parse_entry_requirements(self,entry_requirements_fullurl,item):
        entry_requirements_s = requests.get(entry_requirements_fullurl)
        print('entry_requirements_s:',entry_requirements_s)
        response = etree.HTML(entry_requirements_s.text)
        entry_requirements = response.xpath('/html/body/div[2]//text()')
        print('entry_requirements:',entry_requirements)
        entry_requirements = ''.join(entry_requirements)
        item["entry_requirements"] = entry_requirements

        IELTS = response.xpath('/html/body/div[@class="well"][3]/p[2]/a/@href')
        IELTS = ''.join(IELTS)
        item["IELTS"] = IELTS
        print('IELTS:',IELTS)

        TOEFL =response.xpath('/html/body/div[@class="well"][3]/p[2]/a/@href')
        TOEFL = ''.join(TOEFL)
        item["TOEFL"] = TOEFL
        print("TOEFL:",TOEFL)





    # def pase_item(self,response):
    #     print(3,'==========================',response.url)
    #     item = HooliItem()
    #
    #     url = response.url
    #     university = 'Murdoch University'
    #     country = 'Australia'
    #     city = "Murdoch Perth campus"
    #     website = 'http://www.murdoch.edu.au'
    #     degree_level = '0'
    #     start_date = 'NULL'
    #     teaching = 'NULL'
    #     assessment = "NULL"
    #     career = "NULL"
    #     application_date = "NULL"
    #     deadline = 'NULL'
    #     application_fee = 'NULL'
    #     tuition_fee = "NULL"
    #     ATAS = 'NULL'
    #     GPA = 'NULL'
    #     average_score = 'NULL'
    #     accredited_university = 'NULL'
    #     Alevel = 'NULL'
    #     IB = 'NULL'
    #     IELTS = "NULL"
    #     IELTS_L = 'NULL'
    #     IELTS_S = 'NULL'
    #     IELTS_R = 'NULL'
    #     IELTS_W = 'NULL'
    #     TOEFL = 'NULL'
    #     TOEFL_L = 'NULL'
    #     TOEFL_S = 'NULL'
    #     TOEFL_R = 'NULL'
    #     TOEFL_W = 'NULL'
    #     GRE = 'NULL'
    #     GMAT = 'NULL'
    #     LSAT = "NULL"
    #     MCAT = 'NULL'
    #     working_experience = 'NULL'
    #     interview = 'NULL'
    #     portfolio = 'NULL'
    #     application_documents = 'NULL'
    #     chinese_requirements = "NULL"
    #     school_test = 'NULL'
    #     degree_description = "NULL"
    #     SATI = 'NULL'
    #     SATII = 'NULL'
    #     SAT_code = 'NULL'
    #     ACT = 'NULL'
    #     ACT_code = 'NULL'
    #     other = 'NULL'
    #     department = response.meta["department"]
    #     programme = response.meta["programme"]
    #     ucas_code = response.meta["ucas_code"]
    #     degree_type = response.meta["degree_type"]
    #     overview = response.meta["overview"]
    #     mode = response.meta["mode"]
    #     duration = response.meta["duration"]
    #     modules = response.meta["modules"]
    #     location = response.meta["location"]
    #     how_to_apply = response.meta["how_to_apply"]
    #     entry_requirements = response.meta["entry_requirements"]
    #     create_time = response.meta["create_time"]
    #     modules = response.xpath('').extract()
    #
    #
    #
    #
    #     item["url"] = url
    #     item["university"] = university
    #     item["country"] = country
    #     item["city"] = city
    #     item["website"] = website
    #     item["department"] = department
    #     item["programme"] = programme
    #     item["ucas_code"] = ucas_code
    #     item["degree_level"] = degree_level
    #     item["degree_type"] = degree_type
    #     item["start_date"] = start_date
    #     item["degree_description"] = degree_description
    #     item["overview"] = overview
    #     item["mode"] = mode
    #     item["duration"] = duration
    #     item["modules"] = modules
    #     item["teaching"] = teaching
    #     item["assessment"] = assessment
    #     item["career"] = career
    #     item["application_date"] = application_date
    #     item["deadline"] = deadline
    #     item["application_fee"] = application_fee
    #     item["tuition_fee"] = tuition_fee
    #     item["location"] = location
    #     item["ATAS"] = ATAS
    #     item["GPA"] = GPA
    #     item["average_score"] = average_score
    #     item["accredited_university"] = accredited_university
    #     item["Alevel"] = Alevel
    #     item["IB"] = IB
    #     item["IELTS"] = IELTS
    #     item["IELTS_L"] = IELTS_L
    #     item["IELTS_S"] = IELTS_S
    #     item["IELTS_R"] = IELTS_R
    #     item["IELTS_W"] = IELTS_W
    #     item["TOEFL"] = TOEFL
    #     item["TOEFL_L"] = TOEFL_L
    #     item["TOEFL_S"] = TOEFL_S
    #     item["TOEFL_R"] = TOEFL_R
    #     item["TOEFL_W"] = TOEFL_W
    #     item["GRE"] = GRE
    #     item["GMAT"] = GMAT
    #     item["LSAT"] = LSAT
    #     item["MCAT"] = MCAT
    #     item["working_experience"] = working_experience
    #     item["interview"] = interview
    #     item["portfolio"] = portfolio
    #     item["application_documents"] = application_documents
    #     item["how_to_apply"] = how_to_apply
    #     item["entry_requirements"] = entry_requirements
    #     item["chinese_requirements"] = chinese_requirements
    #     item["school_test"] = school_test
    #     item["SATI"] = SATI
    #     item["SATII"] = SATII
    #     item["SAT_code"] = SAT_code
    #     item["ACT"] = ACT
    #     item["ACT_code"] = ACT_code
    #     item["other"] = other
    #     item["create_time"] = create_time
    #
    #     yield item

