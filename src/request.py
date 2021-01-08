##
# @file request.py
# @author Yanis ATTIA (@yadev83)
# @brief The request class to be used for the Covid19-fr api
# @version 0.1
# @date 2021-01-08
#
# @copyright Copyright (c) 2021
##
import requests

class Request:
    def __init__(self):
        self.__apiAddr = "https://coronavirusapi-france.now.sh/"
    
    def getGlobalData(self):
        httpResponse = requests.get(self.__apiAddr + "FranceLiveGlobalData")
        formattedResponse = {
            "date": httpResponse.json()["FranceGlobalLiveData"][0]["date"],
            "hospitalisations": httpResponse.json()["FranceGlobalLiveData"][0]["hospitalises"],
            "reanimation": httpResponse.json()["FranceGlobalLiveData"][0]["reanimation"],
            "nouvellesHospitalisations": httpResponse.json()["FranceGlobalLiveData"][0]["nouvellesHospitalisations"],
            "nouvellesReanimations": httpResponse.json()["FranceGlobalLiveData"][0]["nouvellesReanimations"],
            "deces": httpResponse.json()["FranceGlobalLiveData"][0]["deces"],
            "gueris": httpResponse.json()["FranceGlobalLiveData"][0]["gueris"]
        }

        return formattedResponse
