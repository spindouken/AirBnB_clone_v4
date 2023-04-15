#!/usr/bin/python3
"""Chillin' with Amenities
(Amenities API routing)
"""
from flask import jsonify, request, abort, make_response
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity


@app_views.route('/amenities', methods=['GET'],
                 strict_slashes=False)
def chill_with_amenities():
    """kick back and get all amenity objects"""
    amenities = [amenity.to_dict() for amenity
                 in storage.all(Amenity).values()]
    return jsonify(amenities)


@app_views.route('/amenities/<amenity_id>', methods=['GET'],
                 strict_slashes=False)
def relax_with_amenity(amenity_id):
    """chill with a specific amenity object"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    return jsonify(amenity.to_dict())


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
def remove_amenity(amenity_id):
    """say goodbye to an amenity object"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    storage.delete(amenity)
    storage.save()
    return jsonify({}), 200


@app_views.route('/amenities', methods=['POST'],
                 strict_slashes=False)
def create_amenity():
    """add a freshy fresh amenity object"""
    body = request.get_json()
    if body is None:
        abort(400, 'Not a JSON')
    if 'name' not in body:
        abort(400, 'Missing name')
    amenity = Amenity(**body)
    amenity.save()
    return jsonify(amenity.to_dict()), 201


@app_views.route('/amenities/<amenity_id>', methods=['PUT'],
                 strict_slashes=False)
def update_amenity(amenity_id):
    """refreshy fresh a specific amenity object"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    body = request.get_json()
    if body is None:
        abort(400, 'Not a JSON')
    for key, value in body.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(amenity, key, value)
    amenity.save()
    return jsonify(amenity.to_dict()), 200
