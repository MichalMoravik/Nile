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
                    "message": f"Couldn't get order. Id: {id}",
                }
            ),
            status=500,
            mimetype="application/json"  
        )

# UPDATE ONE
@app.route("/order/<id>", methods=["PATCH"])
def update_order(id):
    try:
        body = request.get_json()

        data = {
            "deliveryAddress": body["deliveryAddress"],
            "deliveryPrice": body["deliveryPrice"],
            "products": body["products"]
        }

        order = mongoDB.orders.update_one(
            {"_id": ObjectId(id)},
            {"$set": data}
        )

        if order.modified_count == 1:
            return Response(
                response=json.dumps(  
                    {
                        "message": f"order updated. Id: {id}",
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
        print("******* Error in routes/orders.py: update_order(id) *******")
        print(ex)
        return Response(
            response=json.dumps(  
                {
                    "message": "Couldn't update order",
                }
            ),
            status=500,
            mimetype="application/json"  
        )

# DELETE
@app.route("/order/<id>", methods=["DELETE"])
def delete_order(id):  
    try:
        order = mongoDB.orders.delete_one({"_id": ObjectId(id)})

        if order.deleted_count == 1:
            return Response(
                response=json.dumps(  
                    {
                        "message": f"order deleted. Id: {id}"
                    }
                ),
                status=200,
                mimetype="application/json"  
            )

        return Response(
            response=json.dumps(  
                {
                    "message": f"order not found. Id: {id}"
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
                    "message": "Couldn't delete order",
                }
            ),
            status=500,
            mimetype="application/json"  
        )