#!/usr/bin/python3
from flask import Flask, render_template, abort, make_response, jsonify
from flask_cors import CORS
from models import storage
from os import getenv
from api.v1.views import app_views
from flasgger import Swagger
# app
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})
app.url_map.strict_slashes=False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
swagger = Swagger(app)

@app.errorhandler(404)
def page_not_found(e):
    return make_response(jsonify({"error": "Not found"}), 404)

@app.teardown_appcontext
def close(exception):
    storage.close()

if __name__ == "__main__":
    apiHost = getenv("HBNB_API_HOST") or "0.0.0.0"
    apiPort = getenv("HBNB_API_PORT") or 5000
    app.run(host=apiHost, port=apiPort, threaded=True)
