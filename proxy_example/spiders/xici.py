 # -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor

from proxy_example.items import ProxyExampleItem
import requests
import scrapy
from scrapy import Request
import json

class XiciSpider(scrapy.Spider):
    name = "xici"
    allowed_domains = ["www.xicidaili.com"]
    start_urls = ['http://www.xicidaili.com/nn/%s' % i for i in range(1,10)]


    def parse(self, response):
        ipItems = response.css('#ip_list tr:not(:first-child)')
        for item in ipItems:
            ip = item.css('td:nth-child(2)::text').extract_first()
            port = item.css('td:nth-child(3)::text').extract_first()
            scheme = item.css('td:nth-child(6)::text').extract_first()
            proxy = '%s://%s:%s' % (scheme, ip, port)
            try:
                if requests.get('http://ip.cn/', proxies=proxy, timeout=2).status_code == 200:
                    print('success %s' % ip)
                    items = ProxyExampleItem()
                    items['url'] = scheme + '://' + ip + ':' + port
                    items['ip'] = ip
                    items['port'] = port
                    items['scheme'] = scheme
                    yield items
            except:
                print('fail %s' % ip)































