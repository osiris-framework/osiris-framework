#!/usr/bin/env python3
# Project: osiris-framework
# Author: Samir Sanchez Garnica @sasaga92
# Version 1.0
# Date: 14/11/2022

from os import system, name


class ScreenCleaner:
    """
        Description: Class in charge of cleaning the screen in osiris.
    """

    def __init__(self):
        system('cls' if name == 'nt' else 'clear')
