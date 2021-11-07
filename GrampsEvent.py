# grampsEvent.py
import datetime
import pickle
import sqlite3
msg = "Execution started"
print(msg)
conEx = sqlite3.connect('example.db')
conLn = sqlite3.connect('grampsLN.db')
curEx = conEx.cursor()
sql="""
   SELECT event.blob_data,event.gramps_id,event.description,person.Handle,person.given_name,person.surname 
   FROM event
   JOIN reference ON event.handle = reference.ref_handle
   JOIN person ON reference.obj_handle = person.handle
"""
for eventRow in curEx.execute(sql):
    event = pickle.loads((eventRow[0]))
    print(event[1]) # eventID
    print(event[2]) # eventType 12=födelse, 13=död
    print(event[3]) # datum tuple
    d = event[3]
    print(d[3])
    print(event[4]) # description
    print(event[5]) # place.handle ?