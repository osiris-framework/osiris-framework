#!/usr/bin/env python3
# Project: Osiris-Framework
# Version 1.337

from os import system, name


class ScreenCleaner:
    """
        Description: Class in charge of cleaning the screen in osiris.
    """

    def __init__(self):
        system('cls' if name == 'nt' else 'clear')
