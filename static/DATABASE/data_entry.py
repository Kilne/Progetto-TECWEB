from bson import ObjectId


class DatabaseEntry:
    __x: str
    __name: str

    def __init__(self, p_name: str, entryid: str = str(ObjectId())):
        self.__x = entryid
        self.__name= p_name

    def show_me(self):
        print(self.__x)

# @TODO:finire la classe qui
