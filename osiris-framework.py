#!/usr/bin/env python3
# Project: osiris-framework
# Author: Samir Sanchez Garnica @sasaga92
# Version 1.0
# Date: 14/11/2022

from core.Interpreter import interpreter
from core.Banner import banner

def main():
    banner.banner_welcome()
    while True:
        interpreter.start_interpreter()


if __name__ == '__main__':
	main()
