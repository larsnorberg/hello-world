# family_ex

import datetime
import pickle
import sqlite3
from utility_cls import print_collection
from utility_cls import gramps_dateCls
from meta_data import event_types

### To Do
# byt example.db till sqlite.db
# flytta child_parent_rel_text till classen child_family
# kolla och eventuellt ändra namn på klassen child_family

msg = "\nExecution of family_ex started: "
print(msg)

class familyCls:
    def __init__(self, tuple):
        self.handle = tuple[0]
        self.gramps_id = tuple[1]
        self.father_handle = tuple[2]
        self.mother_handle = tuple[3]
        self.children_list = tuple[4]
        self.private = tuple[14]
        self.change = tuple[12]
    def __str__(self):
        return f"{self.handle} {self.gramps_id} father:{self.father_handle} mother:{self.mother_handle} private:{self.private}"
    sql_insert_txt = "INSERT INTO family_ex (handle, gramps_id, family_type, private, change) values (?,?,?,?,?)"
    def exec_insert(self, cursor):
        private = 1 if self.private else 0
        exec_result = cursor.execute (self.sql_insert_txt, (self.handle, self.gramps_id, self.private, self.change))
        return exec_result

class child_family:
    def __init__(self, relation):
        self.child_handle = relation[3]
        self.private = relation[0]
        self.father_relation_code = relation[3][0]
        self.father_relation_text = child_parent_rel_text[relation[3][0]]
        self.mother_relation_code = relation[4][0]
        self.mother_relation_text = child_parent_rel_text[relation[4][0]]

# child parent relation
child_parent_rel_text = ('inget','födelse','adopterad','styvbarn','fadderbarn','fosterbarn','okänd')
        
con = sqlite3.connect('file:example.db?mode=ro', uri=True)
con.row_factory = sqlite3.Row # use row_faktory
for row in con.execute("SELECT handle, blob_data FROM family LIMIT 10 "):
    family = familyCls(pickle.loads(row['blob_data']))
    print(family)
    # print(pickle.loads(row['blob_data']))
    ## print("children_list:", family.children_list)
    for child in family.children_list:
        print(child)

con.close()
print ('Execution ended\n')