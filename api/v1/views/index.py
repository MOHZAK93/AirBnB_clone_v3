#!/usr/bin/python3
"""Index file for flask app"""

from flask import Blueprint, jsonify
from models import storage
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def get_status():
    """Confirm status of route"""

    return jsonify({'status': 'OK'})


@app_views.route('/stats', strict_slashes=False)
def object_status():
    """Create endpoint that retrieves the number of each objects by type"""

    objs = {
            "amenities": storage.count('Amenity'),
            "cities": storage.count('City'),
            "places": storage.count('Place'),
            "reviews": storage.count('Review'),
            "states": storage.count('State'),
            "users": storage.count('User')
    }
    return jsonify(objs)
