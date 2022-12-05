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

    def __init__(self):
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
                                       [color.color('green', 'reload_modules'),'Performs an update of the module database in osiris'],
                                       [color.color('green', 'generator_list'),'Displays the list of payloads available to generate from osiris']
                                       ]
        print('\n')
        print(color.color('yellow', '\t\t\t\t\tCORE COMMANDS'))
        print(tabulate(self.__core_commands_osiris, headers='firstrow', tablefmt='grid', stralign='center'))

    def show_payloads_osiris(self):
        self.__show_payloads = [[color.color('yellow', 'payloads'), color.color('yellow', 'description')],
                                [color.color('green', 'payload/generic/shell/bind_tcp'),
                                 'generate payloads generic shell to bind_tcp'],
                                [color.color('green', 'payload/generic/shell/rce/reverse_tcp'),
                                 'generate payloads generic shell to reverse_tcp'],
                                ]
        print("\n")
        print(color.color("yellow", '\t\t\t\t\tShow Payloads'))
        print(tabulate(self.__show_payloads, headers='firstrow', tablefmt='grid', stralign='center'))


help = Help()
