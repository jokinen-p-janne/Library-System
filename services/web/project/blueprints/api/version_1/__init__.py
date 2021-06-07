from flask import Blueprint

bp = Blueprint('api', __name__)

from project.blueprints.api.version_1 import books, customers, employees, errors, ping  # noqa:E402,F401
