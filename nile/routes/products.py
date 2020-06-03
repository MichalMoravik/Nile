from flask import Response, request
from nile import mongoDB, app
import json
from bson.objectid import ObjectId  

############# Products #############
# POST
@app.route("/product", methods=["POST"])
def create_product():
    try:
        body = request.get_json()

        product = {
            "name": body["name"],
            "description": body["description"],
            "price": body["price"]
        }

        product_response = mongoDB.products.insert_one(product)

        return Response(
            response=json.dumps(  
                {
                    "message": "product created",
                    "id": f"{product_response.inserted_id}"
                }
            ),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        print("******* Error in routes/products.py: create_product() *******")
        print(ex)
        return Response(
            response=json.dumps(  
                {
                    "message": "Couldn't create a new product",
                }
            ),
            status=500,
            mimetype="application/json"  
        )


# GET ALL
@app.route("/product", methods=["GET"])
def get_products():
    try:
        data = list(mongoDB.products.find())

        for product in data:
            product["_id"] = str(product["_id"])

        return Response(
            response=json.dumps(data),
            status=200,
            mimetype="application/json"  
        )
    except Exception as ex:
        print("******* Error in routes/products.py: get_products() *******")
        print(ex)
        return Response(
            response=json.dumps(  
                {
                    "message": "Couldn't get products",
                }
            ),
            status=500,
            mimetype="application/json"  
        )

# GET ONE
@app.route("/product/<id>", methods=["GET"])
def get_product(id):
    try:
        product = mongoDB.products.find_one({"_id": ObjectId(id)})
        product["_id"] = str(product["_id"])

        return Response(
            response=json.dumps(product),
            status=200,
            mimetype="application/json"  
        )
    except Exception as ex:
        print("******* Error in routes/products.py: get_product(id) *******")
        print(ex)
        return Response(
            response=json.dumps(  
                {
                    "message": f"Couldn't get product. Id: {id}",
                }
            ),
            status=500,
            mimetype="application/json"  
        )

# UPDATE ONE
@app.route("/product/<id>", methods=["PATCH"])
def update_product(id):
    try:
        body = request.get_json()

        data = {
            "name": body["name"],
            "description": body["description"],
            "price": body["price"]
        }

        product = mongoDB.products.update_one(
            {"_id": ObjectId(id)},
            {"$set": data}
        )

        if product.modified_count == 1:
            return Response(
                response=json.dumps(  
                    {
                        "message": f"product updated. Id: {id}",
                    }
                ),
                status=200,
                mimetype="application/json"  
            )
        return Response(
            response=json.dumps(  
                {
                    "message": f"nothing to update. Id: {id}",
                }
            ),
            status=200,
            mimetype="application/json"  
        )
    except Exception as ex:
        print("******* Error in routes/products.py: update_product(id) *******")
        print(ex)
        return Response(
            response=json.dumps(  
                {
                    "message": "Couldn't update product",
                }
            ),
            status=500,
            mimetype="application/json"  
        )

# DELETE
@app.route("/product/<id>", methods=["DELETE"])
def delete_product(id):  
    try:
        product = mongoDB.products.delete_one({"_id": ObjectId(id)})

        if product.deleted_count == 1:
            return Response(
                response=json.dumps(  
                    {
                        "message": f"product deleted. Id: {id}"
                    }
                ),
                status=200,
                mimetype="application/json"  
            )

        return Response(
            response=json.dumps(  
                {
                    "message": f"product not found. Id: {id}"
                }
            ),
            status=200,
            mimetype="application/json" 
        )

    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps(  
                {
                    "message": "Couldn't delete product",
                }
            ),
            status=500,
            mimetype="application/json"  
        )