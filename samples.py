# samples.py
### *** todo *** ###
## __init__.py , import from other file, check if classes have to be imported by class name
## import from other (sub)folder

# chass måste komma för en instance är skapad
# thisplace = place() här skulle ge ett error
class place:
    def __init__(self):
        self.data = "some data"
thisplace = place()
print(thisplace.data)

# path
import os
print(os.getcwd())
os.chdir("c:\\users\\larsn")
print (os.path.abspath(__file__))
print (os.path.realpath(__file__))
import pathlib
print(pathlib.Path(__file__).parents[0])

# import from file
from utility_cls import * # alla namn i en fil
print_collection((3,4))
d = gramps_dateCls((5,6))
print(d.date)

quit()

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

def print_tuple(tuple):
    colIndex=0
    for col in tuple:
        print(col,colIndex)
        colIndex += 1