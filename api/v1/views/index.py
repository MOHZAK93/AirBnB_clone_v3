#!/usr/bin/python3
""" """
from flask import Blueprint, jsonify
from models import storage
from models.state import State
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def get_status():
    """Confirm status of route"""
    return jsonify({'status': 'OK'})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def object_status():
    """Create endpoint that retrieves the number of each objects by type"""
    objs = {"amenity": 'Amenity', "cities": 'City', "places": 'Place',
            "reviews": 'Review', "states": 'State', "users": 'User'}
    for k, v in objs.items():
        objs[k] = storage.count(v)
    return jsonify(objs)
