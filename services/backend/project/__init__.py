from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    app.config.from_object("config.Config")

    db.init_app(app)
    migrate.init_app(app, db)

    register_blueprints(app)

    return app


def register_blueprints(app):
    from project.blueprints.errors import bp as error_bp

    app.register_blueprint(error_bp)

    from project.blueprints.main import bp as main_bp

    app.register_blueprint(main_bp)

    from project.blueprints.api import bp as api_bp

    app.register_blueprint(api_bp, url_prefix='/api')
