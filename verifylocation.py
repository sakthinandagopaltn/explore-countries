from api import iscity
from api import isplace
from api import get_country_details_by_name
from api import get_cities_in_country
from api import get_country_details

def choose_one(matches, place_type="place", location="None"):
    # Resolve each unique country code once
    unique_codes = {m.get('countryCode') for m in matches if m.get('countryCode')}
    code_to_name = {}
    for code in unique_codes:
        details = get_country_details(code)
        code_to_name[code] = details['name'] if details else code

    # Attach the resolved country name onto every match
    for m in matches:
        m['countryName'] = code_to_name.get(m.get('countryCode'), 'Unknown')

    """If there's one match, return it directly. Otherwise, ask the user to pick."""
    if len(matches) == 1:
        return matches[0]
    
    if location:
        print(f"\nFound multiple {place_type}(s/ies) matching your search with the term {location.title()}")
    else:
        print(f"\nFound multiple {place_type}(s/ies) to choose from:")
    
    print(f"\nI have the name-country-featurecode of the {place_type} for you!")
    
    for i, match in enumerate(matches, start=1):
        print(f"{i}. {match['name']} - {match['countryName']} - {match.get('featureCode', 'Unknown')}")               

    while True:
        choice = input(f"\nWhich one did you mean? Enter a number (1-{len(matches)}): ")
        if choice == "0":
            return None
        try:
            index = int(choice) - 1
            if 0 <= index < len(matches):
                return matches[index]
            print("Invalid number, please try again.")            
        except ValueError:
            print("Please enter a valid number.")
            

def check_location(location, country_data):
    city_matches = iscity(country_data,location) or []
    place_matches = isplace(country_data,location) or []
    """
    Merge results from both endpoints — cities is filtered to larger places,
    places has the fuller (unfiltered) list, so combining gives the complete list
    """
    combined = city_matches + place_matches
 
    # De-duplicate by geonameId, since a place (like a capital city) can appear
    # in both the /cities and /places results
    seen_ids = set()
    all_matches = []
    for match in combined:
        gid = match.get('geonameId')
        if gid not in seen_ids :
            seen_ids.add(gid)
            all_matches.append(match)
 
    if not all_matches:
        return None
 
    return choose_one(all_matches,"location",location)


def resolve_country_input(name):
    """
    Fetch country data once. If name is a country, let the user pick a city
    from it. If not, return the name unchanged with no country data.
    Returns (resolved_location_name, country_data_or_None).
    """
    country_data = get_country_details_by_name(name)
    if not country_data:
        return name, None

    cities = get_cities_in_country(country_data['alpha2Code'])
    if not cities:
        typed = input(f"'{name.title()}' is a country. Where in {name.title()} are you in?: ")
        return typed, country_data

    print(f"\n'{name.title()}' is a country. Here are some cities to choose from:")
    selected = choose_one(cities, "city", None)
    if selected is None:
        return None, None
    return selected['name'], country_data

