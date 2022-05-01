from flask import Flask,Blueprint
from flask_migrate import Migrate
from flask_migrate import Migrate

import json
import os
from .views import main
from .extensions import db
from .model import *
migrate = Migrate()
def create_app(config_files='settings.py'):
    app=Flask(__name__)
    app.config.from_pyfile(config_files)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(main)

    return app








