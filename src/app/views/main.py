"""
Main routes for the app
"""
from app.views import TemplatedView
from app.domain.user import get_current_user, get_log_links


class MainView(TemplatedView):
    """
    Main view for the app
    """

    def get(self):
        """ GET """
        user = get_current_user()
        logout_url, login_url = get_log_links()

        context = {
            "greeting": "Hello world!" if user else "Good night moon",
        }

        if user:
            context["logout"] = logout_url
        else:
            context["login"] = login_url
        self.render_response("home.html", **context)
