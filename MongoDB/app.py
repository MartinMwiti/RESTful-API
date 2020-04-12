from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['SECRET_KEY'] = 'randomsecretkey'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/shadow'

mongo = PyMongo(app)

# Add user
@app.route('/user', methods=['POST'])
def add_user():
    _json = request.get_json()
    _name = _json['name']
    _email = _json['email']
    _password = _json['password']


    if _name and _email and _password and request.method == 'POST':
        _hashed_password = generate_password_hash(_password, method='sha256')

        data = mongo.db.user.insert({'name': _name, 'email': _email, 'password': _hashed_password})

        response = jsonify('User added successfully')
        response.status_code = 200

        return response

    else:
        return not_found()


# Find all users
@app.route('/users', methods=['GET'])
def users():
    users = mongo.db.user.find()
    response = dumps(users)

    return response 

# Find user by id
@app.route('/user/<id>', methods=['GET'])
def user(id):
    user = mongo.db.user.find_one({'_id': ObjectId(id)})
    response = dumps(user)

    return response

# Delete user by id
@app.route('/delete/<id>', methods=['DELETE'])
def delete_user(id):
    user = mongo.db.user.delete_one({'_id': ObjectId(id)})
    response = jsonify("User deleted successfully")

    response.status_code = 200

    return response


# Update user by id
@app.route('/update/<id>', methods=['PUT'])
def update_user(id):
    _id = id
    _json = request.get_json()
    _name = _json['name']
    _email = _json['email']
    _password = _json['password']

    if _name and _email and _password and request.method == 'PUT':
        _hashed_password = generate_password_hash(_password)

        data = mongo.db.user.update_one({'_id': ObjectId(id['$oid']) if '$oid' in _id else ObjectId(_id)}, {'$set':{'name': _name, 'email': _email, 'password': _hashed_password}})

        response = jsonify('User data updated successfully')
        response.status_code = 200
    else:
        return not_found()

    return response




@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found' + request.url
    }

    response = jsonify(message)

    response.status_code = 404

    return response




if __name__=="__main__":
    app.run(debug=True)
