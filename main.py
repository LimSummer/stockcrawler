#coding=utf-8
import tushare as ts
import csv,time,codecs
from datetime import datetime
from datetime import timedelta
if __name__ == "__main__":
    sid='603611'
    date='2018-04-04'
    cur_datetime = datetime.strptime(date, '%Y-%m-%d')
    delta = timedelta(days=-1)
    yestoday_datetime = cur_datetime + delta
    yestoday_str = yestoday_datetime.strftime('%Y-%m-%d')
    df_yestoday = ts.get_k_data(sid,start=yestoday_str,end=yestoday_str)
    close_yestoday = float(df_yestoday.close)
    
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
    prePrice = 0
    dis = 0
    for data in all_datas:
        dtstr = date + ' ' + data[1]
        dt = datetime.strptime(dtstr, "%Y-%m-%d %H:%M:%S")
        price = float(data[2])
        if predatetime is not None:
            ndt = dt - predatetime
            print(ndt.seconds)
        if prePrice == 0:
            dis = 0
        else:
            dis = round(price - prePrice,2)   
        data.append(dis) 
        per = round(dis / close_yestoday * 100,2)
        data.append(per)
        predatetime = dt
        prePrice = price
        print(data)
        #timestamp = time.mktime(data[1])
        #print(timestamp)
    