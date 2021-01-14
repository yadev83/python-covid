##
# @file cli.py
# @author Yanis ATTIA (@yadev83)
# @brief This file contains specification for a cli Class and its components
# @version 0.1
# @date 2021-01-10
#
# @copyright Copyright (c) 2021
##
from types import MethodType
import request as req

class CLI:
    def __init__(self, keyword):
        self.__keyword = keyword
        self.__api = req.Request()

        self.__commands = []
        self.__commands.append(Command("help", "h", "Prints a help page about all this CLI commands", []))
        self.__commands.append(Command("quit", "q", "Quits the CLI", []))
        self.__commands.append(Command("date", "d", "Specifies the data Date", []))
        self.__commands.append(Command("department", "dpt", "Specifies the department", []))

        self.shouldQuit = False

    def __handleCmd(self, instruction, param = ""):
        Ran = False
        if instruction[:1] == "-":
            if instruction[:2] == "--":
                for cmd in self.__commands:
                    if instruction[2:] == cmd.getName():
                        self.__execCmd(cmd, param)
                        Ran = True
            else:
                for cmd in self.__commands:
                    if instruction[1:] == cmd.getAlias():
                        self.__execCmd(cmd, param)
                        Ran = True
        if not Ran :
            print("WARNING - Unkown option \"" + instruction + "\"")
            print("Run \"covid -h\" or \"covid --help\" for a list of commands")
        
    def __execCmd(self, command, param = ""):
        if command.getName() == "quit":
            print("Exiting covid CLI")
            self.shouldQuit = True
        
        if command.getName() == "help":
            print("Help window :")
            print("Please type \"covid\" followed by one of the following options")
            print("Help : --help or -h | Displays this help message")
            print("Quit : --quit or -q | Closes the covid CLI (Note that you can also quit by typing directly \"quit\" or \"q\")")
            print("Date : --date or -d | Followed by a date will give data for the said date, like : \"covid -d yyyy-mm-dd\"")
            print("Departement : --department or -dpt | Followed by either the Department name or number like : \"covid -dpt Var\"")
        
        if command.getName() == "date":
            self.__api.getAllData(param)
            self.__api.printResponse()
        
        if command.getName() == "department":
            self.__api.getDptData(param)
            self.__api.printResponse()

    def exec(self, command):
        instructions = command.split()
        keyword = instructions[0]
        instructions.pop(0)
        if keyword == self.__keyword:
            if len(instructions) != 0:
                i = 0
                while (i < len(instructions)):
                    if i == (len(instructions)-1):
                        self.__handleCmd(instructions[i])
                        i = i+1
                    else:
                        self.__handleCmd(instructions[i], instructions[i+1])
                        i = i+2
            else:
                self.__api.getAllData()
                self.__api.printResponse()
        elif keyword == "quit" or keyword == "q":
            self.__handleCmd("--quit")
        else:
            print("WARNING - Your instructions should start by \"" + self.__keyword + "\"")
    
    def run(self):
        while not self.shouldQuit:
            command = input("> ")
            if command != "":
                self.exec(command)
            else:
                self.__handleCmd("--help")

class Command:
    def __init__(self, name, alias, desc, parameters):
        self.__description = desc
        self.__name = name
        self.__alias = alias
        self.__parameters = []
        for param in parameters:
            self.__parameters.append(param)
    
    def getDescription(self):
        return self.__description
    
    def getName(self):
        return self.__name
    
    def getAlias(self):
        return self.__alias