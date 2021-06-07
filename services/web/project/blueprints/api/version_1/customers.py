from project.blueprints.api.version_1 import bp


@bp.route('/customers/<int:id>', methods=['GET'])
def get_customer(id):
    pass


@bp.route('/customers', methods=['GET'])
def get_customers():
    pass


@bp.route('/customers/<int:id>/loans', methods=['GET'])
def get_loans(id):
    pass


@bp.route('/customers', methods=['POST'])
def create_customer():
    pass


@bp.route('/customers/<int:id>', methods=['PUT'])
def update_customer(id):
    pass
