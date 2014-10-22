import os

DOMAIN = {'people': {}}

# Mongo Configuration
MONGO_HOST = os.environ["MONGOHQ_HOST"]
MONGO_PORT = os.environ["MONGOHQ_PORT"]
MONGO_USERNAME = os.environ["MONGOHQ_USER"]
MONGO_PASSWORD = os.environ["MONGOHQ_PASS"]
MONGO_DBNAME = os.environ["MONGOHQ_DBNAME"]