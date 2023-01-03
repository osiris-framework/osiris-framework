#!/usr/bin/env python3
# Project: osiris-framework
# Author: Samir Sanchez Garnica @sasaga92
# Version 1.0
# Date: 14/11/2022

from utilities.Colors import color
from tabulate import tabulate
from os import path, walk
from importlib import reload


class Help(object):
    """
        Description: This class shows the description of the osiris framework commands.
    """

    def __init__(self):
        self.__path_list = None
        self.__payload_result = None
        self.__cant_payloads = None
        self.__result = None
        self.__unfiltered_result = None
        self.__show_payloads = None
        self.__core_commands_osiris = None

    def help_osiris(self):
        self.__core_commands_osiris = [[color.color('yellow', 'commands'), color.color('yellow', 'description')],
                                       [color.color('green', 'clean'), 'clean the screen'],
                                       [color.color('green', 'search'), 'search for modules in osiris'],
                                       [color.color('green', 'banner'), 'Show an osiris banner'],
                                       [color.color('green', 'exit'), 'close the program in osiris'],
                                       [color.color('green', 'use'), 'select an osiris module for later use'],
                                       [color.color('green', 'restart'), 'Restart osiris interpreter'],
                                       [color.color('green', 'exec'), 'run an operating system command'],
                                       [color.color('green', 'back'), 'goes to a section back'],
                                       [color.color('green', 'upgrade'), 'Check for a new osiris update'],
                                       [color.color('green', 'reload_modules'),
                                        'Performs an update of the module database in osiris'],
                                       [color.color('green', 'generator'),
                                        'Generates payloads via arguments from the osiris framework base console'],
                                       [color.color('green', 'generator list'),
                                        'Displays the list of payloads available to generate from osiris'],
                                       [color.color('green', 'generator help'),
                                        'Show help about payload generator class'],
                                       [color.color('green', 'pattern_create'),
                                        'Creates a single string that receives as parameter a string size'],
                                       [color.color('green', 'pattern_find'),
                                        'looks for a unique string receiving as parameter the string in hexadecimal format 0x or ascii Aa0']
                                       ]
        print('\n')
        print(color.color('yellow', '\t\t\t\t\tCORE COMMANDS'))
        print(tabulate(self.__core_commands_osiris, headers='firstrow', tablefmt='simple', stralign='Left'))

    def show_payloads_osiris(self):
        import utilities.Files
        from core.ModuleObtainer import obtainer
        reload(utilities.Files)
        from utilities.Files import files
        files.count_sub_folder_files('modules/payloads')

        self.__result = []
        self.__unfiltered_result = []
        self.__path_list = []

        self.__payload_result = [
            [color.color('yellow', 'Modules'), color.color('yellow', 'Name'), color.color('yellow', 'Platform'),
             color.color('yellow', 'Type'), color.color('yellow', 'Description')]]

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
            for i in range(0, int(len(self.__result))):
                for root, dirs, files in walk('modules/payloads'):
                    if self.__result[i] + '.py' in files:
                        __thePath = path.join(root, self.__result[i] + '.py')
                        __thePath = __thePath.split('/')

                        __pathFirstIndex = __thePath[0]
                        __thePath.remove(__pathFirstIndex)
                        __thePath = '/'.join(__thePath)
                        self.__path_list.append(__thePath)

            self.__path_list = set(self.__path_list)
            for __thePath in self.__path_list:
                if obtainer.description_obtainer_payload(__thePath.split('.py')[0]):
                    self.__payload_result.append(
                        [__thePath.split('.py')[0].replace("payloads/", ""), obtainer.info['name'],
                         obtainer.info['platform'], obtainer.info['payload_type'],
                         obtainer.info['description']])
        except IndexError:
            pass
        except ImportError:
            pass

        if len(self.__payload_result) == 1:
            self.__payload_result.append([color.color('red', 'NO RESULTS'), color.color('red', 'NO RESULTS')])

        print(tabulate(self.__payload_result, headers='firstrow', tablefmt='simple', stralign='left'))
        print('')


help = Help()
