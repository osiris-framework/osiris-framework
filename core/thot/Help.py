#!/usr/bin/env python3
# Project: Osiris-Framework
# Version 1.337

from utilities.Colors import color
from tabulate import tabulate


class Help:
    def __init__(self):
        self.__commands_core = None

    def commands_core_thot(self):
        self.__commands_core = [[color.color('yellow', 'core commands Thot'), color.color('yellow', 'description')],
                                [color.color('green', 'sessions'), 'List all active sessions in Thot'],
                                [color.color('green', 'clear'), 'Clean to screen'],
                                [color.color('green', 'select id'), 'Select an active session in Thot and set it as interactive'],
                                [color.color('green', 'kill id'), 'Removes a selected connection through its ID'],
                                [color.color('green', 'background or exit'),
                                 'Send the THOT interpreter terminal in the background'],
                                [color.color('green', 'exec or execute'), 'Execute commands in a local shell'],
                                [color.color('green', 'help'), 'Show Thot help']
                                ]
        print('\n')
        print(color.color('yellow', '\t\t\t\t\t\tSHOW COMMANDS'))
        print(tabulate(self.__commands_core, headers='firstrow', tablefmt='grid', stralign='center'))


help = Help()
