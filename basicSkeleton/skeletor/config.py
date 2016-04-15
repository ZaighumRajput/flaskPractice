import os

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string' 
	


	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True







#will be passed to the Flask app
config = {
	'development' : DevelopmentConfig,
	#'testing': TestingConfig,
	#'production': ProductionConfig,
	'default': DevelopmentConfig
}
