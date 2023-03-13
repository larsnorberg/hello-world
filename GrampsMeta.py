# GrampsMeta.py
import datetime
import pickle
import sqlite3
msg = "Execution started"
print(msg)
conEx = sqlite3.connect('example.db')
curEx = conEx.cursor()
sql="""
   SELECT setting,value FROM metadata WHERE setting = 'event_names'
"""
rows = curEx.execute(sql)
for Row in rows:
    # event = pickle.loads((Row[1]))
    event = Row[1]
    unpackedEvent = pickle.loads(event)
    print (type(event), event, unpackedEvent)
    for e in event:
        print(type(e),e)
print("Execution finished")