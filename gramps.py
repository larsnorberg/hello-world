import pickle
import sqlite3
msg = "Execution started"
print(msg)
con = sqlite3.connect('example.db')
con_ex = sqlite3.connect('grampsLN.db')
cur = con.cursor()
cur_ex = con_ex.cursor()
cur_ex.execute("DROP TABLE IF EXISTS person_ex")
cur_ex.execute("CREATE TABLE person_ex (Handle VARCHAR(50) PRIMARY KEY NOT NULL, given_name TEXT)")

for row in cur.execute("SELECT handle, blob_data FROM person WHERE gramps_id ='I0005' "):
    p = pickle.loads((row[1]))
    print("type(p):", type(p)) 

    colIndex=0
    for col in p:
        print(col,colIndex)
        colIndex += 1
    record = (row[0],p[3][4])
    cur_ex.execute("INSERT INTO person_ex values (?,?)", record)

con_ex.commit()
result = cur_ex.execute("SELECT * FROM person_ex")
print(result)
print("Execution finished")