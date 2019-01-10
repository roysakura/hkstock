# -*- coding: utf-8 -*-
import scrapy


class StockUpdateSpider(scrapy.Spider):
    name = 'stock_update'
    allowed_domains = ['finance.sina.com.cn']
    start_urls = ['http://finance.sina.com.cn/']

    def parse(self, response):
        pass
