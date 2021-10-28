# https://hackersandslackers.com/configure-flask-applications/
# https://flask.palletsprojects.com/en/2.0.x/config/
import datetime

ENV = 'development'
TESTING = True
SECRET_KEY = 'b4ca89e467ba903dfd9ce36402375cde6f8b03f6636fe291142eca7a56ca3e2d'
DATABASE_URI = "mongodb+srv://Luca:WliL3VbEqdbl5VAX@clusterprogetto.0ocor.mongodb.net/ClusterProgetto?retryWrites" \
               "=true&w=majority "
PERMANENT_SESSION_LIFETIME = datetime.timedelta(hours=1)
