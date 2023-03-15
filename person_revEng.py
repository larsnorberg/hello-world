import pickle
import sqlite3
import datetime

msg = "Execution started"
print(msg)

class PersonCls:
    def __init__(self, person_tuple):
        self.handle = person_tuple[0]
        self.given_name = person_tuple[3][4]
        self.name_list = person_tuple[3][5]
        self.change = datetime.datetime.fromtimestamp(person_tuple[17])
        self.change_str = self.change.strftime('%Y-%m-%d %H:%M:%S')

con = sqlite3.connect('example.db')
con_ex = sqlite3.connect('grampsLN.db')
cur = con.cursor()
cur_ex = con_ex.cursor()
cur_ex.execute("DROP TABLE IF EXISTS person_ex")
cur_ex.execute("CREATE TABLE person_ex (Handle VARCHAR(50) PRIMARY KEY NOT NULL, given_name TEXT)")

for row in cur.execute("SELECT handle, blob_data FROM person WHERE gramps_id ='I0015' "):
    p = pickle.loads((row[1]))
    print("type(p):", type(p)) 

# ColIndex 0=handle 1=identity 2= 3=Name mm(tuple) 17=change
# ColIndex 3 Name mm (4=given_name 5=[surname mm] 6=title 7=(gender) 8=tilltalsnamn
    colIndex=0
    for col in p:
        print(col,colIndex)
        colIndex += 1
    
    person = PersonCls(p)
    record = (row[0],p[3][4])
    cur_ex.execute("INSERT INTO person_ex (handle, given_name) values (?,?)", (person.handle,person.given_name))

con_ex.commit()
result = cur_ex.execute("SELECT * FROM person_ex")
print(result)
print("Execution finished")
