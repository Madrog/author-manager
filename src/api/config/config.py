import os
class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_DEFAULT_SENDER= 'your_email_address'
    MAIL_SERVER= 'email_providers_smtp_address'
    MAIL_PORT= '<mail_server_port>'
    MAIL_USERNAME= os.environ.get('EMAIL_ADDR')   # 'your_email_address'
    MAIL_PASSWORD= os.environ.get('EMAIL_PASS')   # 'your_email_password'
    MAIL_USE_TLS= False
    MAIL_USE_SSL= True
    UPLOAD_FOLDER= 'images'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/prod_author_manager' #  <Production DB URL>
    SECRET_KEY = '0dd2ee80c87f66cd357a32222b647180'
    SECURITY_PASSWORD_SALT = '9e7c2d846ff68d43c756c3c7a78ef766'
    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/dev_author_manager' # <Development DB URL>
    SQLALCHEMY_ECHO = False
    SECRET_KEY = '2415fc81fc6e2efa72e9ac96f0103028'
    SECURITY_PASSWORD_SALT = '6c22a001d37733eb92449581b0bb3771'
    
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/test_author_manager' # <Testing DB URL>
    SQLALCHEMY_ECHO = False
    SECRET_KEY = '5a382f1bd6656f68e61f7d18131316b2'
    SECURITY_PASSWORD_SALT = '989321b0d9cfaff57011e308f250ad93'
