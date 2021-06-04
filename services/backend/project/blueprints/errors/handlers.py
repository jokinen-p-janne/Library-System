from project import db
from project.blueprints.errors import bp


@bp.app_errorhandler(404)
def not_found_error(error):
    return "Not found", 404


@bp.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return "Internal error", 500
