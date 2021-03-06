# RESTful-API
Building REST API using Python and Flask. 

## Comparison between REST and RESTful API

**REST** (**RE**presentational **S**tate **T**ransfer) is basically an architectural style of development having some principles...

* It should be stateless

* It should access all the resources from the server using only URI

* It does not have inbuilt encryption

* It does not have session

* It uses one and only one protocol that is HTTP

* For performing CRUD operations, it should use HTTP verbs such as get, post, put and delete

* It should return the result only in the form of JSON or XML, atom, OData etc. (lightweight data )


**RESTFUL** services means it follows all the above principles.

**REST** is an "architectural style" that basically exploits the existing technology and protocols of the Web. 

**RESTful** is typically used to refer to web services implementing such an architecture.

#
### Directories
1. `venv`: Virtual Environment for this repository which runs on `Python 3.8`

2. `SQLAlchemy`: Contains the code that creates the Flask REST API with  SQLAlchemy.

#
### Dependencies
```pip install -r requirements.txt```

#

### Working with *curl* and *JSON* for rendering.

* Alternatively, one also use `Postman` app

```curl localhost:5000/``` : default is **GET** unless specified.

```curl -v localhost:5000/``` : for *verbose mode*

**NB** : With curl, you need to have two actively running terminals. 
- One for running the flask app ```flask run```. 
- Second terminal for the ```curl localhost:5000/```

* e.g. For the second REST API in the directory RESTFUL_vs_Vanilla_Flask
2nd terminal would look like this for the func `get_multiply10(num)` ```curl http://localhost:5000/multi/10``` to get (10*10)

* Post content: ```curl -H 'Content-Type: application/json' -X POST -d '{"name": "Steph", "password":"12345"}' http://localhost:5000/```

* Delete content: ```curl -X "DELETE" http://localhost:5000/```

* Update content: ```curl -X PUT -H "Content-Type: application/json" -d '{"key1":"value"}' "http://localhost:5000/"```

#
### Initiating the SQL database (SQLAlchemy)
- In the `Terminal`
1. ```python```
2. ```from vanilla_flask import db```
3. ```db.create_all()```
#
### Summary
* When using an extension like FLASK-RESTful, it simplifies code and code maintainability.
