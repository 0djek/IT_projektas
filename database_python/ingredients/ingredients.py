from datetime import datetime
import uuid
from sqlalchemy import orm
from cachetools import cached
from database_python import db_session, ingredient, database_ingredient_cache, database_ingredient_suggestion_cache, suggested_ingredient


def clear_ingredient_cache():
    """Clears all caches that are used when communicating with database and getting info about ingredient
    """
    database_ingredient_cache.clear()


def clear_ingredient_suggestion_cache():
    """Clears all caches that are used when communicating with database and getting info about recipe
    """
    database_ingredient_suggestion_cache.clear()


@cached(database_ingredient_cache)
def get_ingredient_single(seo_title: str):
    with db_session() as session:
        return session.query(ingredient).options(orm.joinedload('user')).filter(ingredient.ingredient_seo_title == seo_title).order_by(ingredient.ingredient_date_created.desc()).first()


def is_ingredient_single_seo_title(seo_title: str):
    with db_session() as session:
        return bool(session.query(ingredient.ingredient_seo_title).filter(ingredient.ingredient_seo_title == seo_title.lower()).order_by(ingredient.ingredient_date_created.desc()).all())


def update_ingredient_single(title: str, seo_title: str, unit: str):
    with db_session() as session:
        clear_ingredient_cache()
        session.query(ingredient).filter(ingredient.ingredient_seo_title == seo_title).update({ingredient.ingredient_title: title, ingredient.ingredient_seo_title: seo_title, ingredient.ingredient_unit: unit}, synchronize_session=False)
        session.commit()


def delete_ingredient_single(seo_title: str):
    with db_session() as session:
        obj_to_delete = session.query(ingredient).filter(ingredient.ingredient_seo_title == seo_title).order_by(ingredient.ingredient_date_created.desc()).first()
        if obj_to_delete:
            session.delete(obj_to_delete)
            session.commit()
            clear_ingredient_cache()
            return True
        return False


def create_ingredient_single(title: str, seo_title: str, unit: str, user_id: str):
    cur_date = datetime.utcnow()
    with db_session() as session:
        ingredient_to_add = ingredient(ingredient_id=uuid.uuid4(), ingredient_title=title, ingredient_seo_title=seo_title.lower(), ingredient_unit=unit, ingredient_date_created=cur_date, fk_ingredient_user_id=user_id)
        session.add(ingredient_to_add)
        session.commit()
    clear_ingredient_cache()


def create_ingredient_suggestion_single(title: str, seo_title: str, unit: str, user_id: str):
    clear_ingredient_suggestion_cache()
    cur_date = datetime.utcnow()
    with db_session() as session:
        ingredient_to_add = suggested_ingredient(suggested_ingredient_id=uuid.uuid4(), suggested_ingredient_title=title, suggested_ingredient_seo_title=seo_title.lower(), suggested_ingredient_unit=unit, suggested_ingredient_date_suggested=cur_date, fk_suggested_ingredient_user_id=user_id)
        session.add(ingredient_to_add)
        session.commit()


def approve_ingredient_suggestion_single(seo_title: str, user_id: str):
    with db_session() as session:
        suggestion = get_ingredient_suggestion_single(seo_title)[0]
        create_ingredient_single(suggestion.suggested_ingredient_title, suggestion.suggested_ingredient_seo_title, suggestion.suggested_ingredient_unit, user_id)
        session.delete(suggestion)
        session.commit()
    clear_ingredient_suggestion_cache()


def remove_ingredient_suggestion_single(seo_title: str):
    """Remove suggested ingredient. First, get it from the database, and then remove it.

    Parameters
    ----------
    seo_title : str
        What is the seo title of the ingredient suggestion that needs to be removed
    """
    with db_session() as session:
        suggestion = get_ingredient_suggestion_single(seo_title)[0]
        session.delete(suggestion)
        session.commit()
    clear_ingredient_suggestion_cache()


@cached(database_ingredient_cache)
def get_ingredient_all():
    with db_session() as session:
        return session.query(ingredient).options(orm.joinedload('user')).order_by(ingredient.ingredient_date_created.desc()).all()


@cached(database_ingredient_cache)
def get_ingredient_filtered(item_filters: dict):
    with db_session() as session:
        return session.query(ingredient).options(orm.joinedload('user')).order_by(ingredient.ingredient_date_created.desc()).all()


@cached(database_ingredient_suggestion_cache)
def get_ingredient_suggestions():
    with db_session() as session:
        return session.query(suggested_ingredient).options(orm.joinedload('user')).order_by(suggested_ingredient.suggested_ingredient_date_suggested).all()


def get_ingredient_suggestion_single(seo_title: str):
    with db_session() as session:
        return session.query(suggested_ingredient).filter(suggested_ingredient.suggested_ingredient_seo_title == seo_title).all()


def is_ingredient_suggestion_single_seo_title(seo_title: str):
    with db_session() as session:
        return bool(session.query(suggested_ingredient).filter(suggested_ingredient.suggested_ingredient_seo_title == seo_title).all())
