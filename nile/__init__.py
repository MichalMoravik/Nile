from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import pymongo

app = Flask(__name__)

############# MongoDB DATABASE SETUP #############
try: 
    # mongo_uri = "mongodb://localhost:27017/nile"
    # mongoDB = pymongo.MongoClient(mongo_uri)
    mongo = pymongo.MongoClient(
        host="localhost",
        port=27017,  # default mongoDB port 
        serverSelectionTimeoutMS=1000  
    )
    mongoDB = mongo.nile
    mongo.server_info()  # triggers exception if cannot connect to DB
except:
    print(f"******* Error in __init__.py: Cannot establish MongoDB connection *******")

############# MySQL DATABASE SETUP #############
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:8889/Nile'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

############# MySQL INIT #############
try:
    db = SQLAlchemy(app)
    ma = Marshmallow(app)
except Exception as e:
    print(f"******* Error in __init__.py: Cannot establish MySQL connection *******")
    print(e)
    
############# END #############
# by importing routes after the app is initialized, circular import error are avoided
from nile.routes import customers, telephones, orders