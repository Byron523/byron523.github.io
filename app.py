from flask import Flask, render_template, request, url_for, flash, session
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from sqlalchemy import text

#my functions
from databases import Comments, Transport
from ride import ref_number

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sample.db'
db = SQLAlchemy(app)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#home page
@app.route("/", methods=["GET", "POST"])
def index():

	if request.method == "POST":
		n = request.form.get("username")
		e = request.form.get('mail')
		c =request.form.get('comments')
		d = datetime.now()

		comment = Comments(n, e, c, d)

		db.session.add(comment)
		db.session.commit()

		sql = text('SELECT * FROM comments ORDER BY date DESC LIMIT 5')
		re = db.engine.execute(sql)

		return render_template("/home.html", items=re)
	else:
		sql = text('SELECT * FROM comments ORDER BY date DESC LIMIT 5')
		re = db.engine.execute(sql)

		return render_template("/home.html", items=re)

#checking local exchange rates
@app.route("/exchange", methods=["GET", "POST"])
def exchange():
	return render_template("exchange.html")

#booking accomodation
@app.route("/ride", methods=["GET", "POST"])
def ride():

	if request.method == "POST":

		name = request.form.get("first")
		last = request.form.get("last")
		mail = request.form.get("email")
		day = request.form.get("days")
		ref = 'NA-' + ref_number()
		d = datetime.now()

		t = Transport(ref, name, last, mail, day, d)
		db.session.add(t)
		db.session.commit()

		check1 = text('SELECT * FROM transport WHERE name = :name')
		item = db.engine.execute(check1, name=name)
		item = [tuple(row) for row in item]

		return render_template("output.html", items=item)

	else:
		return render_template("ride.html")

@app.route("/about")
def about():
	return render_template("about.html")

if __name__ == '__main__':
	app.run(debug=True)