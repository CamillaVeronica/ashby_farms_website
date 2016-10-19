from flask import Flask
from flask import render_template
from flask import request
from flask_assets import Environment, Bundle

app = Flask(__name__)
assets = Environment(app)

#assets.url = app.static_url_path
scss = Bundle('sass/main.scss', filters='pyscss', output='main.css')
assets.register('scss_all', scss)

@app.route("/home")
def index():
	return render_template('index.html')

if __name__ == "__main__":
	app.run(host="127.0.0.1", port=5000,debug=True)