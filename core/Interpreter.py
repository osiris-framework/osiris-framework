#!/usr/bin/env python3
# Project: osiris-framework
# Author: Samir Sanchez Garnica @sasaga92
# Version 1.0
# Date: 14/11/2022

from utilities.Colors import color
from utilities.ScreenCleaner import ScreenCleaner
from core.Banner import banner
from core.Completer import completer
from os import path, walk
from tabulate import tabulate
from urllib.request import urlopen
from urllib.error import URLError
from importlib import reload


class Interpreter(object):
    """
        Description: This class has the methods to check if there is a new version of osiris, the methods to search for modules with the search command, and the method that starts the osiris interpreter at the prompt.
    """
    def __init__(self):
        self.__path_current_version = 'core/version.txt'
        self.__url_new_version = 'https://raw.githubusercontent.com/sasaga/sasaga/Osiris-framework/master/core/version.txt'

    def search_module(self, query):
        import utilities.Files
        from core.ModuleObtainer import obtainer
        reload(utilities.Files)
        from utilities.Files import files

        self.__cant_modules = files.count_sub_folder_files('modules')

        self.__unfiltered_result = []
        self.__result = []

        self.__search_module = [[color.color('yellow','Modules'),color.color('yellow','Description')]]

        for first_result in files.count_sub_folder_files_result:
            for second_result in first_result:
                self.__unfiltered_result.append(''.join(second_result))
                for final_result in self.__unfiltered_result:
                    if final_result.endswith('.pyc') or final_result.startswith(
                            '__init__') or not final_result.endswith('.py'):
                        self.__unfiltered_result.remove(final_result)

        for filter_result in self.__unfiltered_result:
            self.__result.append(filter_result.split('.')[0])

        try:
            for i in range(int(self.__cant_modules)):
                for root, dirs, files in walk('modules'):
                    if query in root+self.__result[i]:
                        if self.__result[i]+'.py' in files:
                            self.__thePath = path.join(root, self.__result[i]+'.py')
                            self.__thePath = self.__thePath.split('/')
                            self.__pathFirstIndex = self.__thePath[0]
                            self.__thePath.remove(self.__pathFirstIndex)
                            self.__thePath = '/'.join(self.__thePath)

                            if obtainer.description_obtainer(self.__thePath.split('.py')[0]):
                                self.__search_module.append([self.__thePath.split('.py')[0],obtainer.info['description']])
        except IndexError:
            pass
        except ImportError:
            pass

        if len(self.__search_module) == 1:
            self.__search_module.append([color.color('red','NO RESULTS'),color.color('red','NO RESULTS')])

        print(tabulate(self.__search_module, headers='firstrow', tablefmt='grid', stralign='center'))
        print('')

    def check_upgrade(self):
        try:
            self.__current_version = open(self.__path_current_version, 'r').read()
            self.__new_version = urlopen(self.__url_new_version).read()

            if float(self.__current_version) < float(self.__new_version):
                print(color.color("green","[+]") + color.color("blue", "Congratulations There is a new version of osiris-framework"))
            else:
                print(color.color("yellow","[!]") + color.color("lgray", "You have the most recent version of osiris-framework"))
        except FileNotFoundError:
            print(color.color("red", "[-]") + color.color("lgray",
                                                              "sorry, check if the core/version.txt file exists and try again"))
        except URLError:
            print(color.color("red", "[-]") + color.color("lgray",
                                                              "Please check the internet connection and try again"))

    def start_interpreter(self):
        completer()
        from core.Validator import Validator
        while True:
            try:
                self.__main_ask = input(color.color("underline",
                                                    color.color("lgray", "%s" % ("osiris"))) + " " + color.color(
                    'lgray', '>') + " ").split()
                Validator(self.__main_ask).validate_interpreter_mode()
            except (KeyboardInterrupt, EOFError):
                print(color.color("red", "[!]") + color.color("lgray", "Type exit to close the program"))


interpreter = Interpreter()