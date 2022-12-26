#!/usr/bin/env python3
# Project: osiris-framework
# Author: Samir Sanchez Garnica @sasaga92
# Version 1.0
# Date: 16/11/2022
# Description: This class provides messages for the execution of modules

from utilities.Colors import color
import time


class Messages(object):
    def __init__(self):
        self.__password = None
        self.__username = None
        self.__target = None
        self.__module = None
        self.__category = None
        self.__message = ''
        self.__local_time = ''
        localtime = time.asctime(time.localtime(time.time()))
        self.name_module = ''

    def start_execution(self):
        self.__category = self.name_module.split('/')[-4]
        self.__module = self.name_module.split('/')[-1].split('.')[0]
        self.__local_time = time.asctime(time.localtime(time.time()))
        print(color.color("yellow", "[!] ") + color.color("lgray", "Starting ") + color.color("blue",
                                                                                              self.__category) + " " + color.color(
            "green", self.__module) + color.color("red", " Time: ") + color.color("green", self.__local_time))

    def end_execution(self):
        self.__category = self.name_module.split('/')[-4]
        self.__module = self.name_module.split('/')[-1].split('.')[0]
        self.__local_time = time.asctime(time.localtime(time.time()))
        print(color.color("blue", "[*] ") + color.color("green", self.__category) + " " + color.color("lgray",
                                                                                                      "Module execution completed ") + color.color(
            "red", "Time: ") + color.color("green", self.__local_time))

    def execution_info(self, message):
        self.__local_time = time.asctime(time.localtime(time.time()))
        print(color.color("yellow", "[!] INFO ") + color.color("green", "{}".format(message)) + color.color("red",
                                                                                                            " Time: ") + color.color(
            "green", self.__local_time))

    def execution_warning(self, message):
        self.__local_time = time.asctime(time.localtime(time.time()))
        print(color.color("yellow", "[!] WARNING ") + color.color("lgray", "{}".format(message)) + color.color("red",
                                                                                                               " Time: ") + color.color(
            "green", self.__local_time))

    def execution_error(self, message):
        self.__local_time = time.asctime(time.localtime(time.time()))
        print(color.color("red", "[-] ERROR ") + color.color("yellow", "{}".format(message)) + color.color("red",
                                                                                                           " Time: ") + color.color(
            "green", self.__local_time))

    def execution_credentials_found(self, message):
        if len(message) == 3:
            self.__target, self.__username, self.__password = message
            print(color.color("lgray", "[+] Password found in target: ") + color.color("cafe",
                                                                                       str(self.__target)) + " " + color.color(
                "lgray", "credentials:[") + color.color("cafe", str(self.__username)) + ":" + color.color("green",
                                                                                                          str(self.__password)) + "]" + color.color(
                "blue", " Correct Password"))

    def execution_try_credentials(self, message):
        if len(message) == 3:
            self.__target, self.__username, self.__password = message
            print(color.color("lgray", "[-] Testing on target: ") + color.color("cafe",
                                                                                str(self.__target)) + " " + color.color(
                "lgray", "credentials:") + " " + color.color("lgray",
                                                             str(self.__username)) + ":" + color.color(
                "cyan", str(self.__password)) + color.color("red", " Incorrect Password"))


print_message = Messages()
