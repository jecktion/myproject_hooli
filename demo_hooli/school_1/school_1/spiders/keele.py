


import scrapy
from school_1.items import HooliItem
import datetime
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor

class PlymouthSpider(CrawlSpider):
    name = 'keele'
    allowed_domains = ['www.keele.ac.uk']
    start_urls = ['https://www.keele.ac.uk/ugcourses/']

    rules = (
        Rule(LinkExtractor(allow=r'www.keele.ac.uk/ugcourses/'),follow=True),
        Rule(LinkExtractor(allow=r'ugcourses\/.*'), callback='parse_item', follow=False),
    )

    def parse_item(self,response):
        print('==================================',response.url)
        item = HooliItem()
        
        url = response.url
        university= "Keele"
        programme = response.xpath('').extract()
        programme = ' '.join(programme)
        
        