import os

DOMAIN = {'people': {}}

# Mongo Configuration
MONGO_HOST = os.environ["MONGOHQ_PATH"]
MONGO_PORT = 27017
MONGO_USERNAME = os.environ["MONGOHQ_USER"]
MONGO_PASSWORD = os.environ["MONGOHQ_PASS"]
MONGO_DBNAME = 'recipe'