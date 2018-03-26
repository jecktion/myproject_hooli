
# -*- coding: utf-8 -*-






import scrapy
from school_3.items import HooliItem
import datetime
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import re

class PlymouthSpider(scrapy.Spider):
    name = 'South_Queensland_ug'
    allowed_domains = ['www.usq.edu.au']
    start_urls = []
    base_url = '%s'

    Lists = ['https://www.usq.edu.au/study/degrees/tertiary-preparation-program-domestic',
'https://www.usq.edu.au/study/degrees/tertiary-preparation-program-domestic/international',
'https://www.usq.edu.au/study/degrees/juris-doctor',
'https://www.usq.edu.au/study/degrees/juris-doctor/international',
'https://www.usq.edu.au/study/degrees/bachelor-of-science-honours/chemistry',
'https://www.usq.edu.au/study/degrees/bachelor-of-science-honours/chemistry/international',
'https://www.usq.edu.au/study/degrees/health-and-community/psychology',
'https://www.usq.edu.au/study/degrees/certificate-of-university-studies',
'https://www.usq.edu.au/study/degrees/diploma-of-university-studies/spatial-science',
'https://www.usq.edu.au/study/degrees/diploma-of-university-studies/social-studies',
'https://www.usq.edu.au/study/degrees/diploma-of-university-studies/construction',
'https://www.usq.edu.au/study/degrees/diploma-of-university-studies/indigenous-community-development',
'https://www.usq.edu.au/study/degrees/diploma-of-university-studies/science',
'https://www.usq.edu.au/study/degrees/diploma-of-university-studies/creative-arts',
'https://www.usq.edu.au/study/degrees/diploma-of-university-studies/engineering',
'https://www.usq.edu.au/study/degrees/diploma-of-university-studies/business-commerce',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-engineering-science/electrical-electronic-engineering',
'https://www.usq.edu.au/study/degrees/law-and-justice-postgraduate',
'https://www.usq.edu.au/study/degrees/certificate-of-university-studies/international',
'https://www.usq.edu.au/study/degrees/diploma-of-university-studies/business-commerce/international',
'https://www.usq.edu.au/study/degrees/diploma-of-university-studies/construction/international',
'https://www.usq.edu.au/study/degrees/diploma-of-university-studies/spatial-science/international',
'https://www.usq.edu.au/study/degrees/diploma-of-university-studies/indigenous-community-development/international',
'https://www.usq.edu.au/study/degrees/diploma-of-university-studies/social-studies/international',
'https://www.usq.edu.au/study/degrees/diploma-of-university-studies/science/international',
'https://www.usq.edu.au/study/degrees/bachelor-of-science-honours/psychology',
'https://www.usq.edu.au/study/degrees/diploma-of-university-studies/engineering/international',
'https://www.usq.edu.au/study/degrees/diploma-of-university-studies/creative-arts/international',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-engineering-science/electrical-electronic-engineering/international',
'https://www.usq.edu.au/study/degrees/bachelor-of-science-honours/psychology/international',
'https://www.usq.edu.au/study/degrees/health-and-community/counselling',
'https://www.usq.edu.au/study/degrees/master-of-computing',
'https://www.usq.edu.au/study/degrees/master-of-computing/international',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-spatial-science-technology',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-spatial-science-technology/international',
'https://www.usq.edu.au/study/degrees/accelerated-entry-pathway-program',
'https://www.usq.edu.au/study/degrees/pathway-programs',
'https://www.usq.edu.au/study/degrees/careers/surveyor',
'https://www.usq.edu.au/study/degrees/bachelor-of-creative-arts/theatre',
'https://www.usq.edu.au/study/degrees/diploma-of-university-studies',
'https://www.usq.edu.au/study/degrees/master-of-business-research',
'https://www.usq.edu.au/study/degrees/indigenous-higher-education-pathways-program',
'https://www.usq.edu.au/study/degrees/master-of-business-research/international',
'https://www.usq.edu.au/study/degrees/bachelor-of-creative-arts/film-television-radio',
'https://www.usq.edu.au/study/degrees/bachelor-of-creative-arts/visual-arts',
'https://www.usq.edu.au/study/degrees/bachelor-of-communication-and-media/television-radio-extended',
'https://www.usq.edu.au/study/degrees/bachelor-of-communication-and-media/television-radio',
'https://www.usq.edu.au/study/degrees/master-of-counselling/foundations-of-practice',
'https://www.usq.edu.au/study/degrees/bachelor-of-communication-and-media/public-relations',
'https://www.usq.edu.au/study/degrees/bachelor-of-communication-and-media/journalism',
'https://www.usq.edu.au/study/degrees/bachelor-of-communication-and-media/communication-media-studies',
'https://www.usq.edu.au/study/degrees/bachelor-of-communication-and-media/advertising',
'https://www.usq.edu.au/study/degrees/bachelor-of-communication-and-media/public-relations-extended',
'https://www.usq.edu.au/study/degrees/bachelor-of-communication-and-media/marketing',
'https://www.usq.edu.au/study/degrees/diploma-of-english-for-university-studies',
'https://www.usq.edu.au/study/degrees/english-language-intensive-courses-for-overseas-students',
'https://www.usq.edu.au/study/degrees/certificate-of-english-for-university-studies',
'https://www.usq.edu.au/study/degrees/bachelor-of-science-honours/biology',
'https://www.usq.edu.au/study/degrees/bachelor-of-science-honours/physics',
'https://www.usq.edu.au/study/degrees/bachelor-of-science-honours/environment-sustainability',
'https://www.usq.edu.au/study/degrees/bachelor-of-science-honours/applied-mathematics-statistics',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-science/physics',
'https://www.usq.edu.au/study/degrees/bachelor-of-creative-arts/music',
'https://www.usq.edu.au/study/degrees/graduate-diploma-of-science/physics-astronomy',
'https://www.usq.edu.au/study/degrees/master-of-health/health-leadership',
'https://www.usq.edu.au/study/degrees/bachelor-of-communication-and-media/journalism-extended',
'https://www.usq.edu.au/study/degrees/health-and-community/sport-and-exercise',
'https://www.usq.edu.au/study/degrees/health-and-community/midwifery',
'https://www.usq.edu.au/study/degrees/health-and-community/nursing',
'https://www.usq.edu.au/study/degrees/health-and-community/paramedicine',
'https://www.usq.edu.au/study/degrees/health-and-community/human-services',
'https://www.usq.edu.au/study/degrees/graduate-diploma-of-business',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-business',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-education/early-childhood',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-engineering-science/agricultural-engineering',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-engineering-science/structural-engineering',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-engineering-science/environmental-engineering',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-engineering-science/power-engineering',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-engineering-technology/electrical-electronic-engineering',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-engineering-science/civil-engineering',
'https://www.usq.edu.au/study/degrees/bachelor-of-communication-and-media/interactive-media',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-engineering-science/mechanical-engineering',
'https://www.usq.edu.au/study/degrees/english-for-academic-purposes',
'https://www.usq.edu.au/study/degrees/law-and-justice/law',
'https://www.usq.edu.au/study/degrees/it/information-systems',
'https://www.usq.edu.au/study/degrees/arts/film-television-and-radio',
'https://www.usq.edu.au/study/degrees/it/computing',
'https://www.usq.edu.au/study/degrees/humanities-and-communication/communication-and-media',
'https://www.usq.edu.au/study/degrees/arts/visual-arts',
'https://www.usq.edu.au/study/degrees/engineering/power-engineering',
'https://www.usq.edu.au/study/degrees/engineering/geographic-information-systems',
'https://www.usq.edu.au/study/degrees/education/early-childhood',
'https://www.usq.edu.au/study/degrees/engineering/agricultural-engineering',
'https://www.usq.edu.au/study/degrees/health-and-community/child-youth-family',
'https://www.usq.edu.au/study/degrees/humanities-and-communication/advertising',
'https://www.usq.edu.au/study/degrees/business/international-business',
'https://www.usq.edu.au/study/degrees/humanities-and-communication/journalism',
'https://www.usq.edu.au/study/degrees/arts/music',
'https://www.usq.edu.au/study/degrees/business/management-and-leadership',
'https://www.usq.edu.au/study/degrees/engineering/environmental-engineering',
'https://www.usq.edu.au/study/degrees/business/business-economics',
'https://www.usq.edu.au/study/degrees/humanities-and-communication/public-relations',
'https://www.usq.edu.au/study/degrees/humanities-and-communication/archaeology',
'https://www.usq.edu.au/study/degrees/engineering/mechanical-and-mechatronic-engineering',
'https://www.usq.edu.au/study/degrees/sciences/wine-science',
'https://www.usq.edu.au/study/degrees/business/finance',
'https://www.usq.edu.au/study/degrees/engineering/construction',
'https://www.usq.edu.au/study/degrees/humanities-and-communication/english-literature',
'https://www.usq.edu.au/study/degrees/engineering/mining-engineering',
'https://www.usq.edu.au/study/degrees/sciences/climate-studies',
'https://www.usq.edu.au/study/degrees/engineering/electrical-and-electronic-engineering',
'https://www.usq.edu.au/study/degrees/engineering/surveying',
'https://www.usq.edu.au/study/degrees/humanities-and-communication/language-and-culture',
'https://www.usq.edu.au/study/degrees/humanities-and-communication/general-studies',
'https://www.usq.edu.au/study/degrees/sciences/environment-and-sustainability',
'https://www.usq.edu.au/study/degrees/humanities-and-communication/indigenous-studies',
'https://www.usq.edu.au/study/degrees/humanities-and-communication/legal-studies',
'https://www.usq.edu.au/study/degrees/sciences/applied-data-science',
'https://www.usq.edu.au/study/degrees/engineering/computer-systems-engineering',
'https://www.usq.edu.au/study/degrees/arts/theatre',
'https://www.usq.edu.au/study/degrees/humanities-and-communication/creative-writing',
'https://www.usq.edu.au/study/degrees/sciences/biology',
'https://www.usq.edu.au/study/degrees/sciences/physics-and-physical-sciences',
'https://www.usq.edu.au/study/degrees/sciences/astronomy',
'https://www.usq.edu.au/study/degrees/business/sustainable-business-and-economics',
'https://www.usq.edu.au/study/degrees/sciences/mathematics-and-statistics',
'https://www.usq.edu.au/study/degrees/business/human-resource-management',
'https://www.usq.edu.au/study/degrees/education/secondary-education',
'https://www.usq.edu.au/study/degrees/humanities-and-communication/anthropology',
'https://www.usq.edu.au/study/degrees/it/information-technology',
'https://www.usq.edu.au/study/degrees/business/tourism-and-events-management',
'https://www.usq.edu.au/study/degrees/education/primary-education',
'https://www.usq.edu.au/study/degrees/engineering/civil-engineering',
'https://www.usq.edu.au/study/degrees/humanities-and-communication/international-relations',
'https://www.usq.edu.au/study/degrees/sciences/agricultural-science',
'https://www.usq.edu.au/study/degrees/health-and-community/biomedical-and-medical-laboratory-science',
'https://www.usq.edu.au/study/degrees/sciences/chemistry',
'https://www.usq.edu.au/study/degrees/engineering/urban-and-regional-planning',
'https://www.usq.edu.au/study/degrees/business/accounting',
'https://www.usq.edu.au/study/degrees/humanities-and-communication/history',
'https://www.usq.edu.au/study/degrees/sciences/food-science',
'https://www.usq.edu.au/study/degrees/business/aviation',
'https://www.usq.edu.au/study/degrees/business/marketing',
'https://www.usq.edu.au/study/degrees/diploma-of-university-studies/international',
'https://www.usq.edu.au/study/degrees/bachelor-of-creative-arts/theatre/international',
'https://www.usq.edu.au/study/degrees/master-of-learning-and-teaching/secondary',
'https://www.usq.edu.au/study/degrees/master-of-science-research/psychology-research',
'https://www.usq.edu.au/study/degrees/english-for-academic-purposes/international',
'https://www.usq.edu.au/study/degrees/bachelor-of-creative-arts/film-television-radio/international',
'https://www.usq.edu.au/study/degrees/bachelor-of-creative-arts/visual-arts/international',
'https://www.usq.edu.au/study/degrees/bachelor-of-creative-arts/music/international',
'https://www.usq.edu.au/study/degrees/diploma-of-english-for-university-studies/international',
'https://www.usq.edu.au/study/degrees/master-of-counselling/foundations-of-practice/international',
'https://www.usq.edu.au/study/degrees/bachelor-of-science-honours/biology/international',
'https://www.usq.edu.au/study/degrees/bachelor-of-communication-and-media/television-radio-extended/international',
'https://www.usq.edu.au/study/degrees/bachelor-of-communication-and-media/television-radio/international',
'https://www.usq.edu.au/study/degrees/bachelor-of-communication-and-media/public-relations-extended/international',
'https://www.usq.edu.au/study/degrees/bachelor-of-science-honours/physics/international',
'https://www.usq.edu.au/study/degrees/bachelor-of-communication-and-media/journalism/international',
'https://www.usq.edu.au/study/degrees/bachelor-of-communication-and-media/communication-media-studies/international',
'https://www.usq.edu.au/study/degrees/bachelor-of-communication-and-media/public-relations/international',
'https://www.usq.edu.au/study/degrees/bachelor-of-communication-and-media/advertising/international',
'https://www.usq.edu.au/study/degrees/english-language-intensive-courses-for-overseas-students/international',
'https://www.usq.edu.au/study/degrees/bachelor-of-communication-and-media/marketing/international',
'https://www.usq.edu.au/study/degrees/bachelor-of-science-honours/environment-sustainability/international',
'https://www.usq.edu.au/study/degrees/bachelor-of-science-honours/applied-mathematics-statistics/international',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-science/physics/international',
'https://www.usq.edu.au/study/degrees/graduate-diploma-of-science/physics-astronomy/international',
'https://www.usq.edu.au/study/degrees/graduate-diploma-of-business/international',
'https://www.usq.edu.au/study/degrees/master-of-health/gerontology/international',
'https://www.usq.edu.au/study/degrees/bachelor-of-communication-and-media/journalism-extended/international',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-engineering-science',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-engineering-science/structural-engineering/international',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-engineering-science/agricultural-engineering/international',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-engineering-science/environmental-engineering/international',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-engineering-science/power-engineering/international',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-business/international',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-education/early-childhood/international',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-engineering-science/civil-engineering/international',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-engineering-science/mechanical-engineering/international',
'https://www.usq.edu.au/study/degrees/bachelor-of-communication-and-media/journalism-extended/international',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-engineering-science',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-engineering-science/structural-engineering/international',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-engineering-science/agricultural-engineering/international',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-engineering-science/environmental-engineering/international',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-engineering-science/power-engineering/international',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-business/international',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-education/early-childhood/international',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-engineering-science/civil-engineering/international',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-engineering-science/mechanical-engineering/international',
'https://www.usq.edu.au/handbook/current/conted/cpa.html',
'https://www.usq.edu.au/handbook/current/business-commerce/mmgt.html',
'https://www.usq.edu.au/handbook/current/pdfs/msta.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/mlad.pdf',
'https://www.usq.edu.au/handbook/current/law-justice/bclw.html',
'https://www.usq.edu.au/handbook/current/eng-lang/eapp.html',
'https://www.usq.edu.au/handbook/current/engineering-built-environment/menc.html',
'https://www.usq.edu.au/handbook/current/education/bvet.html',
'https://www.usq.edu.au/handbook/current/business-commerce/basb.html',
'https://www.usq.edu.au/handbook/current/law-justice/law-justice-all.html',
'https://www.usq.edu.au/handbook/current/business-commerce/bcsc.html',
'https://www.usq.edu.au/handbook/current/pdfs/bcla.pdf',
'https://www.usq.edu.au/handbook/current/sciences/bsch.html',
'https://www.usq.edu.au/handbook/current/pathways/dssf.html',
'https://www.usq.edu.au/handbook/current/humanities-communication/bahn.html',
'https://www.usq.edu.au/handbook/current/pathways/dobf.html',
'https://www.usq.edu.au/handbook/current/pdfs/dpba.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/misx.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/gcbs.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/bech.pdf',
'https://www.usq.edu.au/handbook/current/information-technology/mscn.html',
'https://www.usq.edu.au/handbook/current/humanities-communication/bcmm.html',
'https://www.usq.edu.au/handbook/current/education/pgtt.html',
'https://www.usq.edu.au/handbook/current/pdfs/pgce.pdf',
'https://www.usq.edu.au/handbook/current/pathways/desf.html',
'https://www.usq.edu.au/handbook/current/pdfs/blaw.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/mmnt.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/bcit.pdf',
'https://www.usq.edu.au/handbook/current/health-community/dhsd.html',
'https://www.usq.edu.au/handbook/current/pdfs/dssf.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/metc.pdf',
'https://www.usq.edu.au/handbook/current/pathways/disf.html',
'https://www.usq.edu.au/handbook/current/creative-arts-media/bcnm.html',
'https://www.usq.edu.au/handbook/current/pdfs/mprl.pdf',
'https://www.usq.edu.au/handbook/current/humanities-communication/bssc.html',
'https://www.usq.edu.au/handbook/current/eng-lang/ceus.html',
'https://www.usq.edu.au/handbook/current/creative-arts-media/babl.html',
'https://www.usq.edu.au/handbook/current/pdfs/dcwd.pdf',
'https://www.usq.edu.au/handbook/current/creative-arts-media/bahn.html',
'https://www.usq.edu.au/handbook/current/pdfs/bcbz.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/bssc.pdf',
'https://www.usq.edu.au/handbook/current/health-community/bsch.html',
'https://www.usq.edu.au/handbook/current/pdfs/mscn.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/dpsc.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/bbus.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/bacs.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/desf.pdf',
'https://www.usq.edu.au/handbook/current/information-technology/misp.html',
'https://www.usq.edu.au/handbook/current/pdfs/bedu.pdf',
'https://www.usq.edu.au/handbook/current/business-commerce/dpba.html',
'https://www.usq.edu.au/handbook/current/information-technology/misx.html',
'https://www.usq.edu.au/handbook/current/pdfs/basb.pdf',
'https://www.usq.edu.au/handbook/current/humanities-communication/msta.html',
'https://www.usq.edu.au/handbook/current/pdfs/aepp.pdf',
'https://www.usq.edu.au/handbook/current/education/molt.html',
'https://www.usq.edu.au/handbook/current/engineering-built-environment/metc.html',
'https://www.usq.edu.au/handbook/current/creative-arts-media/msta.html',
'https://www.usq.edu.au/handbook/current/pdfs/bnbv.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/bbla.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/bcar.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/gdbs.pdf',
'https://www.usq.edu.au/handbook/current/sciences/mscr.html',
'https://www.usq.edu.au/handbook/current/creative-arts-media/bcar.html',
'https://www.usq.edu.au/handbook/current/information-technology/mcop.html',
'https://www.usq.edu.au/handbook/current/pdfs/ceus.pdf',
'https://www.usq.edu.au/handbook/current/information-technology/pcbs.html',
'https://www.usq.edu.au/handbook/current/optionstudies/rep.html',
'https://www.usq.edu.au/handbook/current/education/pgld.html',
'https://www.usq.edu.au/handbook/current/business-commerce/mmnt.html',
'https://www.usq.edu.au/handbook/current/pdfs/mmgt.pdf',
'https://www.usq.edu.au/handbook/current/business-commerce/gcbs.html',
'https://www.usq.edu.au/handbook/current/information-technology/information-technology.html',
'https://www.usq.edu.au/handbook/current/pdfs/mpae.pdf',
'https://www.usq.edu.au/handbook/current/business-commerce/adbs.html',
'https://www.usq.edu.au/handbook/current/pdfs/bcra.pdf',
'https://www.usq.edu.au/handbook/current/engineering-built-environment/msst.html',
'https://www.usq.edu.au/handbook/current/education/bech.html',
'https://www.usq.edu.au/handbook/current/pdfs/pgcn.pdf',
'https://www.usq.edu.au/handbook/current/information-technology/dosf.html',
'https://www.usq.edu.au/handbook/current/information-technology/mist.html',
'https://www.usq.edu.au/handbook/current/pdfs/bitc.pdf',
'https://www.usq.edu.au/handbook/current/humanities-communication/bist.html',
'https://www.usq.edu.au/handbook/current/business-commerce/mp12.html',
'https://www.usq.edu.au/handbook/current/business-commerce/mpac.html',
'https://www.usq.edu.au/handbook/current/pathways/aepp.html',
'https://www.usq.edu.au/handbook/current/health-community/dssf.html',
'https://www.usq.edu.au/handbook/current/sciences/mscn.html',
'https://www.usq.edu.au/handbook/current/pdfs/bahn.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/med1.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/dhsd.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/mspt.pdf',
'https://www.usq.edu.au/handbook/current/engineering-built-environment/pgcn.html',
'https://www.usq.edu.au/handbook/current/business-commerce/bavn.html',
'https://www.usq.edu.au/handbook/current/pdfs/douf.pdf',
'https://www.usq.edu.au/handbook/current/law-justice/djur.html',
'https://www.usq.edu.au/handbook/current/pdfs/ihep.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/mbsr.pdf',
'https://www.usq.edu.au/handbook/current/pathways/fdus.html',
'https://www.usq.edu.au/handbook/current/pdfs/bedh.pdf',
'https://www.usq.edu.au/handbook/current/allprog.html',
'https://www.usq.edu.au/handbook/current/pdfs/pcbs.pdf',
'https://www.usq.edu.au/handbook/current/law-justice/balw.html',
'https://www.usq.edu.au/handbook/current/health-community/gcse.html',
'https://www.usq.edu.au/handbook/current/pdfs/disf.pdf',
'https://www.usq.edu.au/handbook/current/education/education.html',
'https://www.usq.edu.au/handbook/current/information-technology/mctn.html',
'https://www.usq.edu.au/handbook/current/engineering-built-environment/desf.html',
'https://www.usq.edu.au/handbook/current/pdfs/bcom.pdf',
'https://www.usq.edu.au/handbook/current/business-commerce/business-commerce.html',
'https://www.usq.edu.au/handbook/current/pdfs/djur.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/eapp.pdf',
'https://www.usq.edu.au/handbook/current/eng-lang/deus.html',
'https://www.usq.edu.au/handbook/current/engineering-built-environment/bens.html',
'https://www.usq.edu.au/handbook/current/engineering-built-environment/mssr.html',
'https://www.usq.edu.au/handbook/current/law-justice/blaw.html',
'https://www.usq.edu.au/handbook/current/information-technology/mbis.html',
'https://www.usq.edu.au/handbook/current/business-commerce/gdbs.html',
'https://www.usq.edu.au/handbook/current/pdfs/bcsc.pdf',
'https://www.usq.edu.au/handbook/current/creative-arts-media/creative-arts-media-all.html',
'https://www.usq.edu.au/handbook/current/humanities-communication/bcnm.html',
'https://www.usq.edu.au/handbook/current/pdfs/fdus.pdf',
'https://www.usq.edu.au/handbook/current/sciences/bsci.html',
'https://www.usq.edu.au/handbook/current/pdfs/pgld.pdf',
'https://www.usq.edu.au/handbook/current/business-commerce/mpae.html',
'https://www.usq.edu.au/handbook/current/pdfs/med3.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/bavn.pdf',
'https://www.usq.edu.au/handbook/current/engineering-built-environment/bnbv.html',
'https://www.usq.edu.au/handbook/current/pdfs/dous.pdf',
'https://www.usq.edu.au/handbook/current/law-justice/law-justice.html',
'https://www.usq.edu.au/handbook/current/pdfs/msst.pdf',
'https://www.usq.edu.au/handbook/current/business-commerce/dobf.html',
'https://www.usq.edu.au/handbook/current/pdfs/dosf.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/dart.pdf',
'https://www.usq.edu.au/handbook/current/education/medcormedf.html',
'https://www.usq.edu.au/handbook/current/humanities-communication/bart.html',
'https://www.usq.edu.au/handbook/current/business-commerce/bclw.html',
'https://www.usq.edu.au/handbook/current/law-justice/pcbs.html',
'https://www.usq.edu.au/handbook/current/pathways/ihpp.html',
'https://www.usq.edu.au/handbook/current/pdfs/bcmm.pdf',
'https://www.usq.edu.au/handbook/current/health-community/bcsc.html',
'https://www.usq.edu.au/handbook/current/creative-arts-media/bart.html',
'https://www.usq.edu.au/handbook/current/pdfs/btwn.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/mlda.pdf',
'https://www.usq.edu.au/handbook/current/law-justice/bcla.html',
'https://www.usq.edu.au/handbook/current/sciences/bcsc.html',
'https://www.usq.edu.au/handbook/current/pdfs/mbap.pdf',
'https://www.usq.edu.au/handbook/current/education/bnbv.html',
'https://www.usq.edu.au/handbook/current/humanities-communication/humanities-communication-all.html',
'https://www.usq.edu.au/handbook/current/pdfs/bclw.pdf',
'https://www.usq.edu.au/handbook/current/sciences/dpsc.html',
'https://www.usq.edu.au/handbook/current/filter-programs.html',
'https://www.usq.edu.au/handbook/current/pathways/dcaf.html',
'https://www.usq.edu.au/handbook/current/business-commerce/bitc.html',
'https://www.usq.edu.au/handbook/current/sciences/btwn.html',
'https://www.usq.edu.au/handbook/current/humanities-communication/balw.html',
'https://www.usq.edu.au/handbook/current/business-commerce/bsbc.html',
'https://www.usq.edu.au/handbook/current/humanities-communication/mprl.html',
'https://www.usq.edu.au/handbook/current/pdfs/mctn.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/mist.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/medcormedf.pdf',
'https://www.usq.edu.au/handbook/current/creative-arts-media/creative-arts-media.html',
'https://www.usq.edu.au/handbook/current/pdfs/mapl.pdf',
'https://www.usq.edu.au/handbook/current/education/bedh.html',
'https://www.usq.edu.au/handbook/current/law-justice/babl.html',
'https://www.usq.edu.au/handbook/current/pdfs/mscr.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/dobf.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/bart.pdf',
'https://www.usq.edu.au/handbook/current/information-technology/gcbs.html',
'https://www.usq.edu.au/handbook/current/information-technology/bsch.html',
'https://www.usq.edu.au/handbook/current/pdfs/gdto.pdf',
'https://www.usq.edu.au/handbook/current/information-technology/bbcm.html',
'https://www.usq.edu.au/handbook/current/pdfs/gdedorgdef.pdf',
'https://www.usq.edu.au/handbook/current/sciences/sciences-all.html',
'https://www.usq.edu.au/handbook/current/creative-arts-media/bcra.html',
'https://www.usq.edu.au/handbook/current/information-technology/gdbs.html',
'https://www.usq.edu.au/handbook/current/engineering-built-environment/betc.html',
'https://www.usq.edu.au/handbook/current/creative-arts-media/dart.html',
'https://www.usq.edu.au/handbook/current/pdfs/misp.pdf',
'https://www.usq.edu.au/handbook/current/education/mld1.html',
'https://www.usq.edu.au/handbook/current/pdfs/bsbc.pdf',
'https://www.usq.edu.au/handbook/current/business-commerce/bbad.html',
'https://www.usq.edu.au/handbook/current/information-technology/bitc.html',
'https://www.usq.edu.au/handbook/current/business-commerce/bcbz.html',
'https://www.usq.edu.au/handbook/current/education/pgce.html',
'https://www.usq.edu.au/handbook/current/pdfs/deus.pdf',
'https://www.usq.edu.au/handbook/current/pathways/dosf.html',
'https://www.usq.edu.au/handbook/current/pdfs/bcse.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/mp12.pdf',
'https://www.usq.edu.au/handbook/current/business-commerce/mbsr.html',
'https://www.usq.edu.au/handbook/current/health-community/mscr.html',
'https://www.usq.edu.au/handbook/current/business-commerce/bbad.html',
'https://www.usq.edu.au/handbook/current/information-technology/bitc.html',
'https://www.usq.edu.au/handbook/current/business-commerce/bcbz.html',
'https://www.usq.edu.au/handbook/current/education/pgce.html',
'https://www.usq.edu.au/handbook/current/pdfs/deus.pdf',
'https://www.usq.edu.au/handbook/current/pathways/dosf.html',
'https://www.usq.edu.au/handbook/current/pdfs/bcse.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/mp12.pdf',
'https://www.usq.edu.au/handbook/current/business-commerce/mbsr.html',
'https://www.usq.edu.au/handbook/current/health-community/mscr.html',
'https://www.usq.edu.au/handbook/current/health-community/health-community-all.html',
'https://www.usq.edu.au/handbook/current/health-community/health-community.html',
'https://www.usq.edu.au/handbook/current/pdfs/mcop.pdf',
'https://www.usq.edu.au/handbook/current/education/med1.html',
'https://www.usq.edu.au/handbook/current/engineering-built-environment/engineering-built-environment-all.html',
'https://www.usq.edu.au/handbook/current/business-commerce/mbap.html',
'https://www.usq.edu.au/handbook/current/education/mapl.html',
'https://www.usq.edu.au/handbook/current/business-commerce/bcin.html',
'https://www.usq.edu.au/handbook/current/pdfs/dcaf.pdf',
'https://www.usq.edu.au/handbook/current/information-technology/bcin.html',
'https://www.usq.edu.au/handbook/current/pdfs/bbit.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/adbc.pdf',
'https://www.usq.edu.au/handbook/current/sciences/bcse.html',
'https://www.usq.edu.au/handbook/current/humanities-communication/dart.html',
'https://www.usq.edu.au/handbook/current/pdfs/adbs.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/cous.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/bist.pdf',
'https://www.usq.edu.au/handbook/current/pathways/aceqorpreportppg.html',
'https://www.usq.edu.au/handbook/current/health-community/bbmh.html',
'https://www.usq.edu.au/handbook/current/health-community/dcwd.html',
'https://www.usq.edu.au/handbook/current/pdfs/bcnm.pdf',
'https://www.usq.edu.au/handbook/current/education/education-all.html',
'https://www.usq.edu.au/handbook/current/pdfs/menc.pdf',
'https://www.usq.edu.au/handbook/current/law-justice/gcbs.html',
'https://www.usq.edu.au/handbook/current/education/mlda.html',
'https://www.usq.edu.au/handbook/current/engineering-built-environment/engineering-built-environment.html',
'https://www.usq.edu.au/handbook/current/humanities-communication/humanities-communication.html',
'https://www.usq.edu.au/handbook/current/pathways/douf.html',
'https://www.usq.edu.au/handbook/current/creative-arts-media/balw.html',
'https://www.usq.edu.au/handbook/current/pathways/dous.html',
'https://www.usq.edu.au/handbook/current/humanities-communication/mara.html',
'https://www.usq.edu.au/handbook/current/law-justice/bbla.html',
'https://www.usq.edu.au/handbook/current/information-technology/information-technology-all.html',
'https://www.usq.edu.au/handbook/current/business-commerce/bbit.html',
'https://www.usq.edu.au/handbook/current/pathways/ihep.html',
'https://www.usq.edu.au/handbook/current/pdfs/aceqorpreportppg.pdf',
'https://www.usq.edu.au/handbook/current/business-commerce/adbc.html',
'https://www.usq.edu.au/handbook/current/pdfs/bsch.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/bbmh.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/ihpp.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/bapm.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/mpac.pdf',
'https://www.usq.edu.au/handbook/current/education/bedu.html',
'https://www.usq.edu.au/handbook/current/education/gdto.html',
'https://www.usq.edu.au/handbook/current/allprog-all.html',
'https://www.usq.edu.au/handbook/current/pathways/cous.html',
'https://www.usq.edu.au/handbook/current/information-technology/bsci.html',
'https://www.usq.edu.au/handbook/current/engineering-built-environment/mspt.html',
'https://www.usq.edu.au/handbook/current/pdfs/pgtt.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/bvet.pdf',
'https://www.usq.edu.au/handbook/current/creative-arts-media/mara.html',
'https://www.usq.edu.au/handbook/current/business-commerce/pcbs.html',
'https://www.usq.edu.au/handbook/current/business-commerce/bcit.html',
'https://www.usq.edu.au/handbook/current/pdfs/bbcm.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/molt.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/bsci.pdf',
'https://www.usq.edu.au/handbook/current/humanities-communication/babl.html',
'https://www.usq.edu.au/handbook/current/pdfs/mssr.pdf',
'https://www.usq.edu.au/handbook/current/business-commerce/bbus.html',
'https://www.usq.edu.au/handbook/current/creative-arts-media/bapm.html',
'https://www.usq.edu.au/handbook/current/business-commerce/bcom.html',
'https://www.usq.edu.au/handbook/current/pdfs/mld1.pdf',
'https://www.usq.edu.au/handbook/current/health-community/bsci.html',
'https://www.usq.edu.au/handbook/current/education/gdedorgdef.html',
'https://www.usq.edu.au/handbook/current/information-technology/bcsc.html',
'https://www.usq.edu.au/handbook/current/pdfs/mbis.pdf',
'https://www.usq.edu.au/handbook/current/education/med3.html',
'https://www.usq.edu.au/handbook/current/pdfs/mara.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/gcse.pdf'
]

    for i in Lists:
        fullurl = base_url % i
        start_urls.append(fullurl)

    # rules = (
    #     # Rule(LinkExtractor(allow=(r'.*'), restrict_xpaths=('')),callback='parse_item', follow=True),
    #     Rule(LinkExtractor(allow=r'https://www.usq.edu.au/extrafiles/templates/gsa/search.htm\?q=undergraduate&proxystylesheet=USQ_Search&site=USQ_Degrees&d=1519875929197&page=\d+'),follow=True),
    #     Rule(LinkExtractor(allow=(r'.*'),restrict_xpaths=('//*[@id="USQ_Degrees"]/div/h3/a')),callback='parse_item', follow=False),
    #     # Rule(LinkExtractor(allow=(r'.*'), restrict_xpaths=('//*[@id="wrapper"]//div[@class="component component--wysiwyg"]/p/font/a')),callback='parse_item', follow=False),
    # )

    def parse(self,response):
        print('==================================',response.url)
        item = HooliItem()

        url = response.url
        print(1,url)

        university = 'University of South Queensland'
        print(2,university)

        department = "NULL"
        # department_s = ''.join(department_s).replace('\n','')
        # try:
        #     if "Offered by:" in department_s:
        #         start = department_s.find("Offered by:")
        #         department = department_s[start:]
        #         department = department[:80]
        #         department = department.lstrip("Offered by:")
        #         item["department"] = department
        #     else:
        #         department = "NULL"
        #
        # except:
        #     department = "报错!"
        #
        # print(3,department)

        country = 'Australia'
        city = "South Queensland"
        website = 'https://www.usq.edu.au/'
        degree_level = '0'

        # programme = response.xpath('//div[@class="section picture-nav"]/h1/text()').extract()
        programme = response.xpath('//*[@id="main-wrap"]/section/div/div/div/h1/text()').extract()
        programme = ''.join(programme)
        print(4,programme)

        ucas_code = "NULL"
        # ucas_code_s = ''.join(ucas_code_s).replace('    ','').replace('\n','')
        # try:
        #     if "VU course code:" in ucas_code_s:
        #         start = ucas_code_s.find("VU course code:")
        #         ucas_code = ucas_code_s[start:]
        #         ucas_code = ucas_code[:50]
        #         ucas_code = ucas_code.lstrip("VU course code:")
        #         item["ucas_code"] = ucas_code
        #     else:
        #         ucas_code = "NULL"
        # except:
        #     ucas_code = "报错!"
        # print(5,ucas_code)

        # degree_type = response.xpath('//div[@class="section picture-nav"]/h1/text()').extract()
        degree_type = response.xpath('//*[@id="main-wrap"]/section//div/h1/text()').extract()
        degree_type = ''.join(degree_type)
        # degree_type = self.getDegree_type(degree_type)
        try:
            if "Bachelor" in degree_type:
                degree_type = "Bachelor"
            elif "Master" in degree_type:
                degree_type = "Master"
            elif "Doctor" in degree_type:
                degree_type = "Doctor"
            else:
                degree_type = "NULL"
        except:
            degree_type = "报错!"
        print(6,degree_type)

        start_date_s = response.xpath('//*[@id="summary"]//div[@class="program-details__detail-section"]//text()').extract()
        start_date_s = ''.join(start_date_s)
        try:
            if " Start" in start_date_s:
                start = start_date_s.find(" Start")
                start_date = start_date_s[start:]
                start_date = start_date[:100]
                item["start_date"] = start_date
            else:
                start_date = "NULL"
        except:
            start_date = "报错!"
        print(7,start_date)

        # overview = response.xpath('//div[@class="left logo-bg"]//text()').extract()
        overview = response.xpath('//*[@class="col-sm-12 aligned-content-top"]/p/text()').extract()
        overview = ''.join(overview).replace('\n','')
        print(7, overview)

        mode_s = response.xpath('//*[@id="summary"]//div[@class="program-details__detail-section"]//text()').extract()
        mode_s = ''.join(mode_s)
        try:
            if " Duration" in mode_s:
                start = mode_s.find("Duration")
                mode = mode_s[start:]
                mode = mode[:80]
                mode = mode.lstrip("Duration")
                item["mode"] = mode
            else:
                mode = "NULL"
        except:
            mode = "报错!"
        print(8,mode)



        duration_s = response.xpath('//*[@id="summary"]//div[@class="program-details__detail-section"]//text()').extract()
        duration_s = ''.join(duration_s)
        # duration = duration.replace('\n','')
        # duration = duration.replace('    ','')
        try:
            if "Duration" in duration_s:
                start = duration_s.find("Duration")
                # end = duration_s.find("Location:")
                duration = duration_s[start:]
                duration = duration[:100]
                duration = duration.lstrip("Duration")
                item["duration"] = duration
            else:
                duration = "NULL"
        except:
            duration = "报错!"
        print(9,duration)

        modules = response.xpath('//*[@id="combination-0-collapse"]/div//text()').extract()
        modules = ''.join(modules)
        modules = modules.replace('\n','')
        # try:
        #     if "Modules" in modules_s:
        #         start = modules_s.find("Modules")
        #         end = modules_s.find("Assessment")
        #         modules = modules_s[start:end]
        #         item["modules"] = modules
        #     else:
        #         modules = modules_s
        # except:
        #     modules = modules_s
        print(10,modules)

        teaching = 'NULL'

        assessment = 'NULL'
        # assessment_s = ''.join(assessment_s).replace("\r\n","").replace('      ','').replace('\n','')
        # try:
        #     if "Admission & pathways" in assessment_s:
        #         start = assessment_s.find("Admission & pathways")
        #         end = assessment_s.find("How to apply")
        #         assessment = assessment_s[start:end]
        #         item["assessment"] = assessment
        #     else:
        #         assessment = "NULL"
        # except:
        #     assessment = "报错!"
        # print(11, assessment)

        career = response.xpath('//*[@id="careerOutcomesCollapse"]/div/p/text()').extract()
        career = ''.join(career)

        # try:
        #     if "Career opportunities" in career_s:
        #         start = career_s.find("Career opportunities")
        #         end = career_s.find("Course specific information")
        #         career = career_s[start:end]
        #         item["career"] = career
        #     else:
        #         career = "NULL"
        # except:
        #     career = "报错!"
        print(12,career)

        application_date = "NULL"

        deadline = 'NULL'
        # deadline = ''.join(deadline)
        # print(9,deadline)

        application_fee = 'NULL'

        tuition_fee_s = response.xpath('//*[@id="fees"]/div/div/table/tbody/tr/td/text()').extract()
        tuition_fee_s = ''.join(tuition_fee_s)
        # tuition_fee = tuition_fee.replace('\n','')
        # tuition_fee = tuition_fee.replace('    ','')
        tuition_fee_s = self.getTuition_fee(tuition_fee_s)
        try:
            if tuition_fee_s > 0:
                tuition_fee = tuition_fee_s
            else:
                tuition_fee = "CSP"
        except:
            tuition_fee = "报错!"

        print(13, tuition_fee)

        location = "NULL"
        # location_s = ''.join(location_s)
        # try:
        #     if "Location:" in location_s:
        #         start = location_s.find("Location:")
        #         location = location_s[start:]
        #         location = location[:30]
        #         location = location.lstrip("Location:")
        #         item["location"] = location
        #     else:
        #         location = "NULL"
        # except:
        #     location = "报错!"
        # print(14,location)

        ATAS = 'NULL'

        GPA = 'NULL'

        average_score = 'NULL'

        accredited_university = 'NULL'

        Alevel = 'NULL'

        IB = 'NULL'

        IELTS_s = response.xpath('//*[@id="entry-requirements"]/div/div/p//text()').extract()
        IELTS_s = ''.join(IELTS_s)
        # # IELTS = re.findall('(IELTS:|IELTS)? (.*){0,5} \d?.\d? .{0,70}',IELTS)
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
        LSAT = "NULL"
        MCAT = 'NULL'

        working_experience = 'NULL'

        interview = 'NULL'

        portfolio = 'NULL'

        application_documents = 'NULL'

        how_to_apply = "NULL"
        # how_to_apply = ''.join(how_to_apply)
        # try:
        #     if "How to Apply" in how_to_apply_s:
        #         start = how_to_apply_s.find("How to Apply")
        #         end = how_to_apply_s.find("Entry requirements")
        #         how_to_apply = how_to_apply_s[start:end]
        #         item["how_to_apply"] = how_to_apply
        #     else:
        #         how_to_apply = how_to_apply_s
        # except:
        #     how_to_apply = '报错!'
        # print(15,how_to_apply)

        entry_requirements = response.xpath('//*[@id="entry-requirements"]/div/div/ul//text()').extract()
        entry_requirements = ''.join(entry_requirements)
        # # EntryRequirements = EntryRequirements.replace(' ','')
        # # try:
        # #     if "Entry requirements" in entry_requirements_s:
        # #         start = entry_requirements_s.find("Entry requirements")
        # #         end = entry_requirements_s.find("Study options")
        # #         entry_requirements = entry_requirements_s[start:end]
        # #         item["entry_requirements"] = entry_requirements
        # #     else:
        # #         entry_requirements = entry_requirements_s
        # #
        # # except:
        # #     entry_requirements = '报错!'
        #
        print(12,entry_requirements)

        chinese_requirements = "NULL"

        school_test = 'NULL'

        degree_description = "NULL"

        SATI = 'NULL'

        SATII = 'NULL'

        SAT_code = 'NULL'

        ACT = 'NULL'

        ACT_code = 'NULL'

        other = 'NULL'

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
        allfee = re.findall(r'\d+', tuition_fee)
        # print(allfee)
        for index in range(len(allfee)):
            fee = allfee[index]
            allfee[index] = ''.join(fee)
            # print(allfee[index])
        # print(allfee)
        maxfee = 0
        for fee in allfee:
            if int(fee) >= maxfee:
                maxfee = int(fee)
        return maxfee

