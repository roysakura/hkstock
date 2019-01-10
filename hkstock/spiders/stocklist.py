# -*- coding: utf-8 -*-
import scrapy


class StocklistSpider(scrapy.Spider):
    name = 'stocklist'
    allowed_domains = ['finance.sina.com.cn']
    start_urls = ['http://finance.sina.com.cn/']

    def parse(self, response):
        pass
