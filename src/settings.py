from os import environ


class Config:
    DEBUG = False
    DEVELOPMENT = False
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')
    POSTGRES_URI = environ.get('POSTGRES_URI')
    SECRET_KEY = environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    GMAIL_PW = environ.get('GMAIL_PW')
    SENDER_EMAIL = environ.get('SENDER_EMAIL')
    RECEIVER_EMAIL = environ.get('RECEIVER_EMAIL')
    
class ProductionConfig(Config):
    pass

class StagingConfig(Config):
    DEBUG = True

class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True