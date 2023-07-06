from flask import Blueprint
from controllers.machineController import MachineController

blueprint = Blueprint('blueprint', __name__)

blueprint.route('/', methods=['GET'])(MachineController.index)
blueprint.route('/create', methods=['GET'])(MachineController.create)
blueprint.route('/insert', methods=['GET'])(MachineController.insert)
blueprint.route('/sum/<int:num1>', methods=['GET'])(MachineController.countRouter)