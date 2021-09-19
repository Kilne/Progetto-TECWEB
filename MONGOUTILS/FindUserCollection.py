from MONGOUTILS.GettingUserDB import user_db


def get_collection_list():
    user_collection_list = user_db()

    print(user_collection_list.list_collection_names())

    # @TODO: continuare a lavorare sulle funzioni json e retrieve data
