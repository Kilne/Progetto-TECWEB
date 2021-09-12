# MongoDB atlas connection client
from pymongo import MongoClient


def connect_mongo():
    client_db = MongoClient("mongodb+srv://Luca:WliL3VbEqdbl5VAX@clusterprogetto.0ocor.mongodb.net/ClusterProgetto"
                            "?retryWrites=true&w=majority", ssl=True, ssl_cert_reqs='CERT_NONE')
    return client_db
