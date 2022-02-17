import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUGA = False
    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY")


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    DEBUG = True

