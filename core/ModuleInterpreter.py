#!/usr/bin/env python3
# Project: osiris-framework
# Author: Samir Sanchez Garnica @sasaga92
# Version 1.0
# Date: 14/11/2022

from utilities.Colors import color
from core.ModuleObtainer import obtainer
import readline
from glob import glob
from core.Validator import Validator
from tabulate import tabulate


def module_completer():
    # source: https://gist.github.com/iamatypeofwalrus/5637895
    def pathCompleter(text, state):
        line = readline.get_line_buffer().split()
        return [x for x in glob(text + '*')][state]

    class tabCompleter(object):

        def __init__(self):
            self.listCompleter = None

        def createListCompleter(self, ll):
            pass

            def listCompleter(text, state):
                line = readline.get_line_buffer()
                if not line:
                    return [c + " " for c in ll][state]
                else:
                    return [c + " " for c in ll if c.startswith(line)][state]

            self.listCompleter = listCompleter

    t = tabCompleter()
    t.createListCompleter(
        ["set", "exploit", "back", "check", "help", "info", 'banner', 'run', 'exec', 'clean', 'search', 'options',
         'set rhost', 'set rport', 'set target', 'set proxy', 'set password_file', 'set username_file', 'set username',
         'set password', 'sessions', 'set lhost', 'set lport', 'set payload generic/shell/bind_tcp',
         'set payload generic/shell/reverse_tcp'])
    readline.set_completer_delims('\t')
    readline.parse_and_bind("tab: complete")
    readline.set_completer(t.listCompleter)

class ModuleInterpreter(object):
    """
        Description: Class in charge of handling the interpretation of the module loading when using the use command
    """

    def __init__(self, module, category, module_input):
        self.option_value = None
        self.option_name = None
        self.__id = None
        self.__targets_message = None
        self.__options_message = None
        self.__option_value = None
        self.__option_name = None
        self.__module_input = module_input
        from core.ModuleObtainer import obtainer
        obtainer.obtaining_info(self.__module_input)
        module_completer()

        self.__module_name = module
        self.__category = category
        self.__options = obtainer.options
        self.__info = obtainer.info
        self.__exploit = obtainer.exploit
        self.__required = obtainer.required

        try:
            self.__options_payload = obtainer.options_payload
        except:
            pass

        while True:
            try:
                self.__user = "osiris"
                self.__shell_ask = input(color.color("underline", color.color("lgray", "%s" % (
                    self.__user))) + " " + self.__category + "(" + color.color('green_ptrl',
                                                                               self.__module_name) + ") > ").split()
                Validator(self.__shell_ask).validate_module_interpreter_mode()
            except (KeyboardInterrupt, EOFError):
                print(color.color("red", "[!]") + color.color("lgray", " Type exit to close the program"))

    def command_set_call(self, option_name, option_value):
        self.__option_name = option_name
        self.__option_value = option_value

        self.command_set_configure(ModuleInterpreter, self.__option_name, self.__option_value)

    def options_message(self):
        print('')
        self.__options_message = [[color.color('yellow', 'Options'), color.color('yellow', 'Require'),
                                   color.color('yellow', 'Description'), color.color('yellow', 'Value')]]

        for opt, val in obtainer.options.items():
            self.__options_message.append([opt, val[0], val[1], val[2]])
        print(tabulate(self.__options_message, headers='firstrow', tablefmt='simple', stralign='left'))
        print('\n')

    def help_message(self):
        print('')
        print(color.color('green', 'Options:              Require:              Description:              Value:'))
        print(color.color('lgray', '--------              --------              ------------              ------'))
        for opt, val in obtainer.options.items():
            print("{:23s}".format(opt) + '' + '            '.join(val))
        print('')

    def command_info_call(self):
        try:
            print('')
            print(color.color('green', '   Author: ') + obtainer.info['author'])
            print(color.color('green', '   Date: ') + obtainer.info['date'])
            print(color.color('green', '   Rank: ') + obtainer.info['rank'])
            print(color.color('green', '   Category: ') + obtainer.info['category'])
            print(color.color('green', '   Path: ') + obtainer.info['path'])
            print(color.color('green', '   License: ') + obtainer.info['license'])

            try:
                try:
                    obtainer.extra_info_obtainer(obtainer, __file__)
                except Exception:
                    pass
                try:
                    pass
                except (KeyError, NameError):
                    pass
                else:
                    if type(obtainer.extra_info['cve']) != list:
                        pass
                    else:
                        print(color.color('green', '   CVE ID: '), end='')
                        for id in obtainer.extra_info['cve']:
                            print(color.color('lgray', id), end=', ')
            except Exception as Error:
                pass
            print('\n\n')
            print(color.color('green', 'Module Options:'))
            print(color.color('green', '-' * 16))
            self.options_message(ModuleInterpreter)
            print('\n')
            print(color.color('green', 'Description:') + obtainer.info['description'] + '\n')
            print(color.color('green', 'References:'))
            for ref in obtainer.info['references']:
                print(color.color('red', ' - ') + ref)
        except KeyError:
            print(color.color("red", "[!]") + color.color("lgray",
                                                          "You must define author, date, rank, category, path, "
                                                          "license, description, reference keys in your information "
                                                          "dictionary")) 

        if obtainer.extra_info_obtainer(__file__):
            try:
                print(color.color('green', 'Targets') + color.color('red', '[{0}]'.format(
                    len(obtainer.extra_info['targets']))) + color.color('green', ':'))
                self.__targets_message = [[color.color('yellow', 'id'), color.color('yellow', 'Name')]]

                self.__id = 0
                for element in obtainer.extra_info['targets']:
                    self.__targets_message.append([self.__id, element])
                    self.__id += 1
                print('\n')
                print(tabulate(self.__targets_message, headers='firstrow', tablefmt='simple', stralign='left'))
                print('\n')
            except (NameError, KeyError, TypeError):
                pass
        print('')

    def command_set_configure(self, option_name, option_value):
        self.option_name = option_name
        self.option_value = option_value

        if self.option_name in obtainer.options:
            if self.option_value == "\"\"" or self.option_value == "\'\'":
                self.option_value = ""
            obtainer.options[str(self.option_name)][2] = self.option_value
        else:
            try:
                if self.option_value == "\"\"" or self.option_value == "\'\'":
                    self.option_value = ""
                obtainer.options_payload[str(self.option_name)][2] = self.option_value
            except Exception as e:
                print(color.color("red", "[!]") + color.color("lgray", " Option not defined in the module or payload"))
