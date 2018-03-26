
from scrapy import cmdline
import os
os.chdir('spiders')


# cmdline.execute('scrapy crawl Newcastle_ug'.split())
cmdline.execute('scrapy crawl Newcastle_pg'.split())