#!/usr/bin/python3
"""Starting flask app"""
from flask import Flask, render_template
from models import storage
import uuid
from models.state import State
from models.amenity import Amenity
from models.place import Place


"""flask req"""
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """close after"""
    storage.close()


@app.route('/1-hbnb', strict_slashes=False)
def hbnb_filters(the_id=None):
    """routing for 0-hbnb"""
    state_objs = storage.all('State').values()
    states = dict([state.name, state] for state in state_objs)
    amenities = storage.all('Amenity').values()
    places = storage.all('Place').values()
    users = dict([user.id, "{} {}".format(user.first_name, user.last_name)]
                 for user in storage.all('User').values())
    cache_id = (str(uuid.uuid4()))
    return render_template('1-hbnb.html',
                           states=states,
                           amens=amenities,
                           places=places,
                           users=users,
                           cache_id=cache_id)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
