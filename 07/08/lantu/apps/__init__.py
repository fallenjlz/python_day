#!/usr/bin/env python

from flask import Flask
from apps.views import index_bp
from apps.views.blog_view import blog_bp
from apps.views.ent_view import ent_bp
from apps.views.house_view import house_bp
from settings import DevelopmentConfig

def create_app():
	app = Flask(__name__, template_folder='../templates')
	app.config.from_object(DevelopmentConfig)
	app.register_blueprint(blog_bp)
	app.register_blueprint(ent_bp)
	app.register_blueprint(house_bp)
	app.register_blueprint(index_bp)
	return app
