# -*- coding: utf-8 -*-
import scrapy
import datetime
import pandas as pd
import numpy as np
import datetime
import json
import re
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
from scrapy_splash import SplashRequest
from hkstock.items import StockItem
from scrapy.http.request import Request


class StockSpider(scrapy.Spider):
	name = 'stock'
	allowed_domains = ['finance.sina.com.cn']
	start_urls = ['http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHKStockData?page=1&num=10000&sort=symbol&asc=1&node=qbgg_hk&_s_r_a=page']

	#def start_requests(self):
	#	for i in range(100):
	#		yield Request('http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHKStockData?page={}&num=10000&sort=symbol&asc=1&node=qbgg_hk&_s_r_a=page'.format(i),self.parse)

	def parse(self, response):
		# add double quote to key
		t = re.sub(r'(\w+_\d{2}[a-zA-Z_]*)(:)',r'"\1"\2',response.body.decode('unicode-escape'))
		tt = re.sub(r'([a-z_]+)(:)',r'"\1"\2',t)
		jsonobj = json.loads(tt)

		for j in jsonobj:
			item = StockItem()
			item["symbol"] = j["symbol"]
			item["name"] = j["engname"] 
			item["engname"] = j["engname"] 
			item["tradetype"] = j["tradetype"] 
			item["lasttrade"] = j["lasttrade"] 
			item["prevclose"] = j["prevclose"] 
			item["open"] = j["open"] 
			item["high"] = j["high"] 
			item["low"] = j["low"]
			item["volume"] = j["volume"]
			item["amount"] = j["amount"]  
			item["low"] = j["low"] 
			item["currentvolume"] = j["currentvolume"] 
			item["buy"] = j["buy"] 
			item["sell"] = j["sell"]
			item["high_52week"] = j["high_52week"] 
			item["low_52week"] = j["low_52week"]
			item["eps"] = j["eps"]
			item["dividend"] = j["dividend"]
			item["stocks_sum"] = j["stocks_sum"]
			item["pricechange"] = j["pricechange"]
			item["changepercent"] = j["changepercent"]
			item["ticktime"] = datetime.datetime.strptime(j["ticktime"],'%Y-%m-%d %H:%M:%S')

			yield item
