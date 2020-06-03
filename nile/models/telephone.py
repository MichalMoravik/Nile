# importing from __init__.py file
from nile import db, ma

############# Customer Class/Model #############
class Telephone(db.Model):
    __tablename__ = 'telephone_numbers'
    id = db.Column(db.Integer, primary_key=True)
    telephone_number = db.Column(db.String(20))

    # one-to-many relationship
    fk_customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    customer = db.relationship('Customer', backref=db.backref('telephone_numbers', lazy=True))

    def __init__(self, telephone_number, fk_customer_id, customer):
        self.telephone_number = telephone_number
        self.fk_customer_id = fk_customer_id
        self.customer = customer

class TelephoneSchema(ma.Schema):
    class Meta:
        fields = ('id', 'telephone_number', 'fk_customer_id')

telephone_schema = TelephoneSchema()
telephones_schema = TelephoneSchema(many=True)


