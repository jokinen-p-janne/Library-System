from flask import Blueprint

bp = Blueprint('main', __name__)

from project.blueprints.main import routes  # noqa:E402,F401
