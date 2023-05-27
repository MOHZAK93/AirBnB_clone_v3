#!/usr/bin/python3
""" """
from flask import Flask, Blueprint, jsonify
from os import getenv
from models import storage
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_db_session(errpr):
    """For slash routing"""
    storage.close()


if __name__ == "__main__":
    HBNB_API_HOST = getenv("HBNB_API_HOST")
    HBNB_API_PORT = getenv("HBNB_API_PORT")
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT,
            threaded=True, debug=True)
