import uuid
from datetime import datetime
import secrets
import flask_marshmallow

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from flask_marshmallow import Marshmallow
from sqlalchemy import ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()
login_manager = LoginManager()
ma = Marshmallow()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key = True)
    first_name = db.Column(db.String(50), nullable = True, default = '')
    last_name = db.Column(db.String(50), nullable = True, default = '')
    email = db.Column(db.String(50), nullable = False)
    password = db.Column(db.String, nullable = True, default = '')
    g_auth_verify = db.Column(db.Boolean, default = False)
    token = db.Column(db.String, default = '', unique = True)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    car = db.relationship('Car', backref = 'owner', lazy = True)

    def __init__(self, email, first_name, last_name, id='', password='', token='', g_auth_verify=False):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.set_password(password)
        self.email = email
        self.token = self.set_token(24)
        self.g_auth_verify = g_auth_verify

    def set_id(self):
        return str(uuid.uuid4())

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def set_token(self, length):
        return secrets.token_hex(length)

    def __repr__(self):
        return f'{self.first_name}, you are a member of us. Welcome!'
    
class Car(db.Model):
    id = db.Column(db.String, primary_key = True)
    make = db.Column(db.String(50))
    model = db.Column(db.String(50))
    year = db.Column(db.Numeric(precision=4))
    price = db.Column(db.Numeric(precision=11, scale=2))
    color = db.Column(db.String(50))
    type = db.Column(db.String(50), nullable = True)
    wheels = db.Column(db.Numeric(precision=2), nullable=True)
    speed_rating = db.Column(db.Numeric(precision=2), nullable = True)
    rarity = db.Column(db.Numeric(precision=2), nullable = True)
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self, make, model, year, price, color, type, wheels, speed_rating, rarity, user_token, id=''):
        self.id = self.set_id()
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.color = color
        self.type = type
        self.wheels = wheels
        self.speed_rating = speed_rating
        self.rarity = rarity
        self.user_token = user_token

    def set_id(self):
        return secrets.token_urlsafe()

    def __repr__(self):
        return f"{self.make} {self.model} {self.year} is now in our database."
    

class CarSchema(ma.Schema):
    class Meta:
        fields = ['id', 'make', 'model', 'year', 'price', 'color', 'type', 'wheels', 'speed_rating', 'rarity']

car_schema = CarSchema()
cars_schema = CarSchema(many = True)