from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_user import UserManager

from project.models import User


login = LoginManager()
db = SQLAlchemy()
migrate = Migrate()
user_manager = UserManager()


def create_app():
    app = Flask(__name__)

    app.config.from_object("config.Config")

    db.init_app(app)
    migrate.init_app(app, db)

    login.init_app(app)
    login.login_view = 'login'

    user_manager.init_app(app, db, User)

    register_blueprints(app)

    return app


def register_blueprints(app):
    from project.blueprints.errors import bp as error_bp

    app.register_blueprint(error_bp)

    from project.blueprints.main import bp as main_bp

    app.register_blueprint(main_bp)

    from project.blueprints.api.version_1 import bp as api_v1_bp

    app.register_blueprint(api_v1_bp, url_prefix='/api/v1')

    from project.blueprints.auth import bp as auth_bp

    app.register_blueprint(auth_bp)
