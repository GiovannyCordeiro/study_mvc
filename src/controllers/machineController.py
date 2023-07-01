import json
from models.machine import db
from services.user_service import UserService

class MachineController:
    def index():
        return {
        'status': 'OK',
        'localhost:8080/machines/create': 'Create table in mysql database',
        'localhost:8080/machines/insert': 'Insert data in mysql database table(Inserttable)'
    }

    def create():
        UserService.create_logic()
    
    def insert():
        UserService.insert_logic()
