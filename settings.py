import os

if os.environ.get("PORT"):

    # Service Configuration
    SERVER_NAME = "%s:%s" % (os.environ.get("HOST"), os.environ.get("PORT"))

    # Mongo Configuration
    MONGO_HOST = os.environ.get("MONGOHQ_HOST")
    MONGO_PORT = int(os.environ.get("MONGOHQ_PORT"))
    MONGO_USERNAME = os.environ.get("MONGOHQ_USER")
    MONGO_PASSWORD = os.environ.get("MONGOHQ_PASS")
    MONGO_DBNAME = os.environ.get("MONGOHQ_DBNAME")

else:

    # Service Configuration
    SERVER_NAME = "0.0.0.0:3507"

    # Mongo Configuration
    MONGO_HOST = "localhost"
    MONGO_PORT = 27017
    MONGO_DBNAME = "recipe"


# API Configuration
DOMAIN = {'people': {}}
