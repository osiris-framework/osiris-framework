#!/usr/bin/env python3
#Project: osiris-framework
#Author: Samir Sanchez Garnica @sasaga92
#Version 1.0
#Date: 14/11/2022

class Color:
    def __init__(self):
        '''
            Description: This class format with colors the text passed by argument
        '''
        self.__colors = {
            'end_color':'\033[0m',
            'red':'\033[91m',
            'gray':'\033[2m',
            'strike':'\033[9m',
            'underline':'\033[4m',
            'blue':'\033[94m',
            'green':'\033[92m',
            'yellow':'\033[93m',
            'cyan':'\033[96m',
            'cafe':'\033[52m',
            'black':'\033[30m',
            'lpurple':'\033[94m',
            'purple':'\033[95m',
            'green_ptrl':'\033[1;36m',
            'lgray':'\033[2m'
        }

        self.__text_format = ''

    def color(self, color, text):
        self.__color = color
        self.__text = str(text)

        if self.__color in self.__colors.keys():
            return self.__colors[self.__color] + self.__text + self.__colors['end_color']
        else:
            return self.__text_format




color = Color()