from flask import Blueprint

admin_window_blueprint = Blueprint("admin", __name__, url_prefix="/admin")

# from app.blueprints.admin import routes  # noqa
from . import routes_recipes    # noqa
from . import routes_ingredients    # noqa
