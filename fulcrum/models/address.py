from datetime import datetime as dt
from fulcrum import db

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_modified = db.Column(db.DateTime, default=dt.utcnow, onupdate=dt.utcnow)
    date_created = db.Column(db.DateTime, default=dt.utcnow)
    address_line1 = db.Column(db.String, nullable=False)
    address_line2 = db.Column(db.String)
    city = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    zip = db.Column(db.String, nullable=False)
    country = db.Column(db.String, nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
