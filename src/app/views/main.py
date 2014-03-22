"""
Main routes for the app
"""
from app.views import TemplatedView
from app.workflow.user import check_and_return_user


class MainView(TemplatedView):
    """
    Main view for the app
    """

    def get(self):
        """ GET """
        user, login_url, logout_url = check_and_return_user()

        context = {
            "greeting": "Hello world!" if user else "Good night moon",
        }

        if user:
            context["logout"] = logout_url
        else:
            context["login"] = login_url
        self.render_response("home.html", **context)
