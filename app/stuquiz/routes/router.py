# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 02/07/23
from app.stuquiz.routes.admin.login_admin import login_admin_page
from app.stuquiz.routes.admin.logout_admin import logout_admin_page


def register_routes(app) -> None:
    """Registers the blueprints (aka the routes) of the app.
    :param app: the app in which we want to register the blueprints.
    :return: void
    """
    app.register_blueprint(login_admin_page)
    app.register_blueprint(logout_admin_page)
