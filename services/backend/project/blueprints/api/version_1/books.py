from project.blueprints.api.version_1 import bp


@bp.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    pass


@bp.route('/books', methods=['GET'])
def get_books():
    pass


@bp.route('/books', methods=['POST'])
def create_book():
    pass


@bp.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    pass
