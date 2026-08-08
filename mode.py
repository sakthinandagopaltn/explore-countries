from constants import SHORT_DISTANCE_LIMIT
from constants import MEDIUM_DISTANCE_LIMIT

def find_mode(distance):
    """
    Suggest a mode of transport based purely on distance.
    Assumption: assumes car/bus/flight options exist between any source
    and destination — does not account for real-world route availability
    (e.g. no roads across oceans, no direct flights between some city pairs).
    """
    if 0 < distance < SHORT_DISTANCE_LIMIT:
        return "Car/Bus"
    elif 0 < distance < MEDIUM_DISTANCE_LIMIT:
        return "Short-haul flight"
    elif distance==0:
        return "You are right there!!!"
    else:
        return "Long-haul flight"