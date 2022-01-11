import database_python as db
from typing import cast


def get_ingredient_choices() -> list[tuple[str, str]]:
    """Get all possible (accepted) ingredients from the database and return them all in a list of tuples.

    Returns
    -------
    list[tuple[str, str]]
        Ingredients, which can be added to `SelectField` choices
    """
    ingredients = db.get_ingredient_all()
    ingredients_to_append: list[tuple[str, str]] = []
    for ingredient in ingredients:
        ingredient_title: str = f"{ingredient.ingredient_title} ({ingredient.ingredient_unit})"
        ingredients_to_append.append((cast(str, ingredient.ingredient_seo_title), ingredient_title))
    ingredients_to_append.sort(key=lambda tup: tup[1])
    return ingredients_to_append
