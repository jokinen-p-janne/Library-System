from flask import Blueprint

bp = Blueprint('api', __name__)

from project.blueprints.api import books, errors  # noqa:E402,F401
