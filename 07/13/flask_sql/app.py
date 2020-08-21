from flask_sqlalchemy import SQLAlchemy

import settings

from flask import Flask

app = Flask(__name__)
app.config.from_object(settings.DevelopmentConfig)

db = SQLAlchemy(app)

class User(db.Model):

	id = db.Column(db.Integer, primary_key = True, autoincrement = True)
	username = db.Column(db.String(10),nullable = False)
	password = db.Column(db.String(10), nullable=False)
	phone = db.Column(db.String(11), nullable = False)

def __str__(self):
	return self.username

class Goods(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(50), nullable = False)
	price = db.Column(db.Float, nullable = False)



if __name__ == '__main__':
	db.create_all()
	app.run()
