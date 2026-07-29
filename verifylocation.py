from api import iscity
from api import isplace
from api import iscountry
from api import get_country_details_by_name
from api import get_cities_in_country

from exactlocation import choose_one

def check_location(location):

    city_matches = iscity(location) or []
    place_matches = isplace(location) or []
 
    """
    Merge results from both endpoints — cities is filtered to larger places,
    places has the fuller (unfiltered) gazetteer, so combining gives the full picture
    """
    combined = city_matches + place_matches
 
    # De-duplicate by geonameId, since a place (like a capital city) can appear
    # in both the /cities and /places results
    seen_ids = set()
    all_matches = []
    for match in combined:
        gid = match.get('geonameId')
        if gid not in seen_ids:
            seen_ids.add(gid)
            all_matches.append(match)
 
    if not all_matches:
        return None
 
    return choose_one(all_matches,location, "location")


def resolve_country_input(name):
    """
    If the input is a country, fetch its cities and let the user pick one
    from the list instead of typing a place name freely.
    If it's not a country, return the name unchanged.
    """
    if not iscountry(name):
        return name
 
    country_data = get_country_details_by_name(name)
    if country_data is None:
        # couldn't fetch country details for some reason — fall back to free text
        return input(f"'{name}' is a country. Where in {name} are you in?: ")
 
    cities = get_cities_in_country(country_data['alpha2Code'])
    if not cities:
        # no cities found via the API — fall back to free text
        return input(f"'{name}' is a country. Where in {name} are you in?: ")
 
    print(f"\n'{name}' is a country. Here are some cities to choose from:")
    selected = choose_one(cities, "city")
    return selected['name']