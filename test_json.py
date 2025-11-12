import json
import sqlite3

db_source_uri = 'file:///C:/Users/larsn/Google%20Drive/gramps6/6914604a/sqlite.db?mode=ro' 

con = sqlite3.connect(db_source_uri, uri=True)
con.row_factory = sqlite3.Row

sql="""
   SELECT * FROM person
"""
res = con.execute(sql)
person = res.fetchone()
person.keys()
pass
con.close()