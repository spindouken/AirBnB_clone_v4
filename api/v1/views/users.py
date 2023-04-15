#!/usr/bin/python3
"""A highly RESTful User API
(Users API routing)
"""
from flask import jsonify, request, abort, make_response
from api.v1.views import app_views
from models import storage
from models.user import User


@app_views.route('/users', methods=['GET'],
                 strict_slashes=False)
def grabdaHomies():
    """hootie hoo"""
    homies = [user.to_dict() for user in storage.all(User).values()]
    return jsonify(homies)


@app_views.route('/users/<user_id>', methods=['GET'],
                 strict_slashes=False)
def findtheOne(user_id):
    """red pill"""
    neo = storage.get(User, user_id)
    if neo is None:
        abort(404)
    return jsonify(neo.to_dict())


@app_views.route('/users/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
def to_the_curb(user_id):
    """DELETED. Bye, Felicia!"""
    felicia = storage.get(User, user_id)
    if felicia is None:
        abort(404)
    storage.delete(felicia)
    storage.save()
    return jsonify({}), 200


@app_views.route('/users', methods=['POST'],
                 strict_slashes=False)
def whippin():
    """in the kitchen"""
    spaghetti = request.get_json()
    if spaghetti is None:
        abort(400, 'Not a JSON')
    if 'email' not in spaghetti:
        abort(400, 'Missing email')
    if 'password' not in spaghetti:
        abort(400, 'Missing password')
    lilHomie = User(**spaghetti)
    lilHomie.save()
    return jsonify(lilHomie.to_dict()), 201


@app_views.route('/users/<user_id>', methods=['PUT'],
                 strict_slashes=False)
def give_user_a_makeover(user_id):
    """Sprucing up this User with some fresh deets"""
    user_to_fix = storage.get(User, user_id)
    if user_to_fix is None:
        abort(404)
    fresh_deets = request.get_json()
    if fresh_deets is None:
        abort(400, 'Not a JSON')
    for key, value in fresh_deets.items():
        if key not in ['id', 'email', 'created_at', 'updated_at']:
            setattr(user_to_fix, key, value)
    user_to_fix.save()
    return jsonify(user_to_fix.to_dict()), 200
