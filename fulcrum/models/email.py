from datetime import datetime as dt
from fulcrum import db


class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    date_modified = db.Column(db.DateTime, default=dt.utcnow, onupdate=dt.utcnow)
    date_created = db.Column(db.DateTime, default=dt.utcnow)
    email = db.Column(db.String(64), unique=True)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
