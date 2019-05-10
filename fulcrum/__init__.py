from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api
from .config import config_by_name

db = SQLAlchemy()
# api = Api() # Relocating to app factory for testing purposes
ma = Marshmallow()


def create_app(config_name):
    """Flask app creation factory"""
    app = Flask(__name__, static_folder=None)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    ma.init_app(app)
    # Relocating api to app factory for testing purposes. Leaving this in global scope causes issues with
    # the test runner trying to overwrite an existing endpoint function
    api = Api()

    # Import placed here to avoid circular import
    from .resources import (
        ToDoCollection,
        ToDoDocument,
        UserCollection,
        UserDocument,
        UserToDoCollection,
    )

    api.add_resource(UserCollection, "/users", endpoint="users")
    api.add_resource(UserDocument, "/users/<int:user_id>")
    api.add_resource(UserToDoCollection, "/users/<int:user_id>/todos")
    api.add_resource(ToDoCollection, "/todos")
    api.add_resource(ToDoDocument, "/todos/<int:todo_id>")

    api.init_app(app)

    return app


import fulcrum.models
import fulcrum.resources
