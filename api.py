import requests

def api_call(url,place):

    result=requests.request("GET",url)
    countries=result.json()
     # Find the exact match, not just the first result
    for country in countries:
        if country['name'].lower() == place.lower():
            return country
    return None  #no match found