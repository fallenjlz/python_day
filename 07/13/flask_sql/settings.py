class Config:
	Debug = False
	Testing = False
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:goodluck2019@127.0.0.1:3306/practice'

class DevelopmentConfig(Config):

	DEBUG = True
	ENV = 'development'


class ProductionConfig(Config):
	DATABASE_URI = ''

class TestingConfig(Config):
	TESTING = True

