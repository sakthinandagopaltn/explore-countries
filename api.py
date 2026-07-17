import requests
from constants import API_BASE_URL
# get all country names
def iscountry(country):
        yescountry = requests.request("GET",API_BASE_URL+"name/"+country.lower())
        if yescountry.status_code != 200:
                return False   # no match found, not a country
        yescountry=yescountry.json()
        if not yescountry:
                return False
        return True
        
        
def iscity(city):
        yescity=requests.request("GET",API_BASE_URL+"cities?q="+city.lower())
        print("URL called:", yescity.url)
        print("Status code:", yescity.status_code)
        print("Raw response:", yescity.text[:300])
        if yescity.status_code != 200:
                return False   # no match found
        yescity=yescity.json()
        if not yescity:
                return None
        # Find all countries whose name contains what the user typed
        matches = [c for c in yescity if city.lower() in c['name'].lower()]
        if not matches:
                return None
        # Return the one with the shortest name (usually the common/preferred one)
        return min(matches, key=lambda c: len(c['name']))

def isplace(place):
        yesplace=requests.request("GET",API_BASE_URL+"places?q="+place.lower())
        print("URL called:", yesplace.url)
        print("Status code:", yesplace.status_code)
        print("Raw response:", yesplace.text[:300])
        if yesplace.status_code != 200:
                return False   # no match found
        yesplace=yesplace.json()
        if not yesplace:
                return None
        matches = [c for c in yesplace if place.lower() in c['name'].lower()]
        if not matches:
                return None
        # Return the one with the shortest name (usually the common/preferred one)
        return min(matches, key=lambda c: len(c['name']))

def calculatedistance(sid,did,slat,slng,dlat,dlng):
        url=API_BASE_URL+"distance?from="+str(sid)+"&to="+str(did)+"&lat1="+str(slat)+"&lng1="+str(slng)+"&lat2="+str(dlat)+"&lng2="+str(dlng)
        distance=requests.request("GET",url)
        if distance.status_code !=200:
                return False
        distance=distance.json()
        return distance["distanceKm"]
# def api_call(url,place):
#     result=requests.request("GET",url)
#     places=result.json()
#     if not places:
#         return None  
#     # Find all countries whose name contains what the user typed
#     matches = [c for c in places if place.lower() in c['name'].lower()]   
#     if not matches:
#         return None    
#     # Return the one with the shortest name (usually the common/preferred one)
#     return min(matches, key=lambda c: len(c['name']))