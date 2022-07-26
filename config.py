
class Config(object):
    DEBUG = False
    TESTING = False
    
    SECRET_KEY = "a74ff61d1310200933d3b7201ba3ba00"
    
    DB_NAME = "production-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "example"
    
    GMAIL_PW = "fdadisgioynmjxig"
    POSTGRES_URI = "postgresql:///oncoor_db"
    
class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    
    DB_NAME = "development-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "example"
    
    GMAIL_PW = "fdadisgioynmjxig"
    POSTGRES_URI = "postgresql:///oncoor_db"
    
class TestingConfig(Config):
    TESTING = True
    
    DB_NAME = "development-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "example"
    
    GMAIL_PW = "fdadisgioynmjxig"
    POSTGRES_URI = "postgresql:///oncoor_db"