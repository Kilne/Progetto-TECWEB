import pprint

from MONGOUTILS.GettingUserDB import user_db


def get_projects():
    user_collection = user_db().UserTest
    pprint.pprint(user_collection.find_one())
