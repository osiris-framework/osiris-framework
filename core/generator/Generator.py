#!/usr/bin/env python3
# Project: osiris-framework
# Author: Samir Sanchez Garnica @sasaga92
# Version 1.0
# Date: 01/12/2022

from utilities.Colors import color
from core.generator.ShellGenerator import ShellGenerator
from core.generator.TemplateGenerator import TemplateGenerator


class GeneratorBase:
    def __init__(self):
        self.__result = None
        self.__shell_generate_table = None
        self.__shell_template_table = None
        self.__parameter = None
        self.__permitted = ['target', 'port', 'platform', 'payload', 'ShellcodeGenerator', 'TemplateGenerator']
        self.__status = {'message': '', 'code': 0}
        self.__parameters = {}

    def generator_base(self, __parameters):
        self.__parameter = __parameters
        if 'shell' in self.__parameter[0].lower():
            try:
                self.__parameter.pop(0)
                self.__parameter[4] = self.__parameter[4].replace(")", "")
                for values in self.__parameter:
                    key, value = values.replace(",","").split("=")
                    self.__parameters[key] = value

                self.__shell_generate_table = {
                    'bash_i': ShellGenerator(**self.__parameters).bash_i()['message'],
                    'bash_196': ShellGenerator(**self.__parameters).bash_196()['message'],
                    'bash_readline': ShellGenerator(**self.__parameters).bash_readline()['message'],
                    'bash_5': ShellGenerator(**self.__parameters).bash_5()['message'],
                    'bash_udp': ShellGenerator(**self.__parameters).bash_udp()['message'],
                    'nc_mkfifo': ShellGenerator(**self.__parameters).nc_mkfifo()['message'],
                    'nc_e': ShellGenerator(**self.__parameters).nc_e()['message'],
                    'nc_exe': ShellGenerator(**self.__parameters).nc_exe()['message'],
                    'Groovy': ShellGenerator(**self.__parameters).Groovy()['message'],
                    'ncat_exe': ShellGenerator(**self.__parameters).ncat_exe()['message'],
                    'nc_c': ShellGenerator(**self.__parameters).nc_c()['message'],
                    'ncat_e': ShellGenerator(**self.__parameters).ncat_e()['message'],
                    'ncat_udp': ShellGenerator(**self.__parameters).ncat_udp()['message'],
                    'rustcat': ShellGenerator(**self.__parameters).rustcat()['message'],
                    'perl': ShellGenerator(**self.__parameters).perl()['message'],
                    'perl_nosh': ShellGenerator(**self.__parameters).perl_nosh()['message'],
                    'php_exec': ShellGenerator(**self.__parameters).php_exec()['message'],
                    'php_shell_exec': ShellGenerator(**self.__parameters).php_shell_exec()['message'],
                    'php_system': ShellGenerator(**self.__parameters).php_system()['message'],
                    'php_passthru': ShellGenerator(**self.__parameters).php_passthru()['message'],
                    'php_popen': ShellGenerator(**self.__parameters).php_popen()['message'],
                    'php_proc_open': ShellGenerator(**self.__parameters).php_proc_popen()['message'],
                    'powershell': ShellGenerator(**self.__parameters).powershell()['message'],
                    'powershell_2': ShellGenerator(**self.__parameters).powershell_2()['message'],
                    'powershell_3': ShellGenerator(**self.__parameters).powershell_3()['message'],
                    'powershell_3_base64': ShellGenerator(**self.__parameters).powershell_3_base64()['message'],
                    'powershell_4_tls': ShellGenerator(**self.__parameters).powershell_4_tls()['message'],
                    'python_1': ShellGenerator(**self.__parameters).python_1()['message'],
                    'python_2': ShellGenerator(**self.__parameters).python_2()['message'],
                    'python_3_1': ShellGenerator(**self.__parameters).python_3_1()['message'],
                    'python_3_2': ShellGenerator(**self.__parameters).python_3_2()['message'],
                    'python3_shortest': ShellGenerator(**self.__parameters).python3_shortest()['message'],
                    'ruby': ShellGenerator(**self.__parameters).ruby()['message'],
                    'ruby_nosh': ShellGenerator(**self.__parameters).ruby_nosh()['message'],
                    'socat': ShellGenerator(**self.__parameters).socat()['message'],
                    'socat_tty': ShellGenerator(**self.__parameters).socat_tty()['message'],
                    'nodejs': ShellGenerator(**self.__parameters).nodejs()['message'],
                    'telnet': ShellGenerator(**self.__parameters).telnet()['message'],
                    'zsh': ShellGenerator(**self.__parameters).zsh()['message'],
                    'lua': ShellGenerator(**self.__parameters).lua()['message'],
                    'lua_2': ShellGenerator(**self.__parameters).lua_2()['message'],
                    'golang': ShellGenerator(**self.__parameters).golang()['message'],
                    'vlang': ShellGenerator(**self.__parameters).vlang()['message'],
                    'awk': ShellGenerator(**self.__parameters).awk()['message']
                }

                self.__result = self.__shell_generate_table.get(self.__parameters['payload'])

                if self.__result is None:
                    return color.color("red", "[-] ") + color.color("lgray","The selected payload is not correct, try again")
                else:
                    return self.__result
            except IndexError as Error:
                return color.color("red", "[-] ") + color.color("lgray","Mandatory parameters have not been provided, check the commands in ") + color.color("yellow","{") + color.color("lgray", "generator help") + color.color("yellow","}")

        elif 'template' in self.__parameter[0].lower():
            try:
                self.__parameter.pop(0)
                self.__parameter[4] = self.__parameter[4].replace(")", "")
                for values in self.__parameter:
                    key, value = values.replace(",", "").split("=")
                    self.__parameters[key] = value

                self.__shell_template_table = {
                    'C': TemplateGenerator(**self.__parameters).C()['message'],
                    'Dart': TemplateGenerator(**self.__parameters).Dart()['message'],
                    'Python3_windows': TemplateGenerator(**self.__parameters).Python3_windows()['message'],
                    'Nodejs': TemplateGenerator(**self.__parameters).Nodejs()['message'],
                    'Java': TemplateGenerator(**self.__parameters).Java()['message'],
                    'Java_2': TemplateGenerator(**self.__parameters).Java_2()['message'],
                    'Java_3': TemplateGenerator(**self.__parameters).Java_3()['message'],
                    'Javascript': TemplateGenerator(**self.__parameters).Javascript()['message'],
                    'PHP': TemplateGenerator(**self.__parameters).PHP()['message'],
                    'Perl': TemplateGenerator(**self.__parameters).Perl()['message'],
                    'Haskell_1': TemplateGenerator(**self.__parameters).Haskell_1()['message'],
                    'CsharpBash_i': TemplateGenerator(**self.__parameters).CsharpBash_i()['message'],
                    'CsharpTcpClient': TemplateGenerator(**self.__parameters).CsharpTcpClient()['message']
                }

                self.__result = self.__shell_template_table.get(self.__parameters['payload'])

                if self.__result is None:
                    return color.color("red", "[-] ") + color.color("lgray",
                                                                    "The selected payload is not correct, try again")
                else:
                    return self.__result
            except IndexError as Error:
                return color.color("red", "[-] ") + color.color("lgray",
                                                                "Mandatory parameters have not been provided, check the commands in ") + color.color(
                    "yellow", "{") + color.color("lgray", "generate help") + color.color("yellow", "}")
        else:
            return color.color("red", "[-] ") + color.color("lgray",
                                                            "This generator is not valid, check the commands in ") + color.color(
                "yellow", "{") + color.color("lgray", "generator help") + color.color("yellow", "}")


generator_base = GeneratorBase()
