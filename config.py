from flask_login import current_user, logout_user
from flask import flash


# database settings
db_dialect = "mysql"
db_driver = "pymysql"
db_username = "root"
db_password = ""
db_host = "localhost"
db_port = "3306"
db_database = "it_maistas"


def specific_rights_required(user_role=["admin"]):
    def inner(func):
        def wrapper(*args, **kwargs):
            from app import login_manager
            if current_user.role in user_role:
                return func(*args, **kwargs)
            flash("Prašome prisijungti su ta paskyra, kuri turi leidimą patekti į norimą puslapį.")
            logout_user()
            return login_manager.unauthorized()
        wrapper.__name__ = func.__name__
        return wrapper
    return inner
