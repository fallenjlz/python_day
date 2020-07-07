class Config:
	Debug = False
	Testing = False
	DATABASE_URI = ''

class DevelopmentConfig(Config):

	DEBUG = True
	ENV = 'development'


class ProductionConfig(Config):
	DATABASE_URI = ''

class TestingConfig(Config):
	TESTING = True

