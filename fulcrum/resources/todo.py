from flask import request
from flask.views import MethodView
from flask_restful import Resource, fields, marshal_with
from fulcrum import db, ma
from fulcrum.models import ToDo


class ToDoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'date_created', 'date_modified', 'title', 'task', 'completed')

todo_schema = ToDoSchema()
todos_schema = ToDoSchema(many=True)



class ToDoCollection(Resource):
    def get(self):
        return todos_schema.dump(ToDo.query.all()).data

"""
    def post(self):
        data = request.get_json()
        todo = ToDo(task=data['task'], _alt_id=data['_alt_id'])
        db.session.add(todo)
        db.session.commit()
        return todo, 201
"""

class ToDoDocument(Resource):
    def get(self, todo_id=None):
        return todo_schema.dump(ToDo.query.filter_by(id=todo_id).first_or_404()).data


"""
    def put(self, todo_id=None, todo_alt=None):
        payload = request.get_json()
        if todo_id:
            todo = ToDo.query.filter_by(id=todo_id).first_or_404()
        else:
            todo = ToDo.query.filter_by(_alt_id=todo_alt).first_or_404()

        return todo, 200
"""
"""
    def patch(self, todo_id):
        payload = request.get_json()
        result = todos.update_todo(todo_id, payload)
        return result, 200
"""
