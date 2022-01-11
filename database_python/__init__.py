from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config import db_dialect, db_driver, db_username, db_password, db_host, db_port, db_database
from cachetools import TTLCache

database_ingredient_cache = TTLCache(maxsize=300, ttl=7200)
database_ingredient_suggestion_cache = TTLCache(maxsize=300, ttl=7200)
database_recipe_cache = TTLCache(maxsize=300, ttl=7200)

# get database connection and objects
Base = automap_base()

engine = create_engine(f"{db_dialect}+{db_driver}://{db_username}:{db_password}@{db_host}:{db_port}/{db_database}")

# reflect the tables
Base.prepare(engine, reflect=True)

# mapped classes are now created with names by default
# matching that of the table name.
user = Base.classes.user
recipe = Base.classes.recipe
recipe_step = Base.classes.recipe_step
recipe_ingredient = Base.classes.recipe_ingredient
ingredient = Base.classes.ingredient
suggested_ingredient = Base.classes.suggested_ingredient

db_session = sessionmaker(engine)

from .users.users import get_user_by_id, is_email, is_username, register_user, get_user_by_username, get_all_recipe_creators   # noqa
from .ingredients.ingredients import create_ingredient_single, update_ingredient_single, is_ingredient_single_seo_title, get_ingredient_suggestions, get_ingredient_single, get_ingredient_all, delete_ingredient_single, is_ingredient_suggestion_single_seo_title, remove_ingredient_suggestion_single, approve_ingredient_suggestion_single, create_ingredient_suggestion_single    # noqa
from .recipes.recipes import get_recipes_all, get_recipes_user, upload_new_recipe, upload_new_recipe_ingredients, upload_new_recipe_steps, get_recipes_single_title, get_recipes_filtered, update_recipe, delete_recipe, get_recipes_all_from_user    # noqa
