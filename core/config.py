import os
from dotenv import load_dotenv

dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '.env'))

load_dotenv(dotenv_path)


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/authorprod.db'
    SQLALCHEMY_ECHO = False
    JWT_SECRET_KEY = 'JWT-SECRET'
    SECRET_KEY = 'SECRET-KEY'
    SECURITY_PASSWORD_SALT = 'SECRET-KEY-PASSWORD'
    MAIL_DEFAULT_SENDER = 'http://127.0.0.1:5000/'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = '<youremailaddress>'
    MAIL_PASSWORD = '<yourpassword>'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    UPLOAD_FOLDER = 'images'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
    SQLALCHEMY_ECHO = False
    JWT_SECRET_KEY = 'JWT-SECRET'
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SECURITY_PASSWORD_SALT = 'SECRET-KEY-PASSWORD'
    MAIL_DEFAULT_SENDER = 'http://127.0.0.1:5000/'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = os.environ.get('EMAIL')
    MAIL_PASSWORD = os.environ.get('PASSWORD')
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    UPLOAD_FOLDER = 'images'


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///authortest.db'
    SQLALCHEMY_ECHO = False
    JWT_SECRET_KEY = 'JWT-SECRET'
    SECRET_KEY = 'SECRET-KEY'
    SECURITY_PASSWORD_SALT = 'SECRET-KEY-PASSWORD'
    MAIL_DEFAULT_SENDER = 'http://127.0.0.1:5000/'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = '<youremailaddress>'
    MAIL_PASSWORD = '<yourpassword>'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    UPLOAD_FOLDER = 'images'
