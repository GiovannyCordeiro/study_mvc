import json
from models.machine import db
from services.user_service import insert_logic, create_logic

class MachineController:
    def index():
        return {
        'status': 'OK',
        'localhost:5000/machines/create': 'Create table in mysql database',
        'localhost:5000/machines/insert': 'Insert data in mysql database table(Inserttable)'
    }

    def create():
        create_logic()
    
    def insert():
        insert_logic()
