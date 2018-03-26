# -*- coding: utf-8 -*-






import scrapy
from school_3.items import HooliItem
import datetime
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import re

class PlymouthSpider(scrapy.Spider):
    name = 'westernsydney_pg_2'
    allowed_domains = ['www.westernsydney.edu.au']
    start_urls = []
    base_url = '%s'

    Lists = ['https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-engineering.html',
'https://www.westernsydney.edu.au/thecollege/english_programs/master_of_teaching_direct_entry',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-creative-industries.html',
'https://www.westernsydney.edu.au/starting/orientation/sgsm_mcp_and_orientation',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-finance.html',
'https://www.westernsydney.edu.au/future/study/courses/research/master-of-research.html',
'https://www.westernsydney.edu.au/thecollege/english_programs',
'https://www.westernsydney.edu.au/starting/orientation/orientation_program',
'https://www.westernsydney.edu.au/future/study/courses/research/master-of-philosophy.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-accountancy.html',
'https://www.westernsydney.edu.au/starting/enrolling/how_do_i_enrol',
'https://www.westernsydney.edu.au/thecollege/courses_and_pathways',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-epidemiology.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-teaching-primary.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-teaching-secondary.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-nursing.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-data-science.html',
'https://www.westernsydney.edu.au/starting/enrolling/how_do_i_enrol/how_to_defer_your_offer',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-forensic-science.html',
'https://www.westernsydney.edu.au/thecollege/study_with_us/success_stories/stories/afifa_fahez',
'https://www.westernsydney.edu.au/starting/enrolling/how_do_i_enrol',
'https://www.westernsydney.edu.au/thecollege/courses_and_pathways',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-epidemiology.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-teaching-primary.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-teaching-secondary.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-nursing.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-data-science.html',
'https://www.westernsydney.edu.au/starting/enrolling/how_do_i_enrol/how_to_defer_your_offer',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-forensic-science.html',
'https://www.westernsydney.edu.au/thecollege/study_with_us/success_stories/stories/afifa_fahez',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-social-science.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-education-stem.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-professional-accounting.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-education-leadership.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-business-marketing.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-clinical-psychology.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-financial-planning.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-information-governance.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-business-administration.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-digital-humanities.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-in-education-social-ecology.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-management.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-health-science-health-services-management.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-planning.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-education-leadership-and-management.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-business-administration-master-of-applied-finance.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-arts-tesol.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-applied-finance.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-teaching-birth-5-years-birth-12-years.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-art-therapy.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-public-health.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-medicine-pathology.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-cardiac-sonography.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-business-analytics.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-chinese-medicine.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-planning-pathway-to-master-of-urban-management-and-planning.html',
'https://www.westernsydney.edu.au/future/study/how-to-apply/higher-degree-research-candidates/master-of-research.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-inclusive-education.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/masters-qualifying-program.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-advanced-networking.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-translation-and-tesol.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-project-management.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-building-surveying.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-primary-health-care.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-sciencepublichealthnutrition.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-professional-psychology.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-science-food-science.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-teaching-secondary-stem.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-creative-music-therapy.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-bushfire-protection.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-fire-safety-engineering.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-human-resource-management.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-commerce-property-investment-and-development.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-nursing-professional-studies.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-international-criminology.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-laws-international-governance.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-medicine-allergic-diseases.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-psychotherapy-and-counselling.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-social-work-qualifying.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-urban-management-and-planning.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-business-operations-management.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-arts-in-continental-philosophy.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-stockbroking-and-financial-advising.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-information-and-communications-technology.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/executive-master-of-business-administration.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-nurse-practitioner-mental-health.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-health-science-aged-care-management.html',
'https://www.westernsydney.edu.au/future/study/courses/research/doctor-of-philosophy-master-of-clinical-psychology.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-humanitarian-and-development-studies.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-social-science--policing-leadership-.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-interpreting-and-translation.html',
'https://www.westernsydney.edu.au/future/study/courses/engineering-courses.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-social-science-development-security-and-sustainability.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-social-science-digital-research-and-social-data-analytics.html',
'https://www.westernsydney.edu.au/future/our-campuses/parramatta-south-campus.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate.html',
'https://www.westernsydney.edu.au/future/study/courses/arts-courses.html',
'https://www.westernsydney.edu.au/future/study/courses/business-courses.html',
'https://www.westernsydney.edu.au/future/study/courses/social-science-courses.html',
'https://www.westernsydney.edu.au/future/study/courses/research.html',
'https://www.westernsydney.edu.au/future/study/courses/teaching-and-education-courses.html',
'https://www.westernsydney.edu.au/future/study/courses/science-courses.html',
'https://www.westernsydney.edu.au/future/study/courses/psychology-courses.html',
'https://www.westernsydney.edu.au/future/study/courses/medicine-courses.html',
'https://www.westernsydney.edu.au/future/study/courses/creative-industries-courses.html',
'https://www.westernsydney.edu.au/future/study/courses/information-technology-courses.html',
'https://www.westernsydney.edu.au/future/study/courses/the-academy.html',
'https://www.westernsydney.edu.au/future/study/courses/nursing-and-midwifery-courses.html',
'https://www.westernsydney.edu.au/future/study/courses/law-courses.html',
'https://www.westernsydney.edu.au/future/study/courses/lead-innovate-market.html',
'https://www.westernsydney.edu.au/future/study/courses/sydney-graduate-school-of-management.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-certificate-in-financial-planning.html',
'https://www.westernsydney.edu.au/future/study/courses/health-and-sport-sciences-courses.html',
'https://www.westernsydney.edu.au/future/study/courses/advance-human-health.html',
'https://www.westernsydney.edu.au/future/study/courses/create-image-make.html',
'https://www.westernsydney.edu.au/future/study/courses/solve-construct-build.html',
'https://www.westernsydney.edu.au/future/study/courses/build-a-better-society.html',
'https://www.westernsydney.edu.au/future/study/courses/investigate-the-mind.html',
'https://www.westernsydney.edu.au/future/study/courses/discover-the-world.html',
'https://www.westernsydney.edu.au/future/study/courses/open-minds-change-lives.html',
'https://www.westernsydney.edu.au/future/study/courses/tourism-and-urban-planning-courses.html',
'https://www.westernsydney.edu.au/future/study/courses/explore-the-digital-future.html',
'https://www.westernsydney.edu.au/future/study/courses/construction-management-courses.html',
'https://www.westernsydney.edu.au/future/study/how-to-apply/atar-search-for-undergraduates.html',
'https://www.westernsydney.edu.au/future/study/courses/criminology-and-policing-courses.html',
'https://www.westernsydney.edu.au/future/study/courses/research/doctor-of-education.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-policing.html',
'https://www.westernsydney.edu.au/future/study/courses/research/doctor-of-philosophy.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-business.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html',
'https://www.westernsydney.edu.au/future/study/courses/defend-justice-protect-peace.html',
'https://www.westernsydney.edu.au/future/study/how-uni-works/inherent-requirements.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-nursing.html',
'https://www.westernsydney.edu.au/future/why-western/global-rankings.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-criminology.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-accounting.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-socialscience.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-business.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-creative-industries.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-zoology.html',
'https://www.westernsydney.edu.au/future/study/how-to-apply/bonus-points/subject-bonus-points.html',
'https://www.westernsydney.edu.au/future/study/how-to-apply/higher-degree-research-candidates.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-data-science.html',
'https://www.westernsydney.edu.au/future/study/courses/research/doctor-of-cultural-research.html',
'https://www.westernsydney.edu.au/future/study/how-to-apply/mbbs-applicants/general-applicants.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-medical-science.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-midwifery.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-certificate-in-accounting.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-honours.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-health-science.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-arts-pathway-to-teaching-birth.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-communication.html',
'https://www.westernsydney.edu.au/future/study/courses/research/doctor-of-creative-arts-dca.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-social-work.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-business-extended.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-arts-pathway-to-teaching-primary.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-health-science-extended.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-sport-development.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-arts-extended-arts.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-certificate-in-business.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-arts-extended.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-arts-standard.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-laws-graduate-entry.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-nursing-graduate-entry.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-design-standard.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-engineering-standard.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-design-extended.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-arts-pathway-to-teaching-secondary.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-industrial-design.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-secondary.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-arts-bachelor-of-arts.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-forensic-science.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-honours-civil.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-chemistry.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-certificate-in-applied-finance.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-health-science-paramedicine.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-laws-non-graduate-entry.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-science-standard.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-diploma-in-counselling.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-social-science-psychology.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-industrial-design-honours.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-physiotherapy.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-arts-extended-pathway-to-teaching-birth.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-business-fast-track.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-certificate-in-nursing.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-arts-extended-pathway-to-teaching-primary.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-diploma-in-australian-migration-law.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-design-and-technology.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-communication-extended-communication.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-nursing-advanced.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-business-pathway-to-teaching-secondary.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-diploma-in-firesafetyengineering.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-health-science-standard.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-arts-extended-pathway-to-teaching-secondary.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-cyber-security-and-behaviour.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-medicine-bachelor-of-surgery.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-design-visual-communication.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-diploma-in-forensic-science.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-certificate-in-epidemiology.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-diploma-in-advanced-networking.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-ict.html',
'https://www.westernsydney.edu.au/future/study/how-to-apply/higher-degree-research-candidates/find-a-supervisor.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-building-design-management-extended.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-deans-scholars.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-biological-sciences.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-certificate-in-engineering.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-pathway-to-teaching-primary-secondary.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-construction-management-standard.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-diploma-in-bushfire-protection.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-honours-construction.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-graphic-design-pathway-to-teaching-secondary.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-occupational-therapy.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-honours-electrical.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-science-bachelor-of-medical-science.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-honours-mechanical.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-design-extended-visual-communication.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-health-science-bachelor-of-health-science.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-construction-management.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-diploma-in-mental-health-nursing.html',
'https://www.westernsydney.edu.au/future/study/how-to-apply/bonus-points/school-recommendation-scheme.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-criminal-and-community-justice.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-certificate-in-education-social-ecology.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-diploma-in-building-surveying.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-ict-bachelor-of-information-systems.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-certificate-in-social-science.html',
'https://www.westernsydney.edu.au/thecollege/english_programs/english_language_entrance_test',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-diploma-in-primary-health-care.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-certificate-in-tesol.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-certificate-in-primary-science-education.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-criminal-and-community-justice-extended.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-secondary-deans-scholars.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-communication-extended-creative-industries.html',
'https://www.westernsydney.edu.au/starting/orientation/orientation_program/information_for_new_international_students',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-advanced.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-certificate-in-creative-industries.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-certificate-in-mental-health-nursing.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-certificate-in-stockbroking-and-financial-advising.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-diploma-in-international-criminology.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-diploma-in-mental-health-nursing.html',
'https://www.westernsydney.edu.au/future/study/how-to-apply/bonus-points/school-recommendation-scheme.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-criminal-and-community-justice.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-certificate-in-education-social-ecology.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-diploma-in-building-surveying.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-ict-bachelor-of-information-systems.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-certificate-in-social-science.html',
'https://www.westernsydney.edu.au/thecollege/english_programs/english_language_entrance_test',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-diploma-in-primary-health-care.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-certificate-in-tesol.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-certificate-in-primary-mathematics-education.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-health-science-health-and-physical-education-extended.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-health-science-bachelor-of-health-science-hpe.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-certificate-in-primary-health-care.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-design-bachelor-of-design-visual-communication.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-certificate-in-business-administration.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-health-science-hpe-pathway-to-teaching-secondary.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary-deans-scholars.html',
'https://www.westernsydney.edu.au/future/study/how-to-apply/mbbs-applicants/international-applicants.html',
'https://www.westernsydney.edu.au/thecollege/courses_and_pathways/associate_degree_in_engineering',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-diploma-in-humanitarian-and-development-studies.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-certificate-in-humanitarian-and-development-studies.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-diploma-in-public-health.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-certificate-in-international-criminology.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-information-and-communications-technology-bachelor-of-ict.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-design-extended-graphic-design-pathway-to-teaching-secondary.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-diploma-in-health-science.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-certificate-in-fire-safety-engineering.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-information-and-communications-technology-extended-information-systems.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-information-and-communications-technology-extended-ict.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-construction-management-bachelor-of-construction-technology.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-health-science-health-and-physical-education.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-design-bachelor-of-graphic-design-pathway-to-teaching-secondary.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-communication-extended-screen-media-arts-production.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-certificate-in-public-health.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-certificate-in-health-science.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-diploma-in-cardiac-sonography.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-certificate-in-language-teaching-and-bilingualism-birth-12-years.html',
'https://www.westernsydney.edu.au/thecollege/courses_and_pathways/arts/international_diploma_in_arts',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-honours-robotics-and-mechatronics.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-social-science-extended-humanitarian-and-development-studies.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-information-and-communications-technology-standard.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-information-and-communications-technology-extended.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-building-design-management-standard-international.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-diploma-in-continental-philospohy.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-health-science-sport-and-exercise-science.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-occupational-therapy-honours.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-information-and-communications-technology-health-information-management-extended.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-building-design-management-bachelor-of-building-design-management.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-ict-health-information-management-bachelor-of-ict-him.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-communication-bachelor-of-screen-media-arts-and-production.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-information-and-communications-technology-fast-track.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-certificate-in-urban-management-and-planning.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-diploma-in-child-and-family-health-karitane.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-health-information-management.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-zoology-bachelor-of-natural-science-animalscience.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-health-science-health-and-physical-education-standard.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-criminal-and-community-justice-bachelor-of-criminal-and-community-justice.html',
'https://www.westernsydney.edu.au/future/study/courses/the-college/diploma-in-social-science-bachelor-of-humanitarian-and-development-studies.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-medical-science-forensic-mortuary-practice.html',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-construction-management-studies-bachelor-of-laws.html',
'https://www.westernsydney.edu.au/thecollege/courses_and_pathways/arts/international_university_foundation_studies',
'https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-bachelor-of-arts.html',
'https://www.westernsydney.edu.au/future/study/how-to-apply/higher-degree-research-candidates/how-to-apply-for-the-doctor-of-philosophy-and-professional-dr.html',
'https://www.westernsydney.edu.au/future/study/courses/postgraduate/graduate-certificate-in-acute-and-critical-care-nursing.html',
'https://www.westernsydney.edu.au/thecollege/media/documents/pdfs/CLGE1957_The_College_AOS_2018_Web.pdf'
]

    for i in Lists:
        fullurl = base_url % i
        start_urls.append(fullurl)

    # rules = (
    #     # Rule(LinkExtractor(allow=(r'.*'), restrict_xpaths=('')),callback='parse_item', follow=True),
    #     Rule(LinkExtractor(allow=r'https://www.westernsydney.edu.au/search.html\?collection=wsu-futurestudent&query=bachelor'),follow=True),
    #     Rule(LinkExtractor(allow=(r'.*'),restrict_xpaths=('//*[@id="wrapper"]//div[@class="search-results__item"]/a')),callback='parse_item', follow=False),
    #     # Rule(LinkExtractor(allow=(r'.*'), restrict_xpaths=('//*[@id="wrapper"]//div[@class="component component--wysiwyg"]/p/font/a')),callback='parse_item', follow=False),
    # )

    def parse(self,response):
        print('==================================',response.url)
        item = HooliItem()

        url = response.url
        print(1,url)

        university = 'Western Sydney University'
        print(2,university)

        department = 'NULL'
        # department_s = ''.join(department_s)
        # try:
        #     if "Faculty:" in department_s:
        #         start = department_s.find("Faculty:")
        #         department = department_s[start:]
        #         department = department[:48]
        #         item["department"] = department
        #     else:
        #         department = "NULL"
        #
        # except:
        #     department = "报错!"

        print(3,department)

        country = 'Australia'
        city = "Sydney"
        website = 'https://www.westernsydney.edu.au'
        degree_level = '1'

        # programme = response.xpath('//div[@class="section picture-nav"]/h1/text()').extract()
        programme = response.xpath('//*[@id="wrapper"]//div/h1/text()').extract()
        programme = ''.join(programme)
        print(4,programme)

        ucas_code_s = response.xpath('//*[@id="KAKtSSPv"]//div[@class="tile-carousel__description"]/dl//text()').extract()
        ucas_code_s = ''.join(ucas_code_s)
        try:
            if "UAC CODE" in ucas_code_s:
                start = ucas_code_s.find("UAC CODE")
                ucas_code = ucas_code_s[start:]
                ucas_code = ucas_code[:10]
                ucas_code = ucas_code.lstrip("UAC CODE")
                item["ucas_code"] = ucas_code
            else:
                ucas_code = "NULL"
        except:
            ucas_code = "报错!"
        print(5,ucas_code)

        # degree_type = response.xpath('//div[@class="section picture-nav"]/h1/text()').extract()
        degree_type = response.xpath('//*[@id="wrapper"]//div/h1/text()').extract()
        degree_type = ''.join(degree_type)
        # degree_type = self.getDegree_type(degree_type)
        try:
            if "Bachelor" in degree_type:
                degree_type = "Bachelor"
            elif "Master" in degree_type:
                degree_type = "Master"
            else:
                degree_type = "NULL"
        except:
            degree_type = "报错!"
        print(6,degree_type)

        start_date_s = response.xpath('//*[@id="wrapper"]//div[@class="cols-2__body"]//text()').extract()
        start_date_s = ''.join(start_date_s)
        try:
            if "Autumn" in start_date_s:
                start = start_date_s.find("Autumn")
                start_date = start_date_s[start:]
                item["start_date"] = start_date
            else:
                start_date = "NULL"
        except:
            start_date = "报错!"
        print(7,start_date)

        # overview = response.xpath('//div[@class="left logo-bg"]//text()').extract()
        overview = response.xpath('//*[@id="wrapper"]//div[@class="col-sm-6"]/div[@class="component component--wysiwyg"]/p/text()').extract()
        overview = ''.join(overview)
        print(8, overview)

        mode = response.xpath('//*[@id="wrapper"]//div[@class="cols-2__body"]//text()').extract()
        mode = ''.join(mode)
        try:
            if "FULL TIME" in mode:
                mode = "FULL TIME"
            elif "PART TIME" in mode:
                mode = "PART TIME"
            else:
                mode = "NULL"
        except:
            mode = "报错!"
        # mode = mode.replace('\n','')
        # mode = mode.replace('      ','')
        print(7,mode)



        duration_s = response.xpath('//*[@id="wrapper"]//div[@class="cols-2__body"]//text()').extract()
        duration_s = ''.join(duration_s)
        # duration = duration.replace('\n','')
        # duration = duration.replace('    ','')
        try:
            if "FULL TIME" in duration_s:
                start = duration_s.find("FULL TIME")
                end = duration_s.find("Autumn")
                duration = duration_s[start:end]
                item["duration"] = duration
            else:
                duration = "NULL"
        except:
            duration = "报错!"
        print(8,duration)

        modules = "NULL"
        modules = ''.join(modules)
        # modules = modules.replace('\n','')
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
        print(8,modules)

        teaching = 'NULL'

        assessment = "NULL"
        # assessment_s = ''.join(assessment_s)
        # try:
        #     if "Assessment" in assessment_s:
        #         start = assessment_s.find("Assessment")
        #         assessment = assessment_s[start:]
        #         item["assessment"] = assessment
        #     else:
        #         assessment = assessment_s
        # except:
        #     assessment = assessment_s
        # print(7, assessment)

        career = response.xpath('//div[@class="tile-carousel-side"]//text()').extract()
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
        print(8.5, career)

        application_date = "NULL"

        deadline = 'NULL'
        # deadline = ''.join(deadline)
        # print(9,deadline)

        application_fee = 'NULL'

        tuition_fee= 'NULL'
        # tuition_fee = ''.join(tuition_fee)
        # # tuition_fee = tuition_fee.replace('\n','')
        # # tuition_fee = tuition_fee.replace('    ','')
        # tuition_fee = self.getTuition_fee(tuition_fee)
        # # try:
        # #     if tuition_fee_s > 0:
        # #         tuition_fee = tuition_fee_s
        # #     else:
        # #         tuition_fee = "NULL"
        # # except:
        # #     tuition_fee = "报错!"
        #
        # print(9, tuition_fee)
        #
        location = 'Sydney'
        # location_s = ''.join(location_s)
        # try:
        #     if "Location:" in location_s:
        #         start = location_s.find("Location:")
        #         location = location_s[start:]
        #         location = location[:30]
        #         item["location"] = location
        #     else:
        #         location = "NULL"
        # except:
        #     location = "报错!"
        # print(10,location)

        ATAS = 'NULL'

        GPA = 'NULL'

        average_score = 'NULL'

        accredited_university = 'NULL'

        Alevel = 'NULL'

        IB = 'NULL'

        IELTS = 'NULL'
        # IELTS_s = ''.join(IELTS_s)
        # # IELTS = re.findall('(IELTS:|IELTS)? (.*){0,5} \d?.\d? .{0,70}',IELTS)
        # try:
        #     if "English Language Requirements:" in IELTS_s:
        #         start = IELTS_s.find("English Language Requirements:")
        #         IELTS = IELTS_s[start:]
        #         IELTS = IELTS[:150]
        #         item["IELTS"] = IELTS
        #     else:
        #         IELTS = "NULL"
        # except:
        #     IELTS = "报错!"
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
        LSAT = "NULL"
        MCAT = 'NULL'

        working_experience = 'NULL'

        interview = 'NULL'

        portfolio = 'NULL'

        application_documents = 'NULL'

        how_to_apply = 'NULL'
        # how_to_apply_s = ''.join(how_to_apply_s)
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
        # print(11,how_to_apply)

        entry_requirements = "NULL"
        # entry_requirements = ''.join(entry_requirements)
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
        # print(12,entry_requirements)

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

        # yield item

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

