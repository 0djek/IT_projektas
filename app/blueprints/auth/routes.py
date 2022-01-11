from flask import render_template, redirect, url_for, flash, request
from app.blueprints.auth import auth_window_blueprint
from flask_login import login_user, logout_user, current_user   # noqa
from app.models.forms import RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash    # noqa
import database_python as db
from werkzeug.urls import url_parse


@auth_window_blueprint.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        flash("Jūs esate prisijungęs")
        return redirect(url_for("recipes.index"))
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = db.get_user_by_username(login_form.username.data)
        if user and user.check_password(login_form.password.data):
            login_user(user)
            flash("Prisijungta sėkmingai.")
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('recipes.index')
            return redirect(next_page)
            # return redirect(url_for("recipes.index"))
        else:
            flash("Slapyvardis arba slaptažodis buvo neteisingi.")
    return render_template("auth/login.html", form=login_form)


@auth_window_blueprint.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("recipes.index"))
    register_form = RegisterForm()  # noqa
    if register_form.validate_on_submit():
        db.register_user(register_form.username.data, register_form.email.data, generate_password_hash(register_form.password.data))
        user = db.get_user_by_username(register_form.username.data)
        login_user(user)
        flash("Prisiregistruota sėkmingai, buvote prijungtas prie sistemos.")
        return redirect(url_for("recipes.index"))
    return render_template("auth/register.html", form=register_form)


@auth_window_blueprint.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
