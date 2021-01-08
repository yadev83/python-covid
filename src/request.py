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
from tabulate import tabulate

##
# @class Request
# @brief A class made to create some API calls on "https://coronavirusapi-france.now.sh/"
##
class Request:
    ##
    # @fn __init__
    # @brief Constructs a new Request object
    # 
    # Inits the __apiAddr private attribute with the API address
    # Inits the response as an empty list and pushes a "null" response in case some filthy user
    # tries to print it without having a request done at first. :)
    ##
    def __init__(self):
        self.__apiAddr = "https://coronavirusapi-france.now.sh/"
        self.response = []
        self.response.append({
            "null": "Please run a request first"
        })

    ##
    # @fn __pushInfo
    # @brief This pushes an info into the response list
    # @param zone This parameter is the json-formatted dictionnary for a specific department in france (or global)
    # 
    # This creates an element in the response dictionnary properly formatted
    ##
    def __pushInfo(self, zone):
        self.response.append({
            "Dpt/Area": zone["code"]+" - "+zone["nom"],
            "Date": zone["date"],
            "Hospitalisations": zone["hospitalises"],
            "Reanimation": zone["reanimation"],
            "Nouvelles Hospitalisations": zone["nouvellesHospitalisations"],
            "Nouvelles Reanimations": zone["nouvellesReanimations"],
            "Deces": zone["deces"],
            "Gueris": zone["gueris"]
        })

    ##
    # @fn printResponse
    # @brief This prints the self.response dictionnary as a table in the terminal
    ##
    def printResponse(self):
        keys = self.response[0].keys()
        values = []
        for resp in self.response:
            values.append(resp.values())
        print(tabulate(values, headers=keys))
    
    ##
    # @fn getGlobalData
    # @brief Throw a request that gets the data about the whole France
    ##
    def getGlobalData(self):
        httpResponse = requests.get(self.__apiAddr + "FranceLiveGlobalData")
        self.response = []
        self.__pushInfo(httpResponse.json()["FranceGlobalLiveData"][0])
    
    ## 
    # @fn getAllData
    # @brief Throw a request that gets the data about every department of France altogether
    ##
    def getAllData(self):
        httpResponse = requests.get(self.__apiAddr + "AllLiveData")
        self.response = []
        for dept in httpResponse.json()["allLiveFranceData"]:
            self.__pushInfo(dept)