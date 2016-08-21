from datetime import datetime as dt
from fulcrum import db

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_modified = db.Column(db.DateTime, default=dt.utcnow, onupdate=dt.utcnow)
    date_created = db.Column(db.DateTime, default=dt.utcnow)
    name = db.Column(db.String(50), nullable=False, unique=True)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Role(name='%s')>" % self.name