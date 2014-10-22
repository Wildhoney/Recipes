import os

# Service Configuration
SERVER_NAME = "localhost:%d" % int(os.environ["PORT"])

# Mongo Configuration
MONGO_HOST = os.environ["MONGOHQ_HOST"]
MONGO_PORT = os.environ["MONGOHQ_PORT"]
MONGO_USERNAME = os.environ["MONGOHQ_USER"]
MONGO_PASSWORD = os.environ["MONGOHQ_PASS"]
MONGO_DBNAME = os.environ["MONGOHQ_DBNAME"]

# API Configuration
DOMAIN = {'people': {}}