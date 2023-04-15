#!/usr/bin/python3
"""a fancy friggin' Review module for our high-class RESTful API"""
from api.v1.views import app_views
from flask import jsonify, request, abort
from models import storage
from models.review import Review
from models.place import Place
from models.user import User


@app_views.route('/places/<place_id>/reviews', methods=['GET'],
                 strict_slashes=False)
def show_me_the_reviews_darling(place_id):
    """Fetches a list of reviews for this ratchet place"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    reviews = [review.to_dict() for review in place.reviews]
    return jsonify(reviews)


@app_views.route('/reviews/<review_id>', methods=['GET'],
                 strict_slashes=False)
def spill_the_tea(review_id):
    """Fetches a single review, complete with Yelp-worthy snobbery"""
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    return jsonify(review.to_dict())


@app_views.route('/reviews/<review_id>', methods=['DELETE'],
                 strict_slashes=False)
def flush_review_down_the_toilet(review_id):
    """Deletes a review, just like flushing of one-ply toilet paper"""
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    storage.delete(review)
    storage.save()
    return jsonify({}), 200


@app_views.route('/places/<place_id>/reviews', methods=['POST'],
                 strict_slashes=False)
def create_the_next_rant(place_id):
    """Create a new review to slam the place,
    just like a Yelp elitist should"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)

    data = request.get_json()
    if data is None:
        abort(400, 'Not a JSON')

    user_id = data.get('user_id')
    if user_id is None:
        abort(400, 'Missing user_id')

    user = storage.get(User, user_id)
    if user is None:
        abort(404)

    text = data.get('text')
    if text is None:
        abort(400, 'Missing text')

    review = Review(place_id=place_id, user_id=user_id, text=text)
    storage.new(review)
    storage.save()
    return jsonify(review.to_dict()), 201


@app_views.route('/reviews/<review_id>', methods=['PUT'],
                 strict_slashes=False)
def polish_that_turd(review_id):
    """Updates a review, hoping to make it sound as fancy as possible"""
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)

    data = request.get_json()
    if data is None:
        abort(400, 'Not a JSON')

    for key, value in data.items():
        if key not in ['id', 'user_id',
                       'place_id', 'created_at', 'updated_at']:
            setattr(review, key, value)
    storage.save()
    return jsonify(review.to_dict()), 200
