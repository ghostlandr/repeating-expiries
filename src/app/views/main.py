"""
Main routes for the app
"""
from app.views import TemplatedView
from app.domain.user import get_log_links, check_and_return_user


class MainView(TemplatedView):
    """
    Main view for the app
    """

    def get(self):
        """ GET """
        logout_url, login_url = get_log_links()
        user, ndb_user, in_datastore = check_and_return_user()
        stored_user = ndb_user.pop() if ndb_user else None

        context = {
            "user": stored_user if in_datastore else user
        }
        import logging
        logging.info("Users user: {0}, ndb_user: {1}".format(user, ndb_user))
        if user:
            context["logout"] = logout_url
        else:
            context["login"] = login_url
        self.render_response("home.html", **context)
