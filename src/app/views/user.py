"""
User views
"""
from app.views import TemplatedView
from app.domain.user import check_and_return_user, get_current_user
from app.workflow.user import get_or_create_user

class NewUserView(TemplatedView):
    """ New user view, gets called when someone signs in """

    def get(self):
        """ GET """
        user, ndb_user, in_datastore = check_and_return_user()

        if in_datastore:
            # Not making someone new, redirect back home
            self.redirect('/')

        context = {
            "new_user": not in_datastore,
            "user": user,
            "ndb_user": ndb_user
        }

        self.render_response("user.html", **context)

    def post(self):
        """ POST """
        name = self.request.POST.get('name')
        email = self.request.POST.get('email')
        users_user = get_current_user()

        # Acknowledging that it will return something, but have no use for it
        _ = get_or_create_user(name, email, users_user.user_id())

        self.redirect('/')
