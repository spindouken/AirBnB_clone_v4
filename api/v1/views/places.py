#!/usr/bin/python3
"""MTV Cribs edition of Place API views"""
from models.place import Place
from models.city import City
from models.user import User
from api.v1.views import app_views
from flask import jsonify, request, make_response, abort
from models import storage


@app_views.route('/cities/<city_id>/places', methods=['GET'],
                 strict_slashes=False)
def show_me_all_the_cribs(city_id=None):
    """
    Show me all the cribs...
    Endpoint to retrieve all Place objects of a City
    (Uses city_id to retrieve city object and get all associated places)
    """
    if city_id:
        city = storage.get(City, city_id)
        if city is not None:
            placeList = [place.to_dict() for place in city.places]
            return jsonify(placeList)
        else:
            return abort(404)


@app_views.route('/places/<place_id>', methods=['GET'],
                 strict_slashes=False)
def one_single(place_id=None):
    """
    A single dope crib...
    Endpoint to retrieve a specific Place object
    (Uses the place_id to fetch the associated Place object)
    """
    if place_id:
        place = storage.get(Place, place_id)
        if place:
            return jsonify(place.to_dict())
        else:
            return abort(404)


@app_views.route('/places/<place_id>', methods=['DELETE'],
                 strict_slashes=False)
def we_dont_need_no_water(place_id):
    """
    let the place burn...
    Endpoint to delete a specific Place object
    (Uses the place_id to fetch the associated
    Place object and delete it from storage)
    """
    crib = storage.get(Place, place_id)
    if crib is None:
        abort(404)
    storage.delete(crib)
    storage.save()
    return jsonify({}), 200


@app_views.route('/cities/<city_id>/places', methods=['POST'],
                 strict_slashes=False)
def bobby_builder(city_id):
    """
    Show all the JSON crib data...
    Endpoint to create a new Place object
    (Uses the city_id to associate the new Place object with a City,
    Validates the JSON request data,
    and creates a new Place object accordingly)
    """
    city = storage.get(City, city_id)
    if city is None:
        return abort(404)
    if not request.get_json():
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    if 'user_id' not in request.get_json():
        return make_response(jsonify({"error": "Missing user_id"}), 400)
    if 'name' not in request.get_json():
        return make_response(jsonify({"error": "Missing name"}), 400)
    places = request.get_json()
    user = storage.get(User, places['user_id'])
    if user is None:
        abort(404)
    places['city_id'] = city_id
    newPlace = Place(**places)
    newPlace.save()
    return make_response(jsonify(newPlace.to_dict()), 201)


@app_views.route("/places/<place_id>", methods=['PUT'],
                 strict_slashes=False)
def put_place(place_id):
    """placeholder test"""
    place = storage.get(Place, place_id)
    if place is None:
        return abort(404)
    data = request.get_json()
    if data is None:
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    notThese = ["id", "created_at", "updated_at", "city_id", "user_id"]
    for key, value in data.items():
        if key not in notThese:
            setattr(place, key, value)
    storage.save()
    return make_response(jsonify(place.to_dict()), 200)
