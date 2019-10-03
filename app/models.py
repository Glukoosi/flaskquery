from app import db

class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    short = db.Column(db.String(64))
    url = db.Column(db.String(64))
    public = db.Column(db.Boolean)
    expiration = db.Column(db.String(64))


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    adminpass = db.Column(db.String(64))
