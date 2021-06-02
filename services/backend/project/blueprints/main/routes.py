from project.blueprints.main import bp


@bp.route("/ping")
def ping():
    return "pong"
