#!/usr/bin/python3
from models import storage
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import os

os.environ['HBNB_MYSQL_USER'] = 'hbnb_dev'
os.environ['HBNB_MYSQL_PWD'] = 'hbnb_dev_pwd'
os.environ['HBNB_MYSQL_HOST'] = 'localhost'
os.environ['HBNB_MYSQL_DB'] = 'hbnb_dev_db'
os.environ['HBNB_TYPE_STORAGE'] = 'db'


# Create and insert a State object
state = State(name="California")
storage.new(state)
storage.save()
print(f"Saved state: {state}")

# Create and insert a City object
city = City(state_id=state.id, name="San Francisco")
storage.new(city)
storage.save()
print(f"Saved state: {city}")

# Create and insert a User object
user = User(email="test@example.com", password="test_password", first_name="John", last_name="Doe")
storage.new(user)
storage.save()
print(f"Saved state: {user}")

# Create and insert a Place object
place = Place(city_id=city.id, user_id=user.id, name="My house", description="A beautiful house", number_rooms=3,
              number_bathrooms=2, max_guest=6, price_by_night=100, latitude=37.7749, longitude=-122.4194)
storage.new(place)
storage.save()
print(f"Saved state: {place}")

# Create and insert an Amenity object
amenity = Amenity(name="Wi-Fi")
storage.new(amenity)
storage.save()
print(f"Saved state: {amenity}")

# Create and insert a Review object
review = Review(place_id=place.id, user_id=user.id, text="This is a great place to stay!")
storage.new(review)
storage.save()
print("Review saved")
print(f"Saved state: {review}")

# Associate the amenity with the place
place.amenities.append(amenity)
storage.save()

print("Inserted objects:")
print(f"State: {state}")
print(f"City: {city}")
print(f"User: {user}")
print(f"Place: {place}")
print(f"Amenity: {amenity}")
print(f"Review: {review}")
