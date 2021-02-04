import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY', 'secret')
	STREAM_API_KEY = '9r7t89tmg2ur'
	STREAM_SECRET = '45b9mb84ukm2smh548vwp5e5kqt2u3pk49xhb8skuru7b26ryws2jvy3emc2vqva'

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \ 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \ 'sqlite://''
	WTF_CSRF_ENABLED = False
class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get(‘DATABASE_URL’) or \ 'sqlite:///'' + os.path.join(basedir, 'data/sqlite')

	@classmethod
	def init_app(cls, app):
		Config.init_app(app)

config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'production': ProductionConfig,
	
	'default': DevelopmentConfig
} 