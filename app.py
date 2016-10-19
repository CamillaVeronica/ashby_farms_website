import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/home")
def index():
	return render_template('index.html')

@app.route("/properties")
def our_properties():
	return render_template('OurProperties.html')

@app.route("/properties/default")
def property_template():
	return render_template('property_template.html')

@app.route("/properties/lodges")
def lodges():
	return render_template('lodges.html')

@app.route("/properties/roughlands")
def roughlands():
	return render_template('roughlands.html')

@app.route("/properties/springcottages")
def springcottages():
	return render_template('springcottages.html')

@app.route("/properties/oldfarm")
def oldfarm():
	return render_template('oldfarm.html')

@app.route("/properties/65street")
def street65():
	return render_template('65street.html')

@app.route("/contactus")
def contactus():
	return render_template('contact.html')

@app.route("/activities")
def activities():
	return render_template('activities.html')

@app.route("/shoot")
def shooting():
	return render_template('shooting.html')

@app.route("/fish")
def fishing():
	return render_template('fishing.html')

@app.route("/aboutus/history")
def history():
	return render_template('history.html')

@app.route("/book")
def book():
	return render_template('book.html')

@app.route("/book/prices")
def price_list():
	return render_template('price_list.html')

@app.route("/book/form")
def booking_form():
	return render_template('booking_form.html')

@app.route("/book/holiday")
def holiday_booking():
	return render_template('booking_holiday.html')

@app.route("/blog")
def blog():
	return render_template('blog.html')

if __name__ == "__main__":
	app.run(host="127.0.0.1", port=5000,debug=True)