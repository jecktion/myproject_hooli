
# -*- coding: utf-8 -*-






import scrapy
from school_3.items import HooliItem
import datetime
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import re

class PlymouthSpider(scrapy.Spider):
    name = 'South_Queensland_pg_2'
    allowed_domains = ['www.usq.edu.au']
    start_urls = []
    base_url = '%s'

    Lists = ['https://www.usq.edu.au/study/degrees/sciences-postgraduate',
'https://www.usq.edu.au/handbook/current/business-commerce/pcbs.html',
'https://www.usq.edu.au/handbook/current/education/pgce.html',
'https://www.usq.edu.au/handbook/current/education/pgal.html',
'https://www.usq.edu.au/handbook/current/engineering-built-environment/pgcn.html',
'https://www.usq.edu.au/handbook/current/information-technology/pcbs.html',
'https://www.usq.edu.au/handbook/current/law-justice/pcbs.html',
'https://www.usq.edu.au/handbook/current/education/pgld.html',
'https://www.usq.edu.au/handbook/current/sciences/pcss.html',
'https://www.usq.edu.au/handbook/current/education/pgtt.html',
'https://www.usq.edu.au/handbook/current/pdfs/pcbs.pdf',
'https://www.usq.edu.au/handbook/current/health-community/pdpp.html',
'https://www.usq.edu.au/handbook/current/pdfs/pgce.pdf',
'https://www.usq.edu.au/study/degrees/law-and-justice-postgraduate',
'https://www.usq.edu.au/handbook/current/pdfs/pgal.pdf',
'https://www.usq.edu.au/study/degrees/education-postgraduate',
'https://www.usq.edu.au/handbook/current/pdfs/pgcn.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/pgtt.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/pgld.pdf',
'https://www.usq.edu.au/study/degrees/humanities-and-communication-postgraduate',
'https://www.usq.edu.au/handbook/current/pdfs/pcss.pdf',
'https://www.usq.edu.au/study/degrees/education-postgraduate?sa=education',
'https://www.usq.edu.au/study/degrees/health-and-community-postgraduate?sa=health+%26+community',
'https://www.usq.edu.au/study/degrees/sciences-postgraduate?sa=sciences',
'https://www.usq.edu.au/study/degrees/engineering-and-built-environment-postgraduate?sa=engineering+%26built+environment',
'https://www.usq.edu.au/study/degrees/information-technology-postgraduate',
'https://www.usq.edu.au/study/degrees/business-executive',
'https://www.usq.edu.au/study/degrees/creative-arts-and-media-postgraduate',
'https://www.usq.edu.au/handbook/current/pdfs/pdpp.pdf',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-business',
'https://www.usq.edu.au/handbook/current/pdfs/pcss.pdf',
'https://www.usq.edu.au/study/degrees/education-postgraduate?sa=education',
'https://www.usq.edu.au/study/degrees/health-and-community-postgraduate?sa=health+%26+community',
'https://www.usq.edu.au/study/degrees/sciences-postgraduate?sa=sciences',
'https://www.usq.edu.au/study/degrees/engineering-and-built-environment-postgraduate?sa=engineering+%26built+environment',
'https://www.usq.edu.au/study/degrees/information-technology-postgraduate',
'https://www.usq.edu.au/study/degrees/business-executive',
'https://www.usq.edu.au/study/degrees/creative-arts-and-media-postgraduate',
'https://www.usq.edu.au/handbook/current/pdfs/pdpp.pdf',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-business',
'https://www.usq.edu.au/handbook/current/pdfs/mlad.pdf',
'https://www.usq.edu.au/handbook/current/education/mld1.html',
'https://www.usq.edu.au/handbook/current/education/medb.html',
'https://www.usq.edu.au/handbook/current/pdfs/medb.pdf',
'https://www.usq.edu.au/handbook/current/filter-programs.html',
'https://www.usq.edu.au/handbook/current/pdfs/menr.pdf',
'https://www.usq.edu.au/handbook/current/engineering-built-environment/menr.html',
'https://www.usq.edu.au/handbook/current/pdfs/eapp.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/mld1.pdf',
'https://www.usq.edu.au/handbook/current/humanities-communication/msta.html',
'https://www.usq.edu.au/handbook/current/creative-arts-media/msta.html',
'https://www.usq.edu.au/handbook/current/allprog.html',
'https://www.usq.edu.au/handbook/current/education/gdedorgdef.html',
'https://www.usq.edu.au/handbook/current/pdfs/mmnt.pdf',
'https://www.usq.edu.au/handbook/current/business-commerce/mmnt.html',
'https://www.usq.edu.au/handbook/current/pdfs/gdedorgdef.pdf',
'https://www.usq.edu.au/handbook/current/allprog-all.html',
'https://www.usq.edu.au/study/degrees/health-and-community/psychology',
'https://www.usq.edu.au/study/degrees/master-of-laws-research',
'https://www.usq.edu.au/study/degrees/health-and-community/mental-health',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-professional-studies',
'https://www.usq.edu.au/study/degrees/master-of-laws-research/international',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-professional-studies/international',
'https://www.usq.edu.au/study/degrees/careers/psychologist',
'https://www.usq.edu.au/study/degrees/careers/doctor',
'https://www.usq.edu.au/handbook/current/eng-lang/eapp.html',
'https://www.usq.edu.au/study/degrees/graduate-diploma-of-business',
'https://www.usq.edu.au/study/degrees/graduate-diploma-of-education-full-fee-paying/curriculum-pedagogical-leadership',
'https://www.usq.edu.au/study/degrees/graduate-diploma-of-education-commonwealth-supported/early-childhood',
'https://www.usq.edu.au/study/degrees/master-of-laws',
'https://www.usq.edu.au/study/degrees/graduate-diploma-of-engineering-science/environmental-engineering',
'https://www.usq.edu.au/study/degrees/graduate-diploma-of-engineering-science/civil-engineering',
'https://www.usq.edu.au/study/degrees/english-for-academic-purposes',
'https://www.usq.edu.au/study/degrees/english-for-academic-purposes/international',
'https://www.usq.edu.au/study/degrees/graduate-diploma-of-business/international',
'https://www.usq.edu.au/study/degrees/master-of-laws/international',
'https://www.usq.edu.au/study/degrees/graduate-diploma-of-education-commonwealth-supported/special-education',
'https://www.usq.edu.au/study/degrees/graduate-diploma-of-education-full-fee-paying/online-distributed-learning',
'https://www.usq.edu.au/study/degrees/graduate-diploma-of-education-full-fee-paying/curriculum-pedagogical-leadership/international',
'https://www.usq.edu.au/study/degrees/graduate-diploma-of-engineering-science/environmental-engineering/international',
'https://www.usq.edu.au/study/degrees/graduate-diploma-of-education-commonwealth-supported/early-childhood/international',
'https://www.usq.edu.au/study/degrees/graduate-diploma-of-engineering-science/civil-engineering/international',
'https://www.usq.edu.au/study/degrees/health-and-community/nursing',
'https://www.usq.edu.au/study/degrees/health-and-community/counselling',
'https://www.usq.edu.au/study/degrees/master-of-professional-studies-research',
'https://www.usq.edu.au/study/degrees/it/computing',
'https://www.usq.edu.au/study/degrees/health-and-community/child-youth-family',
'https://www.usq.edu.au/study/degrees/education/guidance-and-counselling',
'https://www.usq.edu.au/study/degrees/health-and-community/clinical-practice',
'https://www.usq.edu.au/handbook/current/business-commerce/mpac.html',
'https://www.usq.edu.au/handbook/current/education/maln.html',
'https://www.usq.edu.au/study/degrees/graduate-diploma-of-education-commonwealth-supported/special-education/international',
'https://www.usq.edu.au/handbook/current/education/medcormedf.html',
'https://www.usq.edu.au/handbook/current/pdfs/mpac.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/maln.pdf',
'https://www.usq.edu.au/study/degrees/master-of-professional-studies-research/international',
'https://www.usq.edu.au/study/degrees/graduate-diploma-of-engineering-science/agricultural-engineering',
'https://www.usq.edu.au/handbook/current/education/gced.html',
'https://www.usq.edu.au/handbook/current/information-technology/mbis.html',
'https://www.usq.edu.au/handbook/current/business-commerce/mbis.html',
'https://www.usq.edu.au/study/degrees/graduate-diploma-of-education-full-fee-paying/online-distributed-learning/international',
'https://www.usq.edu.au/handbook/current/pdfs/gced.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/medcormedf.pdf',
'https://www.usq.edu.au/study/degrees/graduate-diploma-of-engineering-science/agricultural-engineering/international',
'https://www.usq.edu.au/handbook/current/creative-arts-media/bcah.html',
'https://www.usq.edu.au/handbook/current/sciences/mssc.html',
'https://www.usq.edu.au/handbook/current/pdfs/mssc.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/mbai.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/menc.pdf',
'https://www.usq.edu.au/handbook/current/business-commerce/mbai.html',
'https://www.usq.edu.au/handbook/current/pdfs/gcbs.pdf',
'https://www.usq.edu.au/handbook/current/engineering-built-environment/menc.html',
'https://www.usq.edu.au/handbook/current/pdfs/bcah.pdf',
'https://www.usq.edu.au/handbook/current/business-commerce/mp12.html',
'https://www.usq.edu.au/handbook/current/business-commerce/mpae.html',
'https://www.usq.edu.au/handbook/current/pdfs/mp12.pdf',
'https://www.usq.edu.au/handbook/current/education/gcef.html',
'https://www.usq.edu.au/handbook/current/pdfs/mpae.pdf',
'https://www.usq.edu.au/handbook/current/information-technology/gcbs.html',
'https://www.usq.edu.au/handbook/current/business-commerce/gcbs.html',
'https://www.usq.edu.au/handbook/current/pdfs/gcbs.pdf',
'https://www.usq.edu.au/handbook/current/engineering-built-environment/menc.html',
'https://www.usq.edu.au/handbook/current/pdfs/bcah.pdf',
'https://www.usq.edu.au/handbook/current/business-commerce/mp12.html',
'https://www.usq.edu.au/handbook/current/business-commerce/mpae.html',
'https://www.usq.edu.au/handbook/current/pdfs/mp12.pdf',
'https://www.usq.edu.au/handbook/current/education/gcef.html',
'https://www.usq.edu.au/handbook/current/pdfs/mpae.pdf',
'https://www.usq.edu.au/handbook/current/information-technology/gcbs.html',
'https://www.usq.edu.au/handbook/current/business-commerce/gcbs.html',
'https://www.usq.edu.au/handbook/current/pdfs/gdbz.pdf',
'https://www.usq.edu.au/handbook/current/business-commerce/mmgt.html',
'https://www.usq.edu.au/handbook/current/information-technology/gcbu.html',
'https://www.usq.edu.au/handbook/current/business-commerce/gcbu.html',
'https://www.usq.edu.au/study/degrees/health-and-community/human-services',
'https://www.usq.edu.au/study/degrees/master-of-engineering-research',
'https://www.usq.edu.au/study/degrees/bachelor-of-science-honours/psychology',
'https://www.usq.edu.au/handbook/current/pdfs/gcbu.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/mmgt.pdf',
'https://www.usq.edu.au/handbook/current/education/education.html',
'https://www.usq.edu.au/handbook/current/business-commerce/mbac.html',
'https://www.usq.edu.au/handbook/current/education/meda.html',
'https://www.usq.edu.au/handbook/current/business-commerce/business-commerce.html',
'https://www.usq.edu.au/handbook/current/law-justice/law-justice.html',
'https://www.usq.edu.au/handbook/current/health-community/health-community.html',
'https://www.usq.edu.au/handbook/current/engineering-built-environment/engd.html',
'https://www.usq.edu.au/study/degrees/health-and-community',
'https://www.usq.edu.au/handbook/current/business-commerce/gcav.html',
'https://www.usq.edu.au/handbook/current/pdfs/gcav.pdf',
'https://www.usq.edu.au/study/degrees/bachelor-of-creative-arts',
'https://www.usq.edu.au/handbook/current/information-technology/information-technology.html',
'https://www.usq.edu.au/handbook/current/sciences/sciences.html',
'https://www.usq.edu.au/handbook/current/engineering-built-environment/engineering-built-environment.html',
'https://www.usq.edu.au/handbook/current/pdfs/engd.pdf',
'https://www.usq.edu.au/study/degrees/master-of-engineering-research/international',
'https://www.usq.edu.au/handbook/current/business-commerce/mbap.html',
'https://www.usq.edu.au/study/degrees/english-language-intensive-courses-for-overseas-students',
'https://www.usq.edu.au/study/degrees/bachelor-of-science-honours/biology',
'https://www.usq.edu.au/study/degrees/bachelor-of-science-honours/chemistry',
'https://www.usq.edu.au/study/degrees/bachelor-of-science-honours',
'https://www.usq.edu.au/handbook/current/pdfs/meda.pdf',
'https://www.usq.edu.au/study/degrees/bachelor-of-science-honours/physics',
'https://www.usq.edu.au/study/degrees/bachelor-of-science-honours/environment-sustainability',
'https://www.usq.edu.au/study/degrees/bachelor-of-science-honours/applied-mathematics-statistics',
'https://www.usq.edu.au/study/degrees/bachelor-of-arts/creative-critical-writing',
'https://www.usq.edu.au/study/degrees/bachelor-of-science-honours/psychology/international',
'https://www.usq.edu.au/handbook/current/pdfs/mbac.pdf',
'https://www.usq.edu.au/study/degrees/bachelor-of-science/biology',
'https://www.usq.edu.au/study/degrees/bachelor-of-science/physical-sciences',
'https://www.usq.edu.au/handbook/current/pdfs/dprs.pdf',
'https://www.usq.edu.au/study/degrees/bachelor-of-arts-honours/history',
'https://www.usq.edu.au/handbook/current/creative-arts-media/creative-arts-media.html',
'https://www.usq.edu.au/handbook/current/humanities-communication/humanities-communication.html',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-health/gerontology',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-health/scheduled-medicines',
'https://www.usq.edu.au/study/degrees/health-and-community/sport-and-exercise',
'https://www.usq.edu.au/study/degrees/master-of-psychology-phd-clinical-psychology',
'https://www.usq.edu.au/study/degrees/bachelor-of-sport-and-exercise/sport-exercise-science',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-science/biology',
'https://www.usq.edu.au/study/degrees/master-of-education-full-fee-paying/adult-professional-workplace-learning',
'https://www.usq.edu.au/study/degrees/graduate-diploma-of-education-commonwealth-supported/guidance-counselling',
'https://www.usq.edu.au/study/degrees/graduate-diploma-of-education-full-fee-paying/adult-professional-workplace-learning',
'https://www.usq.edu.au/study/degrees/graduate-diploma-of-education-full-fee-paying/leading-managing-educational-organisations',
'https://www.usq.edu.au/study/degrees/graduate-diploma-of-education-full-fee-paying/career-development',
'https://www.usq.edu.au/study/degrees/bachelor-of-arts-honours/social-justice-studies',
'https://www.usq.edu.au/study/degrees/master-of-education-full-fee-paying/career-development',
'https://www.usq.edu.au/study/degrees/master-of-psychology-clinical',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-spatial-science-technology/geographic-information-systems',
'https://www.usq.edu.au/study/degrees/graduate-diploma-of-spatial-science-technology/geographical-information-systems',
'https://www.usq.edu.au/study/degrees/master-of-education-commonwealth-supported/early-childhood',
'https://www.usq.edu.au/study/degrees/bachelor-of-arts-honours/journalism-studies',
'https://www.usq.edu.au/study/degrees/bachelor-of-science/human-physiology',
'https://www.usq.edu.au/study/degrees/master-of-arts/corporate-communication',
'https://www.usq.edu.au/study/degrees/master-of-business-administration/general',
'https://www.usq.edu.au/study/degrees/master-of-education-commonwealth-supported',
'https://www.usq.edu.au/study/degrees/graduate-diploma-of-spatial-science-technology/surveying',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-spatial-science-technology/surveying',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-engineering-science/agricultural-engineering',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-engineering-science/structural-engineering',
'https://www.usq.edu.au/study/degrees/graduate-diploma-of-engineering-science/structural-engineering',
'https://www.usq.edu.au/study/degrees/master-of-laws/comparative-law',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-engineering-science/environmental-engineering',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-engineering-science/power-engineering',
'https://www.usq.edu.au/study/degrees/graduate-diploma-of-engineering-science/power-engineering',
'https://www.usq.edu.au/study/degrees/bachelor-of-arts-honours/creative-critical-writing',
'https://www.usq.edu.au/study/degrees/bachelor-of-arts-honours/contemporary-media-studies',
'https://www.usq.edu.au/study/degrees/master-of-business-and-innovation/general',
'https://www.usq.edu.au/handbook/current/education/education-all.html',
'https://www.usq.edu.au/study/degrees/graduate-diploma-of-engineering-science/electrical-electronic-engineering',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-engineering-science/electrical-electronic-engineering',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-engineering-science/civil-engineering',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-business/general',
'https://www.usq.edu.au/study/degrees/bachelor-of-arts-honours/public-relations-studies',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-engineering-science/mechanical-engineering',
'https://www.usq.edu.au/study/degrees/graduate-diploma-of-engineering-science/mechanical-engineering',
'https://www.usq.edu.au/study/degrees/master-of-aviation/aviation-human-factors',
'https://www.usq.edu.au/study/degrees/master-of-aviation/aviation-management',
'https://www.usq.edu.au/handbook/current/business-commerce/gdav.html',
'https://www.usq.edu.au/handbook/current/pdfs/gdav.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/misp.pdf',
'https://www.usq.edu.au/study/degrees/careers/accountant',
'https://www.usq.edu.au/study/degrees/law-and-justice/law',
'https://www.usq.edu.au/study/degrees/it/information-systems',
'https://www.usq.edu.au/study/degrees/arts/film-television-and-radio',
'https://www.usq.edu.au/study/degrees/humanities-and-communication/communication-and-media',
'https://www.usq.edu.au/study/degrees/arts/visual-arts',
'https://www.usq.edu.au/study/degrees/engineering/power-engineering',
'https://www.usq.edu.au/study/degrees/engineering/geographic-information-systems',
'https://www.usq.edu.au/study/degrees/education/early-childhood',
'https://www.usq.edu.au/study/degrees/education/applied-linguistics-and-tesol',
'https://www.usq.edu.au/study/degrees/engineering/agricultural-engineering',
'https://www.usq.edu.au/study/degrees/business/international-business',
'https://www.usq.edu.au/study/degrees/humanities-and-communication/journalism',
'https://www.usq.edu.au/study/degrees/arts/music',
'https://www.usq.edu.au/study/degrees/business/management-and-leadership',
'https://www.usq.edu.au/study/degrees/engineering/environmental-engineering',
'https://www.usq.edu.au/study/degrees/humanities-and-communication/public-relations',
'https://www.usq.edu.au/study/degrees/business/project-management',
'https://www.usq.edu.au/study/degrees/education/adult-and-workplace-learning',
'https://www.usq.edu.au/study/degrees/engineering/mechanical-and-mechatronic-engineering',
'https://www.usq.edu.au/study/degrees/humanities-and-communication/professional-studies',
'https://www.usq.edu.au/study/degrees/sciences/wine-science',
'https://www.usq.edu.au/study/degrees/business/finance',
'https://www.usq.edu.au/study/degrees/humanities-and-communication/english-literature',
'https://www.usq.edu.au/study/degrees/health-and-community/health-leadership',
'https://www.usq.edu.au/study/degrees/sciences/climate-studies',
'https://www.usq.edu.au/study/degrees/education/education-leadership',
'https://www.usq.edu.au/study/degrees/engineering/electrical-and-electronic-engineering',
'https://www.usq.edu.au/study/degrees/engineering/surveying',
'https://www.usq.edu.au/study/degrees/sciences/environment-and-sustainability',
'https://www.usq.edu.au/study/degrees/sciences/applied-data-science',
'https://www.usq.edu.au/study/degrees/engineering/computer-systems-engineering',
'https://www.usq.edu.au/study/degrees/arts/theatre',
'https://www.usq.edu.au/study/degrees/sciences/biology',
'https://www.usq.edu.au/study/degrees/sciences/physics-and-physical-sciences',
'https://www.usq.edu.au/study/degrees/sciences/astronomy',
'https://www.usq.edu.au/study/degrees/business/sustainable-business-and-economics',
'https://www.usq.edu.au/study/degrees/sciences/mathematics-and-statistics',
'https://www.usq.edu.au/study/degrees/business/human-resource-management',
'https://www.usq.edu.au/study/degrees/humanities-and-communication/editing-and-publishing',
'https://www.usq.edu.au/study/degrees/education/secondary-education',
'https://www.usq.edu.au/study/degrees/health-and-community/alcohol-and-drug-studies',
'https://www.usq.edu.au/study/degrees/it/information-technology',
'https://www.usq.edu.au/study/degrees/education/primary-education',
'https://www.usq.edu.au/study/degrees/engineering/civil-engineering',
'https://www.usq.edu.au/study/degrees/humanities-and-communication/international-relations',
'https://www.usq.edu.au/study/degrees/engineering/engineering-management',
'https://www.usq.edu.au/study/degrees/sciences/agricultural-science',
'https://www.usq.edu.au/study/degrees/sciences/chemistry',
'https://www.usq.edu.au/study/degrees/health-and-community/rural-and-remote-health',
'https://www.usq.edu.au/study/degrees/education/secondary-education',
'https://www.usq.edu.au/study/degrees/health-and-community/alcohol-and-drug-studies',
'https://www.usq.edu.au/study/degrees/it/information-technology',
'https://www.usq.edu.au/study/degrees/education/primary-education',
'https://www.usq.edu.au/study/degrees/engineering/civil-engineering',
'https://www.usq.edu.au/study/degrees/humanities-and-communication/international-relations',
'https://www.usq.edu.au/study/degrees/engineering/engineering-management',
'https://www.usq.edu.au/study/degrees/sciences/agricultural-science',
'https://www.usq.edu.au/study/degrees/sciences/chemistry',
'https://www.usq.edu.au/study/degrees/health-and-community/rural-and-remote-health',
'https://www.usq.edu.au/handbook/current/humanities-communication/dprs.html',
'https://www.usq.edu.au/handbook/current/law-justice/law-justice-all.html',
'https://www.usq.edu.au/study/degrees/bachelor-of-creative-arts/international',
'https://www.usq.edu.au/handbook/current/health-community/health-community-all.html',
'https://www.usq.edu.au/handbook/current/creative-arts-media/creative-arts-media-all.html',
'https://www.usq.edu.au/handbook/current/sciences/sciences-all.html',
'https://www.usq.edu.au/study/degrees/master-of-professional-psychology',
'https://www.usq.edu.au/handbook/current/information-technology/information-technology-all.html',
'https://www.usq.edu.au/handbook/current/humanities-communication/humanities-communication-all.html',
'https://www.usq.edu.au/handbook/current/engineering-built-environment/engineering-built-environment-all.html',
'https://www.usq.edu.au/handbook/current/information-technology/misp.html',
'https://www.usq.edu.au/handbook/current/information-technology/gdbs.html',
'https://www.usq.edu.au/handbook/current/business-commerce/business-commerce-all.html',
'https://www.usq.edu.au/handbook/current/business-commerce/gdbs.html',
'https://www.usq.edu.au/study/degrees/graduate-diploma-of-health',
'https://www.usq.edu.au/handbook/current/pdfs/gdbs.pdf',
'https://www.usq.edu.au/study/degrees/bachelor-of-science-honours/international',
'https://www.usq.edu.au/study/degrees/bachelor-of-science-honours/biology/international',
'https://www.usq.edu.au/study/degrees/bachelor-of-science-honours/chemistry/international',
'https://www.usq.edu.au/study/degrees/bachelor-of-science-honours/physics/international',
'https://www.usq.edu.au/handbook/current/information-technology/mbsi.html',
'https://www.usq.edu.au/study/degrees/english-language-intensive-courses-for-overseas-students/international',
'https://www.usq.edu.au/handbook/current/business-commerce/mbsi.html',
'https://www.usq.edu.au/study/degrees/bachelor-of-science-honours/environment-sustainability/international',
'https://www.usq.edu.au/study/degrees/bachelor-of-science-honours/applied-mathematics-statistics/international',
'https://www.usq.edu.au/handbook/current/pdfs/mbis.pdf',
'https://www.usq.edu.au/study/degrees/master-of-education-full-fee-paying/online-distributed-learning',
'https://www.usq.edu.au/study/degrees/master-of-education-full-fee-paying/multicultural-education',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-education',
'https://www.usq.edu.au/study/degrees/bachelor-of-arts-honours/history/international',
'https://www.usq.edu.au/study/degrees/master-of-psychology-phd-clinical-psychology/international',
'https://www.usq.edu.au/study/degrees/bachelor-of-science/biology/international',
'https://www.usq.edu.au/study/degrees/bachelor-of-science/physical-sciences/international',
'https://www.usq.edu.au/study/degrees/master-of-psychology-clinical/international',
'https://www.usq.edu.au/study/degrees/bachelor-of-arts/creative-critical-writing/international',
'https://www.usq.edu.au/study/degrees/bachelor-of-science-honours/computing',
'https://www.usq.edu.au/study/degrees/master-of-arts/corporate-communication/international',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-health/scheduled-medicines/international',
'https://www.usq.edu.au/study/degrees/bachelor-of-sport-and-exercise/sport-exercise-science/international',
'https://www.usq.edu.au/study/degrees/graduate-diploma-of-spatial-science-technology/geographical-information-systems/international',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-health/gerontology/international',
'https://www.usq.edu.au/study/degrees/graduate-diploma-of-spatial-science-technology/surveying/international',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-spatial-science-technology/geographic-information-systems/international',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-spatial-science-technology/surveying/international',
'https://www.usq.edu.au/study/degrees/bachelor-of-arts-honours/social-justice-studies/international',
'https://www.usq.edu.au/study/degrees/master-of-laws/comparative-law/international',
'https://www.usq.edu.au/study/degrees/bachelor-of-arts-honours/journalism-studies/international',
'https://www.usq.edu.au/study/degrees/master-of-education-commonwealth-supported/international',
'https://www.usq.edu.au/study/degrees/master-of-business-administration/general/international',
'https://www.usq.edu.au/study/degrees/graduate-diploma-of-education-full-fee-paying/adult-professional-workplace-learning/international',
'https://www.usq.edu.au/study/degrees/graduate-diploma-of-education-commonwealth-supported/guidance-counselling/international',
'https://www.usq.edu.au/study/degrees/graduate-diploma-of-education-full-fee-paying/multicultural-education',
'https://www.usq.edu.au/study/degrees/graduate-diploma-of-education-full-fee-paying/leading-managing-educational-organisations/international',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-science/biology/international',
'https://www.usq.edu.au/study/degrees/graduate-diploma-of-engineering-science/structural-engineering/international',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-engineering-science/structural-engineering/international',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-engineering-science/agricultural-engineering/international',
'https://www.usq.edu.au/study/degrees/master-of-education-full-fee-paying/adult-professional-workplace-learning/international',
'https://www.usq.edu.au/study/degrees/graduate-diploma-of-education-full-fee-paying/career-development/international',
'https://www.usq.edu.au/study/degrees/graduate-diploma-of-engineering-science/power-engineering/international',
'https://www.usq.edu.au/study/degrees/master-of-aviation/aviation-human-factors/international',
'https://www.usq.edu.au/study/degrees/master-of-aviation/aviation-management/international',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-engineering-science/environmental-engineering/international',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-engineering-science/power-engineering/international',
'https://www.usq.edu.au/study/degrees/master-of-education-full-fee-paying/career-development/international',
'https://www.usq.edu.au/study/degrees/bachelor-of-arts-honours/creative-critical-writing/international',
'https://www.usq.edu.au/study/degrees/bachelor-of-arts-honours/contemporary-media-studies/international',
'https://www.usq.edu.au/study/degrees/master-of-business-and-innovation/general/international',
'https://www.usq.edu.au/study/degrees/graduate-diploma-of-engineering-science/electrical-electronic-engineering/international',
'https://www.usq.edu.au/study/degrees/master-of-education-commonwealth-supported/early-childhood/international',
'https://www.usq.edu.au/study/degrees/graduate-diploma-of-engineering-science/mechanical-engineering/international',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-engineering-science/electrical-electronic-engineering/international',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-engineering-science/civil-engineering/international',
'https://www.usq.edu.au/study/degrees/bachelor-of-science/human-physiology/international',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-engineering-science/mechanical-engineering/international',
'https://www.usq.edu.au/study/degrees/bachelor-of-arts-honours/public-relations-studies/international',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-business/general/international',
'https://www.usq.edu.au/study/degrees/master-of-professional-psychology/international',
'https://www.usq.edu.au/handbook/current/engineering-built-environment/dpen.html',
'https://www.usq.edu.au/study/degrees/graduate-diploma-of-health/international',
'https://www.usq.edu.au/study/degrees/master-of-education-full-fee-paying/multicultural-education/international',
'https://www.usq.edu.au/handbook/current/pdfs/dpen.pdf',
'https://www.usq.edu.au/study/degrees/bachelor-of-science-honours/computing/international',
'https://www.usq.edu.au/handbook/current/pdfs/mist.pdf',
'https://www.usq.edu.au/handbook/current/information-technology/mist.html',
'https://www.usq.edu.au/handbook/current/information-technology/misx.html',
'https://www.usq.edu.au/handbook/current/pdfs/misx.pdf',
'https://www.usq.edu.au/study/degrees/graduate-certificate-of-education/international',
'https://www.usq.edu.au/handbook/current/pdfs/mcotormcte.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/mbsi.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/mara.pdf',
'https://www.usq.edu.au/handbook/current/health-community/gdhh.html',
'https://www.usq.edu.au/handbook/current/humanities-communication/mara.html',
'https://www.usq.edu.au/handbook/current/creative-arts-media/mara.html',
'https://www.usq.edu.au/handbook/current/pdfs/gdhh.pdf',
'https://www.usq.edu.au/handbook/current/education/dphd.html',
'https://www.usq.edu.au/handbook/current/sciences/dphd.html',
'https://www.usq.edu.au/handbook/current/information-technology/dphd.html',
'https://www.usq.edu.au/handbook/current/law-justice/dphd.html',
'https://www.usq.edu.au/handbook/current/business-commerce/dphd.html',
'https://www.usq.edu.au/handbook/current/health-community/dphd.html',
'https://www.usq.edu.au/handbook/current/humanities-communication/dphd.html',
'https://www.usq.edu.au/handbook/current/engineering-built-environment/dphd.html',
'https://www.usq.edu.au/handbook/current/creative-arts-media/dphd.html',
'https://www.usq.edu.au/study/degrees/graduate-diploma-of-education-full-fee-paying/multicultural-education/international',
'https://www.usq.edu.au/study/degrees/master-of-education-full-fee-paying/online-distributed-learning/international',
'https://www.usq.edu.au/handbook/current/pdfs/dphd.pdf',
'https://www.usq.edu.au/handbook/current/engineering-built-environment/bsps.html',
'https://www.usq.edu.au/handbook/current/engineering-built-environment/gcae.html',
'https://www.usq.edu.au/handbook/current/eng-lang/ceus.html',
'https://www.usq.edu.au/handbook/current/engineering-built-environment/bsph.html',
'https://www.usq.edu.au/handbook/current/health-community/gcse.html',
'https://www.usq.edu.au/handbook/current/engineering-built-environment/gcen.html',
'https://www.usq.edu.au/handbook/current/engineering-built-environment/mssr.html',
'https://www.usq.edu.au/handbook/current/humanities-communication/mprs.html',
'https://www.usq.edu.au/handbook/current/health-community/mpps.html',
'https://www.usq.edu.au/handbook/current/education/mlda.html',
'https://www.usq.edu.au/handbook/current/humanities-communication/bgen.html',
'https://www.usq.edu.au/handbook/current/engineering-built-environment/mspt.html',
'https://www.usq.edu.au/handbook/current/business-commerce/mprm.html',
'https://www.usq.edu.au/handbook/current/conted/cpa.html',
'https://www.usq.edu.au/handbook/current/pdfs/mprm.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/elas.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/ceus.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/deus.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/gdtl.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/mssr.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/gcen.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/mprs.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/mpps.pdf',
'https://www.usq.edu.au/handbook/current/conted/cpa.html',
'https://www.usq.edu.au/handbook/current/pdfs/mprm.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/elas.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/ceus.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/deus.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/gdtl.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/mssr.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/gcen.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/mprs.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/mpps.pdf',
'https://www.usq.edu.au/handbook/current/information-technology/mcop.html',
'https://www.usq.edu.au/handbook/current/business-commerce/mpjm.html',
'https://www.usq.edu.au/handbook/current/business-commerce/mpmb.html',
'https://www.usq.edu.au/handbook/current/law-justice/llmc.html',
'https://www.usq.edu.au/handbook/current/law-justice/djur.html',
'https://www.usq.edu.au/handbook/current/information-technology/mctn.html',
'https://www.usq.edu.au/handbook/current/information-technology/mipm.html',
'https://www.usq.edu.au/handbook/current/business-commerce/imba.html',
'https://www.usq.edu.au/handbook/current/sciences/bsci.html',
'https://www.usq.edu.au/handbook/current/business-commerce/mipm.html',
'https://www.usq.edu.au/handbook/current/business-commerce/mavn.html',
'https://www.usq.edu.au/handbook/current/creative-arts-media/bart.html',
'https://www.usq.edu.au/handbook/current/business-commerce/mspm.html',
'https://www.usq.edu.au/handbook/current/sciences/btwn.html',
'https://www.usq.edu.au/handbook/current/humanities-communication/mprl.html',
'https://www.usq.edu.au/handbook/current/business-commerce/mppm.html',
'https://www.usq.edu.au/handbook/current/law-justice/llmr.html',
'https://www.usq.edu.au/handbook/current/creative-arts-media/bcra.html',
'https://www.usq.edu.au/handbook/current/health-community/mscr.html',
'https://www.usq.edu.au/handbook/current/information-technology/mbad.html',
'https://www.usq.edu.au/handbook/current/business-commerce/mbpm.html',
'https://www.usq.edu.au/handbook/current/business-commerce/bcin.html',
'https://www.usq.edu.au/handbook/current/information-technology/bcin.html',
'https://www.usq.edu.au/handbook/current/creative-arts-media/dcar.html',
'https://www.usq.edu.au/handbook/current/education/gdtl.html',
'https://www.usq.edu.au/handbook/current/information-technology/mspm.html',
'https://www.usq.edu.au/handbook/current/health-community/mnrs.html',
'https://www.usq.edu.au/handbook/current/engineering-built-environment/gcst.html',
'https://www.usq.edu.au/handbook/current/business-commerce/bbit.html',
'https://www.usq.edu.au/handbook/current/health-community/mnsg.html',
'https://www.usq.edu.au/handbook/current/information-technology/bsci.html',
'https://www.usq.edu.au/handbook/current/business-commerce/bcit.html',
'https://www.usq.edu.au/handbook/current/health-community/bsci.html',
'https://www.usq.edu.au/handbook/current/humanities-communication/bart.html',
'https://www.usq.edu.au/handbook/current/creative-arts-media/bcar.html',
'https://www.usq.edu.au/handbook/current/business-commerce/mbad.html',
'https://www.usq.edu.au/handbook/current/pdfs/mprl.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/bart.pdf',
'https://www.usq.edu.au/handbook/current/information-technology/mcotormcte.html',
'https://www.usq.edu.au/handbook/current/pdfs/bcar.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/llmc.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/dcar.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/mnsg.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/mbad.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/bcra.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/llmr.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/bedh.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/btwn.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/mnrs.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/mcop.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/bssc.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/mavn.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/imba.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/bcin.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/mspm.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/mscr.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/mipm.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/mpmb.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/mctn.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/mpjm.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/mbpm.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/mppm.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/bcit.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/bbit.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/bsci.pdf',
'https://www.usq.edu.au/handbook/current/pdfs/dbar.pdf',
'https://www.usq.edu.au/handbook/current/intprog-all.html',
'https://www.usq.edu.au/handbook/current/externalprog-all.html',
'https://www.usq.edu.au/handbook/current/toowoombaprog-all.html',
'https://www.usq.edu.au/handbook/current/springfieldprog-all.html',
'https://www.usq.edu.au/handbook/current/education/bedh.html',
'https://www.usq.edu.au/handbook/current/pdfs/mpst.pdf',
'https://www.usq.edu.au/handbook/current/humanities-communication/mpst.html',
'https://www.usq.edu.au/handbook/current/education/mpst.html']

    for i in Lists:
        fullurl = base_url % i
        start_urls.append(fullurl)

    # rules = (
    #     # Rule(LinkExtractor(allow=(r'.*'), restrict_xpaths=('')),callback='parse_item', follow=True),
    #     Rule(LinkExtractor(allow=r'https://www.usq.edu.au/extrafiles/templates/gsa/search.htm\?q=postgraduate&proxystylesheet=USQ_Search&site=USQ_Degrees&d=1519884829480&page=\d+'),follow=True),
    #     # Rule(LinkExtractor(allow=(r'.*'),restrict_xpaths=('//*[@id="USQ_Degrees"]/div/h3/a')),callback='parse_item', follow=False),
    #     Rule(LinkExtractor(allow=r'/handbook/current/.*'),callback='parse_item', follow=False),
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
        degree_level = '1'

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
        degree_type = response.xpath('//*[@id="main-wrap"]/section/div/div/div/h1/text()').extract()
        degree_type = ''.join(degree_type)
        degree_type = self.getDegree_type(degree_type)
        # try:
        #     if "Bachelor" in degree_type:
        #         degree_type = "Bachelor"
        #     elif "Master" in degree_type:
        #         degree_type = "Master"
        #     else:
        #         degree_type = "NULL"
        # except:
        #     degree_type = "报错!"
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

        mode = response.xpath('//*[@id="programprogram.time.limits"]/p//text()').extract()
        mode = ''.join(mode)
        # try:
        #     if "Duration" in mode_s:
        #         start = mode_s.find("Duration")
        #         mode = mode_s[start:]
        #         mode = mode[:80]
        #         mode = mode.lstrip("Duration")
        #         item["mode"] = mode
        #     else:
        #         mode = "NULL"
        # except:
        #     mode = "报错!"
        print(8,mode)



        duration = response.xpath('//*[@id="programprogram.time.limits"]/p//text()').extract()
        duration = ''.join(duration)
        # duration = duration.replace('\n','')
        # duration = duration.replace('    ','')
        # try:
        #     if "Duration" in duration_s:
        #         start = duration_s.find("Duration")
        #         # end = duration_s.find("Location:")
        #         duration = duration_s[start:]
        #         duration = duration[:100]
        #         duration = duration.lstrip("Duration")
        #         item["duration"] = duration
        #     else:
        #         duration = "NULL"
        # except:
        #     duration = "报错!"
        print(9,duration)

        modules = response.xpath('//*[@id="programprogram.structure"]//text()').extract()
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
        print(12, career)

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

        entry_requirements = response.xpath('//*[@id="programadmission.reqs"]//text()').extract()
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

    def getDegree_type(self, degree_type):
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
            elif "HND" in degree_type:
                degree_type = 'HND'
            elif "MEd" in degree_type:
                degree_type = 'MEd'
            elif len(degree_type) == 0:
                degree_type = 'NULL'

            else:
                degree_type = 'Ordinary degree'
        except:
            degree_type = "NULL"
        return degree_type



