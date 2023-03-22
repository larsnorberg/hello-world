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
        self.change = tuple[12]
    def __str__(self):
        return f"{self.handle} {self.gramps_id} private:{self.private}"
    sql_insert_txt = "INSERT INTO family_ex (handle, gramps_id, family_type, private, change) values (?,?,?,?,?)"
    def exec_insert(self, cursor):
        private = 1 if self.private else 0
        exec_result = cursor.execute (self.sql_insert_txt, (self.handle, self.gramps_id, self.private, self.change))
        return exec_result

con = sqlite3.connect('example.db')
cur = con.cursor()
for row in cur.execute("SELECT handle, blob_data FROM family LIMIT 10 "):
    family = familyCls(pickle.loads(row[1]))
    print(family)
    print("children_list:", family.children_list)

cur.close()
con.close()