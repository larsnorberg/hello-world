# GrampsMeta.py
import datetime
import pickle
import sqlite3
msg = "Execution started"
print(msg)

con = sqlite3.connect('sqlite52.db') 
sql="""
   SELECT setting,value FROM metadata
"""
rows = con.execute(sql)
for Row in rows:
    try:
        print(f"setting: {Row[0]} value:{pickle.loads(Row[1])} type:{type(pickle.loads(Row[1]))}")
    except:
        print(f"setting {Row[0]} can not be unpickled")
con.close()
print("Execution finished")