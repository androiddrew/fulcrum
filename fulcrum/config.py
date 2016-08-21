import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = b'\x19\xb0\xe5l)\x18\xfb\xfc\x00\xc9"H\x87\x0c\x85\xc7_}\xd0\xa3\xe9\xa5\xb1\x8e\x04\xe8\x1a\x9a\
    x9c\x031\xde'
    DEBUG = False
    ERROR_404_HELP = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ['POSTGRES_DEV_CONFIG_STRING']


class TestingConfig(Config):
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False #Remove Debug tool bar intercept redirects or you won't be able to test them
    TESTING = True


class ProductionConfig(Config):
    pass

config_by_name = dict(dev=DevelopmentConfig,
                      test=TestingConfig,
                      prod=ProductionConfig)

