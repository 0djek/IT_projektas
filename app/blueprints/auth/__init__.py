from flask import Blueprint

auth_window_blueprint = Blueprint("auth", __name__, url_prefix="/auth")

from app.blueprints.auth import routes  # noqa
