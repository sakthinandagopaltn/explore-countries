import requests
from constants import API_BASE_URL


def safe_get(url):
    """Make a GET request, returning None on any connection/SSL failure instead of crashing."""
    try:
        return requests.request("GET", url, timeout=10)
    except requests.exceptions.RequestException:
        return None

def iscountry(country):
        """check if the given place is a country"""
        yescountry = safe_get(API_BASE_URL+"name/"+country.lower())
        if yescountry.status_code != 200:
                return False   # no match found, not a country
        yescountry=yescountry.json()
        if not yescountry:
                return False
        return True


def get_country_details_by_name(name):
    """Fetch full country data by name, using an exact match against results"""
    response = safe_get(API_BASE_URL + "name/" + name.lower())
    if response is None or response.status_code != 200:
        return None
    data = response.json()
    if not data:
        return None
 
    # If the API returns a single dict (not a list), just return it directly
    if isinstance(data, dict):
        return data
 
    # Otherwise, data is a list of loosely-matched countries — find the exact match
    for country in data:
        if country['name'].lower() == name.lower():
            return country
 
    # No exact match (e.g. "Iran" only matches "Iran (Islamic Republic of)") —
    # fall back to the shortest matching name, which is usually the common one
    matches = [c for c in data if name.lower() in c['name'].lower()]
    if matches:
        return min(matches, key=lambda c: len(c['name']))
 
    return None
  

               
def iscity(city):
        yescity=safe_get(API_BASE_URL+"cities?q="+city.lower())
        
        if yescity.status_code != 200:
                return False   # no match found
        yescity=yescity.json()
        if not yescity:
                return None
        """Find all cities whose name contains what the user typed"""
        matches = [c for c in yescity if city.lower() in c['name'].lower()]
        if not matches:
                return None
        """Return all the cities matching the given string"""
        return matches

def isplace(place):
        yesplace=safe_get(API_BASE_URL+"places?q="+place.lower())
    
        if yesplace.status_code != 200:
                return False   # no match found
        yesplace=yesplace.json()
        if not yesplace:
                return None
        matches = [c for c in yesplace if place.lower() in c['name'].lower()]
        if not matches:
                return None
        """ Return all matches"""
        return matches

def get_country_details(country_code):
    """Fetch full country data (currency, languages, calling code) by ISO code."""
    response = safe_get(API_BASE_URL + "alpha/" + country_code)  # adjust path once confirmed
    if response.status_code != 200:
        return None
    data = response.json()
    if not data:
        return None
    # some APIs return a list even for a single code match — handle both cases
    if isinstance(data, list):
        return data[0] if data else None
    return data

def calculate_distance(sid,did,slat,slng,dlat,dlng):
        url=API_BASE_URL+"distance?from="+str(sid)+"&to="+str(did)+"&lat1="+str(slat)+"&lng1="+str(slng)+"&lat2="+str(dlat)+"&lng2="+str(dlng)
        distance=safe_get(url)
        if distance.status_code !=200:
                return False
        distance=distance.json()
        return distance["distanceKm"]

def get_cities_in_country(country_code, limit=20):
    """Fetch a list of cities in a given country, sorted by population."""
    response = safe_get(f"{API_BASE_URL}cities?country={country_code}")
    if response is None or response.status_code != 200:
        return None
    data = response.json()
    if not data:
        return None
    return data[:limit]