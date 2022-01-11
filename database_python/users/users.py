from app.models.user import User
import uuid
from datetime import datetime
from sqlalchemy import or_
from database_python import user, db_session


def get_user_by_id(user_id: str):
    with db_session() as session:
        db_user = session.query(user).filter(user.user_id == user_id).first()
        if db_user:
            return User(db_user.user_id, db_user.user_username, db_user.user_email, db_user.user_password, db_user.user_date_registered, db_user.user_role)
        return None


def get_user_by_username(username: str):
    with db_session() as session:
        db_user = session.query(user).filter(user.user_username == username).first()
        if db_user:
            return User(db_user.user_id, db_user.user_username, db_user.user_email, db_user.user_password, db_user.user_date_registered, db_user.user_role)
        return None


def is_username(username: str):
    with db_session() as session:
        db_user = session.query(user.user_username).filter(user.user_username == username).first()
        return bool(db_user)


def is_email(email: str):
    with db_session() as session:
        db_user = session.query(user.user_email).filter(user.user_email == email).first()
        return bool(db_user)


def register_user(username: str, email: str, password: str):
    cur_date = datetime.utcnow()
    db_date = cur_date.strftime('%Y-%m-%d %H:%M:%S')
    with db_session() as session:
        user_to_add = user(user_id=uuid.uuid4(), user_username=username, user_email=email, user_password=password, user_date_registered=db_date)
        session.add(user_to_add)
        session.commit()


def get_all_recipe_creators() -> list[user] | None:
    """Get all recipe creators, that have created any recipes.
    """
    with db_session() as session:
        db_user = session.query(user).filter(or_(user.user_role == "recipe_creator")).all()
        return db_user
