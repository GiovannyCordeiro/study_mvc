from flask import Flask
from flask_migrate import Migrate
from routes.blueprint import blueprint
from models.machine import db

class App:
    def __init__(self):
        self.app = self.create_app()
    
    def create_app(self):
        app = Flask(__name__)
        app.config.from_object('config')
        db.init_app(app)
        return app
    
    
    def run(self):
        if __name__ == '__main__':
            self.app.run(host='127.0.0.1', port=5000, debug=True)

app = App()
app.run()