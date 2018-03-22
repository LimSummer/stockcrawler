import scrapy
import json 
from stockcrawler.items import StockItem
class Allstocks(scrapy.Spider):
    name = 'AllStocks'
    start_urls = ['http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx/JS.aspx?type=ct&st=(FFRank)&sr=1&p=1&ps=3500&js=var%20mozselQI={pages:(pc),data:[(x)]}&token=894050c76af8597a853f5b408b759f5d&cmd=C._AB&sty=DCFFITAM&rt=49461817']

    def parse(self, response):
        # follow links to author pages
        text = response.text
        text = text[text.find('['):-1]
        allstocks = json.loads(text)
        self.log('allstocks',len(allstocks))
        for stock in allstocks:
            items_stock = stock.split(',')
            stockitem = StockItem(stocktype=items_stock[13],stockid=items_stock[1],stockname=items_stock[2])
            yield stockitem
    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()

        yield {
            'name': extract_with_css('h3.author-title::text'),
            'birthdate': extract_with_css('.author-born-date::text'),
            #'bio': extract_with_css('.author-description::text'),
        }