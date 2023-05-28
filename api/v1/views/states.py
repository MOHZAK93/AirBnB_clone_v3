#!/usr/bin/python3
"""View for State objects that handles all
defualt RESTFul API actions
"""
from flask import Blueprint, jsonify, request, abort
from api.v1.views import app_views
from models.state import State
from models import storage


@app_views.route('/states', method=['GET', 'POST'], strict_slashes=False)
def states():
    """Creates new view for State objects"""
    if request.method == 'GET':
        return jsonify([val.to_dict() for val in storage.all('State')
                        .values()])
    elif request.method == 'POST':
        post = request.get_json()
        if post is None or type(post) != dict:
            return jsonify({"error": "Not a JSON"}), 400
        elif post.get("name") is None:
            return jsonify({"error": "Missing name"}), 400
        new_state = State(**post)
        new_state.save()
        return jsonify(new_state.to_dict()), 201

    @app_views.route('/states/<string:state_id>',
                     method=["GET", "PUT", "DELETE"], strict_slashes=False)
    def get_state_id(state_id):
        """Retrieves a state object with a specific id"""
        state = storage.get("State", state_id)
        if state is None:
            abort(404)
        elif request.method == "GET":
            return jsonify(state.to_dict())
        elif request.method == "DELETE":
            state = storage.get("State", state_id)
            storage.delete(state)
            storage.save()
            return jsonify({}), 200
        elif request.method == "PUT":
            put = request.get_json()
            if put is None or type(put) != dict:
                return jsonify({"error": "Not a JSON"}), 400
            for k, v in put.items():
                if k not in ['id', 'created_at', 'updated_at']:
                    setattr(state, k, v)
                    storage.save()
            return jsonify(state.to_dict()), 200