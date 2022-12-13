#!/usr/bin/env python3
# Project: osiris-framework
# Author: Samir Sanchez Garnica @sasaga92
# Version 1.0
# Date: 14/11/2022


from utilities.Colors import color
from utilities.ScreenCleaner import ScreenCleaner
from core.Banner import banner
from importlib import reload
from os import system
from core.ModuleObtainer import obtainer
from core.Help import help
from core.generator.Help import help_generator
from core.Interpreter import interpreter
from utilities.Files import update_modules
from core.Processor import processor
from core.generator.Generator import generator_base


class Validator(object):
    """
        Description: Class that manages the invocation of osiris commands.
    """

    def __init__(self, command):
        self.__command = command
        self.__target = None
        self.__port = None
        self.__type = None
        self.__platform = None
        self.__payload = None

    def validate_interpreter_mode(self):
        try:
            if self.__command[0].lower() == 'clean':
                ScreenCleaner()
            elif self.__command[0].lower() == 'search':
                try:
                    interpreter.search_module(query=self.__command[1])
                except IndexError:
                    print(color.color("yellow", "[!]") + color.color("lgray",
                                                                     " Invalid syntax must enter the search query!"))
                except TypeError:
                    pass
            elif self.__command[0].lower() == 'banner':
                banner.banner_welcome()
            elif self.__command[0].lower() == 'generator' and self.__command[1].lower() == 'list':
                help_generator.show_payloads()
            elif self.__command[0].lower() == 'generator' and self.__command[1].lower() == 'help':
                help_generator.show_help_generator()
            elif 'generator(' in self.__command[0].lower():
                print(color.color("green", "Generator: ") + color.color("lgray",
                                                                        generator_base.generator_base(self.__command)))
            elif self.__command[0].lower() == 'exit' or self.__command[0].lower() == 'close' or self.__command[
                0].lower() == 'quit':
                processor.kill_connections()
                exit(0)
            elif self.__command[0].lower() == 'use':
                from core.ModuleObtainer import obtainer
                from core.ModuleInterpreter import ModuleInterpreter

                try:
                    if obtainer.obtaining_info(self.__command[1]):
                        while True:
                            ModuleInterpreter("/".join(self.__command[1].split("/")[1:]),
                                              self.__command[1].split('/')[0], self.__command[1])

                except IndexError:
                    print(color.color("yellow", "[!]") + color.color("lgray", " Please enter the name of the module!"))
            elif self.__command[0].lower() == 'restart':
                import core.ModuleInterpreter  # import module_interpreter module from core foloder
                print(color.color("blue", "[~]") + color.color("lgray",
                                                               " Restarting the program please wait ... Finished!"))
                reload(core.ModuleInterpreter)
                from core.ModuleInterpreter import ModuleInterpreter
            elif self.__command[0].lower() == 'exec':
                try:
                    self.__command.remove('exec' if self.__command[0] == 'exec' else 'execute')
                    system(' '.join(self.__command))
                except IndexError:
                    print(color.color("yellow", "[!]") + color.color("lgray", " Please enter a command!"))

            elif self.__command[0].lower() == 'upgrade':
                interpreter.check_upgrade()
            elif self.__command[0].lower() == 'help':
                help.help_osiris()
            elif self.__command[0].lower() == 'sessions':
                processor.list_sessions()
            elif 'select' in self.__command[0].lower():
                processor.get_console(self.__command[0].lower() + str(" ") + str(self.__command[1]), "base")
            elif self.__command[0].lower() == 'reload_modules':
                update_modules.processor_update_module('core/Completer.py')
            else:
                print(color.color("yellow", "[!]") + color.color("lgray", " Option not found :("))

        except (KeyboardInterrupt, EOFError):
            print(color.color("yellow", "[!]") + color.color("lgray", "Type exit to close the program"))
        except IndexError:
            return None

    def validate_module_interpreter_mode(self):
        from core.ModuleInterpreter import ModuleInterpreter
        from core.Interpreter import interpreter

        try:
            if self.__command[0].lower() == "clean":
                ScreenCleaner()
            elif self.__command[0].lower() == "banner":
                banner.banner_welcome()
            elif self.__command[0].lower() == 'search':
                try:
                    interpreter.search_module(query=self.__command[1])
                except IndexError:
                    print(color.color("red", "[!]") + color.color("lgray",
                                                                  " Invalid syntax must enter the search query!"))
                except TypeError:
                    pass
            elif self.__command[0].lower() == 'exit' or self.__command[0].lower() == 'close' or self.__command[0].lower() == "back":
                import core.Interpreter
                from core.Completer import completer  # import completer
                reload(core.Interpreter)
                from core.Interpreter import interpreter
                completer()  # start completer
                while True:
                    interpreter.start_interpreter()  # restart interpreter
            elif self.__command[0].lower() == "options":
                ModuleInterpreter.options_message(ModuleInterpreter)

                try:
                    self.__payload = obtainer.options['payload'][2]
                    obtainer.payload_info(self.__payload)
                except Exception as Error:
                    pass
            elif self.__command[0].lower() == "show":
                if 'payloads' in self.__command[1].lower():
                    help.show_payloads_osiris()  # Show payloads
            elif self.__command[0].lower() == 'set':
                try:
                    if 'payload' in self.__command[1] and '/' in self.__command[2]:
                        self.__name_payload = self.__command[2]
                        self.__path_payloads = 'modules/payloads/' + self.__command[2]
                        try:
                            obtainer.options_payload = getattr(
                                __import__(self.__path_payloads.replace("/", "."), fromlist=['options_payload']),
                                'options_payload')
                        except:
                            print(color.color('red', '[!]') + color.color("lgray", " Please select a valid payload"))
                            return False
                    ModuleInterpreter.command_set_call(ModuleInterpreter, self.__command[1],
                                                       " ".join(self.__command[2:]))
                except IndexError:
                    print(color.color("red", "[!]") + color.color("lgray",
                                                                  " Invalid syntax you must enter the option and the new value!"))
            elif self.__command[0].lower() == 'info' or self.__command[0].lower() == 'information':
                ModuleInterpreter.command_info_call(ModuleInterpreter)
                ModuleInterpreter.command_set_call(ModuleInterpreter, self.__command[1], " ".join(self.__command[2:]))
            elif self.__command[0].lower() == 'exploit' or self.__command[0].lower() == 'run':
                self.__opt = []
                self.__val = []
                self.__stat = []

                for o, v in obtainer.options.items():
                    self.__opt.append(o)
                    self.__val.append(v[2])
                    self.__stat.append(v[0])
                try:
                    for o, v in obtainer.options_payload.items():
                        self.__opt.append(o)
                        self.__val.append(v[2])
                        self.__stat.append(v[0])
                except:
                    pass

                self.__i = 0

                while self.__i < len(self.__opt):
                    try:
                        if self.__stat[self.__i] == 'Yes':

                            if len(self.__val[self.__i]) <= 0:
                                print(color.color("red", "[!]") + color.color("lgray",
                                                                              " You must set the option {0}").format(
                                    self.__opt[self.__i]))
                                return False
                                # _flag = True
                                break
                    except IndexError:
                        print
                    self.__i += 1

                if obtainer.required['start_required'] == True or obtainer.required['start_required'].lower() == "True":
                    print(color("green", "[+]") + color.color("lgray", " Starting module..."))
                    obtainer.exploit()
                    print(color.color("green", "[+]") + color.color("lgray", " Execution of finished module..."))
                else:
                    obtainer.exploit()
            elif self.__command[0].lower() == 'check':
                if obtainer.required['check_required'] == True or obtainer.required['check_required'].lower() == "true":
                    obtainer.check()
                else:
                    print(color.color("red", "[!]") + color.color("lgray",
                                                                  " The module does not have verification option!"))
            elif self.__command[0].lower() == 'exec' or self.__command[0].lower() == 'execute':
                try:
                    self.__command.remove('exec' if self.__command[0] == 'exec' else 'execute')
                    system(' '.join(self.__command))
                except IndexError:
                    print(color.color("red", "[!]") + color.color("lgray", " Please enter a command!"))
            elif self.__command[0].lower() == 'upgrade':
                interpreter.check_upgrade()
            elif self.__command[0].lower() == 'sessions':
                processor.list_sessions()
            elif 'select' in self.__command[0].lower():
                processor.get_console(self.__command[0].lower() + str(" ") + str(self.__command[1]), "module")
            else:
                print(color.color("red", "[!]") + color.color("lgray", " Option not found :("))
        except (KeyboardInterrupt, EOFError):
            print(color.color("red", "[!]") + color.color("lgray", "Type exit to close the program"))
        except IndexError:
            return None
