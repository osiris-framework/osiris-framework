#!/usr/bin/env python3
# Project: Osiris-Framework
# Version 1.337

from core.Interpreter import interpreter
from core.Banner import banner


def main():
    banner.banner_welcome()
    while True:
        interpreter.start_interpreter()


if __name__ == '__main__':
    main()
