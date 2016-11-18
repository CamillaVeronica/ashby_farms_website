import os
from flask import Flask, render_template, request, send_file, current_app as app
from flask_frozen import Freezer

app = Flask(__name__)

@app.route("/index.html")
def index():
	return render_template('index.html', title='Family-run holiday properties with fishing in Kent', meta_description='Self-catering country cottages and fishing lodges set in bluebell woods with fishing available. Family and pet friendly. Located in Woodchurch, Kenardington and Appledore in Kent. Near to the coast, Romney Marsh, Rye and Ashford.')

@app.route("/properties/")
def our_properties():
	return render_template('OurProperties.html', meta_description='We have a selection of properties available for rent allowing you to get away from it all in the Kent countryside. Whether you want a rural retreat or a taste of village life we have options to suit for a weekend break through to longer stays.')

@app.route("/properties/lodges/")
def lodges():
	return render_template('lodges.html', meta_description='Scandanavian-inspired lodges nestled on the banks of two lakes offer an idyllic location for a getaway whether you are looking for a fishing break or a base for exploring the local area. Sleeps 6 people')

@app.route("/properties/roughlands/")
def roughlands():
	return render_template('roughlands.html', meta_description='A country bungalow with its own large garden, set well back from the quiet country road between Appledore and Woodchurch with Roughlands Wood and our fishing lakes in the woods on the North side and open fields on the others. Sleeps 5.')

@app.route("/properties/springcottages/")
def springcottages():
	return render_template('springcottages.html', meta_description='Three terraced Cottages with views to Kenardington Church. The large rear garden backs onto farmland. Sleeps 5.')

@app.route("/properties/oldfarm/")
def oldfarm():
	return render_template('oldfarm.html', meta_description='This flat within a Grade II listed building gives you a chance to see authentic farm life, it is situated on a working farm among fields on the Romney Marsh.')

@app.route("/properties/65street/")
def street65():
	return render_template('65street.html', meta_description='Get a taste of village life with this semi-detached home right in the middle of the picturesque village of Appledore. Small but perfectly formed, its main street lined with period buildings has everything you need; a village shop, tearoom and local pub with hops hanging from the rafters.')

@app.route("/contactus/")
def contactus():
	return render_template('contact.html', meta_description='Get in touch with Ashby Farms about booking your holiday.')

@app.route("/contactus/success/")
def form_submitted():
	return render_template('formsuccess.html', meta_description='Enquiry form submitted successfully.')

@app.route("/activities/")
def activities():
	return render_template('activities.html', meta_description='Highlights of the activities that are available close to Ashby Farms in Kent and Sussex. Includes options for families, culture, outdoor activities and foodies.')

@app.route("/shoot/")
def shooting():
	return render_template('shooting.html', meta_description='Rough shooting is available on our farmland for rabbits and pigeons.')

@app.route("/fish/")
def fishing():
	return render_template('fishing.html', meta_description='Our two fishing lakes are available for fishing year round and are stocked with Bream, Gudgeon, Roach, Rudd, Tench, Common and Mirror Carp (up to 36lb.), Perch.')

@app.route("/aboutus/history/")
def history():
	return render_template('history.html', meta_description='A little about the Ashby family, the history of the business and how we farm.')

@app.route("/book/")
def book():
	return render_template('book.html', meta_description='Information for booking your delf-catering holiday or long-let with Ashby Farms including prices, discounts and terms.')

@app.route("/book/conditions/")
def conditions():
	return render_template('booking_conditions.html', meta_description='Booking conditions')

'''@app.route("/book/form/")
def booking_form():
	try:
		return send_file('static/file/Ashby_Farms_Ltd_Bookingform.pdf', attachment_filename='Ashby_Farms_Ltd_Bookingform.pdf')
	except Exception as e:
		return str(e)'''

@app.route("/blog/")
def blog():
	return render_template('blog.html', meta_description='Our blog with latest news and ideas of things to do in Kent and East Sussex.')

@app.route("/privacy/")
def privacy():
	return render_template('privacypolicy.html', meta_description='Privacy policy')

@app.route("/location/")
def location():
	return render_template('location.html', meta_description='Our self catering properties are in Woodchurch, Kenardington and Appledore with excellent connections for transport and near to Ashford International station.')

@app.route("/aboutus/faq/")
def faq():
	return render_template('faq.html', meta_description='frequently asked questions')

if __name__ == '__main__':
	app.run(host="127.0.0.1", port=5000,debug=True)