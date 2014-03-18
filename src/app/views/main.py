"""
Main routes for the app
"""
from app.views import TemplatedView


class MainView(TemplatedView):
    """
    Main view for the app
    """

    def get(self):
        """ GET """
        context = {
            "greeting": "Hello world!"
        }
        self.render_response("home.html", **context)
