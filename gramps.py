import pickle
import sqlite3
msg = "hello world"
print(msg)
con = sqlite3.connect('example.db')
cur = con.cursor()
for row in cur.execute("SELECT * FROM person WHERE gramps_id ='I0005' "):
    print(type(row[3]))
    p = pickle.loads((row[3]))
    print(type(p))
    print(p)
