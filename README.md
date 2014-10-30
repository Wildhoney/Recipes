# Learn Recipes

Base Python API for a series of on-going *recipe learning* projects in various front-end frameworks.

## Flavours

* [React.js](https://github.com/Wildhoney/Recipes.React);
* [Ember.js](https://github.com/Wildhoney/Recipes.Ember);
* [Angular.js](https://github.com/Wildhoney/Recipes.Angular);
* [Meteor.js](https://github.com/Wildhoney/Recipes.Meteor);

## Getting Started

Initiate the [virtualenv](http://virtualenv.readthedocs.org/en/latest/) environment:

```shell
virtualenv env
source env/bin/activate
```

Once you have your virtual environment installed, you can use `pip` to install the dependencies:

```shell
pip install -r requirements.txt
```

Followed by the starting of the server on port `5000` &ndash; ensure that it is executable (with `chmod +x run_server.sh`):

```shell
./run_server.sh
```

Note that the base Python API uses MongoDB &ndash; it attempts to parse the environment variable `MONGOHQ_URL`, but failing that will attempt to connect to `localhost` on port `27017`. If you'd like to specify the MongoDB credentials then you can export the MONGOHQ_URL environment variable:

```shell
export MONGOHQ_URL=mongodb://myUsername:myPassword@myHost:myPort/myDBName
```

## API Endpoints

**Read:**

```shell
curl -i http://localhost:5000/recipes
     -X GET
```

**Create:**

```shell
curl -i http://localhost:5000/recipes
     -X POST
     -H "Content-Type: application/json"
     -d '{"name":"Banana Cake","description":"Delectable banana cake!","ingredients":["Banana","Flour"]}'
```

**Delete:**

Assume that **`123456789`** is the model's primary key in MongoDB.

```shell
curl -i http://localhost:5000/recipes/123456789
     -X DELETE
```