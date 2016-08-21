from flask import request
from flask_restful import Resource
from flask_marshmallow.fields import fields
from fulcrum import ma, db
from fulcrum.models import User, ToDo, Email, Address
from .todo import ToDoSchema, todo_schema, todos_schema


class AddressSchema(ma.ModelSchema):
    class Meta:
        model = Address


class EmailSchema(ma.ModelSchema):
    class Meta:
        model = Email


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User

    to_dos = fields.Nested(ToDoSchema, many=True)
    mail_addresses = fields.Nested(AddressSchema, many=True)
    email_addresses = fields.Nested(EmailSchema, many=True)

user_schema = UserSchema()
users_schema = UserSchema(many=True)


class UserCollection(Resource):
    def get(self):
        result = users_schema.dump(User.query.all())
        return result.data, 200, {'Cache-Control': 'max-age=30, must-revalidate'}

    def post(self):
        json_data = request.get_json()
        if not json_data:
            return {'message': 'No input data provided'}, 400
        new_user, errors = user_schema.load(json_data)
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user).data, 201


class UserDocument(Resource):
    def get(self, user_id):
        result = user_schema.dump(User.query.filter_by(id=user_id).first_or_404())
        return result.data


class UserToDoCollection(Resource):
    def get(self, user_id):
        result = todos_schema.dump(ToDo.query.filter_by(user_id=user_id).all())
        return result.data

    def post(self, user_id):
        json_data = request.get_json()
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = todo_schema.load(json_data)
        if errors:
            return errors, 422
        user = User.query.filter_by(id=user_id).first_or_404()
        title, task = data['title'], data['task']
        new_todo = ToDo(title=title, task=task)
        user.to_dos.append(new_todo)
        db.session.add(new_todo)
        db.session.commit()
        return todo_schema.dump(new_todo).data, 201


class UserEmailCollection(Resource):
    def get(self, user_id):
        result = todos_schema.dump(ToDo.query.filter_by(user_id=user_id).all())
        return result.data