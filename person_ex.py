# person_ex.py

# todo: lägg till all surnames

import pickle
import sqlite3
import datetime
from utility import print_collection

print("\nExecution of person_ex started")

db_source_uri = 'file:///C:/Users/larsn/Google%20Drive/grampsdb/5ed79042/sqlite.db?mode=ro' # Lars Norberg övning

class person_cls:
    def __init__(self, person):
        # ColIndex 0=handle 1=identity 2= 3=Name mm(tuple) 17=change
        # ColIndex 3 Name mm (4=given_name 5=[surname mm] 6=title 7=(gender) 8=tilltalsnamn
        self.handle = person[0]
        self.gramps_id = person[1]
        gender = ('kvinna','man','okänt')
        self.gender = gender[person[2]]
        self.given_name_all = person[3][4]
        self.given_name = person[3][12]
        self.nickname = person[3][13]
        self.surname = person[3][5][0][0]
        self.surname_list = person[3][5]
        self.title = person[3][7].lower()
        self.change = person[17]
        self.change_str = datetime.datetime.fromtimestamp(person[17]).strftime('%Y-%m-%d %H:%M:%S')
        self.private = person[19]
        self.gender_code = person[2]
    def __str__(self):
        return f"{self.handle} {self.gramps_id} {self.surname} {self.given_name_all if self.given_name == '' else self.given_name} {self.title} {self.private}"
    sql_insert_txt = "REPLACE INTO base_person (handle, gramps_id, gender, given_name, surname, title, change, private, given_name_all, gender_code, nickname) values (?,?,?,?,?,?,?,?,?,?,?)"
    def exec_insert(self, con):
        given_name = self.given_name if self.given_name != '' else self.given_name_all
        exec_result = con.execute (self.sql_insert_txt, (self.handle, self.gramps_id, self.gender, given_name, self.surname \
                                                         , self.title, self.change, self.private, self.given_name_all, self.gender_code, self.nickname))
        return exec_result

def create_table(con):
    con.execute("DROP TABLE IF EXISTS person_ex")
    con.execute("CREATE TABLE person_ex (Handle VARCHAR(50) PRIMARY KEY NOT NULL, gramps_id TEXT, gender TEXT, given_name TEXT, surname TEXT, title TEXT, private INTEGER)")

### main
source_con = sqlite3.connect(db_source_uri, uri=True)
con_ex = sqlite3.connect('C:\\Users\\larsn\\source\\django\\db.sqlite3')

for row in source_con.execute("""SELECT handle, blob_data FROM person """):
    person = person_cls(pickle.loads(row[1]))
    print(person)
    print(pickle.loads(row[1]))
    result = person.exec_insert(con_ex)

con_ex.commit()

result = con_ex.execute("SELECT * FROM base_person")
print(result)
source_con.close()
con_ex.close()
print("Execution finished")
