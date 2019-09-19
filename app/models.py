from app import db

class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    mail = db.Column(db.String(64))
    year = db.Column(db.String(64))
    active = db.Column(db.String(64))
    nonalcoholic = db.Column(db.Boolean())
    food = db.Column(db.String(256))
    speechbox = db.Column(db.Boolean())
    speech = db.Column(db.String(256))
    other = db.Column(db.String(512))
    public = db.Column(db.Boolean())
    datetime = db.Column(db.DateTime())
