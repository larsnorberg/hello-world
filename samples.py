# samples.py

# attach database
import sqlite3
con = sqlite3.connect('example.db')
con_ex = sqlite3.connect('grampsLN.db')
cur = con.cursor()
attachDatabaseSQL = "ATTACH DATABASE ? AS gramps_ex"
dbSpec  = ("grampsLN.db",)
cur.execute(attachDatabaseSQL,dbSpec)
for person_db in cur.execute("SELECT * FROM gramps_ex.person_ex"):
    print(person_db)

# empty tuple
empty_tuple = tuple()
print(empty_tuple, type(empty_tuple))

# add dictionary to tuple
my_tuple_1 = (7, 8, 0, 3, 45, 3, 2, 22, 4)

print ("The tuple is : " )
print(my_tuple_1)

my_dict = {"Hey" : 11, "there" : 31, "Jane" : 23}

print("The dictionary is : ")
print(my_dict)

my_tuple_1 = list(my_tuple_1)
my_tuple_1.append(my_dict)
my_tuple_1 = tuple(my_tuple_1)

print("The tuple after adding the dictionary elements is : ")
print(my_tuple_1)