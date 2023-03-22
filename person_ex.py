# person_ex.py

import pickle
import sqlite3
import datetime
from utility_cls import print_collection

print("\nExecution of person_ex started")

class person_cls:
    def __init__(self, person):
        # ColIndex 0=handle 1=identity 2= 3=Name mm(tuple) 17=change
        # ColIndex 3 Name mm (4=given_name 5=[surname mm] 6=title 7=(gender) 8=tilltalsnamn
        self.handle = person[0]
        self.gramps_id = person[1]
        gender = ('kvinna','man','okänt')
        self.gender = gender[person[2]]
        self.given_name_list = person[3][4]
        self.given_name = person[3][12]
        self.surname = person[3][5][0][0]
        self.surname_list = person[3][5]
        self.title = person[3][7].lower()
        self.change = datetime.datetime.fromtimestamp(person[17])
        self.change_str = self.change.strftime('%Y-%m-%d %H:%M:%S')
        self.private = person[19]
    def __str__(self):
        return f"{self.handle} {self.gramps_id} {self.surname} {self.given_name_list if self.given_name == '' else self.given_name} {self.title} {self.private}"
    sql_insert_txt = "INSERT INTO person_ex (handle, gramps_id, gender, given_name, surname, title, private) values (?,?,?,?,?,?,?)"
    def exec_insert(self, cursor):
        private = 1 if self.private else 0
        exec_result = cursor.execute (self.sql_insert_txt, (self.handle, self.gramps_id, self.gender, self.given_name, self.surname, self.title, private))
        return exec_result

def create_table(cur_ex):
    cur_ex.execute("DROP TABLE IF EXISTS person_ex")
    cur_ex.execute("CREATE TABLE person_ex (Handle VARCHAR(50) PRIMARY KEY NOT NULL, gramps_id TEXT, gender TEXT, given_name TEXT, surname TEXT, title TEXT, private INTEGER)")

### main
con = sqlite3.connect('example.db')
con_ex = sqlite3.connect('grampsLN.db')
cur = con.cursor()
cur_ex = con_ex.cursor()

for row in cur.execute("SELECT handle, blob_data FROM person LIMIT 100 "):
    person = person_cls(pickle.loads(row[1]))
    print(person)
    ## print(pickle.loads(row[1]))
    result = person.exec_insert(cur_ex)

con_ex.commit()
result = cur_ex.execute("SELECT * FROM person_ex")
print(result)
print("Execution finished")
