import os
from flask import Flask, render_template, request
from flask_assets import assets, Environment, Bundle

app = Flask(__name__)

env = assets.Environment(app)

# Tell flask-assets where to look for our coffeescript and sass files.

#env.load_path = [
#    os.path.join(os.path.dirname(__file__), 'sass'),
#    os.path.join(os.path.dirname(__file__), 'coffee'),
#    os.path.join(os.path.dirname(__file__), 'bower_components'),
#]

#env.register(
#   'js_all',
#    assets.Bundle(
#        'jquery/dist/jquery.min.js',
#        assets.Bundle(
#            'all.coffee',
#            filters=['coffeescript']
#        ),
#        output='js_all.js'
#    )
#)

env.register(
    'css_main',
    assets.Bundle(
        'main.sass',
        filters='sass',
        output='css_main.css'
    )
)

#assets = Environment(app)
#assets.url = app.static_url_path
#scss = Bundle('sass/main.scss', filters='pyscss', output='all.css')
#assets.register('scss_all', scss)

@app.route("/home")
def index():
	return render_template('index.html')

if __name__ == "__main__":
	app.run(host="127.0.0.1", port=5000,debug=True)