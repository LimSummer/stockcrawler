# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
class StockcrawlerPipeline(object):
    def __init__(self):
        self.file = codecs.open('stocks.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(lines)
        return item

     # 处理结束后关闭 文件 IO 流
    def close_spider(self, spider):
        self.file.close()
