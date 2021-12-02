import os
class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/prod_author_manager' #  <Production DB URL>
    SQLALCHEMY_ECHO = False
    JWT_SECRET_KEY= '5f108c7af7baa5974b6ff804755ae14e'
    SECRET_KEY = '0dd2ee80c87f66cd357a32222b647180'
    SECURITY_PASSWORD_SALT = '9e7c2d846ff68d43c756c3c7a78ef766'
    MAIL_DEFAULT_SENDER= os.environ.get('EMAIL_ADDR') # 'your_email_address'
    MAIL_SERVER= 'smtp.googlemail.com' # 'email_providers_smtp_address'
    MAIL_PORT= 587 # '<mail_server_port>'
    MAIL_USERNAME= os.environ.get('EMAIL_ADDR')   # 'your_email_address'
    MAIL_PASSWORD= os.environ.get('EMAIL_PASS')   # 'your_email_password'
    MAIL_USE_TLS= False
    MAIL_USE_SSL= True
    UPLOAD_FOLDER= 'images'
    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/dev_author_manager' # <Development DB URL>
    SQLALCHEMY_ECHO = False
    JWT_SECRET_KEY = 'e039c32a48a52dd91cde83244b33c68e'
    SECRET_KEY = '2415fc81fc6e2efa72e9ac96f0103028'
    SECURITY_PASSWORD_SALT = '6c22a001d37733eb92449581b0bb3771'
    MAIL_DEFAULT_SENDER= os.environ.get('EMAIL_ADDR')  # 'your_email_address'
    MAIL_SERVER= 'smtp.gmail.com' # 'email_providers_smtp_address'
    MAIL_PORT= 465 # '<mail_server_port>'
    MAIL_USERNAME= os.environ.get('EMAIL_ADDR')   # 'your_email_address'
    MAIL_PASSWORD= os.environ.get('EMAIL_PASS')   # 'your_email_password'
    MAIL_USE_TLS= False
    MAIL_USE_SSL= True
    UPLOAD_FOLDER= 'images'
    
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = '' # <Testing DB URL>
    SQLALCHEMY_ECHO = False
    JWT_SECRET_KEY = 'dab49619ff2cfc5622de9d8d82eb8d24'
    SECRET_KEY = '5a382f1bd6656f68e61f7d18131316b2'
    SECURITY_PASSWORD_SALT = '989321b0d9cfaff57011e308f250ad93'
    MAIL_DEFAULT_SENDER= os.environ.get('EMAIL_ADDR')  # 'your_email_address'
    MAIL_SERVER= 'smtp.gmail.com' # 'email_providers_smtp_address'
    MAIL_PORT= 465 # '<mail_server_port>'
    MAIL_USERNAME= os.environ.get('EMAIL_ADDR')   # 'your_email_address'
    MAIL_PASSWORD= os.environ.get('EMAIL_PASS')   # 'your_email_password'
    MAIL_USE_TLS= False
    MAIL_USE_SSL= True
    UPLOAD_FOLDER= 'images'
