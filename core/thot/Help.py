#!/usr/bin/env python3
# Project: osiris-framework
# Author: Samir Sanchez Garnica @sasaga92
# Version 1.0
# Date: 14/11/2022

from utilities.Colors import color
from tabulate import tabulate

class Help():
    def commands_core_thot(self):
        self.__commands_core = [[color.color('yellow', 'core commands Thot'), color.color('yellow', 'description')],
                          [color.color('green', 'sessions'), 'List all active sessions in Thot'],
                          [color.color('green', 'clear'), 'Clean to screen'],
                          [color.color('green', 'select id'),
                           'Select an active session in Thot and set it as interactive'],
                          [color.color('green', 'background or exit'),
                           'Send the THOT interpreter terminal in the background'],
                          [color.color('green', 'exec or execute'), 'Execute commands in a local shell'],
                          [color.color('green', 'help'), 'Show Thot help']
                          ]
        print('\n')
        print(color.color('yellow', '\t\t\t\t\t\tSHOW COMMANDS'))
        print(tabulate(self.__commands_core, headers='firstrow', tablefmt='grid', stralign='center'))


help = Help()