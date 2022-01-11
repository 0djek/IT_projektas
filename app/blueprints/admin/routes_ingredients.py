from flask import render_template, redirect, url_for, flash
from app.blueprints.admin import admin_window_blueprint
import database_python as db
from flask_login import login_required, current_user
from config import specific_rights_required
from app.models.forms import IngredientForm, IngredientSuggestionForm    # noqa
from wtforms.fields import Label


@admin_window_blueprint.route("ingredients")
@login_required
@specific_rights_required(user_role="admin")
def view_ingredients():
    ingredients = db.get_ingredient_all()
    return render_template("admin/view_ingredients.html", ingredients=ingredients)


@admin_window_blueprint.route("delete-ingredient/<string:seo_title>")
@login_required
@specific_rights_required(user_role="admin")
def delete_ingredient(seo_title):
    status = db.delete_ingredient_single(seo_title)
    if status:
        flash(f"Ingredientas '{seo_title}' buvo ištrintas.")
    else:
        flash(f"Nepavyko ištrinti '{seo_title}'.")
    return redirect(url_for("admin.view_ingredients"))


@admin_window_blueprint.route("create-ingredient", methods=["GET", "POST"])
@login_required
@specific_rights_required(user_role="admin")
def create_ingredient():
    ingredient_form = IngredientForm()
    if ingredient_form.validate_on_submit():
        db.create_ingredient_single(ingredient_form.title.data, ingredient_form.seo_title.data, ingredient_form.unit.data, current_user.id)
        flash(f"Ingredientas '{ingredient_form.title.data}' sukurtas")
        return redirect(url_for("admin.view_ingredients"))
    else:
        if ingredient_form.create.data:
            ingredient_form.title.data = ingredient_form.title.data
            ingredient_form.seo_title.data = ingredient_form.seo_title.data
            ingredient_form.unit.data = ingredient_form.unit.data
    return render_template("admin/create_ingredients.html", ingredient=edit_ingredient, form=ingredient_form)


@admin_window_blueprint.route("suggest-ingredient", methods=["GET", "POST"])
@login_required
@specific_rights_required(user_role=["recipe_creator", "admin"])
def suggest_ingredient():
    ingredient_form = IngredientSuggestionForm()
    if ingredient_form.validate_on_submit():
        db.create_ingredient_suggestion_single(ingredient_form.title.data, ingredient_form.seo_title.data, ingredient_form.unit.data, current_user.id)
        flash(f"Ingredient '{ingredient_form.title.data}' pasiūlymas sukurtas")
        return redirect(url_for("admin.view_ingredients"))
    else:
        if ingredient_form.create.data:
            ingredient_form.title.data = ingredient_form.title.data
            ingredient_form.seo_title.data = ingredient_form.seo_title.data
            ingredient_form.unit.data = ingredient_form.unit.data
    return render_template("admin/create_ingredients.html", ingredient=edit_ingredient, form=ingredient_form)


@admin_window_blueprint.route("view-ingredient-suggestions")
@login_required
@specific_rights_required(user_role=["recipe_creator", "admin"])
def view_ingredient_suggestions():
    return render_template("admin/view_ingredient_suggestions.html", ingredients=db.get_ingredient_suggestions())


@admin_window_blueprint.route("approve-suggestion/<string:seo_title>")
@login_required
@specific_rights_required(user_role="admin")
def approve_ingredient_suggestion(seo_title):
    db.approve_ingredient_suggestion_single(seo_title, current_user.id)
    flash(f"Ingrediento '{seo_title}' pasiūlymas patvirtintas")
    return redirect(url_for("admin.view_ingredient_suggestions"))


@admin_window_blueprint.route("disapprove-suggestion/<string:seo_title>")
@login_required
@specific_rights_required(user_role="admin")
def disapprove_ingredient_suggestion(seo_title):
    db.remove_ingredient_suggestion_single(seo_title)
    flash(f"Ingrediento '{seo_title}' pasiūlymas atmestas")
    return redirect(url_for("admin.view_ingredient_suggestions"))


@admin_window_blueprint.route("edit-ingredient/<string:seo_title>", methods=["GET", "POST"])
@login_required
@specific_rights_required(user_role="admin")
def edit_ingredient(seo_title):
    edit_form = IngredientForm(seo_title)
    if edit_form.validate_on_submit():
        db.update_ingredient_single(edit_form.title.data, edit_form.seo_title.data, edit_form.unit.data)
        flash(f"Ingredientas '{seo_title}' atnaujintas")
        return redirect(url_for("admin.view_ingredients"))
    else:
        edit_ingredient = db.get_ingredient_single(seo_title)
        if edit_form.create.data:
            edit_form.title.data = edit_form.title.data
            edit_form.seo_title.data = edit_form.seo_title.data
            edit_form.unit.data = edit_form.unit.data
        else:
            edit_form.title.data = edit_ingredient.ingredient_title
            edit_form.seo_title.data = edit_ingredient.ingredient_seo_title
            edit_form.unit.data = edit_ingredient.ingredient_unit
        edit_form.create.label = Label(field_id="unit", text="Redaguoti ingredientą")
    return render_template("admin/edit_ingredients.html", ingredient=edit_ingredient, form=edit_form)
