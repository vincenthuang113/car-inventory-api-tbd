import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or "You'll never know!"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'splite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False #turn off update messages from sqlalchemy
    