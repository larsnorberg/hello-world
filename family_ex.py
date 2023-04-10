# family_ex

import datetime
import pickle
import sqlite3
from utility_cls import print_collection
from utility_cls import gramps_dateCls
# from meta_data import event_types

### To Do
# lägg till sql insert till family_ex
# lägg till sql insert till child_family_ex

msg = "\nExecution of family_ex started: "
print(msg)

class familyCls:
    MARRIED = 0
    UNMARRIED = 1
    CIVIL_UNION = 2
    UNKNOWN = 3
    CUSTOM = 4
    family_type_tuple = ('gifta','ogifta','civil_union','okänd','partner')

    def __init__(self, tuple):
        self.handle = tuple[0]
        self.gramps_id = tuple[1]
        self.father_handle = tuple[2]
        self.mother_handle = tuple[3]
        self.family_type = self.family_type_tuple[tuple[5][0]]
        self.children_list = tuple[4]
        self.private = tuple[14]
        self.change = tuple[12]
    def __str__(self):
        return f"{self.handle} {self.gramps_id} father:{self.father_handle} mother:{self.mother_handle} {self.family_type} private:{self.private}"
    ### sql_insert_txt = "INSERT INTO family_ex (handle, gramps_id, father_handle, mother_handle, family_type, private, change) values (?,?,?,?,?,?,?)"
    sql_insert_txt = "INSERT INTO persons_family (handle, gramps_id, father_handle, mother_handle, family_type, private, change) values (?,?,?,?,?,?,?)"
    def exec_insert(self, cursor):
        exec_result = cursor.execute (self.sql_insert_txt, (self.handle, self.gramps_id, self.father_handle, self.mother_handle, self.family_type, self.private, self.change))
        return exec_result

class child_family_cls:
    def __init__(self, relation):
        self.child_handle = relation[3]
        self.private = relation[0]
        self.father_relation_code = relation[4][0]
        self.father_relation_text = self.child_parent_rel_text[self.father_relation_code]
        self.mother_relation_code = relation[5][0]
        self.mother_relation_text = self.child_parent_rel_text[self.mother_relation_code]
    # child parent relation
    child_parent_rel_text = ('inget','födelse','adopterad','styvbarn','fadderbarn','fosterbarn','okänd')
    def __str__(self):
        return f"{self.child_handle} fader relation:{self.father_relation_text} moder relation:{self.mother_relation_text} private:{self.private}"
    ### sql_insert_txt = "INSERT INTO family_child_ex (family_handle, child_handle, father_relation, mother_relation, change, private) values (?,?,?,?,?,?)"
    sql_insert_txt = "INSERT INTO persons_family_child (family_handle, child_handle, father_relation, mother_relation, change, private) values (?,?,?,?,?,?)"
    def exec_insert(self, con, family_handle, change):
        exec_result = con.execute (self.sql_insert_txt, (family_handle, self.child_handle, self.father_relation_text, self.mother_relation_text, change, self.private))
        return exec_result

### main ###
con = sqlite3.connect('file:sqlite.db?mode=ro', uri=True)
con.row_factory = sqlite3.Row # use row_faktory
### con_ex = sqlite3.connect('grampsLN.db')
con_ex = sqlite3.connect('C:\\Users\\larsn\\GitHub\\my-django\\my_gramps\\db.sqlite3')

for row in con.execute("SELECT handle, blob_data FROM family"):
    family = familyCls(pickle.loads(row['blob_data']))
    print(family)
    print(pickle.loads(row['blob_data']))
    ## print("children_list:", family.children_list)
    family.exec_insert(con_ex)
    for child in family.children_list:
        child_family = child_family_cls(child)
        print(child_family)
        child_family.exec_insert(con_ex, family.handle, family.change)

con_ex.commit()
con_ex.close()
con.close()
print ('Execution ended\n')