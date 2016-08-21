from datetime import datetime as dt
from fulcrum import db

user_role_tbl = db.Table('user_role',
                    db.Column('date_modified', db.DateTime, default=dt.utcnow, onupdate=dt.utcnow),
                    db.Column('date_created',db.DateTime, default=dt.utcnow),
                    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE')),
                    db.Column('role_id', db.Integer, db.ForeignKey('role.id', ondelete='CASCADE')),
                    db.Column('is_active', db.Boolean, nullable=False, default=True)
                )

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_modified = db.Column(db.DateTime, default=dt.utcnow, onupdate=dt.utcnow)
    date_created = db.Column(db.DateTime, default=dt.utcnow)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    roles = db.relationship('Role', secondary='user_role',
        backref=db.backref('users', lazy='dynamic'))
    email_addresses = db.relationship('Email', backref='user', lazy='dynamic')
    mail_addressess = db.relationship('Address', backref='user', lazy='dynamic')
    to_dos = db.relationship('ToDo', backref='user', lazy='dynamic')
    is_confirmed = db.Column(db.Boolean, nullable=False, default=False)
    is_active = db.Column(db.Boolean, nullable=False, default=True)