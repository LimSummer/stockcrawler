#coding=utf-8
import tushare as ts
import csv,time,codecs,getopt,sys
from datetime import datetime
from datetime import timedelta

def getOptvalue(opt,name):
    for opt, arg in opts:
        if opt == name:
            return arg
def getBeforeData(code,cur_datetime):
    r = 0
    while r == 0:
        delta = timedelta(days=-1)
        yestoday_datetime = cur_datetime + delta
        yestoday_str = yestoday_datetime.strftime('%Y-%m-%d')
        df_yestoday = ts.get_k_data(sid,start=yestoday_str,end=yestoday_str)
        r = df_yestoday.code.count()
        if r != 0:
            return df_yestoday
        cur_datetime = yestoday_datetime
#python main.py -s 603611 -d 2018-04-09
if __name__ == "__main__":
    opts, args = getopt.getopt(sys.argv[1:],"s:d:",["sid=","date="])
    sid = getOptvalue(opts,'-s')
    date = getOptvalue(opts,'-d')
    cur_datetime = datetime.strptime(date, '%Y-%m-%d')
    df_yestoday = getBeforeData(sid,cur_datetime)
    print(df_yestoday)
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
    suList = []
    for data in all_datas:
        dtstr = date + ' ' + data[1]
        dt = datetime.strptime(dtstr, "%Y-%m-%d %H:%M:%S")
        price = float(data[2])
        if predatetime is not None:
            ndt = dt - predatetime
        if prePrice == 0:
            dis = 0
        else:
            dis = round(price - prePrice,2)
        if dis >= 0:
            suList.append(data)
        else:
            print('------------------------')
            for item in suList:
                print(item)
            suList = []   
        data.append(dis) 
        per = round(dis / close_yestoday * 100,2)
        data.append(per)
        predatetime = dt
        prePrice = price
        #print(data)
        #timestamp = time.mktime(data[1])
        #print(timestamp)
    