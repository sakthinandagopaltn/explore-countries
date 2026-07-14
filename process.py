import math
import constants
from api import api_call
from distance import haversine
from mode import findmode
from display import display_result
def process_data(source,destination):

    # building the urls
    sourceurl=constants.API_BASE_URL+"/name/"+source
    destinationurl=constants.API_BASE_URL+"/name/"+destination
    
    # calling the API and storing the country details 
    sourceresponse=api_call(sourceurl,source)
    destresponse=api_call(destinationurl,destination)

    # Determining the mode of transportation between source and destination
    # get the latitude and longitude information 
    sourcelat=sourceresponse['latlng'][0]
    sourcelng=sourceresponse['latlng'][1]
    destlat=destresponse['latlng'][0]
    destlng=destresponse['latlng'][1]

    # calculate the distance between the two using haversine formula
    distance=math.floor(haversine(sourcelat,sourcelng,destlat,destlng))

    # find mode of transport 
    mode=findmode(distance)
    # print(mode)

    #Determining the currency 
    currency=destresponse['currencies'][0]['name']
    # print(currency)

    #Determining the languages to be known
    languages=destresponse['languages']
    langlist=[]
    for language in languages:
        langlist.append(language['name'])
    # print(langlist)

    #Determining the calling code
    callingcode=destresponse['callingCodes']
    # print(callingcode)

    # result={f"Approximate distance between {source.capitalize()} and {destination.capitalize()} in kilometer": distance, "Mode of transporatation":mode, "Currency you need":currency,"Language(s) you should know":langlist,"Calling codes":callingcode}

    display_result(source,destination,distance,mode,currency,langlist,callingcode)