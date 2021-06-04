from project.blueprints.api.version_1 import bp


@bp.route('/ping', methods=['GET'])
def ping():
    return "pong"
