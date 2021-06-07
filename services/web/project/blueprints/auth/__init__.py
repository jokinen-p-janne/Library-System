from flask import Blueprint

bp = Blueprint('auth', __name__)

from project.blueprints.auth import routes  # noqa:E402,F401
