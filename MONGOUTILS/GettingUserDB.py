from MONGOUTILS.ConnectToDB import connect_mongo


def user_db():
    defined_user_database = connect_mongo().UserProjects
    return defined_user_database
