from bson import ObjectId
from datetime import datetime


class DatabaseEntry:
    __p_id: str
    __name: str
    __objective: str
    __owner: str
    __time: datetime

    def __init__(self,
                 p_name: str,
                 p_obj: str,
                 p_owner: str,
                 p_date: datetime = datetime.now(),
                 entry_id: str = str(ObjectId())
                 ):
        self.__objective = p_obj
        self.__p_id = entry_id
        self.__name = p_name
        self.__owner = p_owner
        self.__time = p_date

    def show_me(self):
        print(self.__p_id)

# @TODO:finire la classe qui,
#   c'è un bel problema con le date, sarebbe il caso di demandare
#   nelle funzioni che gestiscono mongo e salvare in formato che
#   poi posso riformare
