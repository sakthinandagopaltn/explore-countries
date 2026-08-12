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
    if destresponse is None:
        print(f"Sorry, couldn't find '{destination}' as a city or a place.")
        return
    """
      Determining the distance between source and destination
      get the latitude and longitude information 
    """""
    sourcelat = sourceresponse.get('latitude')
    sourcelng = sourceresponse.get('longitude')
    sourcegeoid = sourceresponse.get('geonameId')
    destlat = destresponse.get('latitude')
    destlng = destresponse.get('longitude')
    destgeoid = destresponse.get('geonameId')

    if None in (sourcelat, sourcelng, sourcegeoid, destlat, destlng, destgeoid):
        print("Sorry, one of the selected locations is missing location data. Please try again.")
        return

    distance=calculate_distance(sourcegeoid,destgeoid,sourcelat,sourcelng,destlat,destlng)
    if distance is not None:
    # find mode of transport 
        mode=find_mode(distance)
    else:
        mode="Unknown"
    # get country code
    country_code = destresponse.get('countryCode')
    if country_code:
        dest_country = get_country_details(country_code)
    else:
        dest_country = None
    # get currency,language and calling code 
    if dest_country:
        """List all the currencies, languages and the calling code of the destination."""
        currency = [curr['name'] for curr in dest_country.get('currencies',[])]
        languages = [lang['name'] for lang in dest_country.get('languages',[])]
        calling_code = [f"+{code}" for code in dest_country.get('callingCodes', [])]
    else:
        currency = ["Unknown"]
        languages = ["Unknown"]
        calling_code = ["Unknown"]

    source_name = sourceresponse.get('name')
    dest_name = destresponse.get('name')
    
    if not source_name or not dest_name:
        print("Sorry, one of the selected locations is missing a name. Please try again.")
        return
    
    display_result(sourceresponse['name'], destresponse['name'], distance, mode, currency, languages, calling_code)
