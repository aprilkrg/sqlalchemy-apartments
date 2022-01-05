from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Dino(db.Model):
    __tablename__ = 'dinos'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    type = db.Column(db.String)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String)

class Apartment(db.Model):
    __tablename__ = 'apartments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    units = db.Column(db.Integer)
    owner_id = db.Column(db.Integer, db.ForeignKey('owners.id'))

    def __str__(self):
        return f'{self.name}'

class Owner(db.Model):
    __tablename__ = 'owners'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer)
    apartments = db.relationship('Apartment') 

    def __str__(self):
        return f'{self.name}, {self.age}'
