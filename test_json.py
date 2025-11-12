import json
import sqlite3

print("execution started\n")
db_source_uri = 'file:///C:/Users/larsn/Google%20Drive/gramps6/6914604a/sqlite.db?mode=ro' 

con = sqlite3.connect(db_source_uri, uri=True)
con.row_factory = sqlite3.Row

sql="""
   SELECT * FROM person
"""
res = con.execute(sql)
person = res.fetchone()
print(person.keys())
### print(person["json_data"])
person_dict =json.loads(person["json_data"])
for column in person_dict:
    ###print(column,person_dict[column], type(person_dict[column]))
    ...
con.close()
print('execution ended')