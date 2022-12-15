#!/usr/bin/env python3
# Project: osiris-framework
# Author: Samir Sanchez Garnica @sasaga92
# Version 1.0
# Date: 14/11/2022

from tabulate import tabulate
from utilities.Colors import color


class Anubis:
    def __init__(self):
        self.__sysinfo_result = None
        self.__data = None
        self.__anubis_command_permitted = ['download', 'upload', 'sysinfo']

    def processor(self, information: dict):
        try:
            for __key, __value in information.items():
                if __key in self.__anubis_command_permitted:
                    if __key == 'sysinfo':
                        self._print_sysinfo(__value)
                        break
        except KeyError:
            pass

    def _print_sysinfo(self, sysinfo: list):
        self.__sysinfo_result = [
            [color.color('yellow', 'System'), color.color('yellow', 'Processor'), color.color('yellow', 'Node'), color.color('yellow', 'Machine'),
             color.color('yellow', 'version'), color.color('yellow', 'Release'), color.color('yellow', 'Username')]]

        self.__sysinfo_result.append(
            [color.color("lgray", sysinfo[0]), color.color("lgray", sysinfo[1]), color.color("lgray", sysinfo[2]),
             color.color("lgray", sysinfo[3]), color.color("lgray", sysinfo[4]), color.color("lgray", sysinfo[5]), color.color("cyan", sysinfo[6])])

        if len(self.__sysinfo_result) > 1:
            print(tabulate(self.__sysinfo_result, headers='firstrow', tablefmt='simple', stralign='left'))
            print('')


anubis = Anubis()
