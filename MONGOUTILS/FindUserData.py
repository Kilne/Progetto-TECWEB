from pprint import pprint

from pymongo import MongoClient


def find_data(user):
    client_db = MongoClient("mongodb+srv://Luca:WliL3VbEqdbl5VAX@clusterprogetto.0ocor.mongodb.net/ClusterProgetto"
                            "?retryWrites=true&w=majority", ssl=True, ssl_cert_reqs='CERT_NONE')
    user_dbs = client_db.UserProjects

    pprint(user_dbs.list_collection_names())

    for coll_names in user_dbs.list_collection_names():
        if coll_names == user:
            user_coll = user_dbs[coll_names]
            pprint(user_coll.find_one())
            # @todo:ci siamo quasi vedere perchè il OBJECT ID di mongo non JSON serializzabile
            return user_coll.find_one()

    return "not found"
