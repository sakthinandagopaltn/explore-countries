def choose_one(matches, place_type="place"):
    """If there's one match, return it directly. Otherwise, ask the user to pick."""
    if len(matches) == 1:
        return matches[0]
 
    print(f"\nFound multiple {place_type}s matching your search:")
    for i, match in enumerate(matches, start=1):
        country_code = match.get('countryCode', 'Unknown')
        admin_code = match.get('admin1Code','Unknown')
        print(f"{i}. {match['name']} ({country_code}) ({admin_code})")
 
    choice = input(f"\nWhich one did you mean? Enter a number (1-{len(matches)}): ")
    try:
        index = int(choice) - 1
        if 0 <= index < len(matches):
            return matches[index]
        print("Invalid number, please try again.")
        return choose_one(matches, place_type)
    except ValueError:
        print("Please enter a valid number.")
        return choose_one(matches, place_type)
 