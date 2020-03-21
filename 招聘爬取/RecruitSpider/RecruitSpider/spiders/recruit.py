# -*- coding: utf-8 -*-
import scrapy


class RecruitSpider(scrapy.Spider):
    name = 'recruit'
    allowed_domains = ['zhipin.com']
    start_urls = ['http://zhipin.com/']

    def parse(self, response):
        pass
