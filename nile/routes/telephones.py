from flask import request, jsonify
# from __init__.py file import app - for routes (@app.route)
from nile import app
from nile.models.customer import *
from nile.models.telephone import *

############# Telephones #############
# Add a new telephone number
@app.route('/telephone', methods=['POST'])
def add_telephone():
    try:
        fk_customer_id = request.json['fk_customer_id']
        telephone_number = request.json['telephone_number']
        
        # find customer in the database by id
        # object is needed in order to save via sqlalchemy
        customer = Customer.query.filter_by(id=fk_customer_id).first()

        new_telephone = Telephone(telephone_number, fk_customer_id, customer)

        db.session.add(new_telephone)
        db.session.commit()

        return telephone_schema.jsonify(new_telephone)
    except Exception as e:
        print(f"******* Error in routes/telephones.py: add_telephone() *******")
        print(f"Error: {e}")
        return jsonify("Cannot add telephone!"), 500

# # Get all telephones
# @app.route('/telephone', methods=['GET'])
# def get_telephones():
#     try:
#         all_telephones = telephone.query.all()
#         result = telephones_schema.dump(all_telephones)
#         return jsonify(result)
#     except Exception as e:
#         print(f"******* Error in routes/telephones.py: get_telephones() *******")
#         print(f"Error: {e}")
#         return jsonify("Cannot get telephones!"), 500

# # Get one telephone
# @app.route('/telephone/<id>', methods=['GET'])
# def get_telephone(id):
#     try:
#         telephone = telephone.query.get(id)
#         return telephone_schema.jsonify(telephone)
#     except Exception as e:
#         print(f"******* Error in routes/telephones.py: get_telephone(id) *******")
#         print(f"Error: {e}")
#         return jsonify("Cannot get telephone!"), 500

# # Update a telephone
# @app.route('/telephone/<id>', methods=['PUT'])
# def update_telephone(id):
#     try:
#         delivery_address = request.json['delivery_address']
#         status = request.json['status']
#         fk_customer_id = request.json['fk_customer_id']
#         productsIdArray = request.json['productsIdArray']
        
#         # find customer in the database by id
#         customer = Customer.query.filter_by(id=fk_customer_id).first()

#         # find products in the database by id
#         products = []
#         for product_id in productsIdArray:
#             product = Product.query.filter_by(id=product_id).first()
#             products.append(product)

#         telephone = telephone.query.get(id)
#         telephone.delivery_address = delivery_address
#         telephone.status = status
#         telephone.fk_customer_id = fk_customer_id
#         telephone.customer = customer
#         telephone.products = products

#         db.session.commit()

#         return telephone_schema.jsonify(telephone)
#     except Exception as e:
#         print(f"******* Error in routes/telephones.py: update_telephone(id) *******")
#         print(f"Error: {e}")
#         return jsonify("Cannot update product!"), 500

# # Delete telephone
# @app.route('/telephone/<id>', methods=['DELETE'])
# def delete_telephone(id):
#     try:
#         telephone = telephone.query.get(id)
#         db.session.delete(telephone)
#         db.session.commit()

#         return telephone_schema.jsonify(telephone)
#     except Exception as e:
#         print(f"******* Error in routes/telephones.py: delete_telephone(id) *******")
#         print(f"Error: {e}")
#         return jsonify("Cannot delete telephone!"), 500