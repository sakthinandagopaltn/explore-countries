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
    actualsource,source_country_data = resolve_country_input(source)
    if actualsource is None:
        print("Selection cancelled for source. Returning to main menu.")
        return    
    sourceresponse = check_location(actualsource, source_country_data)
    if sourceresponse is None:
        print(f"Sorry, couldn't find '{source}' as a city or a place.")
        return
    
    """resolve destination down to a specific city or place record"""
    actualdestination,dest_country_data = resolve_country_input(destination)
    if actualdestination is None:
        print("Selection cancelled for destination. Returning to main menu.")
        return
    destresponse = check_location(actualdestination, dest_country_data)
    print(destresponse)
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
    else:
        mode="Unknown"

    country_code = destresponse.get('countryCode')
    if country_code:
        dest_country = get_country_details(country_code)
    else:
        dest_country = None

    if dest_country:
        """List all the currencies, languages and the calling code of the destination."""
        currency = [curr['name'] for curr in dest_country.get('currencies',[])]
        languages = [lang['name'] for lang in dest_country.get('languages',[])]
        calling_code = [f"+{code}" for code in dest_country.get('callingCodes', [])]
    else:
        currency = ["Unknown"]
        languages = ["Unknown"]
        calling_code = ["Unknown"]

    display_result(sourceresponse['name'], destresponse['name'], distance, mode, currency, languages, calling_code)
