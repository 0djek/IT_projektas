from flask import Blueprint

recipes_window_blueprint = Blueprint("recipes", __name__)

from app.blueprints.recipes import routes  # noqa
