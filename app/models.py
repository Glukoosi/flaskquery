from app import db

class Reg(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    representative = db.Column(db.String(64), index=True)
    greeting = db.Column(db.Boolean())
    food = db.Column(db.String(500))
    alcohol = db.Column(db.String(10))
    gambina = db.Column(db.Boolean())
    avec = db.Column(db.String(64))
    free = db.Column(db.String(500))
