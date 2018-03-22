# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import configparser,os
from stockcrawler.biz import stockobserver
class StockcrawlerPipeline(object):
    def __init__(self):
        cf = configparser.ConfigParser()
        curpath = os.path.dirname(os.path.realpath(__file__))
        cf.read(os.path.join(curpath,'globalconfig.ini'))
        localpath = cf.get('base','localpath')
        self.filepath = os.path.join(localpath,'stocks.json')
        self.file = codecs.open(self.filepath, 'w', encoding='utf-8')
    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(lines)
        return item

     # 处理结束后关闭 文件 IO 流
    def close_spider(self, spider):
        self.file.close()
        sto = stockobserver.StockObs()
        sto.refreshAllStocks(self.filepath)
