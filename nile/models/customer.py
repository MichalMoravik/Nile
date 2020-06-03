# importing from __init__.py file
from nile import db, ma

############# Customer Class/Model #############
class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(35))
    last_name = db.Column(db.String(35))
    email = db.Column(db.String(255), unique=True)

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

class CustomerSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email')

customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)



