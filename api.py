import requests

def api_call(url,place):

    result=requests.request("GET",url)
    places=result.json()
    #  # Find the exact match, not just the first result
    # for eachplace in places:
    #     if eachplace['name'].lower() == place.lower():
    #         return eachplace
    # return None  #no match found


    if not places:
        return None
    
    # Find all countries whose name contains what the user typed
    matches = [c for c in places if place.lower() in c['name'].lower()]
    
    if not matches:
        return None
    
    # Return the one with the shortest name (usually the common/preferred one)
    return min(matches, key=lambda c: len(c['name']))