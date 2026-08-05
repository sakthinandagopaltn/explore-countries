from constants import API_BASE_URL
from api import calculate_distance
from api import get_country_details
from verifylocation import check_location
from verifylocation import resolve_country_input
from mode import find_mode
from display import display_result

def process_data(source,destination):

    sourceresponse = None
    destresponse = None

    """resolve source down to a specific city or place record"""
    source = resolve_country_input(source)    
    sourceresponse = check_location(source)
    if sourceresponse is None:
        print(f"Sorry, couldn't find '{source}' as a city or a place.")
        return

    """resolve destination down to a specific city or place record"""
    destination = resolve_country_input(destination)
    destresponse = check_location(destination)
    if destresponse is None:
        print(f"Sorry, couldn't find '{destination}' as a city or a place.")
        return
    """
      Determining the distance between source and destination
      get the latitude and longitude information 
    """""
    sourcelat=sourceresponse['latitude']
    sourcelng=sourceresponse['longitude']
    sourcegeoid=sourceresponse['geonameId']
    destlat=destresponse['latitude']
    destlng=destresponse['longitude']
    destgeoid=destresponse['geonameId']

    distance=calculate_distance(sourcegeoid,destgeoid,sourcelat,sourcelng,destlat,destlng)
    if distance is not None:
    # find mode of transport 
        mode=find_mode(distance)

    dest_country = get_country_details(destresponse['countryCode'])

    if dest_country:
        currency = dest_country['currencies'][0]['name']
        languages = [lang['name'] for lang in dest_country['languages']]
        calling_code = "+" + dest_country['callingCodes'][0]
    else:
        currency = "Unknown"
        languages = []
        calling_code = "Unknown"

    display_result(sourceresponse['name'], destresponse['name'], distance, mode, currency, languages, calling_code)