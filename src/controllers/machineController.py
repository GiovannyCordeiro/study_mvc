import json
from models.machine import db
from services.user_service import UserService

class MachineController:
    def index():
        return {
    }

    def create():
        UserService.create_logic()
    
    def insert():
        UserService.insert_logic()


class ClasseInutil:
    def metodoInutil():
        print("print mais inutil ainda")