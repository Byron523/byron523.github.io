from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sample.db'
db = SQLAlchemy(app)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

class Comments(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(100))
	email = db.Column(db.String(100))
	comment = db.Column(db.String(255))
	date = db.Column(db.String(50))

	def __init__(self, name, email, comment, date):
		self.name = name
		self.email = email
		self.comment = comment
		self.date = date

class Transport(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	ref = db.Column(db.Integer, unique=True)
	name = db.Column(db.String(100))
	last = db.Column(db.String(100))
	email = db.Column(db.String(100))
	days = db.Column(db.Integer)
	date = db.Column(db.String(50))

	def __init__(self, ref, name, last, email, days, date):
		self.ref = ref
		self.name = name
		self.last = last
		self.email = email
		self.days = days
		self.date = date