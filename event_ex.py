# event_ex.py

## todo: utöka event_ex med platsinformation

import datetime
import pickle
import sqlite3
from utility_cls import print_collection
from utility_cls import gramps_dateCls
from meta_data import event_types

msg = "\nExecution of event_revEng started: "
print(msg)

class event_cls: # class to handle event data and extension table
    def __init__(self, tuple): # tuple is the tuple returned from unpickle blob_data in event table
        self.change = tuple[10]
        self.change_str = datetime.datetime.fromtimestamp(tuple[10]).strftime('%Y-%m-%d %H:%M:%S')
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
    def exec_insert(self, con):
        exec_result = con.execute (self.sql_insert_txt, (self.handle, self.gramps_id, self.date_str, self.description, self.place_handle, self.change, self.private))
        return exec_result
# end event_cls

#*** start main ***
con = sqlite3.connect('file:sqlite.db?mode=ro', uri=True)
con.row_factory = sqlite3.Row # use row_faktory
con_ex = sqlite3.connect('grampsLN.db')
for row in con.execute("SELECT handle, blob_data, description FROM event"):
    p = pickle.loads((row[1]))
    # print("type(p):", type(p)) 
    # print_collection(p)
    event = event_cls(p)
    print(event)
    result = event.exec_insert(con_ex)
con_ex.commit()
con_ex.close()
con.close()