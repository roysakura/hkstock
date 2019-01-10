# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class StockItem(Item):
    symbol = Field()
    name = Field()
    engname = Field()
    tradetype = Field()
    lasttrade = Field()
    prevclose = Field()
    open = Field()
    high = Field()
    low = Field()
    volume = Field()
    currentvolume = Field()
    amount = Field()
    ticktime = Field()
    buy=Field()
    sell = Field()
    high_52week = Field()
    low_52week = Field()
    eps = Field()
    dividend = Field()
    stocks_sum = Field()
    pricechange = Field()
    changepercent = Field()
