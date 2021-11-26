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
   SELECT event.blob_data,event.gramps_id,event.description,person.Handle,person.given_name,person.surname,place.title  
   FROM event
   JOIN reference ON event.handle = reference.ref_handle
   JOIN person ON reference.obj_handle = person.handle
   LEFT JOIN place on event.place = place.handle
"""
for eventRow in curEx.execute(sql):
    event = pickle.loads((eventRow[0]))
    print(eventRow[1]) # gramps.id
    print(eventRow[2]) # event.description
    print(eventRow[3]) # Person.Handle
    print(eventRow[4]) # person.given_name
    print(eventRow[5]) # person.surname
    print(eventRow[6]) # place.title
    print(event[1]) # eventID
    print(event[2]) # eventType 12=födelse, 13=död
    print(event[3]) # datum tuple
    d = event[3] # event.date
    if d is not None:
      print(d[3])