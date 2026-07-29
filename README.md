# explore-countries
This repository is created for Python Advanced Pre-Work course with Code The Dream 

API:

    The API that is used is Countries (countries.dev).
    A database of every country in the world, with data on population, area, region, languages, capital city, and places.
    Base endpoint: https://countries.dev/countries
    Docs: https://countries.dev/docs

Network Requirement:

    This app makes live requests to the countries.dev API. If you're on a home network protected by a router-level security feature, these requests may be silently blocked, resulting in connection or SSL errors. 

    If the app fails to connect:

        Try running it on a mobile hotspot instead of your home Wi-Fi
        Or temporarily disable your router's web/security filtering for testing
        Verify the issue by opening https://countries.dev directly in your browser — if it loads there but the app still fails, it's likely a network-level block specific to non-browser traffic

    This is a known limitation of certain ISP security features and is unrelated to the app's code.

Inputs

    Source 
    Destination

Output: 

    Mode of transporatation from the source to the destination
    Currency you will need at the destination 
    Language(s) you should know at the destination
    Calling code(s) of the destination
    Timezone of the destination

Working:

    1.  If the input source is a country, the application asks the user to select a specific city by providing a list of the cities. 
    The URL that is used for this purpose is https://countries.dev/name/{countryname}

    2.  If the 


