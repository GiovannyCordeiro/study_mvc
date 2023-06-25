from flask import Blueprint
from controllers.machineController import index, create, insert

blueprint = Blueprint('blueprint', __name__)

blueprint.route('/', method=['GET'])(index)
blueprint.route('/create', method=['GET'])(create)
blueprint.route('/insert', method=['GET'])(insert)