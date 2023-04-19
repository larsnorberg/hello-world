# utility.py

class gramps_dateCls:
    def __init__(self, date_tuple):
        self.date = '1950-05-23'

# print all elements in collection
def print_collection(collection):
    index=0
    for element in collection:
        print(element, index)
        index += 1