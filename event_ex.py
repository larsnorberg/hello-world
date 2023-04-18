# event_ex.py

## todo:

import datetime
import pickle
import sqlite3
from utility_cls import print_collection
from utility_cls import gramps_dateCls
from meta_data import event_type

msg = "\nExecution of event_revEng started: "
print(msg)

source_list = [
    {'source_app': 8, 'app_name': 'Malmön2', 'db_source_uri': 'file:///C:/Users/larsn/Google%20Drive/grampsdb/60671bde/sqlite.db?mode=ro'}, # Malmön2
]

class Event: # class to handle event data and extension table
    def __init__(self, tuple): # tuple is the tuple returned from unpickle blob_data in event table
        self.change = tuple[10]
        self.change_str = datetime.datetime.fromtimestamp(tuple[10]).strftime('%Y-%m-%d %H:%M:%S')
        # date processing
        self.date_str = ''
        if(tuple[3]):
            try:
                self.date_str = datetime.date(year=tuple[3][3][2],month=tuple[3][3][1],day=tuple[3][3][0]).isoformat()
            except:
                self.date_str = tuple[3][4] ### if tuple[3] != None else ''
            ### if (len(self.date_str)==8): self.date_str = self.date_str[:4] + '-' + self.date_str[4:6] + '-' + self.date_str[6:]
        self.description = tuple[4]
        self.event_code = tuple[2][0]
        self.event_type = event_type(tuple[2][0]) ### if len(event_types) > tuple[2][0] else str(tuple[2][0])
        self.gramps_id = tuple[1]
        self.handle = tuple[0]
        self.place_handle = tuple[5] if tuple[5] != None else ''
        self.private = tuple[12]
    def __str__(self):
        return f"{self.event_type} {self.description} {self.date_str} {self.gramps_id} place:{self.place_handle}"
    ### sql_insert_txt = "INSERT INTO event_ex (handle, gramps_id, date, event_type, description, place_title, change, private, obj_handle, obj_class) values (?,?,?,?,?,?,?,?,?,?)"
    sql_insert_txt = """INSERT INTO persons_event (handle, gramps_id, date, event_type
        , description, place_title, change, private, obj_handle, obj_class, event_code, source_app) values (?,?,?,?,?,?,?,?,?,?,?,?)"""
    def exec_insert(self, con, place_title, obj_handle, obj_class):
        exec_result = con.execute (self.sql_insert_txt, (self.handle, self.gramps_id, self.date_str, self.event_type, self.description, \
                                                         place_title, self.change, self.private, obj_handle, obj_class, self.event_code, source['source_app'])) 
        return exec_result
# end Event


#*** start main ***
### con_ex = sqlite3.connect('grampsLN.db')
con_ex = sqlite3.connect('C:\\Users\\larsn\\GitHub\\my-django\\my_gramps\\db.sqlite3')
for source in source_list:
    source_con = sqlite3.connect(source['db_source_uri'], uri=True)
    source_con.row_factory = sqlite3.Row # use row_faktory

    for row in source_con.execute("""SELECT event.handle, event.blob_data, place.title, r.obj_handle, r.obj_class 
            FROM event LEFT JOIN place ON event.place = place.handle
            JOIN reference AS r ON r.ref_handle = event.handle"""):
        print_collection(pickle.loads(row[1])) # for debugging
        event = Event(pickle.loads(row[1]))
        print(event)
        result = event.exec_insert(con_ex, row[2], row[3], row[4])
    con_ex.commit()
    source_con.close()
con_ex.close() 