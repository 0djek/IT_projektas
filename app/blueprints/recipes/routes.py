from flask import render_template, redirect, url_for
from app.blueprints.recipes import recipes_window_blueprint
from flask_login import login_required
from app.models.forms import FilterForm, RecipeCreatorForm
import database_python as db
from typing import cast
# from app.models.forms import RecipeForm


@recipes_window_blueprint.route("/", methods=["GET", "POST"])
@login_required
def index():  # sourcery skip: simplify-dictionary-update
    # NOTE: RecipeCreator filter form
    recipe_creator_form = RecipeCreatorForm()
    all_users = cast(list, db.get_all_recipe_creators())
    users_to_append: list[tuple[str, str]] = []
    filter_recipe_creator: bool = False
    for user in all_users:
        users_to_append.append((cast(str, user.user_id), user.user_username))
    users_to_append.sort(key=lambda tup: tup[1])
    recipe_creator_form.recipe_creators.choices = users_to_append

    if recipe_creator_form.validate_on_submit():
        filter_recipe_creator = True
        recipes = db.get_recipes_all_from_user(cast(str, recipe_creator_form.recipe_creators.data))
    print(recipe_creator_form.form_errors)
    print(recipe_creator_form.errors)

    # NOTE: Recipe filter form
    form = FilterForm()
    item_filters: dict[str, str] = {}
    query_type: str | None = None
    if form.validate_on_submit():
        for item in form.items:
            if item.item.data and float(item.item.data) > 0:
                item_filters.update({item.hidden_seo.data: float(item.item.data)})
    ingredients = db.get_ingredient_all()

    if not filter_recipe_creator and not item_filters:
        query_type = "all"
        recipes = db.get_recipes_all()
    elif not filter_recipe_creator and item_filters:
        query_type = "filter"
        item_keys = [*item_filters]
        recipes = db.get_recipes_filtered(item_keys)
        del item_keys

    for count, ingredient in enumerate(ingredients):
        if len(form.items) != len(ingredients):
            form.items.append_entry()
        # fixing labels
        form.items[count].form.item.label.text = ingredient.ingredient_title
        form.items[count].form.item.data = form.items[count].form.item.data
        form.items[count].form.unit.label.text = ingredient.ingredient_unit
        form.items[count].form.hidden_seo.data = ingredient.ingredient_seo_title
    return render_template("recipes/index.html", form=form, recipes=recipes, query_type=query_type, item_filters=item_filters, recipe_creator_form=recipe_creator_form)


@recipes_window_blueprint.route("/recipe/<string:seo_title>")
@login_required
def view_recipe(seo_title: str):
    recipe = db.get_recipes_single_title(seo_title)
    if not recipe:
        return redirect(url_for("recipes.index"))
    return render_template("recipes/view_recipe.html", recipe=recipe)


@recipes_window_blueprint.route("/ingredients")
@login_required
def view_all_ingredients():
    return render_template("recipes/view_ingredients.html", ingredients=mock_up_data.mock_up_recipes_ingredients_seperate)


@recipes_window_blueprint.route("/ingredients/<string:seo_title>")
@login_required
def view_ingredient(seo_title):
    ingredient = mock_up_data.mock_up_recipes_ingredients_seperate.get(seo_title)
    return render_template("recipes/view_ingredient.html", ingredient=ingredient)
