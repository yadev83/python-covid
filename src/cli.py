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

class CLI:
    def __init__(self, keyword):
        self.__keyword = keyword
        self.__commands = []
        self.__commands.append(Command("help", "h", "Prints a help page about all this CLI commands", []))
        self.__commands.append(Command("quit", "q", "Quits the CLI", []))

        self.shouldQuit = False

    def __handleCmd(self, instruction):
        Ran = False
        if instruction[:1] == "-":
            if instruction[:2] == "--":
                for cmd in self.__commands:
                    if instruction[2:] == cmd.getName():
                        self.__execCmd(cmd)
                        Ran = True
            else:
                for cmd in self.__commands:
                    if instruction[1:] == cmd.getAlias():
                        self.__execCmd(cmd)
                        Ran = True
        if not Ran :
            print("WARNING - Unkown option \"" + instruction + "\"")
            print("Run \"covid -h\" or \"covid --help\" for a list of commands")
        
    def __execCmd(self, command):
        if command.getName() == "quit":
            self.shouldQuit = True

    def exec(self, command):
        instructions = command.split()
        keyword = instructions[0]
        instructions.pop(0)
        if keyword == self.__keyword:
            for instruction in instructions:
                self.__handleCmd(instruction)
        else:
            print("WARNING - Your instructions should start by \"" + self.__keyword + "\"")
    
    def run(self):
        while not self.shouldQuit:
            command = input("> ")
            self.exec(command)

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