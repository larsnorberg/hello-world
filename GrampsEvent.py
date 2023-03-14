# grampsEvent.py
import datetime
import pickle
import sqlite3
import MetaData

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
   LEFT JOIN place on event.place = place.handle WHERE event.description IS NOT '' LIMIT 100
"""
recordset = curEx.execute(sql)
print("type(recordset):", type(recordset))
for eventRow in recordset:
    print ("type of eventRow is:", type(eventRow))
    event = pickle.loads((eventRow[0]))
    print('gid:',eventRow[1], end=', ') # gramps.id
    print('description:',eventRow[2], end=', ') # event.description
    print('Handle:',eventRow[3], end=', ') # Person.Handle
    print('given_name:', eventRow[4],end=', ') # person.given_name
    print('surname:', eventRow[5],end=', ') # person.surname
    print("place:", eventRow[6],end=', ') # place.title
    print("eventID:", event[1],end=', ') # eventID
    print("eventType:", event[2],end=', ') # eventType 12=födelse, 13=död
    # print(event[3]) # datum tuple
    d = event[3] # event.date
    if d is not None:
      print(d[3])