import os

if os.environ.get('HOST'):

    # Service Configuration
    SERVER_NAME = os.environ.get('HOST')

# Mongo Configuration
MONGO_HOST = os.environ.get('MONGOHQ_HOST', 'lennon.mongohq.com')
MONGO_PORT = int(os.environ.get('MONGOHQ_PORT', 10042))
MONGO_USERNAME = os.environ.get('MONGOHQ_USER', 'heroku')
MONGO_PASSWORD = os.environ.get('MONGOHQ_PASS', '6x-3Jj1DA01q9RkFdM7SazZmahEkqaO1YG_jjTgIm6ZAck3N-Aa6f19uZeZvT8t41Fk_lzGSWZUEwEJOnsltDA')
MONGO_DBNAME = os.environ.get('MONGOHQ_DBNAME', 'app30926695')

# Schema Details
schema_recipes = {

    'name': {
        'type': 'string',
        'minlength': 3,
        'maxlength': 32,
        'required': True,
        'unique': True
    },
    'ingredients': {
        'type': 'list',
        'required': True
    }

}

recipes = {
    'schema': schema_recipes,
    'resource_methods': ['GET', 'POST'],
    'item_methods': ['GET', 'DELETE']
}

# API Configuration
DOMAIN    = {'recipes': recipes}
X_DOMAINS = '*'