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

class Request:
    def __init__(self):
        self.__apiAddr = "https://coronavirusapi-france.now.sh/"
        self.response = []
        self.response.append({
            "null": "Please run a request first"
        })

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

    def printResponse(self):
        keys = self.response[0].keys()
        values = []
        for resp in self.response:
            values.append(resp.values())
        print(tabulate(values, headers=keys))

    def getGlobalData(self):
        httpResponse = requests.get(self.__apiAddr + "FranceLiveGlobalData")
        self.response = []
        self.__pushInfo(httpResponse.json()["FranceGlobalLiveData"][0])
    
    def getAllData(self):
        httpResponse = requests.get(self.__apiAddr + "AllLiveData")
        self.response = []
        for dept in httpResponse.json()["allLiveFranceData"]:
            self.__pushInfo(dept)