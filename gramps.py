import pickle
import sqlite3
msg = "Execution started"
print(msg)
con = sqlite3.connect('example.db')
conNew = sqlite3.connect('grampsLN.db')
cur = con.cursor()
curLN = conNew.cursor()

curLN.execute("CREATE TABLE IF NOT EXISTS person (Handle VARCHAR(50) PRIMARY KEY NOT NULL, given_name TEXT)")

for row in cur.execute("SELECT * FROM person WHERE gramps_id ='I0005' "):
    print(type(row[3]))
    p = pickle.loads((row[3]))
    print(type(p))
    print(p)
    curLN.execute("INSERT INTO person values (?,?)", (row[0], row[1]))

conNew.commit()
result = curLN.execute("SELECT * FROM person")
