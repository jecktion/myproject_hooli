# -*- coding: utf-8 -*-






import scrapy
from school_3.items import HooliItem
import datetime
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import re

class PlymouthSpider(scrapy.Spider):
    name = 'Darwin_ug'
    allowed_domains = ['www.cdu.edu.au']
    start_urls = []
    base_url = '%s'

    Lists = ['http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BAH22',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BAH22,2016,4,',
'http://stapps.cdu.edu.au/f?p=100:31:2112469134056703::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:WARLA1',
'http://stapps.cdu.edu.au/f?p=100:31:2112469134056703::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:WARLA1,2016,1,',
'http://stapps.cdu.edu.au/f?p=100:31:1926308230119980::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BCNMIT',
'http://stapps.cdu.edu.au/f?p=100:31:1926308230119980::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BCNMIT',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BCAIH',
'http://stapps.cdu.edu.au/f?p=100:31:1926308230119980::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BAR',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:WARTS1,2018,1,',
'http://stapps.cdu.edu.au/f?p=100:31:1926308230119980::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BAR',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:WCART1,2018,1,',
'http://stapps.cdu.edu.au/f?p=100:31:1926308230119980::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BCAIVA',
'http://stapps.cdu.edu.au/f?p=100:31:1926308230119980::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BCAICM',
'http://stapps.cdu.edu.au/f?p=100:31:1926308230119980::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BCAINM',
'http://stapps.cdu.edu.au/f?p=100:31:1926308230119980::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BDES',
'http://stapps.cdu.edu.au/f?p=100:31:1926308230119980::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BDES',
'http://stapps.cdu.edu.au/f?p=100:31:2112469134056703::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:WACC01',
'http://stapps.cdu.edu.au/f?p=100:31:2112469134056703::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:WACC01,2016,1,',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:WBUS01,2018,1,',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BCOMR',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BCOMR',
'http://stapps.cdu.edu.au/f?p=100:31:4348157312007::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BEDEC',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BEDP,2017,1,',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:WEDS01,2018,1,',
'http://stapps.cdu.edu.au/f?p=100:31:4348157312007::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BEDGE',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:WEDST1,2018,1,',
'http://stapps.cdu.edu.au/f?p=100:31:1926308230119980::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BEDSVA',
'http://stapps.cdu.edu.au/f?p=100:31:1926308230119980::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BEDSHP',
'http://stapps.cdu.edu.au/f?p=100:31:1926308230119980::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BEDSHP',
'http://stapps.cdu.edu.au/f?p=100:31:1926308230119980::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BEDSSC',
'http://stapps.cdu.edu.au/f?p=100:31:1926308230119980::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BEDSSC',
'http://stapps.cdu.edu.au/f?p=100:31:1926308230119980::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BEDSMU',
'http://stapps.cdu.edu.au/f?p=100:31:1926308230119980::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BEDSMU',
'http://stapps.cdu.edu.au/f?p=100:31:1926308230119980::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BEDSMA',
'http://stapps.cdu.edu.au/f?p=100:31:1926308230119980::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BEDSMA',
'http://stapps.cdu.edu.au/f?p=100:31:1926308230119980::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BEDSIT',
'http://stapps.cdu.edu.au/f?p=100:31:1926308230119980::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BEDSIT',
'http://stapps.cdu.edu.au/f?p=100:31:1926308230119980::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BEDSHS',
'http://stapps.cdu.edu.au/f?p=100:31:1926308230119980::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BEDSHS',

'http://stapps.cdu.edu.au/f?p=100:31:2112469134056703::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:VENG01',
'http://stapps.cdu.edu.au/f?p=100:31:2112469134056703::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:VENG01,2016,1,',
'http://stapps.cdu.edu.au/f?p=100:31:2112469134056703::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:WENGS1',
'http://stapps.cdu.edu.au/f?p=100:31:2112469134056703::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:WENGS1,2016,1,',
'http://stapps.cdu.edu.au/f?p=100:31:2112469134056703::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:HENG01',
'http://stapps.cdu.edu.au/f?p=100:31:2112469134056703::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:HENG01,2016,1,',
'http://stapps.cdu.edu.au/f?p=100:31:2112469134056703::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:XENG01',
'http://stapps.cdu.edu.au/f?p=100:31:2112469134056703::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:XENG01,2016,1,',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO:::',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BES,2017,2,',
'http://stapps.cdu.edu.au/f?p=100:31:1926308230119980::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BES',
'http://stapps.cdu.edu.au/f?p=100:31:7843148162510034::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:YCOUN1',
'http://stapps.cdu.edu.au/f?p=100:31:7843148162510034::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:YCOUN1,2016,1,',
'http://stapps.cdu.edu.au/f?p=100:31:7843148162510034::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:YPSY01',
'http://stapps.cdu.edu.au/f?p=100:31:7843148162510034::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:YPSY01,2016,1,#TAB_LINK#',
'http://stapps.cdu.edu.au/f?p=100:31:2112469134056703::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:WPSYS1',
'http://stapps.cdu.edu.au/f?p=100:31:2112469134056703::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:WPSYS1,2016,1,',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:WPSYG1,2018,1,',
'http://stapps.cdu.edu.au/f?p=100:31:1926308230119980::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BPHAR',
'http://stapps.cdu.edu.au/f?p=100:31:1926308230119980::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BPHAR',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BHSC,2017,2,',
'http://stapps.cdu.edu.au/f?p=100:31:1926308230119980::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BHSC',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:WMIDW1',
'http://stapps.cdu.edu.au/f?p=100:31:1926308230119980::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BMID',
'http://stapps.cdu.edu.au/f?p=100:31:1926308230119980::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BMLSC',
'http://stapps.cdu.edu.au/f?p=100:31:1926308230119980::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BMLSC',
'http://stapps.cdu.edu.au/f?p=100:31:4348157312007::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BNRSG',
'http://stapps.cdu.edu.au/f?p=100:31:4348157312007::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BNRSG,2016,1,',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:XASS01',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:WASS01',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:XINLL1',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:XASS01,2017,1,',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:WINLL1',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:WASS01,2017,1,',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:VINKH1',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:WINLL1,2017,1,',
'http://stapps.cdu.edu.au/f?p=100:31:2112469134056703::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:YATSI1',
'http://stapps.cdu.edu.au/f?p=100:31:8040066213906744::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:XICT01',
'http://stapps.cdu.edu.au/f?p=100:31:8040066213906744::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:XICT01,2016,1,',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:XNENG1,2018,2,',
'http://stapps.cdu.edu.au/f?p=100:31:8040066213906744::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:XICT01,2016,1,',
'http://stapps.cdu.edu.au/f?p=100:31:1926308230119980::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BIT',
'http://stapps.cdu.edu.au/f?p=100:31:1926308230119980::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BIT',
'http://stapps.cdu.edu.au/f?p=100:31:4348157312007::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BSENGH',
'http://stapps.cdu.edu.au/f?p=100:31:4348157312007::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BSENGH,2016,1,',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:WCOMS1,2018,1,',
'http://stapps.cdu.edu.au/f?p=100:31:4348157312007::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BSENGH',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:HCSIT1,2018,1,',
'http://stapps.cdu.edu.au/f?p=100:31:4348157312007::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BSENGH',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:YNENG1,2017,1,',
'http://stapps.cdu.edu.au/f?p=100:31:7843148162510034::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:YLAW01',
'http://stapps.cdu.edu.au/f?p=100:31:7843148162510034::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:YLAW01,2016,1,',
'http://stapps.cdu.edu.au/f?p=100:31:2112469134056703::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:WLAW01',
'http://stapps.cdu.edu.au/f?p=100:31:2112469134056703::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:WLAW01,2016,1,',
'http://stapps.cdu.edu.au/f?p=100:31:2112469134056703::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:WLAWG1',
'http://stapps.cdu.edu.au/f?p=100:31:2112469134056703::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:WLAWG1,2016,1,',
'http://stapps.cdu.edu.au/f?p=100:31:2112469134056703::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:XLEST1',
'http://stapps.cdu.edu.au/f?p=100:31:2173703494117830::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:XEXSS1',
'http://stapps.cdu.edu.au/f?p=100:31:2173703494117830::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:XEXSS1,2016,1,',
'http://stapps.cdu.edu.au/f?p=100:31:11457928108774::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:WSCI01,2018,1,',
'http://stapps.cdu.edu.au/f?p=100:31:4348157312007::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BSCIH',
'http://stapps.cdu.edu.au/f?p=100:31:4348157312007::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BSCIH,2016,6,',
'http://stapps.cdu.edu.au/f?p=100:31:1926308230119980::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BESS',
'http://stapps.cdu.edu.au/f?p=100:31:1926308230119980::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BESS',
'http://stapps.cdu.edu.au/f?p=100:31:2112469134056703::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:YSCI01',
'http://stapps.cdu.edu.au/f?p=100:31:2112469134056703::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:YSCI01,2016,1,',
'http://stapps.cdu.edu.au/f?p=100:31:15412980602795::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:YEXSS1',
'http://stapps.cdu.edu.au/f?p=100:31:15412980602795::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:YEXSS1,2016,1,',
'http://stapps.cdu.edu.au/f?p=100:31:1926308230119980::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BHCS',
'http://stapps.cdu.edu.au/f?p=100:31:1926308230119980::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BHCS',
'http://stapps.cdu.edu.au/f?p=100:31:1926308230119980::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BSW',
'http://stapps.cdu.edu.au/f?p=100:31:1926308230119980::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BSW',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:SPPOL1',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:SPAPP1',
'http://stapps.cdu.edu.au/f?p=100:31:2112469134056703::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:SPACC1',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:MBAP14,2017,1,',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:MBA14,2017,1,',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:TBAD01,2018,1,',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:GCEI,2017,1,',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:SEDI01,2018,1,',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:SDLF01',
'http://stapps.cdu.edu.au/f?p=100:31:1926308230119980::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:MEDI',
'http://stapps.cdu.edu.au/f?p=100:31:2112469134056703::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:SENG01',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:MEMDM',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:MEM,2017,2,',
'http://stapps.cdu.edu.au/f?p=100:31:7843148162510034::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:TEMDM1',
'http://stapps.cdu.edu.au/f?p=100:31:6755497689931::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:MCPHTH',
'http://stapps.cdu.edu.au/f?p=100:31:1926308230119980::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:MITSE',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:SITIS1,2018,1,',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:SITCS1,2018,1,',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:SDASC1,2018,1,',
'http://stapps.cdu.edu.au/f?p=100:31:7843148162510034::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:SITBI1',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:TDASC1,2018,1,',
'http://stapps.cdu.edu.au/f?p=100:31:7843148162510034::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:SITBI1',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:TINTC1,2018,1,',
'http://stapps.cdu.edu.au/f?p=100:31:7843148162510034::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:SITBI1',
'http://stapps.cdu.edu.au/f?p=100:31:7843148162510034::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:SITBI1',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:TIPD01',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:SLAW01,2017,1',
'http://stapps.cdu.edu.au/pls/apex/f?p=100:31::::31:P31_SEARCH_COURSE:DPHEHS',
'http://stapps.cdu.edu.au/pls/apex/f?p=100:31::::31:P31_SEARCH_COURSE:DPHIAS',
'http://stapps.cdu.edu.au/pls/apex/f?p=100:31::::31:P31_SEARCH_COURSE:DPHLBA',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:DPHIKE,2016,2,',
'http://stapps.cdu.edu.au/pls/apex/f?p=100:31::::31:P31_SEARCH_COURSE:MRSEHS',
'http://stapps.cdu.edu.au/pls/apex/f?p=100:31::::31:P31_SEARCH_COURSE:MRSIAS',
'http://stapps.cdu.edu.au/pls/apex/f?p=100:31::::31:P31_SEARCH_COURSE:MRSLBA',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:MRSIKE,2016,2,',
'http://stapps.cdu.edu.au/f?p=100:32:9221184699824::NO:32:P32_SEARCH_COURSE,P32_SEARCH_YEAR,P32_SEARCH_VERSION,P32_TAB_LABEL:SHB30416,2018,1,Overview',
'http://stapps.cdu.edu.au/f?p=100:32:15237980900618::NO:32:P32_SEARCH_COURSE,P32_SEARCH_YEAR,P32_SEARCH_VERSION,P32_TAB_LABEL:SHB30115,2018,1,Overview',
'http://stapps.cdu.edu.au/f?p=100:32:15237980900618::NO:32:P32_SEARCH_COURSE,P32_SEARCH_YEAR,P32_SEARCH_VERSION,P32_TAB_LABEL:SHB50115,2018,1,Overview',
'http://stapps.cdu.edu.au/f?p=100:32:15237980900618::NO:32:P32_SEARCH_COURSE,P32_SEARCH_YEAR,P32_SEARCH_VERSION,P32_TAB_LABEL:CPP40115,2018,1,Overview',
'http://stapps.cdu.edu.au/f?p=100:32:15237980900618::NO:32:P32_SEARCH_COURSE,P32_SEARCH_YEAR,P32_SEARCH_VERSION,P32_TAB_LABEL:FNS30315,2018,1,Overview',
'http://stapps.cdu.edu.au/f?p=100:32:15237980900618::NO:32:P32_SEARCH_COURSE,P32_SEARCH_YEAR,P32_SEARCH_VERSION,P32_TAB_LABEL:FNS40615,2018,1,Overview',
'http://stapps.cdu.edu.au/f?p=100:32:15237980900618::NO:32:P32_SEARCH_COURSE,P32_SEARCH_YEAR,P32_SEARCH_VERSION,P32_TAB_LABEL:BSB30115,2018,1,Overview',
'http://stapps.cdu.edu.au/f?p=100:32:15237980900618::NO:32:P32_SEARCH_COURSE,P32_SEARCH_YEAR,P32_SEARCH_VERSION,P32_TAB_LABEL:BSB40215,2018,1,Overview',
'http://stapps.cdu.edu.au/f?p=100:32:15237980900618::NO:32:P32_SEARCH_COURSE,P32_SEARCH_YEAR,P32_SEARCH_VERSION,P32_TAB_LABEL:CHC50113,2018,1,Overview',
'http://stapps.cdu.edu.au/f?p=100:32:15237980900618::NO:32:P32_SEARCH_COURSE,P32_SEARCH_YEAR,P32_SEARCH_VERSION,P32_TAB_LABEL:AHC21016,2018,1,Overview',
'http://stapps.cdu.edu.au/f?p=100:32:15237980900618::NO:32:P32_SEARCH_COURSE,P32_SEARCH_YEAR,P32_SEARCH_VERSION,P32_TAB_LABEL:AHC31416,2018,1,Overview',
'http://stapps.cdu.edu.au/f?p=100:32:15237980900618::NO:32:P32_SEARCH_COURSE,P32_SEARCH_YEAR,P32_SEARCH_VERSION,P32_TAB_LABEL:AHC40916,2018,1,Overview',
'http://stapps.cdu.edu.au/f?p=100:32:15237980900618::NO:32:P32_SEARCH_COURSE,P32_SEARCH_YEAR,P32_SEARCH_VERSION,P32_TAB_LABEL:AHC51116,2018,1,Overview',
'http://stapps.cdu.edu.au/f?p=100:32:15237980900618::NO:32:P32_SEARCH_COURSE,P32_SEARCH_YEAR,P32_SEARCH_VERSION,P32_TAB_LABEL:SIT50416,2018,1,Overview',
'http://stapps.cdu.edu.au/f?p=100:32:15237980900618::NO:32:P32_SEARCH_COURSE,P32_SEARCH_YEAR,P32_SEARCH_VERSION,P32_TAB_LABEL:FDF30710,2018,1,Overview',
'http://stapps.cdu.edu.au/f?p=100:32:15237980900618::NO:32:P32_SEARCH_COURSE,P32_SEARCH_YEAR,P32_SEARCH_VERSION,P32_TAB_LABEL:SIT30716,2018,1,Overview',
'http://stapps.cdu.edu.au/f?p=100:32:15237980900618::NO:32:P32_SEARCH_COURSE,P32_SEARCH_YEAR,P32_SEARCH_VERSION,P32_TAB_LABEL:SIT30816,2018,1,Overview',
'http://stapps.cdu.edu.au/f?p=100:32:15237980900618::NO:32:P32_SEARCH_COURSE,P32_SEARCH_YEAR,P32_SEARCH_VERSION,P32_TAB_LABEL:SIT40516,2018,1,Overview',
'http://stapps.cdu.edu.au/f?p=100:32:15237980900618::NO:32:P32_SEARCH_COURSE,P32_SEARCH_YEAR,P32_SEARCH_VERSION,P32_TAB_LABEL:ICT41015,2018,1,Overview',
'http://stapps.cdu.edu.au/f?p=100:31:2112469134056703::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:WACC01',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:WBUS01,2018,1,',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BCOMR',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:SPAPP1',
'http://stapps.cdu.edu.au/f?p=100:31:2112469134056703::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:SPACC1',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:SBAPP1,2018,1,',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:SBAD01,2018,1,',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:TBAD01,2018,1,',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:TBAD01,2018,1,',
'http://stapps.cdu.edu.au/f?p=100:31:2112469134056703::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:WACC01',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:WBUS01,2018,1,',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:BCOMR',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:SPAPP1',
'http://stapps.cdu.edu.au/f?p=100:31:2112469134056703::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:SPACC1',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:SBAPP1,2018,1,',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:SBAD01,2018,1,',
'http://stapps.cdu.edu.au/f?p=100:31:0::NO::P31_SEARCH_COURSE,P31_SEARCH_YEAR,P31_SEARCH_VERSION,P31_TAB_LABEL:TBAD01,2018,1,',]

    for i in Lists:
        fullurl = base_url % i
        start_urls.append(fullurl)

    # rules = (
    #     # Rule(LinkExtractor(allow=(r'.*'), restrict_xpaths=('')),callback='parse_item', follow=True),
    #     # Rule(LinkExtractor(allow=r''),follow=True),
    #     # Rule(LinkExtractor(allow=(r'.*'),restrict_xpaths=('//*[@id="tab-menu"]/li/a')), follow=False),
    #     Rule(LinkExtractor(allow=r'.*,2018,3,How2Apply|,2018,3,Course%20Structure'),callback='parse_item',follow=False),
    # )

    def parse(self,response):
        print('==================================',response.url)
        item = HooliItem()

        url = response.url
        print(1,url)

        university = 'Charles Darwin University'
        print(2,university)

        department = response.xpath('//*[@id="P31_ORG_UNIT"]//text()').extract()
        department = ''.join(department)
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
        city = "Darwin"
        website = 'http://www.cdu.edu.au'
        degree_level = '0'

        # programme = response.xpath('//div[@class="section picture-nav"]/h1/text()').extract()
        programme = response.xpath('//*[@id="P31_COURSE_HEADING_NAME"]//text()').extract()
        programme = ''.join(programme)
        print(4,programme)

        ucas_code = response.xpath('//*[@id="P31_COURSE_CODE"]//text()').extract()
        ucas_code = ''.join(ucas_code)
        # try:
        #     if "Course Code:" in ucas_code_s:
        #         start = ucas_code_s.find("Course Code:")
        #         ucas_code = ucas_code_s[start:]
        #         ucas_code = ucas_code[:20]
        #         ucas_code = ucas_code.lstrip("Course Code:")
        #         item["ucas_code"] = ucas_code
        #     else:
        #         ucas_code = "NULL"
        # except:
        #     ucas_code = "报错!"
        print(5,ucas_code)

        # degree_type = response.xpath('//div[@class="section picture-nav"]/h1/text()').extract()
        degree_type = response.xpath('//*[@id="P31_COURSE_HEADING_NAME"]//text()').extract()
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

        start_date = 'NULL'
        # start_date = ''.join(start_date)
        # print(5,start_date)

        # overview = response.xpath('//div[@class="left logo-bg"]//text()').extract()
        overview = response.xpath('//*[@id="P31_GENERAL_DESC"]//text()').extract()
        overview = ''.join(overview)
        print(7, overview)

        mode = "Standard full-time completion"
        # mode = mode.replace('\n','')
        # mode = mode.replace('      ','')
        # print(7,mode)



        duration = response.xpath('//*[@id="P31_STD_FT_TIME"]//text()').extract()
        duration = ''.join(duration)
        # duration = duration.replace('\n','')
        # duration = duration.replace('    ','')
        print(8,duration)

        modules = response.xpath('//*[@id="P31_COURSE_STRUCTURE4"]//text()').extract()
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
        print(9,modules)

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

        career = "NULL"
        # career_s = ''.join(career_s)
        #
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
        # print(8.5, career)

        application_date = "NULL"

        deadline = 'NULL'
        # deadline = ''.join(deadline)
        # print(9,deadline)

        application_fee = 'NULL'

        tuition_fee= "NULL"
        # tuition_fee = ''.join(tuition_fee)
        # # tuition_fee = tuition_fee.replace('\n','')
        # # tuition_fee = tuition_fee.replace('    ','')
        # tuition_fee = self.getTuition_fee(tuition_fee)
        # # try:
        # #     if tuition_fee_s > 0:
        #         tuition_fee = tuition_fee_s
        #     else:
        #         tuition_fee = "NULL"
        # except:
        #     tuition_fee = "报错!"

        # print(9, tuition_fee)

        location = response.xpath('//*[@id="report_R9740105549248339"]//td//text()').extract()
        location = ''.join(location)
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
        print(10,location)

        ATAS = 'NULL'

        GPA = 'NULL'

        average_score = 'NULL'

        accredited_university = 'NULL'

        Alevel = 'NULL'

        IB = 'NULL'

        IELTS = "NULL"
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

        how_to_apply = response.xpath('//*[@id="P31_ADM_INTERNATIONAL"]/p//text()').extract()
        how_to_apply = ''.join(how_to_apply)
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
        print(11,how_to_apply)

        entry_requirements = response.xpath('//*[@id="apex_layout_21626630981069183"]//text()').extract()
        entry_requirements = ''.join(entry_requirements)
        # EntryRequirements = EntryRequirements.replace(' ','')
        # try:
        #     if "Entry requirements" in entry_requirements_s:
        #         start = entry_requirements_s.find("Entry requirements")
        #         end = entry_requirements_s.find("Study options")
        #         entry_requirements = entry_requirements_s[start:end]
        #         item["entry_requirements"] = entry_requirements
        #     else:
        #         entry_requirements = entry_requirements_s
        #
        # except:
        #     entry_requirements = '报错!'

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
            elif len(degree_type) == 0:
                degree_type = 'NULL'

            else:
                degree_type = 'Ordinary degree'
        except:
            degree_type = "NULL"
        return degree_type

