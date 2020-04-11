from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'testdb.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)
api = Api(app)

# Product Class/Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(20), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)

    def __init__(self, customer, description, price, quantity):  # fields i want to input
        self.customer = customer
        self.description = description
        self.price = price
        self.quantity = quantity

# Product Schema
class ProductSchema(ma.Schema):
    class Meta:
        # fields i want to show.
        fields = ('id', 'customer', 'description', 'price', 'quantity')


# Init schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)


class Add_products(Resource):
    def post(self):
    
        data = request.get_json()
        customer = data['customer']
        description = data['description']
        price = data['price']
        quantity = data['quantity']

        new_product = Product(customer, description, price, quantity)
        db.session.add(new_product)
        db.session.commit()

        return product_schema.jsonify(new_product)


class Get_products(Resource):
    def get(self):
        all_products = Product.query.all()
        result = products_schema.dump(all_products)

        return products_schema.jsonify(result)


api.add_resource(Add_products, '/product')
api.add_resource(Get_products, '/product')


if __name__ == '__main__':
    app.run(debug=True)
