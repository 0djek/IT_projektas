from datetime import datetime
from uuid import uuid4, UUID
from sqlalchemy.orm import contains_eager, joinedload
from cachetools import cached
from database_python import database_recipe_cache, recipe, recipe_ingredient, recipe_step, user, get_ingredient_single, db_session, ingredient
from sqlalchemy import or_


def clear_recipe_cache():
    database_recipe_cache.clear()


@cached(database_recipe_cache)
def get_recipes_all():
    with db_session() as session:
        return session.query(recipe).join(recipe.recipe_ingredient_collection).join(ingredient).join(recipe.recipe_step_collection).join(recipe.user).options(contains_eager(recipe.recipe_ingredient_collection).contains_eager(recipe_ingredient.ingredient), contains_eager(recipe.recipe_step_collection), contains_eager(recipe.user)).all()


def get_recipes_all_from_user(user_id: str):
    with db_session() as session:
        return session.query(recipe).join(recipe.recipe_ingredient_collection).join(ingredient).join(recipe.recipe_step_collection).join(recipe.user).options(contains_eager(recipe.recipe_ingredient_collection).contains_eager(recipe_ingredient.ingredient), contains_eager(recipe.recipe_step_collection), contains_eager(recipe.user)).filter(user.user_id == user_id).all()


@cached(database_recipe_cache)
def get_recipes_single_title(seo_title: str):
    with db_session() as session:
        return session.query(recipe).join(recipe.recipe_ingredient_collection).join(ingredient).join(recipe.recipe_step_collection).join(recipe.user).options(contains_eager(recipe.recipe_ingredient_collection).contains_eager(recipe_ingredient.ingredient), contains_eager(recipe.recipe_step_collection), contains_eager(recipe.user)).filter(recipe.recipe_seo_title == seo_title).first()
        # return session.query(recipe).options(joinedload("recipe_ingredient_collection").options(joinedload("ingredient")), joinedload("recipe_step_collection")).filter(recipe.recipe_seo_title == seo_title).first()


def get_recipes_recipe_id(recipe_ids: list[str]):
    with db_session() as session:
        # NOTE: Filter recipes, so that only those that have the needed ingredients are got
        filter_query = [recipe.recipe_id == key for key in recipe_ids]
        all_recipes = session.query(recipe).join(recipe.recipe_ingredient_collection).join(ingredient).join(recipe.recipe_step_collection).options(contains_eager(recipe.recipe_ingredient_collection).contains_eager(recipe_ingredient.ingredient), contains_eager(recipe.recipe_step_collection)).filter(or_(*filter_query))
        return all_recipes.all()


def get_recipes_filtered(filters):
    recipe_ids: list[str] | None = None
    with db_session() as session:
        # NOTE: Filter recipes, so that only those that have the needed ingredients are got
        filter_query = [ingredient.ingredient_seo_title == key for key in filters]
        all_recipes_that_match = session.query(recipe).join(recipe.recipe_ingredient_collection).join(ingredient, isouter=True).join(recipe.recipe_step_collection).options(contains_eager(recipe.recipe_ingredient_collection).contains_eager(recipe_ingredient.ingredient), contains_eager(recipe.recipe_step_collection)).filter(or_(*filter_query))
        all_recipes_not_all_ingredients = all_recipes_that_match.all()
        del all_recipes_that_match
        recipe_ids = [got_recipe.recipe_id for got_recipe in all_recipes_not_all_ingredients]
    return get_recipes_recipe_id(recipe_ids)


@cached(database_recipe_cache)
def get_recipes_user(user_id: str):
    with db_session() as session:
        return session.query(recipe).join(recipe.recipe_ingredient_collection).join(ingredient).join(recipe.recipe_step_collection).join(recipe.user).options(contains_eager(recipe.recipe_ingredient_collection).contains_eager(recipe_ingredient.ingredient), contains_eager(recipe.recipe_step_collection), contains_eager(recipe.user)).filter(user.user_id == user_id).all()


def update_recipe(submitted_form) -> None:
    with db_session() as session:
        base_recipe = session.query(recipe).join(recipe.recipe_ingredient_collection).join(ingredient, isouter=True).join(recipe.recipe_step_collection).options(contains_eager(recipe.recipe_ingredient_collection).contains_eager(recipe_ingredient.ingredient), contains_eager(recipe.recipe_step_collection)).filter(recipe.recipe_seo_title == submitted_form.seo_title.data).all()[0]
        # NOTE: Setting main recipe info
        base_recipe.recipe_title = submitted_form.title.data
        base_recipe.recipe_seo_title = submitted_form.seo_title.data
        base_recipe.recipe_description = submitted_form.description.data
        base_recipe.description_exerpt = submitted_form.description_exerpt.data

        # NOTE: Setting steps info
        for i, step in enumerate(submitted_form.recipe_steps):
            base_recipe.recipe_step_collection[i].recipe_step_title = step.title.data
            base_recipe.recipe_step_collection[i].recipe_step_seo_title = step.seo_title.data
            base_recipe.recipe_step_collection[i].recipe_step_description = step.step_description.data
            base_recipe.recipe_step_collection[i].recipe_step_step_order = step.order.data

        # NOTE: Setting ingredients info
        for i, form_ingredient in enumerate(submitted_form.recipe_ingredients):
            ing_uuid = get_ingredient_single(form_ingredient.ingredient.data)
            base_recipe.recipe_ingredient_collection[i].recipe_ingredient_quantity = form_ingredient.quantity.data
            base_recipe.recipe_ingredient_collection[i].fk_recipe_ingredient_ingredient_id = ing_uuid.ingredient_id
        session.commit()
    clear_recipe_cache()


def delete_recipe(seo_title: str) -> None:
    with db_session() as session:
        obj_to_delete = session.query(recipe).filter(recipe.recipe_seo_title == seo_title).all()[0]
        if obj_to_delete:
            session.delete(obj_to_delete)
            session.commit()
    clear_recipe_cache()


def upload_new_recipe(title: str, seo_title: str, desc: str, desc_e: str, current_user_id: str) -> UUID:
    cur_date = datetime.utcnow()
    db_date = cur_date.strftime('%Y-%m-%d %H:%M:%S')
    recipe_id = uuid4()
    with db_session() as session:
        to_add = recipe(recipe_id=recipe_id, recipe_title=title, recipe_seo_title=seo_title, recipe_description=desc, recipe_desciption_exerpt=desc_e, recipe_date_created=db_date, fk_recipe_user_id=UUID(current_user_id))
        session.add(to_add)
        session.commit()
    return recipe_id


def upload_new_recipe_steps(steps, recipe_id, user_id) -> None:
    with db_session() as session:
        for step in steps:
            to_add = recipe_step(recipe_step_id=uuid4(), recipe_step_title=step.title, recipe_step_seo_title=step.seo_title, recipe_step_description=step.description, recipe_step_step_order=step.order, fk_recipe_step_recipe_id=recipe_id, fk_recipe_step_user_id=UUID(user_id))
            session.add(to_add)
        session.commit()


def upload_new_recipe_ingredients(ingredients: list, recipe_id: UUID) -> None:
    with db_session() as session:
        for ingredient_needed in ingredients:
            ing_uuid = get_ingredient_single(ingredient_needed.seo_title)
            to_add = recipe_ingredient(recipe_ingredient_id=uuid4(), recipe_ingredient_quantity=ingredient_needed.quantity, fk_recipe_ingredient_ingredient_id=UUID(ing_uuid.ingredient_id), fk_recipe_ingredient_recipe_id=str(recipe_id))
            session.add(to_add)
        session.commit()
