class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/prod_author_manager' #  <Production DB URL>

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/dev_author_manager' # <Development DB URL>
    SQLALCHEMY_ECHO = False

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/test_author_manager' # <Testing DB URL>
    SQLALCHEMY_ECHO = False

