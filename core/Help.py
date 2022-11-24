#!/usr/bin/env python3
# Project: osiris-framework
# Author: Samir Sanchez Garnica @sasaga92
# Version 1.0
# Date: 14/11/2022

from utilities.Colors import color
from tabulate import tabulate

class Help(object):
    """
        Description: This class shows the description of the osiris framework commands.
    """
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
                                 [color.color('green', 'reload_modules'), 'Performs an update of the module database in osiris']
                                 ]
        print('\n')
        print(color.color('yellow', '\t\t\t\t\tCORE COMMANDS'))
        print(tabulate(self.__core_commands_osiris, headers='firstrow', tablefmt='grid', stralign='center'))

    def show_payloads_osiris(self):
        pass

help = Help()
