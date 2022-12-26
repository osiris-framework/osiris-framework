#!/usr/bin/env python3
# Project: osiris-framework
# Author: Samir Sanchez Garnica @sasaga92
# Version 1.0
# Date: 01/12/2022

from utilities.Colors import color
from core.generator.ShellGenerator import ShellGenerator
from core.generator.TemplateGenerator import TemplateGenerator
from core.generator.WebShellGenerator import WebshellGenerator


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
                    key, value = values.replace(",", "").split("=")
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
                    return color.color("red", "[-] ") + color.color("lgray",
                                                                    "The selected payload is not correct, try again")
                else:
                    return self.__result
            except IndexError as Error:
                return color.color("red", "[-] ") + color.color("lgray",
                                                                "Mandatory parameters have not been provided, check the commands in ") + color.color(
                    "yellow", "{") + color.color("lgray", "generator help") + color.color("yellow", "}")

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


class Generator:
    def __init__(self):
        self.__list_payload_table = None
        self.__options_extra_info = None
        self.__parameters = {}
        self.__flag_key = None
        self.__port = None
        self.__host = None
        self.__payload = None
        self.__status = {}
        self.__temp_message = None
        self.__options_exploit = None
        self.__options_payload = None
        self.__key_error = None

        self.__keys_permitted = ['lhost', 'lport', 'rhost', 'rport', 'username', 'password', 'uri_webshell']

        self.__type_payload = {
            "cmd/unix/reverse/bash_i": "reverse",
            "cmd/unix/reverse/bash_196": "reverse",
            "cmd/unix/reverse/bash_readline": "reverse",
            "cmd/unix/reverse/bash_5": "reverse",
            "cmd/unix/reverse/bash_udp": "reverse",
            "cmd/unix/reverse/nc_mkfifo": "reverse",
            "cmd/unix/reverse/nc_e": "reverse",
            "cmd/unix/reverse/nc_c": "reverse",
            "cmd/unix/reverse/ncat_e": "reverse",
            "cmd/unix/reverse/ncat_udp": "reverse",
            "cmd/unix/reverse/rustcat": "reverse",
            "cmd/unix/reverse/perl": "reverse",
            "cmd/unix/reverse/perl_nosh": "reverse",
            "cmd/unix/reverse/php_exec": "reverse",
            "cmd/unix/reverse/php_shell_exec": "reverse",
            "cmd/unix/reverse/php_system": "reverse",
            "cmd/unix/reverse/php_passthru": "reverse",
            "cmd/unix/reverse/php_popen": "reverse",
            "cmd/unix/reverse/php_proc_open": "reverse",
            "cmd/unix/reverse/python_1": "reverse",
            "cmd/unix/reverse/python_2": "reverse",
            "cmd/unix/reverse/python_3_1": "reverse",
            "cmd/unix/reverse/python_3_2": "reverse",
            "cmd/unix/reverse/python3_shortest": "reverse",
            "cmd/unix/reverse/ruby": "reverse",
            "cmd/unix/reverse/ruby_nosh": "reverse",
            "cmd/unix/reverse/socat": "reverse",
            "cmd/unix/reverse/socat_tty": "reverse",
            "cmd/unix/reverse/nodejs": "reverse",
            "cmd/unix/reverse/telnet": "reverse",
            "cmd/unix/reverse/zsh": "reverse",
            "cmd/unix/reverse/lua": "reverse",
            "cmd/unix/reverse/lua_2": "reverse",
            "cmd/unix/reverse/golang": "reverse",
            "cmd/unix/reverse/vlang": "reverse",
            "cmd/unix/reverse/awk": "reverse",
            "cmd/unix/bind/php_open": "bind",
            "cmd/unix/bind/python_3_2": "bind",
            "cmd/windows/reverse/nc_exe": "reverse",
            "cmd/windows/reverse/groovy": "reverse",
            "cmd/windows/reverse/ncat_exe": "reverse",
            "cmd/windows/reverse/php_system": "reverse",
            "cmd/windows/reverse/php_popen": "reverse",
            "cmd/windows/bind/php_popen": "bind",
            "cmd/windows/reverse/php_proc_open": "reverse",
            "cmd/windows/reverse/powershell": "reverse",
            "cmd/windows/reverse/powershell_2": "reverse",
            "cmd/windows/reverse/powershell_3": "reverse",
            "cmd/windows/reverse/powershell_3_base64": "reverse",
            "cmd/windows/reverse/powershell_4_tls": "reverse",
            "cmd/windows/reverse/lua_2": "reverse",
        }

    def generator_payload(self, **kwargs):

        for key, value in kwargs.items():
            self.__options_payload = kwargs.get('options_payload') if (
                    kwargs.get('options_payload') is not None) else False
            self.__options_exploit = kwargs.get('options_exploit') if (
                    kwargs.get('options_exploit') is not None) else False
            self.__options_extra_info = kwargs.get('extra_info') if (
                    kwargs.get('extra_info') is not None) else False

        if self._validate_parameters()['code'] == 200:
            self.__list_payload_table = {
                "cmd/unix/reverse/bash_i": ShellGenerator(**self.__parameters).bash_i()['message'],
                "cmd/unix/reverse/bash_196": ShellGenerator(**self.__parameters).bash_196()['message'],
                "cmd/unix/reverse/bash_readline": ShellGenerator(**self.__parameters).bash_readline()['message'],
                "cmd/unix/reverse/bash_5": ShellGenerator(**self.__parameters).bash_5()['message'],
                "cmd/unix/reverse/bash_udp": ShellGenerator(**self.__parameters).bash_udp()['message'],
                "cmd/unix/reverse/nc_mkfifo": ShellGenerator(**self.__parameters).nc_mkfifo()['message'],
                "cmd/unix/reverse/nc_e": ShellGenerator(**self.__parameters).nc_e()['message'],
                "cmd/unix/reverse/nc_c": ShellGenerator(**self.__parameters).nc_c()['message'],
                "cmd/unix/reverse/ncat_e": ShellGenerator(**self.__parameters).nc_e()['message'],
                "cmd/unix/reverse/ncat_udp": ShellGenerator(**self.__parameters).ncat_udp()['message'],
                "cmd/unix/reverse/rustcat": ShellGenerator(**self.__parameters).rustcat()['message'],
                "cmd/unix/reverse/perl": ShellGenerator(**self.__parameters).perl()['message'],
                "cmd/unix/reverse/perl_nosh": ShellGenerator(**self.__parameters).perl_nosh()['message'],
                "cmd/unix/reverse/php_exec": ShellGenerator(**self.__parameters).php_exec()['message'],
                "cmd/unix/reverse/php_shell_exec": ShellGenerator(**self.__parameters).php_shell_exec()['message'],
                "cmd/unix/reverse/php_system": ShellGenerator(**self.__parameters).php_system()['message'],
                "cmd/unix/reverse/php_passthru": ShellGenerator(**self.__parameters).php_passthru()['message'],
                "cmd/unix/reverse/php_popen": ShellGenerator(**self.__parameters).php_popen()['message'],
                "cmd/unix/reverse/php_proc_open": ShellGenerator(**self.__parameters).php_proc_popen()['message'],
                "cmd/unix/reverse/python_1": ShellGenerator(**self.__parameters).python_1()['message'],
                "cmd/unix/reverse/python_2": ShellGenerator(**self.__parameters).python_2()['message'],
                "cmd/unix/reverse/python_3_1": ShellGenerator(**self.__parameters).python_3_1()['message'],
                "cmd/unix/reverse/python_3_2": ShellGenerator(**self.__parameters).python_3_2()['message'],
                "cmd/unix/reverse/python3_shortest": ShellGenerator(**self.__parameters).python3_shortest()['message'],
                "cmd/unix/reverse/ruby": ShellGenerator(**self.__parameters).ruby()['message'],
                "cmd/unix/reverse/ruby_nosh": ShellGenerator(**self.__parameters).ruby_nosh()['message'],
                "cmd/unix/reverse/socat": ShellGenerator(**self.__parameters).socat()['message'],
                "cmd/unix/reverse/socat_tty": ShellGenerator(**self.__parameters).socat_tty()['message'],
                "cmd/unix/reverse/nodejs": ShellGenerator(**self.__parameters).nodejs()['message'],
                "cmd/unix/reverse/telnet": ShellGenerator(**self.__parameters).telnet()['message'],
                "cmd/unix/reverse/zsh": ShellGenerator(**self.__parameters).zsh()['message'],
                "cmd/unix/reverse/lua": ShellGenerator(**self.__parameters).lua()['message'],
                "cmd/unix/reverse/lua_2": ShellGenerator(**self.__parameters).lua_2()['message'],
                "cmd/unix/reverse/golang": ShellGenerator(**self.__parameters).golang()['message'],
                "cmd/unix/reverse/vlang": ShellGenerator(**self.__parameters).vlang()['message'],
                "cmd/unix/reverse/awk": ShellGenerator(**self.__parameters).awk()['message'],
                "cmd/unix/bind/php_open": ShellGenerator(**self.__parameters).php_popen()['message'],
                "cmd/unix/bind/python_3_2": ShellGenerator(**self.__parameters).python_3_2()['message'],
                "cmd/windows/reverse/nc_exe": ShellGenerator(**self.__parameters).nc_exe()['message'],
                "cmd/windows/reverse/groovy": ShellGenerator(**self.__parameters).Groovy()['message'],
                "cmd/windows/reverse/ncat_exe": ShellGenerator(**self.__parameters).ncat_exe()['message'],
                "cmd/windows/reverse/php_system": ShellGenerator(**self.__parameters).php_system()['message'],
                "cmd/windows/reverse/php_popen": ShellGenerator(**self.__parameters).php_popen()['message'],
                "cmd/windows/bind/php_popen": ShellGenerator(**self.__parameters).php_popen()['message'],
                "cmd/windows/reverse/php_proc_open": ShellGenerator(**self.__parameters).php_proc_popen()['message'],
                "cmd/windows/reverse/powershell": ShellGenerator(**self.__parameters).powershell()['message'],
                "cmd/windows/reverse/powershell_2": ShellGenerator(**self.__parameters).powershell_2()['message'],
                "cmd/windows/reverse/powershell_3": ShellGenerator(**self.__parameters).powershell_3()['message'],
                "cmd/windows/reverse/powershell_3_base64": ShellGenerator(**self.__parameters).powershell_3_base64()['message'],
                "cmd/windows/reverse/powershell_4_tls": ShellGenerator(**self.__parameters).powershell_4_tls()['message'],
                "cmd/windows/reverse/lua_2": ShellGenerator(**self.__parameters).lua_2()['message'],
                "cmd/webshell/php_generic": WebshellGenerator(**self.__parameters).PHP()['message']
            }

            if self.__status['code'] == 200:
                self.__status['message'] = self.__list_payload_table.get(self.__payload) if self.__list_payload_table.get(self.__payload) is not None else color.color("lgray", "The payload ") + color.color("yellow", self.__payload) + color.color("lgray"," does not exist")

        return self.__status

    def _validate_parameters(self):
        self.__temp_message, self.__key_error = "", ""
        if not self.__options_payload:
            self.__temp_message += color.color("lgray", "the parameter ") + color.color("yellow", "{") + color.color(
                "green", "options_payload") + color.color("yellow", "}") + color.color("lgray", " is a mandatory ")
        if not self.__options_exploit:
            self.__temp_message += color.color("lgray", "the parameter ") + color.color("yellow", "{") + color.color(
                "green", "options_exploit") + color.color("yellow", "}") + color.color("lgray", " is a mandatory ")
        if not self.__options_extra_info:
            self.__temp_message += color.color("lgray", "the parameter ") + color.color("yellow", "{") + color.color(
                "green", "extra_info") + color.color("yellow", "}") + color.color("lgray", " is a mandatory ")

        self.__payload = self.__options_exploit['payload'][2] if len(
            self.__options_exploit['payload'][2]) > 0 else None

        for key, values in self.__options_payload.items():
            if not key in self.__keys_permitted:
                self.__flag_key = True
                self.__key_error += color.color("yellow", "{") + color.color(
                    "green", key) + color.color("yellow", "}") + " "
            else:
                self.__parameters[
                    'target' if key == 'lhost' or key == 'rhost' else 'port' if key == 'lport' or key == 'rport' else key] = \
                    values[2]

        try:
            self.__parameters['platform'] = self.__options_extra_info['targets'][
                int(self.__options_exploit['platform'][2])]
        except IndexError:
            self.__temp_message += color.color("lgray", "Target ID is out of range")
        except ValueError:
            self.__temp_message += color.color("lgray", "Target ID is not an appropriate value ")
        except KeyError:
            self.__parameters['platform'] = self.__options_extra_info['targets'][0]

        if self.__flag_key:
            self.__temp_message += color.color("lgray", "the parameter ") + self.__key_error + color.color("lgray",
                                                                                                           " Not allowed for this payload")

        self.__parameters['type'] = self.__type_payload.get(self.__payload)

        if len(self.__temp_message) > 0:
            self.__status['code'] = 500
            self.__status['message'] = self.__temp_message

        else:
            self.__status['code'] = 200

        return self.__status



generator_base = GeneratorBase()
generator = Generator()
