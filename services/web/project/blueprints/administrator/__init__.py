from flask import Blueprint

bp = Blueprint('administrator', __name__)

from project.blueprints.administrator import routes  # noqa:E402,F401
