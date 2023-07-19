# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 02/07/23
from app.stuquiz.routes.admin.login_admin import login_admin_page
from app.stuquiz.routes.admin.logout_admin import logout_admin_page
from app.stuquiz.routes.course.get_course_by_id import get_course_by_id_page
from app.stuquiz.routes.course.get_courses import get_courses_page
from app.stuquiz.routes.course.get_courses_by_professor import get_courses_by_professor_page
from app.stuquiz.routes.university.add_university import add_university_page
from app.stuquiz.routes.university.delete_university import delete_university_page
from app.stuquiz.routes.university.get_universities import get_universities_page
from app.stuquiz.routes.university.get_university_by_id import get_university_by_id_page
from app.stuquiz.routes.university.get_university_courses import get_university_courses_page
from app.stuquiz.routes.university.update_university import update_university_page


def register_routes(app) -> None:
    """Registers the blueprints (aka the routes) of the app.
    :param app: the app in which we want to register the blueprints.
    :return: void
    """
    # Admin
    app.register_blueprint(login_admin_page)
    app.register_blueprint(logout_admin_page)

    # University
    app.register_blueprint(get_universities_page)
    app.register_blueprint(get_university_by_id_page)
    app.register_blueprint(add_university_page)
    app.register_blueprint(update_university_page)
    app.register_blueprint(delete_university_page)
    app.register_blueprint(get_university_courses_page)

    # Course
    app.register_blueprint(get_courses_page)
    app.register_blueprint(get_course_by_id_page)
    app.register_blueprint(get_courses_by_professor_page)
