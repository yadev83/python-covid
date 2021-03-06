##
# @file request.py
# @author Yanis ATTIA (@yadev83)
# @brief The request class to be used for the Covid19-fr api
# @version 0.3
# @date 2021-01-08
#
# Version 0.3 - Removes camel case notation\n
# Version 0.2 - Adds getDptData and date parameter\n
# Version 0.1 - File creation\n
#
# @copyright Copyright (c) 2021
##
import requests
from tabulate import tabulate
import re
import xlwt
import os

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
    # @fn __push_info
    # @brief This pushes an info into the response list
    # @param zone This parameter is the json-formatted dictionnary for a specific department in france (or global)
    # 
    # This creates an element in the response dictionnary properly formatted
    ##
    def __push_info(self, zone):
        self.response.append({
            "Code": zone["code"],
            "Nom": zone["nom"],
            "Date": zone["date"],
            "Hospitalisations": zone["hospitalises"],
            "Reanimation": zone["reanimation"],
            "Nouvelles Hospitalisations": zone["nouvellesHospitalisations"],
            "Nouvelles Reanimations": zone["nouvellesReanimations"],
            "Deces": zone["deces"],
            "Gueris": zone["gueris"]
        })

    ##
    # @fn print_response
    # @brief This prints the self.response dictionnary as a table in the terminal
    ##
    def print_response(self):
        if not len(self.response):
            print("ERROR::Can not print an empty response...")
        else:
            keys = self.response[0].keys()
            values = []
            for resp in self.response:
                values.append(resp.values())
            print(tabulate(values, headers=keys))
    
    ##
    # @fn export_response_to_excel
    # @brief This exports the contents of the result response to an xls file
    # 
    # @param fname the name of the file to write to
    ##
    def export_response_to_excel(self, fname = "output.xls"):
        if fname == "":
            print("WARNING::File name for excel export unknown or incorrect. Using \"output.xls\" instead")
            fname = "output.xls"

        if not len(self.response):
            print("ERROR::Can not output an empty response...")
        else:
            keys = self.response[0].keys()
            values = []
            for resp in self.response:
                values.append(resp.values())

            book = xlwt.Workbook()
            sheet = book.add_sheet("Covid")

            row = sheet.row(0)
            for index, col in enumerate(keys):
                row.write(index, col)
            
            row_nb = 1
            for val in values:
                # We need to output as a list to print separately each value
                val_list = list(val)
                row = sheet.row(row_nb)
                for index, key in enumerate(keys):
                    row.write(index, val_list[index])
                row_nb += 1

            if os.path.isfile(fname):
                print ("The output file already exists. Rename it, move it or remove it before we can write to another of the same name")
            else:
                book.save(fname)

    
    ##
    # @fn get_global_data
    # @brief Throw a request that gets the data about the whole France
    ##
    def get_global_data(self):
        httpResponse = requests.get(self.__apiAddr + "FranceLiveGlobalData")
        self.response = []
        self.__push_info(httpResponse.json()["FranceGlobalLiveData"][0])
    
    ## 
    # @fn get_all_data
    # @brief Throw a request that gets the data about every department of France altogether
    # @param date The date from which we want the data. By default, this is today's date
    ##
    def get_all_data(self, date = "0000-00-00"):
        regex = re.compile('\d{4}-\d{2}-\d{2}')
        key = "allLiveFranceData"
        if date != "0000-00-00":
            if regex.match(date) is not None:
                query = {'date': date}
                httpResponse = requests.get(self.__apiAddr + "AllDataByDate", params=query)
                key = "allFranceDataByDate"
            else:
                print("Warning::Please provide a date in the format yyyy-mm-dd. Today's date has been used instead")
                httpResponse = requests.get(self.__apiAddr + "AllLiveData")
        else:
            httpResponse = requests.get(self.__apiAddr + "AllLiveData")
        
        self.response = []
        if len(httpResponse.json()[key]) is 0:
            print("ERROR::Request gave an empty result. Please make sure that every parameter is correct (no overflowing dates and correct internet connection")
        else:
            for dept in httpResponse.json()[key]:
                self.__push_info(dept)
    
    ##
    # @fn get_dpt_data
    # @brief Throw a request that gives data about a specific departement
    # @param dpt The department number to get
    # @param date The date from which we want the data. By default, this is today's date
    #
    # There is in the API a specific "url/LiveDataByDepartement?Departement={dpt}" call available.
    # However, to be able to do a request with a specific date, it has to be a "AllDataByDate" call.
    # So this function makes a get_all_data() call with a specific date and then
    # filters the full request with only the wanted departement.
    ##
    def get_dpt_data(self, dpt, date = "0000-00-00"):
        self.get_all_data(date)

        if len(self.response):
            if type(dpt) is not str:
                dpt = str(dpt)

            keep = "NOT_FOUND"
            for data in self.response:
                if data["Code"] == "DEP-"+dpt or data["Nom"] == dpt:
                    keep = data

            if keep != "NOT_FOUND":
                self.response = []
                self.response.append(keep)
            else:
                print("WARNING::Could not found given department. Using full search instead")