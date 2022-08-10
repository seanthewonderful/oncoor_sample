from os import environ

FLASK_APP = environ.get('FLASK_APP')
FLASK_ENV = environ.get('FLASK_ENV')
POSTGRES_URI = environ.get('POSTGRES_URI')
SECRET_KEY = environ.get('SECRET_KEY')
SQLALCHEMY_TRACK_MODIFICATIONS = environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
GMAIL_PW = environ.get('GMAIL_PW')
SENDER_EMAIL = environ.get('SENDER_EMAIL')
RECEIVER_EMAIL = environ.get('RECEIVER_EMAIL')