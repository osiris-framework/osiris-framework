#!/usr/bin/env python3
# Project: osiris-framework
# Author: Samir Sanchez Garnica @sasaga92
# Version 1.0
# Date: 14/11/2022

from os import getcwd
from sys import path
from importlib import reload
from utilities.Colors import color
from tabulate import tabulate

class ModuleObtainer(object):
    """
        Description: Class in charge of loading all the module logic when the use command is used.
    """

    def __init__(self):
        self.__option_message_payload = None
        self.__path_payload = None
        self.__payload = None
        self.extra_info = None
        self.check = None
        self.required = None
        self.info = None
        self.options_payload = None
        self.__path_payloads = None
        self.options = None
        self.exploit = None
        self.__module = None
        self.__module_path = None
        self.__module_name = None
        self.__category = None

    def obtaining_info(self, module):
        try:
            self.__module = str(module)
            self.__category = self.__module.split('/')[0]
            self.__module_name = self.__module.split('/')[-1]
            self.__module_path = str(getcwd() + '/modules/{}.py'.format(self.__module)).split('/')
            self.__module_path.remove(self.__module_name + '.py')
            self.__module_path = '/'.join(self.__module_path)
            path.append(self.__module_path)
        except IndexError:
            print(color.color("red", "[-] ") + color.color("lgray", "The Module {} ".format(color.color("cafe", self.__module)) + color.color("lgray", " not found")))
            return False

        try:
            try:
                self.__module = __import__(self.__module_name)
            except ValueError:
                print(color.color("red", "[-] ") + color.color("lgray", "Please Enter the full module name"))
                return False
            reload(self.__module)

            self.exploit = getattr(__import__(self.__module_name, fromlist=['exploit']), 'exploit')
            self.options = getattr(__import__(self.__module_name, fromlist=['options']), 'options')

            try:
                self.__path_payloads = 'modules/payloads/' + self.options['payload'][2]
                self.options_payload = getattr(__import__(self.__path_payloads.replace("/","."), fromlist=['options_payload']), 'options_payload')
            except:
                pass
            self.info = getattr(__import__(self.__module_name, fromlist=['info']), 'info')
            self.required = getattr(__import__(self.__module_name, fromlist=['required']), 'required')

            if self.required['check_required'] == True or self.required['check_required'].lower() == "true":
                self.check = getattr(__import__(self.__module_name, fromlist=['check']), 'check')
        except AttributeError:
            print(color.color("red", "[-] ") + color.color("lgray", "Your module {}".format(color.color("cafe", self.__module_name)) + color.color("lgray", " must meet the base template requirements.")))
            return False

        except ImportError as Error:
            print(color.color("red", "[-] ") + color.color("lgray", "The Module {} ".format(
                color.color("cafe", self.__module_name)) + color.color("lgray", " not found")))
            return False
        else:
            return True

    def description_obtainer(self, module):
        try:
            self.__module = str(module)
            self.__category  = self.__module.split('/')[0]
            self.__module_name = self.__module.split('/')[-1]
            self.__module_path = str(getcwd() + '/modules/{}.py'.format(self.__module)).split('/')
            self.__module_path.remove(self.__module_name + '.py')
            self.__module_path = '/'.join(self.__module_path)
            path.append(self.__module_path)
            self.info = getattr(__import__(self.__module_name, fromlist=['info']), 'info')
        except Exception as Error:
            return False
        else:
            return True

    def extra_info_obtainer(self, module):
        reload(self.__module)

        try:
            self.extra_info = getattr(__import__(self.__module_name, fromlist=['extra_info']), 'extra_info')
        except (AttributeError, ImportError, NameError):
            return False
        else:
            return True

    def payload_info(self, payload):
        self.__payload = str(payload)
        self.__path_payload = 'modules/payloads/' + self.__payload

        try:
            self.options_payload = getattr(__import__(self.__path_payload.replace("/", "."), fromlist=['options_payload']), 'options_payload')
            print(color.color("lgray", "Payload options (") + color.color("purple",self.__payload) + color.color("lgray", ")"))
            print('')

            self.__option_message_payload = [[color.color('yellow','Name'),color.color('yellow','Require'),color.color('yellow','Description'),color.color('yellow','Value')]]

            for opt, val in self.options_payload.items():
                self.__option_message_payload.append([opt, val[0], val[1], val[2]])

            print(tabulate(self.__option_message_payload, headers='firstrow', tablefmt='simple', stralign='left'))
            print('\n')

        except Exception as Error:
            return False

obtainer = ModuleObtainer()