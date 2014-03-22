"""
User models
"""
from google.appengine.api import users
from google.appengine.ext import ndb

from app.models import BaseNdbModel

class User(BaseNdbModel):
    user_id = ndb.StringProperty()
    name = ndb.StringProperty()
    email = ndb.StringProperty()

    @classmethod
    def build_key(cls, user_id):
        """ Build and return a key for an entity """
        key = ndb.Key(cls, user_id)
        return key

    @staticmethod
    def lookup_all(limit=100):
        query = User.query()
        return query.fetch(limit=limit)

    @staticmethod
    def lookup_all_by_user_id(user_id):
        """ Look up users by their user_id """
        if not user_id:
            raise ValueError("user_id must be provided")
        query = User.query()
        query = query.filter(User.user_id == user_id)
        # Give them the first one, in the impossible case that there are multiple
        #  User entities with the same user_id
        return query.fetch(1)
