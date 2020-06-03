from flask import request, jsonify
# from __init__.py file import app - for routes (@app.route)
from nile import app
from nile.models.customer import *

############# Customer #############
# Create a customer
@app.route('/customer', methods=['POST'])
def add_customer():
    try:
        first_name = request.json['first_name']
        last_name = request.json['last_name']
        email = request.json['email']

        new_customer = Customer(first_name, last_name, email)
        db.session.add(new_customer)
        db.session.commit()

        return customer_schema.jsonify(new_customer)
    except Exception as e:
        print(f"******* Error in routes/customers.py: add_customer() *******")
        print(f"Error: {e}")
        return jsonify("Cannot add customer!"), 500

# Get all customers
@app.route('/customer', methods=['GET'])
def get_customers():
    try:
        all_customers = Customer.query.all()
        result = customers_schema.dump(all_customers)
        return jsonify(result)
    except Exception as e:
        print(f"******* Error in routes/customers.py: get_customers() *******")
        print(f"Error: {e}")
        return jsonify("Cannot get customers!"), 500

# Get one customer
@app.route('/customer/<id>', methods=['GET'])
def get_customer(id):
    try:
        customer = Customer.query.get(id)
        return customer_schema.jsonify(customer)
    except Exception as e:
        print(f"******* Error in routes/customers.py: get_customer(id) *******")
        print(f"Error: {e}")
        return jsonify("Cannot get customer!"), 500

# Update a customer
@app.route('/customer/<id>', methods=['PUT'])
def update_customer(id):
    try:
        first_name = request.json['first_name']
        last_name = request.json['last_name']
        email = request.json['email']

        customer = Customer.query.get(id)
        customer.first_name = first_name
        customer.last_name = last_name
        customer.email = email

        db.session.commit()

        return customer_schema.jsonify(customer)
    except Exception as e:
        print(f"******* Error in routes/customers.py: update_customer(id) *******")
        print(f"Error: {e}")
        return jsonify("Cannot update customer!"), 500

# Delete customer
@app.route('/customer/<id>', methods=['DELETE'])
def delete_customer(id):
    try:
        customer = Customer.query.get(id)
        db.session.delete(customer)
        db.session.commit()

        return customer_schema.jsonify(customer)
    except Exception as e:
        print(f"******* Error in routes/customers.py: delete_customer(id) *******")
        print(f"Error: {e}")
        return jsonify("Cannot delete customer!"), 500
