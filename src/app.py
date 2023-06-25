from flask import Flask
from flask_migrate import Migrate
from routes.blueprint import blueprint
from models.machine import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    db.init_app(app)
    return app

app = create_app()
app.register_blueprint(blueprint, url_prefix='/machines')
migrate = Migrate(app,db)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)