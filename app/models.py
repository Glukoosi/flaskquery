from app import db

class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    string = db.Column(db.String(64))
    string3 = db.Column(db.String(64))
    boolean = db.Column(db.Boolean())
    radio = db.Column(db.String(64))
    text = db.Column(db.String(500))
    datetime = db.Column(db.DateTime())
