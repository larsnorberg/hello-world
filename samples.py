# samples.py
### *** todo *** ###
## __init__.py , import from other file, check if classes have to be imported by class name
## import from other (sub)folder

# imports
import datetime
import os
import sqlite3
import pathlib
from utility import * # alla namn i en fil
import id

# path
def path_stuff():
    print('path före', os.getcwd())
    os.chdir("c:\\users\\larsn")
    print('path efter os.chdir', os.getcwd())
    print (os.path.abspath(__file__))
    print (os.path.realpath(__file__))
    print(pathlib.Path(__file__).parents[0])

# import from file utility.cls, see import section
def import_from_file():
    print_collection((3,4))
    d = gramps_dateCls((5,6))
    print(d.date)

# calculate age
def calculate_age(dob):
    today = datetime.date.today()
    age = today.year - dob.year -((today.month,today.day) < (dob.month, dob.day))
    return age

def tuple_stuff ():
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

# attach database
def attach_db():
    con = sqlite3.connect('example.db')
    con_ex = sqlite3.connect('grampsLN.db')
    cur_ex = con_ex.cursor()
    attachDatabaseSQL = "ATTACH DATABASE ? AS gramps"
    dbSpec  = ("example.db",)
    cur_ex.execute(attachDatabaseSQL,dbSpec)
    for person_db in cur_ex.execute("SELECT * FROM gramps.person LIMIT 10"):
        print(person_db)

##### __main __ ####
print ("\n\n")
id = id.create_id()
print(id)
# attach_db()
print( "age:", calculate_age(datetime.date(1950,3,20)))
## path_stuff()
print("finished!!")