from api import iscity
from api import isplace
from exactlocation import choose_one

def check_location(location):

    city_matches = iscity(location)
    if city_matches:
        return choose_one(city_matches, "city")
 
    place_matches = isplace(location)
    if place_matches:
        return choose_one(place_matches, "place")
 
    return None