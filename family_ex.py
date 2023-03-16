# family_ex

import datetime
import pickle
import sqlite3
from utility_cls import print_collection
from utility_cls import gramps_dateCls
from meta_data import event_types

msg = "\nExecution of family_ex started: "
print(msg)

class familyCls:
    def __init__(self, tuple):
        self.handle = tuple[0]
        self.gramps_id = tuple[1]
        self.children_list = tuple[4]
        self.private = tuple[14]
        change = datetime.datetime.fromtimestamp(tuple[12])
        self.change_str = change.strftime('%Y-%m-%d %H:%M:%S')
    def __str__(self):
        return f"{self.handle} {self.gramps_id} private:{self.private} {self.change_str}"

con = sqlite3.connect('example.db')
cur = con.cursor()
for row in cur.execute("SELECT handle, blob_data FROM family LIMIT 10 "):
    p = pickle.loads((row[1]))
    # print_collection(p)
    family = familyCls(p)
    print(family)
    print("family.children_list:", family.children_list)

cur.close()
con.close()