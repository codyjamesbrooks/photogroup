import os
from flask import Flask
from config import config
from . import routes


def create_app():
    app = Flask(__name__)

    config_name = os.getenv('FLASK_CONFIG')
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    app.register_blueprint(routes.bp)

    return app