from datetime import datetime as dt
import re
from fulcrum import db

_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')

class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_modified = db.Column(db.DateTime, default=dt.utcnow, onupdate=dt.utcnow)
    date_created = db.Column(db.DateTime, default=dt.utcnow)
    title = db.Column(db.String(80), nullable=False)
    task = db.Column(db.String(160), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
