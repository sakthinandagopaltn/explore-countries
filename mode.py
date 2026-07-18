from constants import SHORT_DISTANCE_LIMIT
from constants import MEDIUM_DISTANCE_LIMIT

def find_mode(distance):
    if distance < SHORT_DISTANCE_LIMIT:
        return "Car/Bus"
    elif distance < MEDIUM_DISTANCE_LIMIT:
        return "Short-haul flight"
    else:
        return "Long-haul flight"