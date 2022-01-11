# imports
from flask import Flask
from flask_login import LoginManager
import database_python as db

flask_app = Flask(__name__)     # configure app
flask_app.config['SECRET_KEY'] = 'you-will-never-guess'   # for forms

# flask login
login_manager = LoginManager()
login_manager.init_app(flask_app)
login_manager.login_view = 'auth.login'
login_manager.login_message = "Prašome prisijungti, jeigu norite pasiekti tą puslapį."
login_manager.user_loader(db.get_user_by_id)

# configure blueprints
from app.blueprints.auth import auth_window_blueprint   # noqa
flask_app.register_blueprint(auth_window_blueprint)

from app.blueprints.recipes import recipes_window_blueprint   # noqa
flask_app.register_blueprint(recipes_window_blueprint)

from app.blueprints.admin import admin_window_blueprint   # noqa
flask_app.register_blueprint(admin_window_blueprint)
