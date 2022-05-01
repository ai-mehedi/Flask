from .extensions import db


class Mehedi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))