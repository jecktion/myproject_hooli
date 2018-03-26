from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import scrapy
import re
import datetime
from school_3.clearSpace import clear_space, clear_space_str
from school_3.getItem import get_item
from school_3.getTuition_fee import getTuition_fee
from school_3.items import HooliItem

class PlymouthSpider(scrapy.Spider):
    name = "Deakin_pg"
    allowed_domains = ['www.deakin.edu.au']
    start_urls = []

    base_url = '%s'

    Lists = ['http://www.deakin.edu.au/course/doctor-medicine',
'http://www.deakin.edu.au/course/doctor-medicine-international',
'http://www.deakin.edu.au/course/doctor-philosophy-architecture-built-environment',
'http://www.deakin.edu.au/course/doctor-philosophy-architecture-built-environment-international',
'http://www.deakin.edu.au/course/doctor-philosophy-arts-international',
'http://www.deakin.edu.au/course/doctor-philosophy-arts',
'http://www.deakin.edu.au/course/doctor-philosophy-biology-chemistry',
'http://www.deakin.edu.au/course/doctor-philosophy-biology-chemistry-international',
'http://www.deakin.edu.au/course/doctor-philosophy-business-law',
'http://www.deakin.edu.au/course/doctor-philosophy-business-law-international',
'http://www.deakin.edu.au/course/doctor-philosophy-copenhagen',
'http://www.deakin.edu.au/course/doctor-philosophy-copenhagen-international',
'http://www.deakin.edu.au/course/doctor-philosophy-education',
'http://www.deakin.edu.au/course/doctor-philosophy-education-international',
'http://www.deakin.edu.au/course/doctor-philosophy-engineering',
'http://www.deakin.edu.au/course/doctor-philosophy-engineering-international',
'http://www.deakin.edu.au/course/doctor-philosophy-environmental-science-international',
'http://www.deakin.edu.au/course/doctor-philosophy-environmental-science',
'http://www.deakin.edu.au/course/doctor-philosophy-exercise-science-sport-international',
'http://www.deakin.edu.au/course/doctor-philosophy-exercise-science-sport',
'http://www.deakin.edu.au/course/doctor-philosophy-health-disease-international',
'http://www.deakin.edu.au/course/doctor-philosophy-health-disease',
'http://www.deakin.edu.au/course/doctor-philosophy-health-promotion-public-health-international',
'http://www.deakin.edu.au/course/doctor-philosophy-health-promotion-public-health',
'http://www.deakin.edu.au/course/doctor-philosophy-health-promotion-international',
'http://www.deakin.edu.au/course/doctor-philosophy-health-promotion',
'http://www.deakin.edu.au/course/doctor-philosophy-health-international',
'http://www.deakin.edu.au/course/doctor-philosophy-health',
'http://www.deakin.edu.au/course/doctor-philosophy-information-technology',
'http://www.deakin.edu.au/course/doctor-philosophy-information-technology-international',
'http://www.deakin.edu.au/course/doctor-philosophy-nursing-international',
'http://www.deakin.edu.au/course/doctor-philosophy-nursing',
'http://www.deakin.edu.au/course/doctor-philosophy-psychology-international',
'http://www.deakin.edu.au/course/doctor-philosophy-psychology',
'http://www.deakin.edu.au/course/doctor-psychology-clinical-international',
'http://www.deakin.edu.au/course/doctor-psychology-clinical',
'http://www.deakin.edu.au/course/graduate-certificate-accounting-and-law',
'http://www.deakin.edu.au/course/graduate-certificate-accounting-and-law-international',
'http://www.deakin.edu.au/course/graduate-certificate-agricultural-health-and-medicine',
'http://www.deakin.edu.au/course/graduate-certificate-agricultural-health-and-medicine-international',
'http://www.deakin.edu.au/course/graduate-certificate-applied-learning-and-teaching',
'http://www.deakin.edu.au/course/graduate-certificate-business-arts-and-cultural-management',
'http://www.deakin.edu.au/course/graduate-certificate-business-arts-and-cultural-management-international',
'http://www.deakin.edu.au/course/graduate-certificate-business-sport-management',
'http://www.deakin.edu.au/course/graduate-certificate-business-sport-management-international',
'http://www.deakin.edu.au/course/graduate-certificate-business-administration',
'http://www.deakin.edu.au/course/graduate-certificate-business-administration-international',
'http://www.deakin.edu.au/course/graduate-certificate-commerce',
'http://www.deakin.edu.au/course/graduate-certificate-commerce-international',
'http://www.deakin.edu.au/course/graduate-certificate-communication',
'http://www.deakin.edu.au/course/graduate-certificate-communication-international',
'http://www.deakin.edu.au/course/graduate-certificate-corporate-management',
'http://www.deakin.edu.au/course/graduate-certificate-corporate-management-international',
'http://www.deakin.edu.au/course/graduate-certificate-creative-arts',
'http://www.deakin.edu.au/course/graduate-certificate-creative-arts-international',
'http://www.deakin.edu.au/course/graduate-certificate-cyber-security',
'http://www.deakin.edu.au/course/graduate-certificate-cyber-security-international',
'http://www.deakin.edu.au/course/graduate-certificate-development-humanitarian-action',
'http://www.deakin.edu.au/course/graduate-certificate-development-humanitarian-action-international',
'http://www.deakin.edu.au/course/graduate-certificate-diabetes-education-international',
'http://www.deakin.edu.au/course/graduate-certificate-diabetes-education',
'http://www.deakin.edu.au/course/graduate-certificate-disability-and-inclusion',
'http://www.deakin.edu.au/course/graduate-certificate-education',
'http://www.deakin.edu.au/course/graduate-certificate-education-international',
'http://www.deakin.edu.au/course/graduate-certificate-education-business-leadership',
'http://www.deakin.edu.au/course/graduate-certificate-education-business-leadership-international',
'http://www.deakin.edu.au/course/graduate-certificate-education-research',
'http://www.deakin.edu.au/course/graduate-certificate-education-research-international',
'http://www.deakin.edu.au/course/graduate-certificate-financial-planning',
'http://www.deakin.edu.au/course/graduate-certificate-financial-planning-international',
'http://www.deakin.edu.au/course/graduate-certificate-health-promotion',
'http://www.deakin.edu.au/course/graduate-certificate-health-research-practice',
'http://www.deakin.edu.au/course/graduate-certificate-health-research-practice-international',
'http://www.deakin.edu.au/course/graduate-certificate-higher-education-learning-and-teaching',
'http://www.deakin.edu.au/course/graduate-certificate-human-nutrition',
'http://www.deakin.edu.au/course/graduate-certificate-human-nutrition-international',
'http://www.deakin.edu.au/course/graduate-certificate-human-resource-management-international',
'http://www.deakin.edu.au/course/graduate-certificate-human-resource-management',
'http://www.deakin.edu.au/course/graduate-certificate-humanitarian-health',
'http://www.deakin.edu.au/course/graduate-certificate-humanitarian-health-international',
'http://www.deakin.edu.au/course/graduate-certificate-information-systems',
'http://www.deakin.edu.au/course/graduate-certificate-information-systems-international',
'http://www.deakin.edu.au/course/graduate-certificate-information-technology',
'http://www.deakin.edu.au/course/graduate-certificate-information-technology-international',
'http://www.deakin.edu.au/course/graduate-certificate-information-technology-leadership',
'http://www.deakin.edu.au/course/graduate-certificate-information-technology-leadership-international',
'http://www.deakin.edu.au/course/graduate-certificate-international-and-community-development',
'http://www.deakin.edu.au/course/graduate-certificate-international-and-community-development-international',
'http://www.deakin.edu.au/course/graduate-certificate-international-finance',
'http://www.deakin.edu.au/course/graduate-certificate-international-finance-international',
'http://www.deakin.edu.au/course/graduate-certificate-international-relations',
'http://www.deakin.edu.au/course/graduate-certificate-international-relations-international',
'http://www.deakin.edu.au/course/graduate-certificate-languages-teaching',
'http://www.deakin.edu.au/course/graduate-certificate-marketing',
'http://www.deakin.edu.au/course/graduate-certificate-marketing-international',
'http://www.deakin.edu.au/course/graduate-certificate-museum-studies',
'http://www.deakin.edu.au/course/graduate-certificate-museum-studies-international',
'http://www.deakin.edu.au/course/graduate-certificate-professional-accounting',
'http://www.deakin.edu.au/course/graduate-certificate-professional-accounting-international',
'http://www.deakin.edu.au/course/graduate-certificate-professional-practice-digital-learning-international',
'http://www.deakin.edu.au/course/graduate-certificate-professional-practice-digital-learning',
'http://www.deakin.edu.au/course/graduate-certificate-professional-practice-financial-planning-international',
'http://www.deakin.edu.au/course/graduate-certificate-professional-practice-financial-planning',
'http://www.deakin.edu.au/course/graduate-certificate-of-professional-practice-leadership',
'http://www.deakin.edu.au/course/graduate-certificate-of-professional-practice-leadership-international',
'http://www.deakin.edu.au/course/graduate-certificate-property',
'http://www.deakin.edu.au/course/graduate-certificate-property-international',
'http://www.deakin.edu.au/course/graduate-certificate-public-health-nutrition',
'http://www.deakin.edu.au/course/graduate-certificate-public-health-nutrition-international',
'http://www.deakin.edu.au/course/graduate-certificate-research-management',
'http://www.deakin.edu.au/course/graduate-certificate-research-management-international',
'http://www.deakin.edu.au/course/graduate-certificate-specialist-inclusive-education',
'http://www.deakin.edu.au/course/graduate-certificate-stem-education',
'http://www.deakin.edu.au/course/graduate-certificate-sustainable-regional-development',
'http://www.deakin.edu.au/course/graduate-certificate-sustainable-regional-development-international',
'http://www.deakin.edu.au/course/graduate-certificate-teaching-english-to-speakers-other-languages-international',
'http://www.deakin.edu.au/course/graduate-certificate-teaching-english-to-speakers-other-languages',
'http://www.deakin.edu.au/course/graduate-certificate-teaching-english-to-speakers-other-languages-education',
'http://www.deakin.edu.au/course/graduate-certificate-therapeutic-child-play',
'http://www.deakin.edu.au/course/graduate-certificate-writing-and-literature',
'http://www.deakin.edu.au/course/graduate-certificate-writing-and-literature-international',
'http://www.deakin.edu.au/course/graduate-diploma-accounting-and-law',
'http://www.deakin.edu.au/course/graduate-diploma-accounting-and-law-international',
'http://www.deakin.edu.au/course/graduate-diploma-business-arts-and-cultural-management',
'http://www.deakin.edu.au/course/graduate-diploma-business-arts-and-cultural-management-international',
'http://www.deakin.edu.au/course/graduate-diploma-business-administration',
'http://www.deakin.edu.au/course/graduate-diploma-business-administration-international',
'http://www.deakin.edu.au/course/graduate-diploma-business-analytics',
'http://www.deakin.edu.au/course/graduate-diploma-business-analytics-international',
'http://www.deakin.edu.au/course/graduate-diploma-childrens-literature',
'http://www.deakin.edu.au/course/graduate-diploma-childrens-literature-international',
'http://www.deakin.edu.au/course/graduate-diploma-commerce',
'http://www.deakin.edu.au/course/graduate-diploma-commerce-international',
'http://www.deakin.edu.au/course/graduate-diploma-communication-international',
'http://www.deakin.edu.au/course/graduate-diploma-communication',
'http://www.deakin.edu.au/course/graduate-diploma-creative-arts',
'http://www.deakin.edu.au/course/graduate-diploma-creative-arts-international',
'http://www.deakin.edu.au/course/graduate-diploma-creative-writing-international',
'http://www.deakin.edu.au/course/graduate-diploma-creative-writing',
'http://www.deakin.edu.au/course/graduate-diploma-cyber-security',
'http://www.deakin.edu.au/course/graduate-diploma-cyber-security-international',
'http://www.deakin.edu.au/course/graduate-diploma-data-analytics-international',
'http://www.deakin.edu.au/course/graduate-diploma-data-analytics',
'http://www.deakin.edu.au/course/graduate-diploma-development-and-humanitarian-action',
'http://www.deakin.edu.au/course/graduate-diploma-development-and-humanitarian-action-international',
'http://www.deakin.edu.au/course/graduate-diploma-digital-media-international',
'http://www.deakin.edu.au/course/graduate-diploma-digital-media',
'http://www.deakin.edu.au/course/graduate-diploma-financial-planning',
'http://www.deakin.edu.au/course/graduate-diploma-financial-planning-international',
'http://www.deakin.edu.au/course/graduate-diploma-health-promotion',
'http://www.deakin.edu.au/course/graduate-diploma-health-promotion-international',
'http://www.deakin.edu.au/course/graduate-diploma-human-nutrition',
'http://www.deakin.edu.au/course/graduate-diploma-human-nutrition-international',
'http://www.deakin.edu.au/course/graduate-diploma-indigenous-research',
'http://www.deakin.edu.au/course/graduate-diploma-information-systems',
'http://www.deakin.edu.au/course/graduate-diploma-information-systems-international',
'http://www.deakin.edu.au/course/graduate-diploma-information-technology',
'http://www.deakin.edu.au/course/graduate-diploma-information-technology-international',
'http://www.deakin.edu.au/course/graduate-diploma-international-and-community-development',
'http://www.deakin.edu.au/course/graduate-diploma-international-and-community-development-international',
'http://www.deakin.edu.au/course/graduate-diploma-international-finance',
'http://www.deakin.edu.au/course/graduate-diploma-international-finance-international',
'http://www.deakin.edu.au/course/graduate-diploma-international-relations',
'http://www.deakin.edu.au/course/graduate-diploma-international-relations-international',
'http://www.deakin.edu.au/course/graduate-diploma-journalism',
'http://www.deakin.edu.au/course/graduate-diploma-journalism-international',
'http://www.deakin.edu.au/course/graduate-diploma-land-and-sea-country-management',
'http://www.deakin.edu.au/course/graduate-diploma-literary-studies',
'http://www.deakin.edu.au/course/graduate-diploma-literary-studies-international',
'http://www.deakin.edu.au/course/graduate-diploma-marketing',
'http://www.deakin.edu.au/course/graduate-diploma-marketing-international',
'http://www.deakin.edu.au/course/graduate-diploma-midwifery',
'http://www.deakin.edu.au/course/graduate-diploma-museum-studies',
'http://www.deakin.edu.au/course/graduate-diploma-museum-studies-international',
'http://www.deakin.edu.au/course/graduate-diploma-professional-accounting-international',
'http://www.deakin.edu.au/course/graduate-diploma-professional-accounting',
'http://www.deakin.edu.au/course/graduate-diploma-professional-political-practice',
'http://www.deakin.edu.au/course/graduate-diploma-professional-practice-financial-planning',
'http://www.deakin.edu.au/course/graduate-diploma-professional-practice-financial-planning-international',
'http://www.deakin.edu.au/course/graduate-diploma-professional-writing',
'http://www.deakin.edu.au/course/graduate-diploma-professional-writing-international',
'http://www.deakin.edu.au/course/graduate-diploma-property',
'http://www.deakin.edu.au/course/graduate-diploma-property-international',
'http://www.deakin.edu.au/course/graduate-diploma-psychology',
'http://www.deakin.edu.au/course/graduate-diploma-psychology-international',
'http://www.deakin.edu.au/course/graduate-diploma-psychology-pre-practice',
'http://www.deakin.edu.au/course/graduate-diploma-public-relations',
'http://www.deakin.edu.au/course/graduate-diploma-public-relations-international',
'http://www.deakin.edu.au/course/graduate-diploma-sustainable-regional-development',
'http://www.deakin.edu.au/course/graduate-diploma-sustainable-regional-development-international',
'http://www.deakin.edu.au/course/graduate-diploma-television-production',
'http://www.deakin.edu.au/course/graduate-diploma-therapeutic-child-play',
'http://www.deakin.edu.au/course/graduate-diploma-virtual-and-augmented-reality-international',
'http://www.deakin.edu.au/course/graduate-diploma-virtual-and-augmented-reality',
'http://www.deakin.edu.au/course/graduate-diploma-visual-communication-design',
'http://www.deakin.edu.au/course/graduate-diploma-visual-communication-design-international',
'http://www.deakin.edu.au/course/graduate-diploma-writing-and-literature',
'http://www.deakin.edu.au/course/graduate-diploma-writing-and-literature-international',
'http://www.deakin.edu.au/course/juris-doctor',
'http://www.deakin.edu.au/course/master-accounting-and-law',
'http://www.deakin.edu.au/course/master-accounting-and-law-international',
'http://www.deakin.edu.au/course/master-applied-learning-and-teaching',
'http://www.deakin.edu.au/course/master-applied-science-health-disease-international',
'http://www.deakin.edu.au/course/master-applied-science-health-disease',
'http://www.deakin.edu.au/course/master-applied-science-health-international',
'http://www.deakin.edu.au/course/master-applied-science-health',
'http://www.deakin.edu.au/course/master-applied-sport-science',
'http://www.deakin.edu.au/course/master-architecture',
'http://www.deakin.edu.au/course/master-architecture-international',
'http://www.deakin.edu.au/course/master-architecture-design-management',
'http://www.deakin.edu.au/course/master-architecture-design-management-international',
'http://www.deakin.edu.au/course/master-architecture-research-international',
'http://www.deakin.edu.au/course/master-architecture-research',
'http://www.deakin.edu.au/course/master-arts-international',
'http://www.deakin.edu.au/course/master-arts',
'http://www.deakin.edu.au/course/master-arts-international-relations',
'http://www.deakin.edu.au/course/master-arts-international-relations-international',
'http://www.deakin.edu.au/course/master-arts-writing-and-literature-international',
'http://www.deakin.edu.au/course/master-arts-writing-and-literature',
'http://www.deakin.edu.au/course/master-biotechnology-bioinformatics',
'http://www.deakin.edu.au/course/master-biotechnology-bioinformatics-international',
'http://www.deakin.edu.au/course/master-business-arts-and-cultural-management',
'http://www.deakin.edu.au/course/master-business-arts-and-cultural-management-international',
'http://www.deakin.edu.au/course/master-business-sport-management',
'http://www.deakin.edu.au/course/master-business-sport-management-international',
'http://www.deakin.edu.au/course/master-business-administration',
'http://www.deakin.edu.au/course/master-business-administration-international',
'http://www.deakin.edu.au/course/master-business-administration-healthcare-management',
'http://www.deakin.edu.au/course/master-business-administration-healthcare-management-international',
'http://www.deakin.edu.au/course/international-master-business-administration-international',
'http://www.deakin.edu.au/course/international-master-business-administration',
'http://www.deakin.edu.au/course/master-business-analytics',
'http://www.deakin.edu.au/course/master-business-analytics-international',
'http://www.deakin.edu.au/course/master-child-play-therapy',
'http://www.deakin.edu.au/course/master-clinical-exercise-physiology',
'http://www.deakin.edu.au/course/master-clinical-exercise-physiology-international',
'http://www.deakin.edu.au/course/master-commerce-international',
'http://www.deakin.edu.au/course/master-commerce',
'http://www.deakin.edu.au/course/master-communication',
'http://www.deakin.edu.au/course/master-communication-international',
'http://www.deakin.edu.au/course/master-construction-management-international',
'http://www.deakin.edu.au/course/master-construction-management',
'http://www.deakin.edu.au/course/master-construction-management-professional-international',
'http://www.deakin.edu.au/course/master-construction-management-professional',
'http://www.deakin.edu.au/course/master-construction-management-research-international',
'http://www.deakin.edu.au/course/master-construction-management-research',
'http://www.deakin.edu.au/course/master-creative-arts',
'http://www.deakin.edu.au/course/master-creative-arts-international',
'http://www.deakin.edu.au/course/master-cultural-heritage-international',
'http://www.deakin.edu.au/course/master-cultural-heritage',
'http://www.deakin.edu.au/course/master-cyber-security',
'http://www.deakin.edu.au/course/master-cyber-security-international',
'http://www.deakin.edu.au/course/master-cyber-security-professional',
'http://www.deakin.edu.au/course/master-cyber-security-professional-international',
'http://www.deakin.edu.au/course/master-data-analytics-international',
'http://www.deakin.edu.au/course/master-data-analytics',
'http://www.deakin.edu.au/course/master-development-and-humanitarian-action',
'http://www.deakin.edu.au/course/master-development-and-humanitarian-action-international',
'http://www.deakin.edu.au/course/master-dietetics-international',
'http://www.deakin.edu.au/course/master-dietetics',
'http://www.deakin.edu.au/course/master-disability-and-inclusion',
'http://www.deakin.edu.au/course/master-education',
'http://www.deakin.edu.au/course/master-education-international',
'http://www.deakin.edu.au/course/master-education-leadership-and-management',
'http://www.deakin.edu.au/course/master-education-leadership-and-management-international',
'http://www.deakin.edu.au/course/master-education-research',
'http://www.deakin.edu.au/course/master-education-research-international',
'http://www.deakin.edu.au/course/master-engineering-research-international',
'http://www.deakin.edu.au/course/master-engineering-research',
'http://www.deakin.edu.au/course/master-engineering-professional-international',
'http://www.deakin.edu.au/course/master-engineering-professional',
'http://www.deakin.edu.au/course/master-financial-planning',
'http://www.deakin.edu.au/course/master-financial-planning-international',
'http://www.deakin.edu.au/course/master-health-and-human-services-management-international',
'http://www.deakin.edu.au/course/master-health-and-human-services-management',
'http://www.deakin.edu.au/course/master-health-economics-international',
'http://www.deakin.edu.au/course/master-health-economics',
'http://www.deakin.edu.au/course/master-health-promotion',
'http://www.deakin.edu.au/course/master-health-promotion-international',
'http://www.deakin.edu.au/course/master-human-nutrition',
'http://www.deakin.edu.au/course/master-human-nutrition-international',
'http://www.deakin.edu.au/course/master-human-resource-management',
'http://www.deakin.edu.au/course/master-human-resource-management-international',
'http://www.deakin.edu.au/course/master-humanitarian-assistance',
'http://www.deakin.edu.au/course/master-humanitarian-assistance-international',
'http://www.deakin.edu.au/course/master-information-systems',
'http://www.deakin.edu.au/course/master-information-systems-international',
'http://www.deakin.edu.au/course/master-information-technology-international',
'http://www.deakin.edu.au/course/master-information-technology',
'http://www.deakin.edu.au/course/master-information-technology-professional',
'http://www.deakin.edu.au/course/master-information-technology-professional-international',
'http://www.deakin.edu.au/course/master-information-technology-leadership',
'http://www.deakin.edu.au/course/master-information-technology-leadership-international',
'http://www.deakin.edu.au/course/master-international-accounting',
'http://www.deakin.edu.au/course/master-international-accounting-international',
'http://www.deakin.edu.au/course/master-international-and-community-development',
'http://www.deakin.edu.au/course/master-international-and-community-development-international',
'http://www.deakin.edu.au/course/master-international-finance-international',
'http://www.deakin.edu.au/course/master-international-finance',
'http://www.deakin.edu.au/course/master-landscape-architecture',
'http://www.deakin.edu.au/course/master-landscape-architecture-international',
'http://www.deakin.edu.au/course/master-languages-teaching',
'http://www.deakin.edu.au/course/master-laws',
'http://www.deakin.edu.au/course/master-laws-international',
'http://www.deakin.edu.au/course/master-laws-major-thesis',
'http://www.deakin.edu.au/course/master-laws-major-thesis-international',
'http://www.deakin.edu.au/course/master-legal-studies',
'http://www.deakin.edu.au/course/master-legal-studies-international',
'http://www.deakin.edu.au/course/master-marketing',
'http://www.deakin.edu.au/course/master-marketing-international',
'http://www.deakin.edu.au/course/master-nursing-international',
'http://www.deakin.edu.au/course/master-nursing',
'http://www.deakin.edu.au/course/master-nursing-practice-international',
'http://www.deakin.edu.au/course/master-nursing-practice',
'http://www.deakin.edu.au/course/master-nursing-practice-nurse-practitioner',
'http://www.deakin.edu.au/course/master-nutrition-and-population-health',
'http://www.deakin.edu.au/course/master-nutrition-and-population-health-international',
'http://www.deakin.edu.au/course/master-optometry',
'http://www.deakin.edu.au/course/master-philosophy',
'http://www.deakin.edu.au/course/master-philosophy-international',
'http://www.deakin.edu.au/course/master-philosophy-electromaterials',
'http://www.deakin.edu.au/course/master-philosophy-electromaterials-international',
'http://www.deakin.edu.au/course/master-politics-and-policy-international',
'http://www.deakin.edu.au/course/master-politics-and-policy',
'http://www.deakin.edu.au/course/master-professional-accounting',
'http://www.deakin.edu.au/course/master-professional-accounting-international',
'http://www.deakin.edu.au/course/master-professional-accounting-and-finance',
'http://www.deakin.edu.au/course/master-professional-accounting-and-finance-international',
'http://www.deakin.edu.au/course/master-professional-practice-digital-learning-international',
'http://www.deakin.edu.au/course/master-professional-practice-digital-learning',
'http://www.deakin.edu.au/course/master-professional-practice-financial-planning',
'http://www.deakin.edu.au/course/master-professional-practice-financial-planning-international',
'http://www.deakin.edu.au/course/master-professional-practice-leadership',
'http://www.deakin.edu.au/course/master-professional-practice-leadership-international',
'http://www.deakin.edu.au/course/master-professional-psychology',
'http://www.deakin.edu.au/course/master-psychology-clinical',
'http://www.deakin.edu.au/course/master-psychology-clinical-international',
'http://www.deakin.edu.au/course/master-psychology-organisational',
'http://www.deakin.edu.au/course/master-psychology-organisational-international',
'http://www.deakin.edu.au/course/master-public-health',
'http://www.deakin.edu.au/course/master-public-health-international',
'http://www.deakin.edu.au/course/master-science-biology-chemical-sciences-international',
'http://www.deakin.edu.au/course/master-science-biology-chemical-sciences',
'http://www.deakin.edu.au/course/master-science-environmental-science-international',
'http://www.deakin.edu.au/course/master-science-environmental-science',
'http://www.deakin.edu.au/course/master-science-information-technology-international',
'http://www.deakin.edu.au/course/master-science-information-technology',
'http://www.deakin.edu.au/course/master-science-research',
'http://www.deakin.edu.au/course/master-science-research-international',
'http://www.deakin.edu.au/course/master-social-work',
'http://www.deakin.edu.au/course/master-social-work-research-international',
'http://www.deakin.edu.au/course/master-social-work-research',
'http://www.deakin.edu.au/course/master-specialist-inclusive-education',
'http://www.deakin.edu.au/course/master-sustainability',
'http://www.deakin.edu.au/course/master-sustainability-international',
'http://www.deakin.edu.au/course/master-teaching-early-childhood',
'http://www.deakin.edu.au/course/master-teaching-early-childhood-international',
'http://www.deakin.edu.au/course/master-teaching-primary-and-early-childhood-international',
'http://www.deakin.edu.au/course/master-teaching-primary-and-early-childhood',
'http://www.deakin.edu.au/course/master-teaching-primary-and-secondary',
'http://www.deakin.edu.au/course/master-teaching-primary-and-secondary-international',
'http://www.deakin.edu.au/course/master-teaching-primary',
'http://www.deakin.edu.au/course/master-teaching-primary-international',
'http://www.deakin.edu.au/course/master-teaching-secondary-international',
'http://www.deakin.edu.au/course/master-teaching-secondary',
'http://www.deakin.edu.au/course/master-teaching-english-to-speakers-other-languages',
'http://www.deakin.edu.au/course/master-teaching-english-to-speakers-other-languages-international']

    for i in Lists:
        fullurl = base_url % i
        start_urls.append(fullurl)

    # rules = (
    #     # Rule(page_link, callback='get_programme_link', follow=True),
    #     # Rule(LinkExtractor(allow=r'startrow=\d+'), follow=True),
    #     Rule(LinkExtractor(restrict_xpaths='//*[@id="DataTables_Table_0"]/tbody/tr/td/a'), follow=True, callback='text1'),
    #     # Rule(LinkExtractor(restrict_xpaths='//ul[@class="no-list-bullets"]/li/a'), follow=False, callback='text2'),
    # )
    # def text(self, response):
    #     print(response.url)

    def parse(self, response):
        item = HooliItem()
        url = response.url
        print("===========================", response.url)

        university = "Deakin University"
        city = "NULL"
        country = 'Australia'
        website = 'http://www.deakin.edu.au'
        degree_level = "1"

        try:
            programme = response.xpath("//div[@class='module__hero-banner--content--inner']/h1//text()").extract()
            clear_space(programme)
            programme = ''.join(programme)
            print(1,programme)
            # print("item['programme']: ", item['programme'])
            degree_type = response.xpath("//div[@class='module__hero-banner--content--inner']/h1//text()").extract()
            clear_space(degree_type)
            # degree_type = ''.join(degree_type)
            # try:
            #     if "Associate Degree" in degree_type:
            #         degree_type = "Associate Degree"
            #     elif "Bachelor" in degree_type:
            #         degree_type = "Bachelor"
            #     elif "Master" in degree_type:
            #         degree_type = "Master"
            #     elif "Doctor" in degree_type:
            #         degree_type = "Doctor"
            #     else:
            #         degree_type = "NULL"
            # except:
            #     degree_type = "报错!"
            print(2,degree_type)

            # //div[@class='module__summary--items']/div[1]/div[2]
            IELTS_s = response.xpath('//*[@id="main-content"]//div[@class="module__summary--items"]//text()').extract()
            clear_space(IELTS_s)
            IELTS_s = ''.join(IELTS_s)
            if "English language requirements" in IELTS_s:
                start = IELTS_s.find("English language requirements")
                IELTS =  IELTS_s[start:]
                IELTS =  IELTS[:100]
                IELTS = IELTS.lstrip("English language requirements")
                item["IELTS"] = IELTS
            else:
                IELTS = "NULL"
            print(3,IELTS)
            # print("item['IELTS']: ", item['IELTS'])

            duration_s = response.xpath('//*[@id="main-content"]//div[@class="module__summary--items"]//text()').extract()
            clear_space(duration_s)
            duration_s = ''.join(duration_s)
            if "Duration" in duration_s:
                start = duration_s.find("Duration")
                end = duration_s.find("Campuses")
                duration = duration_s[start:end]
                # duration = duration[:50]
                item["duration"] = duration
            else:
                duration = "NULL"
            print(4,duration)
            # print("item['duration']: ", item['duration'])

            mode_s = response.xpath('//*[@id="main-content"]//div[@class="module__summary--items"]//text()').extract()
            clear_space(mode_s)
            mode_s = ''.join(mode_s)
            print(mode_s)
            if "Duration" in mode_s:
                start = mode_s.find("Duration")
                mode = mode_s[start:]
                mode = mode.lstrip("Duration")
                mode = mode[:43]

            else:
                mode = "full time"

            print(18,'=============',mode)

            location_s = response.xpath('//*[@id="main-content"]//div[@class="module__summary--items"]//text()').extract()
            clear_space(location_s)
            location_s = ''.join(location_s)
            if "Campuses" in location_s:
                start = location_s.find("Campuses")
                location = location_s[start:]
                location = location[:100]
                item["location"] = location
            else:
                location = "NULL"
            print(5,location)
            # print("item['location']: ", item['location'])



            # //div[@id='navigation__course']/following-sibling::div
            overview = response.xpath("//div[@id='navigation__course']/following-sibling::div[1]//text()").extract()
            clear_space(overview)
            overview = ''.join(overview)
            print(6,overview)
            # print("item['overview']: ", item['overview'])

            modules = response.xpath('//*[@id="module__course-structure"]/div[@class="module__content-panel--wrapper"]//text()').extract()
            clear_space(modules)
            modules = ''.join(modules)
            print(7,modules)
            # print("item['modules']: ", item['modules'])

            # //div[@id='main-content']/div[@class='module__content-panel module__key-information module__no-divider']
            ucascodeContent = response.xpath("//div[@id='main-content']/div[@class='module__content-panel module__key-information module__no-divider']//text()").extract()
            clear_space(ucascodeContent)
            # print("ucascodeContent: ", ucascodeContent)
            if "Deakin code" in ucascodeContent:
                ucascodeIndex = ucascodeContent.index("Deakin code")
                if "CRICOS" in ucascodeContent:
                    ucascodeIndexEnd = ucascodeContent.index("CRICOS")
                else:
                    ucascodeIndexEnd = -1
                ucascode = ucascodeContent[ucascodeIndex+1:ucascodeIndexEnd]
                ucas_code = ''.join(ucascode).strip()
                if len(ucas_code) > 255:
                    ucas_code = ucas_code[:255]
                else:
                    ucas_code = ''.join(ucascode).strip()
            # print("item['ucas_code']: ", item['ucas_code'])
            print(8,ucas_code)

            # //div[@data-section='entry requirements']
            entry_requirements = response.xpath("//div[@data-section='entry requirements']//text()").extract()
            clear_space(entry_requirements)
            entry_requirements = ''.join(entry_requirements)
            # print("item['entry_requirements']: ", item['entry_requirements'])
            print(9,entry_requirements)

            # //div[@data-section='fees and scholarships']
            tuition_fee = response.xpath("//div[@data-section='fees and scholarships']//text()").extract()
            clear_space(tuition_fee)
            tuition_fee = getTuition_fee(''.join(tuition_fee))
            print(10,tuition_fee)

            # print("item['tuition_fee']: ", item['tuition_fee'])

            career1 = response.xpath("//div[@data-section='graduate outcomes']//text()").extract()
            career2= response.xpath("//div[@data-section='graduate outcomes']/following-sibling::div[1]//text()").extract()
            clear_space(career1)
            clear_space(career2)
            career = ''.join(career1) + ''.join(career2)
            print(11,career)

            # print("item['career']: ", item['career'])

            # //div[@data-section='application information']/following-sibling::div[2]
            how_to_apply = response.xpath(
                "//div[@data-section='application information']/following-sibling::div[2]//text()").extract()
            clear_space(how_to_apply)
            how_to_apply = ''.join(how_to_apply)
            print(12,how_to_apply)
            # print("item['how_to_apply']: ", item['how_to_apply'])

            # print(item)
            department = "NULL"
            start_date = "NULL"
            degree_description = "NULL"
            teaching = 'NULL'
            assessment = "NULL"
            application_date = "NULL"
            deadline = "NULL"
            application_fee = "NULL"
            ATAS = "NULL"
            GPA = "NULL"
            average_score = "NULL"
            accredited_university = "NULL"
            Alevel = 'NULL'
            IB = "NULL"
            IELTS_L = "NULL"
            IELTS_S = "NULL"
            IELTS_R = 'NULL'
            IELTS_W = 'NULL'
            TOEFL = "NULL"
            TOEFL_L = 'NULL'
            TOEFL_S = "NULL"
            TOEFL_R = 'NULL'
            TOEFL_W = 'NULL'
            GRE = "NULL"
            GMAT = 'NULL'
            LSAT = "NULL"
            MCAT = "NULL"
            working_experience = 'NULL'
            interview = 'NULL'
            portfolio = 'NULL'
            application_documents = 'NULL'
            chinese_requirements = 'NULL'
            school_test = 'NULL'
            SATI = 'NULL'
            SATII = 'NULL'
            SAT_code = 'NULL'
            ACT = 'NULL'
            ACT_code = 'NULL'
            other = 'NULL'
            create_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


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

        except Exception as e:
            with open("./error/"+item['university']+item['degree_level']+".txt", 'w', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================")
            print("异常：", str(e))
            print("报错url：", response.url)

    # def parse(self, response):
    #     item = get_item(SchoolItem)
    #     item['university'] = "University"
    #     item['country'] = 'Australia'
    #     item['website'] = ''
    #     item['url'] = response.url
    #     print("===========================")
    #     print(response.url)
    #     try:
    #
    #         yield item
    #     except Exception as e:
    #         with open("./error/"+item['university']+item['degree_level']+".txt", 'w', encoding="utf-8") as f:
    #             f.write(str(e) + "\n" + response.url + "\n========================")
    #         print("异常：", str(e))
    #         print("报错url：", response.url)

