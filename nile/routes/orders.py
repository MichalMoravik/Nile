from flask import Response, request
from nile import mongoDB, app
import json
from bson.objectid import ObjectId  

############# Orders #############
# POST
@app.route("/order", methods=["POST"])
def create_order():
    try:
        body = request.get_json()

        order = {
            "deliveryAddress": body["deliveryAddress"],
            "deliveryPrice": body["deliveryPrice"],
            "products": body["products"]
        }

        dbResponse = mongoDB.orders.insert_one(order)

        return Response(
            response=json.dumps(  
                {
                    "message": "order created",
                    "id": f"{dbResponse.inserted_id}"
                }
            ),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        print("******* Error in routes/orders.py: create_order() *******")
        print(ex)
        return Response(
            response=json.dumps(  
                {
                    "message": "Couldn't create a new order",
                }
            ),
            status=500,
            mimetype="application/json"  
        )


# GET ALL
@app.route("/order", methods=["GET"])
def get_orders():
    try:
        data = list(mongoDB.orders.find())

        for user in data:
            user["_id"] = str(user["_id"])

        return Response(
            response=json.dumps(data),
            status=200,
            mimetype="application/json"  
        )
    except Exception as ex:
        print("******* Error in routes/orders.py: get_orders() *******")
        print(ex)
        return Response(
            response=json.dumps(  
                {
                    "message": "Couldn't get orders",
                }
            ),
            status=500,
            mimetype="application/json"  
        )

# GET ONE
@app.route("/order/<id>", methods=["GET"])
def get_order(id):
    try:
        order = mongoDB.orders.find_one({"_id": ObjectId(id)})
        order["_id"] = str(order["_id"])

        return Response(
            response=json.dumps(order),
            status=200,
            mimetype="application/json"  
        )
    except Exception as ex:
        print("******* Error in routes/orders.py: get_order(id) *******")
        print(ex)
        return Response(
            response=json.dumps(  
                {
                    "message": "Couldn't get order",
                }
            ),
            status=500,
            mimetype="application/json"  
        )