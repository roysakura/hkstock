# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from hkstock.models import db_connect,create_deals_table,Stock
from hkstock.items import StockItem

class StockPipeline(object):
	"""Livingsocial pipeline for storing scraped items in the database"""
	def __init__(self):
		engine = db_connect()
		create_deals_table(engine)
		self.Session = sessionmaker(bind=engine)

	def process_item(self, item, spider):
		session = self.Session()
		data = Stock(**item)
		
		try:
			session.add(data)
			session.commit()
		except:
			session.rollback()
			raise
		finally:
			session.close()

		return item
