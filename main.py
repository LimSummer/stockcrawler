#coding=utf-8
import tushare as ts
import csv,time,codecs
from datetime import datetime

if __name__ == "__main__":
    sid='603611'
    date='2018-04-04'
    df = ts.get_tick_data(sid,date=date)
    filename = sid + ".csv" 
    df.to_csv(filename)
    all_datas = []
    with codecs.open(filename,'r', 'utf-8') as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        print(headers)
        for row in f_csv:
            all_datas.insert(0,row)
    predatetime = None
    for data in all_datas:
        dtstr = date + ' ' + data[1]
        dt = datetime.strptime(dtstr, "%Y-%m-%d %H:%M:%S")
        if predatetime is not None:
            ndt = dt - predatetime
            print(ndt.seconds)
        predatetime = dt
        print(data)
        #timestamp = time.mktime(data[1])
        #print(timestamp)