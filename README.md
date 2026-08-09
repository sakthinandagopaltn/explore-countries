# explore-countries
This repository is created for Python Advanced Pre-Work course with Code The Dream 

## API:

    The API that is used is Countries (countries.dev).
    A database of every country in the world, with data on population, area, region, languages, capital city, and places.
    Base endpoint: https://countries.dev/
    Docs: https://countries.dev/docs

## Network Requirement:

    This app makes live requests to the countries.dev API. If you're on a home network protected by a router-level security feature, these requests may be silently blocked, resulting in connection or SSL errors. 

    If the app fails to connect:

        Try running it on a mobile hotspot instead of your home Wi-Fi
        Or temporarily disable your router's web/security filtering for testing
        Verify the issue by opening https://countries.dev directly in your browser — if it loads there but the app still fails, it's likely a network-level block specific to non-browser traffic

    This is a known limitation of certain ISP security features and is unrelated to the app's code.

## Assumption:

    The key assumption made here is that there are options for car/bus/flight from any source to any destination-does not account for real-world route availability.

    There might be repetitions in the places listed, as they have unique geoNameIds, that represent they are actually two different places. 

## Input:

    Source as a string
    Destination as a string

    If the source/destination given is not a specific place, the program prompts to type a number from the list of places that will be displayed. 

## Output: 

    Approximate distance from the source to the destination
    Efficient Mode of transporatation from the source to the destination
    Currency you will need at the destination 
    Language(s) you should know at the destination
    Calling code(s) of the destination

## Working:

    1.  If the input source/destination is a country, the application asks the user to select a specific city by providing a list of 20 cities in the country.
        URL Used : https://countries.dev/name={countryname} and https://countries.dev/cities?country={countrycode}
    2.  If the input source/destination is a city/place, the user is prompted to select a specific place from the list of unique city and places combined,and displayed.
        URL Used : https://countries.dev/places?q={placename} and https://countries.dev/cities?q={cityname}
    3.  After the source and the destination is selected, the latitiude, longitude and geoIds of the source and the destination are retrieved by the program.
    4.  With the above information, the distance between them is calculated in the program with the URL 
    "https://countries.dev/distance?from=source&to=destination&lat1=sourcelatitude&lng1=sourcelongitude&lat2=destinationlatitude&lng2=destinationlongitude
    5.  With the distance , the program gives any one of the following modes of transportations
            -You are right there - if the source and the destination are the same
            -Car/Bus - if the distance is less than 500km
            -Short-haul flight -  if the distance is between 500 and 3000km
            -Long-haul flight -  if the distance is greater than 3000km
    6. The user is also provided with the currency of the destination, the languages they need to know and the destination's calling code.
    


