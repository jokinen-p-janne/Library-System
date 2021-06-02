from flask.cli import FlaskGroup

from project import create_app, db
from project.models import Book


app = create_app()

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    db.session.add(Book(isbn="test_isbn", title="test_title", author="test_author"))
    db.session.commit()


if __name__ == "__main__":
    cli()
