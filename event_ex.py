# event_ex.py

import datetime
import pickle
import sqlite3
from utility_cls import print_collection
from utility_cls import gramps_dateCls
from meta_data import event_types

msg = "\nExecution of event_revEng started: "
print(msg)

class eventCls: # class to handle event data and extension table
    def __init__(self, tuple): # tuple is the tuple returned from unpickle blob_data in event table
        self.change = datetime.datetime.fromtimestamp(tuple[10]).strftime('%Y-%m-%d %H:%M:%S')
        self.date_str = tuple[3][4] if tuple[3] != None else ''
        self.description = tuple[4]
        self.event_type = event_types[tuple[2][0]] if len(event_types) > tuple[2][0] else str(tuple[2][0])
        self.gramps_id = tuple[1]
        self.handle = tuple[0]
        self.place_handle = tuple[5]
        self.private = tuple[12]       
    def __str__(self):
        return f"{self.event_type} {self.description} {self.date_str} {self.gramps_id} place:{self.place_handle}"
    sql_insert_txt = "INSERT INTO event_ex (handle, gramps_id, date, description, place_handle, change, private) values (?,?,?,?,?,?,?)"
    def exec_insert(self, cursor):
        private = 1 if self.private else 0
        exec_result = cursor.execute (self.sql_insert_txt, (self.handle, self.gramps_id, self.date_str, self.description, self.place_handle, self.change, private))
        return exec_result
# end eventCls

#*** start main ***
con = sqlite3.connect('example.db')
cur = con.cursor()
con_ex = sqlite3.connect('grampsLN.db')
cur_ex = con_ex.cursor()
for row in cur.execute("SELECT handle, blob_data, description FROM event"):
    p = pickle.loads((row[1]))
    # print("type(p):", type(p)) 
    # print_collection(p)
    event = eventCls(p)
    print(event)
    result = event.exec_insert(cur_ex)
con_ex.commit()
cur_ex.close()
con_ex.close()
cur.close()
con.close()