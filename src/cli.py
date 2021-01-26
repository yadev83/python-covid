##
# @file cli.py
# @author Yanis ATTIA (@yadev83)
# @brief This file contains specification for a cli Class and its components
# @version 0.2
# @date 2021-01-10
#
# Version 0.2 - Added documentation\n
# Version 0.1 - File creation\n
#
# @copyright Copyright (c) 2021
##
from types import MethodType
from datetime import datetime

import request as req
import matplotlib.pyplot as plt

##
# @class CLI
# @brief A class made to create some CLI and commands interpretation.
##
class CLI:
    ##
    # @fn __init__
    # @brief Constructs a new CLI object
    # 
    # Inits the __keyword private attribute for the cli
    # Inits the __api private object
    #
    # @param keyword the keyword to use for the CLI
    ##
    def __init__(self, keyword):
        self.__keyword = keyword
        self.__api = req.Request()

        self.__commands = []
        self.__commands.append(Command("help", "h", "Prints a help page about all this CLI commands"))
        self.__commands.append(Command("quit", "q", "Quits the CLI"))
        self.__commands.append(Command("date", "d", "Takes a date as \"yyyy-mm-dd\" in parameter"))
        self.__commands.append(Command("department", "dpt", "Takes a department as a parameter (name or number)"))
        self.__commands.append(Command("excel", "e", "Outputs the result to an excel file (file name can be given as parameter)"))
        self.__commands.append(Command("plot", "p", "Outputs a plot from given date in the whole France country"))

        self.shouldQuit = False

    ##
    # @fn __handle_cmd
    # @brief Take an instruction as a parameter (and the following parameter)
    #
    # @param instruction the option to run (either --option or -alias)
    # @param param the parameter to give to that specific option
    ##
    def __handle_cmd(self, instruction, param = ""):
        Ran = False
        if instruction[:1] == "-":
            if instruction[:2] == "--":
                for cmd in self.__commands:
                    if instruction[2:] == cmd.get_name():
                        self.___exec_cmd(cmd, param)
                        Ran = True
            else:
                for cmd in self.__commands:
                    if instruction[1:] == cmd.get_alias():
                        self.___exec_cmd(cmd, param)
                        Ran = True
        if not Ran :
            print("WARNING - Unkown option \"" + instruction + "\"")
            print("Run \""+ self.__keyword +" -h\" or \"" + self.__keyword + " --help\" for a list of commands")
        
    ##
    # @fn __exec_cmd
    # @brief Takes a command and its parameter to execute it
    #
    # @param command the said command to execute
    # @param param the parameters to give to the command
    ##
    def ___exec_cmd(self, command, param = ""):
        if command.get_name() == "quit":
            print("Exiting \""+ self.__keyword +"\" CLI")
            self.shouldQuit = True
        
        if command.get_name() == "help":
            print("Help window :")
            print("Please type \""+ self.__keyword +"\" followed by one of the following options")
            for cmd in self.__commands:
                print(cmd.get_name() + " : --" + cmd.get_name() + " or -" + cmd.get_alias() + " | " + cmd.get_description())
        
        if command.get_name() == "date":
            self.__api.get_all_data()
            self.__api.print_response()
        
        if command.get_name() == "department":
            self.__api.get_dpt_data(param)
            self.__api.print_response()
        
        if command.get_name() == "excel":
            self.__api.get_all_data()
            self.__api.print_response()
            self.__api.export_response_to_excel(param)
        
        if command.get_name() == "plot":
            self.__api.get_data_since("France", param)

            y_axis_hospitalisations = []
            y_axis_nouvelles_hospitalisations = []
            y_axis_reanimations = []
            y_axis_deaths = []
            y_axis_gueris = []

            x_axis = []
            for resp in self.__api.response:
                x_axis.append(resp["Date"])
                y_axis_hospitalisations.append(resp["Hospitalisations"])
                y_axis_nouvelles_hospitalisations.append(resp["Nouvelles Hospitalisations"])
                y_axis_reanimations.append(resp["Reanimation"])
                y_axis_deaths.append(resp["Deces"])
                y_axis_gueris.append(resp["Gueris"])


            # Hospitalisations
            plt.plot(x_axis, y_axis_hospitalisations)
            plt.title("Hospitalisations liées au COVID depuis " + x_axis[0])
            plt.setp(plt.gca().xaxis.get_majorticklabels(), 'rotation', 90)
            plt.ylabel("Hospitalisations")
            plt.xlabel("Date (YYYY-MM-JJ)")
            plt.show()

            # Reanimations
            plt.plot(x_axis, y_axis_reanimations)
            plt.title("Réanimations liées au COVID depuis " + x_axis[0])
            plt.setp(plt.gca().xaxis.get_majorticklabels(), 'rotation', 90)
            plt.ylabel("Reanimations")
            plt.xlabel("Date (YYYY-MM-JJ)")
            plt.show()

            # Deces
            plt.plot(x_axis, y_axis_deaths)
            plt.title("Décés liés au COVID depuis " + x_axis[0])
            plt.setp(plt.gca().xaxis.get_majorticklabels(), 'rotation', 90)
            plt.ylabel("Deces")
            plt.xlabel("Date (YYYY-MM-JJ)")
            plt.show()

            # Gueris
            plt.plot(x_axis, y_axis_gueris)
            plt.title("Patients guéris du COVID depuis " + x_axis[0])
            plt.setp(plt.gca().xaxis.get_majorticklabels(), 'rotation', 90)
            plt.ylabel("Gueris")
            plt.xlabel("Date (YYYY-MM-JJ)")
            plt.show()

            # Nouvelles Hospitalisations
            plt.plot(x_axis, y_axis_nouvelles_hospitalisations)
            plt.title("Nouvelles Hospitalisations par jour depuis " + x_axis[0])
            plt.setp(plt.gca().xaxis.get_majorticklabels(), 'rotation', 90)
            plt.ylabel("Nouvelles Hospitalisations pr jour")
            plt.xlabel("Date (YYYY-MM-JJ)")
            plt.show()
    ##
    # @fn exec
    # @brief Parses and executes the whole line
    #
    # @param command A string containing a full line of command
    ##
    def exec(self, command):
        instructions = command.split()
        keyword = instructions[0]
        instructions.pop(0)
        if keyword == self.__keyword:
            if len(instructions) != 0:
                i = 0
                while (i < len(instructions)):
                    if i == (len(instructions)-1):
                        self.__handle_cmd(instructions[i])
                        i = i+1
                    else:
                        self.__handle_cmd(instructions[i], instructions[i+1])
                        i = i+2
            else:
                self.__api.get_all_data()
                self.__api.print_response()
        elif keyword == "quit" or keyword == "q":
            self.__handle_cmd("--quit")
        else:
            print("WARNING - Your instructions should start by \"" + self.__keyword + "\"")
    
    ##
    # @fn run
    # @brief Tha main loop for the CLI to run
    #
    # Waits for an input and treat it
    ##
    def run(self):
        while not self.shouldQuit:
            command = input("> ")
            if command != "":
                self.exec(command)
            else:
                self.__handle_cmd("--help")

##
# @class Command
# @brief A class made to create some commands with their names and aliases
##
class Command:
    ##
    # @fn __init__
    # @brief Inits a new Command object
    #
    # @param name the full command name (like --help or --quit)
    # @param alias the command short name (like -h or -q)
    # @param desc the description of the command
    ##
    def __init__(self, name, alias, desc):
        self.__description = desc
        self.__name = name
        self.__alias = alias
    
    ##
    # @fn get_description
    # @brief returns the description of the command
    ##
    def get_description(self):
        return self.__description
    
    ##
    # @fn get_name
    # @brief returns the complete name of the command
    ##
    def get_name(self):
        return self.__name
    
    ##
    # @fn get_alias
    # @brief returns the alias of this command
    ##
    def get_alias(self):
        return self.__alias