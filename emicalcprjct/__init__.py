from flask import Flask
from .main import main
from .extensions import mongo
from .cal import app
def create_app(config_object='emicalcprjct.settings'):
	app=Flask(__name__)
	app.config.from_object(config_object)
	mongo.init_app(app)

	app.register_blueprint(cal)
	return app

