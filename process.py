import constants
from api import api_call

def process_data(source,destination):

    # building the urls
    sourceurl=constants.API_BASE_URL+"/name/"+source
    destinationurl=constants.API_BASE_URL+"/name/"+destination
    
    # calling the API and storing the response 
    country1=api_call(sourceurl,source)
    country2=api_call(destinationurl,destination)

    return country1