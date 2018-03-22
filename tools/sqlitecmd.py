#!/usr/bin/python
import sqlite3,sys
dbname,filename = sys.argv[1],sys.argv[2]
conn = sqlite3.connect(dbname)

print(filename)
f = open(filename,'r')
cmd = f.read()
c = conn.cursor()
c.execute(cmd)
conn.commit()
conn.close()
f.close()
