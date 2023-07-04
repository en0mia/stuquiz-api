# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 02/07/23
from app.stuquiz.routes.university.get_universities import get_universities_page
from app.stuquiz.routes.university.get_university_by_id import get_university_by_id_page


def register_routes(app) -> None:
    """Registers the blueprints (aka the routes) of the app.
    :param app: the app in which we want to register the blueprints.
    :return: void
    """
    app.register_blueprint(get_universities_page)
    app.register_blueprint(get_university_by_id_page)
