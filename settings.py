import os

# Service Configuration
SERVER_NAME = "0.0.0.0:%d" % int(os.environ["PORT"])

# Mongo Configuration
MONGO_HOST = os.environ.get("MONGOHQ_HOST", "localhost")
MONGO_PORT = os.environ.get("MONGOHQ_PORT", 27017)
MONGO_USERNAME = os.environ.get("MONGOHQ_USER", "user")
MONGO_PASSWORD = os.environ.get("MONGOHQ_PASS", "pass")
MONGO_DBNAME = os.environ.get("MONGOHQ_DBNAME", "recipe")

# API Configuration
DOMAIN = {'people': {}}