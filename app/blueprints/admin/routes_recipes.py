from typing import cast
from app.models.user import User
from flask import render_template, redirect, url_for, flash
from app.blueprints.admin import admin_window_blueprint
import database_python as db
from uuid import UUID
from flask_login import login_required, current_user
import flask_login
from config import specific_rights_required
from app.models.forms import RecipeForm, RecipeBeforeForm
from app.models.recipe import RecipeIngredient, RecipeStep
from .helper import get_ingredient_choices


@admin_window_blueprint.route("/recipes")
@login_required
@specific_rights_required(user_role=["admin", "recipe_creator"])
def view_recipes():
    current_user = cast(User, flask_login.current_user)
    if current_user.role == "admin":
        recipes = db.get_recipes_all()
    else:
        recipes = db.get_recipes_user(current_user.id)
    for recipe in recipes:
        count = sum(1 for _ in recipe.recipe_step_collection)
        setattr(recipe, "step_count", count)
    return render_template("admin/view_recipes.html", recipes=recipes)


@admin_window_blueprint.route("/create-recipe-before", methods=["GET", "POST"])
@login_required
@specific_rights_required(user_role=["admin", "recipe_creator"])
def create_recipe_before():
    form = RecipeBeforeForm()
    if form.validate_on_submit():
        return redirect(url_for("admin.create_recipe", step_count=form.step_count.data, ingredients_count=form.ingredient_count.data))
    return render_template("recipes/create_recipe_before.html", form=form)


@admin_window_blueprint.route("/create-recipe/<int:step_count>/<int:ingredients_count>", methods=["GET", "POST"])
@login_required
@specific_rights_required(user_role=["admin", "recipe_creator"])
def create_recipe(step_count: int, ingredients_count: int):
    form = RecipeForm()
    ingredients_to_append = get_ingredient_choices()
    for index in range(ingredients_count):
        if len(form.recipe_ingredients) != ingredients_count:
            form.recipe_ingredients.append_entry()
        form.recipe_ingredients[index].ingredient.choices = ingredients_to_append
        form.recipe_ingredients[index].quantity.data = form.recipe_ingredients[index].quantity.data

    for index in range(step_count):
        if len(form.recipe_steps) != step_count:
            form.recipe_steps.append_entry()
        form.recipe_steps[index].form.title.data = form.recipe_steps[index].form.title.data
        form.recipe_steps[index].form.seo_title.data = form.recipe_steps[index].form.seo_title.data
        form.recipe_steps[index].form.step_description.data = form.recipe_steps[index].form.step_description.data
        form.recipe_steps[index].form.order.data = index + 1
    if form.validate_on_submit():
        steps: list[RecipeStep] = []
        for step in form.recipe_steps.data:
            steps.append(RecipeStep(step.get("title"), step.get("seo_title"), step.get("description"), step.get("order")))
        del step
        ingredients_form: list[RecipeIngredient] = []
        for ingredient_form in form.recipe_ingredients.data:
            ingredients_form.append(RecipeIngredient(ingredient_form.get("ingredient"), ingredient_form.get("quantity")))
        del ingredient_form
        recipe_id: UUID = db.upload_new_recipe(form.title.data, form.seo_title.data, form.description.data, form.description_exerpt.data, current_user.id)
        db.upload_new_recipe_ingredients(ingredients_form, recipe_id)
        db.upload_new_recipe_steps(steps, recipe_id, current_user.id)
        flash("Receptas įkeltas sėkmingai.")
        return redirect(url_for("admin.create_recipe_before"))
    return render_template("recipes/create_recipe.html", form=form, page_title="Sukurti receptą")


@admin_window_blueprint.route("/edit-recipe/<string:seo_title>", methods=["GET", "POST"])
@login_required
@specific_rights_required(user_role=["admin", "recipe_creator"])
def edit_recipe(seo_title):
    form = RecipeForm()
    ingredients_to_append = get_ingredient_choices()

    current_recipe = db.get_recipes_single_title(seo_title)
    ingredients_count: int = sum(1 for _ in current_recipe.recipe_ingredient_collection)
    step_count: int = sum(1 for _ in current_recipe.recipe_step_collection)
    # NOTE: Set default recipe information
    # NOTE: Setting title
    if form.title.data and current_recipe.recipe_title != form.title.data:
        form.title.data = form.title.data
    else:
        form.title.data = current_recipe.recipe_title
    # NOTE: Setting seo_title
    if form.seo_title.data and current_recipe.recipe_seo_title != form.seo_title.data:
        form.seo_title.data = form.seo_title.data
    else:
        form.seo_title.data = current_recipe.recipe_seo_title
    # NOTE: Setting description_exerpt
    if form.description_exerpt.data and current_recipe.recipe_desciption_exerpt	 != form.description_exerpt.data:
        form.description_exerpt.data = form.description_exerpt.data
    else:
        form.description_exerpt.data = current_recipe.recipe_desciption_exerpt
    # NOTE: Setting description
    if form.description.data and current_recipe.recipe_description != form.description.data:
        form.description.data = form.description.data
    else:
        form.description.data = current_recipe.recipe_description

    for index in range(ingredients_count):
        if len(form.recipe_ingredients) != ingredients_count:
            form.recipe_ingredients.append_entry()
        form.recipe_ingredients[index].ingredient.choices = ingredients_to_append
        # NOTE: Setting recipe's data
        # NOTE: Setting recipe's ingredient selection
        if form.recipe_ingredients[index].ingredient.data and current_recipe.recipe_ingredient_collection[index].ingredient.ingredient_title != form.recipe_ingredients[index].ingredient.data:
            form.recipe_ingredients[index].ingredient.data = form.recipe_ingredients[index].ingredient.data
        else:
            form.recipe_ingredients[index].ingredient.data = current_recipe.recipe_ingredient_collection[index].ingredient.ingredient_seo_title

        # NOTE: Setting ingredient quantity
        if form.recipe_ingredients[index].quantity.data and current_recipe.recipe_ingredient_collection[index].recipe_ingredient_quantity != form.recipe_ingredients[index].quantity.data:
            form.recipe_ingredients[index].quantity.data = form.recipe_ingredients[index].quantity.data
        else:
            form.recipe_ingredients[index].quantity.data = current_recipe.recipe_ingredient_collection[index].recipe_ingredient_quantity

    for index in range(step_count):
        if len(form.recipe_steps) != step_count:
            form.recipe_steps.append_entry()
        # NOTE: Setting title data
        if form.recipe_steps[index].title.data and current_recipe.recipe_step_collection[index].recipe_step_title != form.recipe_steps[index].title.data:
            form.recipe_steps[index].title.data = form.recipe_steps[index].title.data
        else:
            form.recipe_steps[index].title.data = current_recipe.recipe_step_collection[index].recipe_step_title

        # NOTE: Setting seo title data
        if form.recipe_steps[index].seo_title.data and current_recipe.recipe_step_collection[index].recipe_step_seo_title != form.recipe_steps[index].seo_title.data:
            form.recipe_steps[index].seo_title.data = form.recipe_steps[index].seo_title.data
        else:
            form.recipe_steps[index].seo_title.data = current_recipe.recipe_step_collection[index].recipe_step_seo_title

        # NOTE: Setting description data
        if form.recipe_steps[index].step_description.data and current_recipe.recipe_step_collection[index].recipe_step_description != form.recipe_steps[index].step_description.data:
            form.recipe_steps[index].step_description.data = form.recipe_steps[index].step_description.data
        else:
            form.recipe_steps[index].step_description.data = current_recipe.recipe_step_collection[index].recipe_step_description

        form.recipe_steps[index].form.order.data = index + 1

    form.create.label.text = "Atnaujinti receptą"

    if form.validate_on_submit():
        steps: list[RecipeStep] = []
        for step in form.recipe_steps.data:
            steps.append(RecipeStep(step.get("title"), step.get("seo_title"), step.get("description"), step.get("order")))
        del step
        ingredients_form: list[RecipeIngredient] = []
        for ingredient_form in form.recipe_ingredients.data:
            ingredients_form.append(RecipeIngredient(ingredient_form.get("ingredient"), ingredient_form.get("quantity")))
        del ingredient_form
        db.update_recipe(form)
        flash("Receptas atnaujintas sėkmingai")
        return redirect(url_for("admin.view_recipes"))
    return render_template("recipes/create_recipe.html", form=form, page_title="Atnaujinti receptą")


@admin_window_blueprint.route("/delete-recipe/<string:seo_title>")
@login_required
@specific_rights_required(user_role=["admin", "recipe_creator"])
def delete_recipe(seo_title):
    db.delete_recipe(seo_title)
    flash("Receptas ištrintas sėkmingai")
    return redirect(url_for("admin.view_recipes"))
