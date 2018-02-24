from scrapy import cmdline
import os
os.chdir('spiders')


cmdline.execute('scrapy crawl mastersportal_USA'.split())