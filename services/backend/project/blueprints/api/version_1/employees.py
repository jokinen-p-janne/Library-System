from project.blueprints.api.version_1 import bp


@bp.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    pass


@bp.route('/employees', methods=['GET'])
def get_employees():
    pass


@bp.route('/employees', methods=['POST'])
def create_employee():
    pass


@bp.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    pass
