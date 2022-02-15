from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config
from .site.routes import site
# from .api.routes import api
from .authentication.routes import auth
from .models import db as root_db, login_manager


app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(site)
# app.register_blueprint(api)
app.register_blueprint(auth)

root_db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'auth.signin'
login_manager.login_message = 'You are not logged in.'
login_manager.login_message_category = 'auth-failed'

migrate = Migrate(app, root_db)