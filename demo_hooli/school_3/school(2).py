import json
from urllib.parse import urlencode
from requests.exceptions import ConnectionError, InvalidSchema
from pyquery import PyQuery as pq
from multiprocessing import Pool
import requests


def get_index(page):
    headers = {
        # "Accept": "*/*",
        # "Accept-Encoding": "gzip, deflate, br",
        # "Accept-Language": "zh-CN,zh;q=0.9",
        # "Connection": "keep-alive",
        # "Host": "westernsydney-search.clients.squiz.net",
        # "Origin": "https://www.westernsydney.edu.au",
        # "Referer": "https://www.westernsydney.edu.au/search.html?collection=wsu-futurestudent&query=bachelor",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
    }

    data = {
        'sort':'',
        'form': 'json',
        'start_rank': page,
        'query': 'bachelor',
        'collection': 'wsu-futurestudent'
    }
    url = 'https://westernsydney-search.clients.squiz.net/s/search.html?' + urlencode(data)
    response = requests.get(url, headers=headers)
    try:
        if response.status_code ==200:
            return response.text
        return None
    except ConnectionError:
        return None
def parse_index(html):
    result = json.loads(html)
    if 'results' in result.keys():
        for item in result.get('results'):
            yield item.get('url')

    # if 'resultsSummary' in result.keys():
    #     currStart = result.get('resultsSummary').get('currStart')
    #     get_index(currStart)

def get_page_detail(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
    }
    response = requests.get(url, headers=headers)
    try:
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        return None

def parse_page_detail(html):
    doc = pq(html)
    # try:
    #     url = doc('#wrapper > div > div.template--main.template--product-page > div > div:nth-child(4) > div > div > div > div > div:nth-child(2) > div > p > a').attr.href
    #     return {
    #         'url': url
    #     }
    # except InvalidSchema:
    #     return None
    title = doc('#wrapper > div > div.template--main.template--product-page > div > div.section.component.component--page-banner.component--fullscreen > div > div > div > div > div > div.component.component--title > h1').text()
    return {
        'title':title
    }
#
# def get_detail_content(url):
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
#     }
#     response = requests.get(url, headers=headers)
#     try:
#         if response.status_code == 200:
#             return response.text
#         return None
#     except ConnectionError:
#         return None
#
# def get_content(html):
#     doc = pq(html)
#     title = doc('#hbcontent > span').text()
#     return {
#         'title': title
#     }

def main(page):
    html = get_index(page)
    # print(html)
    if html:
        urls = parse_index(html)
        # print(urls)
        for url in urls:
            # print(url)
            if url:
                html = get_page_detail(url)
                # print(html)
                if html:
                    title = parse_page_detail(html)
                    print(title)
                    # html = get_detail_content(url)
                    # title = get_content(html)
                    # print(title)




if __name__ == '__main__':
    page = [x*10+1 for x in range(0, 44)]
    pool = Pool()
    pool.map(main, page)
