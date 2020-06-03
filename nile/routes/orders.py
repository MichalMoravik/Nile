from flask import Response, request
from nile import mongoDB, app
import json

# POST
@app.route("/order", methods=["POST"])
def create_order():
    try:
        order = {
            "name": "testiiik",
            # "lastname": request.form["lastName"]
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