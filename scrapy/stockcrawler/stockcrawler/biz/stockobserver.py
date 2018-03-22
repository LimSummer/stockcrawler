# -*- coding: utf-8 -*-
import codecs
import json
import sqlite3
import configparser,os
class StockObs(object):
    def refreshAllStocks(self,file):
        cf = configparser.ConfigParser()
        cf.read(os.path.join(os.path.join(os.path.join(os.path.dirname(os.getcwd()),'stockcrawler'),'stockcrawler'),'globalconfig.ini'))
        print('-------------------')
        print(os.path.join(os.path.join(os.path.join(os.path.dirname(os.getcwd()),'stockcrawler'),'stockcrawler'),'globalconfig.ini'))
        dbname = cf.get('database','stockinfo')
        localpath = cf.get('base','localpath')
        dbsource = os.path.join(localpath,dbname)
        conn = sqlite3.connect(dbsource)
        insertformat = 'insert into STOCK_INFO (stockid,stockname,stocktype) VALUES (?,?,?)'
        delfomat = 'delete from STOCK_INFO WHERE stockid=?'
        params = []
        delparams = []
        with open(file,mode='r',encoding='utf-8') as f:
            for line in f:
                item = json.loads(line)
                delparams.append((item['stockid'],))
                params.append((item['stockid'],item['stockname'],item['stocktype']))
        c = conn.cursor()
        c.executemany(delfomat,delparams)
        c.executemany(insertformat, params)
        conn.commit()
        conn.close()


