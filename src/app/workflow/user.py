"""
Workflow methods for users
"""
from google.appengine.api import users

from app.domain.user import create_user
from app.models.user import User

def get_or_create_user(name, email, user_id):
    """
    Gets the user from the datastore, or creates them (with a domain method)
     if they don't exist
    """
    if not name:
        raise ValueError("name is required")
    if not email:
        raise ValueError("email is required")
    if not user_id:
        raise ValueError("user_id is required")

    key = User.build_key(user_id)

    user = key.get()

    if not user:
        user = create_user(name, email, user_id, key=key)

    return user
