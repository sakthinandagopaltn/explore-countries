import math
from constants import API_BASE_URL
from api import isplace
from api import iscountry
from api import iscity
from api import calculatedistance
# from distance import haversine
from mode import findmode
from display import display_result
def process_data(source,destination):

    # Checking if the sourc/destination is a country
    # sourceurl=constants.API_BASE_URL+"/name/"+source
    # destinationurl=constants.API_BASE_URL+"/name/"+destination
    # allcountries=get_all_country_names()
    # sourcecheck=iscountry(source)
    # if sourcecheck:
    #     sourcefollowup = input(f"'{source}' is a country. Where in {source} are you in?: ")
    # destcheck=iscountry(destination)
    # if destcheck:
    #     destfollowup = input(f"'{destination}' is a country. Where in {destination} are you in?: ")
    
    # # to do - check if it is a city or a place in the city and then build the urls
    # if sourcefollowup:
    #     sourceresponse=iscity(sourcefollowup)
    #     if not sourceresponse:
    #         sourceresponse=isplace(sourcefollowup)
    #         if not sourceresponse:
    #             pass
    # else:
    #     sourceresponse=iscity(source)
    
    # if destfollowup:
    #     destresponse=iscity(destfollowup)
    #     if not destresponse:
    #         destresponse=isplace(destfollowup)
    #         if not destresponse:
    #             pass
    # else:
    #     destresponse=iscity(destination)

    sourcefollowup = None
    destfollowup = None
    sourceresponse = None
    destresponse = None

    sourcecheck = iscountry(source)
    if sourcecheck:
        sourcefollowup = input(f"'{source}' is a country. Where in {source} are you in?: ")
        if sourcefollowup:
            sourceresponse = iscity(sourcefollowup)
            if not sourceresponse:
                sourceresponse = isplace(sourcefollowup)
        else:
            sourceresponse = iscity(source)
            if not sourceresponse:
                sourceresponse = isplace(source)
    else:
        sourceresponse=iscity(source)
        if not sourceresponse:
            sourceresponse=isplace(source)
    
    destcheck = iscountry(destination)
    if destcheck:
        destfollowup = input(f"'{destination}' is a country. Where in {destination} are you in?: ")
        if destfollowup:
            destresponse = iscity(destfollowup)
            if not destresponse:
                destresponse = isplace(destfollowup)
        else:
            destresponse = iscity(destination)
            if not destresponse:
                destresponse = isplace(destination)
    else:
        destresponse=iscity(destination)
        if not destresponse:
            destresponse=isplace(destination)


    if sourceresponse is None:
        print(f"Sorry, couldn't find '{sourcefollowup or source}' as a city or place.")
        return
    if destresponse is None:
        print(f"Sorry, couldn't find '{destfollowup or destination}' as a city or place.")
        return

    
    # calling the API and storing the country details 
    # sourceresponse=api_call(sourceurl,source)
    # destresponse=api_call(destinationurl,destination)

    # Determining the mode of transportation between source and destination
    # get the latitude and longitude information 
    sourcelat=sourceresponse['latitude']
    sourcelng=sourceresponse['longitude']
    sourcegeoid=sourceresponse['geonameId']
    destlat=destresponse['latitude']
    destlng=destresponse['longitude']
    destgeoid=destresponse['geonameId']

    # calculate the distance between the two using haversine formula
    # distance=math.floor(haversine(sourcelat,sourcelng,destlat,destlng))
    distance=calculatedistance(sourcegeoid,destgeoid,sourcelat,sourcelng,destlat,destlng)
    if distance is not None:
    # find mode of transport 
        mode=findmode(distance)
    # print(mode)

    #Determining the currency 
    # currency=destresponse['currencies'][0]['name']
    # print(currency)

    #Determining the languages to be known
    # languages=destresponse['languages']
    # langlist=[]
    # for language in languages:
    #     langlist.append(language['name'])
    # print(langlist)

    #Determining the calling code
    # callingcode=destresponse['callingCodes']
    # print(callingcode)

    # result={f"Approximate distance between {source.capitalize()} and {destination.capitalize()} in kilometer": distance, "Mode of transporatation":mode, "Currency you need":currency,"Language(s) you should know":langlist,"Calling codes":callingcode}

    # display_result(source,destination,distance,mode,currency,langlist,callingcode)

    display_result(source,destination,distance,mode)