# -*- coding: utf-8 -*-
import scrapy


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['http://book.zongheng.com/']
    start_urls = ['http://http://book.zongheng.com//']

    def parse(self, response):
        pass
