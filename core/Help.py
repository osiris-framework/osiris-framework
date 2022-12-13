#!/usr/bin/env python3
# Project: osiris-framework
# Author: Samir Sanchez Garnica @sasaga92
# Version 1.0
# Date: 14/11/2022

from utilities.Colors import color
from tabulate import tabulate


class Help(object):
    """
        Description: This class shows the description of the osiris framework commands.
    """

    def __init__(self):
        self.__show_payloads = None
        self.__core_commands_osiris = None

    def help_osiris(self):
        self.__core_commands_osiris = [[color.color('yellow', 'commands'), color.color('yellow', 'description')],
                                       [color.color('green', 'clean'), 'clean the screen'],
                                       [color.color('green', 'search'), 'search for modules in osiris'],
                                       [color.color('green', 'banner'), 'Show an osiris banner'],
                                       [color.color('green', 'exit'), 'close the program in osiris'],
                                       [color.color('green', 'use'), 'select an osiris module for later use'],
                                       [color.color('green', 'restart'), 'Restart osiris interpreter'],
                                       [color.color('green', 'exec'), 'run an operating system command'],
                                       [color.color('green', 'back'), 'goes to a section back'],
                                       [color.color('green', 'upgrade'), 'Check for a new osiris update'],
                                       [color.color('green', 'reload_modules'),'Performs an update of the module database in osiris'],
                                       [color.color('green', 'generator'),'Generates payloads via arguments from the osiris framework base console'],
                                       [color.color('green', 'generator list'),'Displays the list of payloads available to generate from osiris'],
                                       [color.color('green', 'generator help'),'Show help about payload generator class']
                                       ]
        print('\n')
        print(color.color('yellow', '\t\t\t\t\tCORE COMMANDS'))
        print(tabulate(self.__core_commands_osiris, headers='firstrow', tablefmt='simple', stralign='Left'))

    def show_payloads_osiris(self):
        self.__show_payloads = [[color.color('yellow', 'payloads'), color.color('yellow', 'description')],
                                [color.color("green", "cmd/unix/reverse/bash_i"),
                                 color.color("lgray", "generates a reverse shell using bash_i")],
                                [color.color("green", "cmd/unix/reverse/bash_196"),
                                 color.color("lgray", "generates a reverse shell using bash_196")],
                                [color.color("green", "cmd/unix/reverse/bash_readline"),
                                 color.color("lgray", "generates a reverse shell using bash_readline")],
                                [color.color("green", "cmd/unix/reverse/bash_5"),
                                 color.color("lgray", "generates a reverse shell using bash_5")],
                                [color.color("green", "cmd/unix/reverse/bash_udp"),
                                 color.color("lgray", "generates a reverse shell using bash_udp")],
                                [color.color("green", "cmd/unix/reverse/nc_mkfifo"),
                                 color.color("lgray", "generates a reverse shell using nc_mkfifo")],
                                [color.color("green", "cmd/unix/reverse/nc_e"),
                                 color.color("lgray", "generates a reverse shell using nc_e")],
                                [color.color("green", "cmd/unix/reverse/nc_c"),
                                 color.color("lgray", "generates a reverse shell using nc_c")],
                                [color.color("green", "cmd/unix/reverse/ncat_e"),
                                 color.color("lgray", "generates a reverse shell using ncat_e")],
                                [color.color("green", "cmd/unix/reverse/ncat_udp"),
                                 color.color("lgray", "generates a reverse shell using ncat_udp")],
                                [color.color("green", "cmd/unix/reverse/rustcat"),
                                 color.color("lgray", "generates a reverse shell using rustcat")],
                                [color.color("green", "cmd/unix/reverse/perl"),
                                 color.color("lgray", "generates a reverse shell using perl")],
                                [color.color("green", "cmd/unix/reverse/perl_nosh"),
                                 color.color("lgray", "generates a reverse shell using perl_nosh")],
                                [color.color("green", "cmd/unix/reverse/php_exec"),
                                 color.color("lgray", "generates a reverse shell using php_exec")],
                                [color.color("green", "cmd/unix/reverse/php_shell_exec"),
                                 color.color("lgray", "generates a reverse shell using php_shell_exec")],
                                [color.color("green", "cmd/unix/reverse/php_system"),
                                 color.color("lgray", "generates a reverse shell using php_system")],
                                [color.color("green", "cmd/unix/reverse/php_passthru"),
                                 color.color("lgray", "generates a reverse shell using php_passthru")],
                                [color.color("green", "cmd/unix/reverse/php_popen"),
                                 color.color("lgray", "generates a reverse shell using php_popen")],
                                [color.color("green", "cmd/unix/reverse/php_proc_open"),
                                 color.color("lgray", "generates a reverse shell using php_proc_open")],
                                [color.color("green", "cmd/unix/reverse/python_1"),
                                 color.color("lgray", "generates a reverse shell using python_1")],
                                [color.color("green", "cmd/unix/reverse/python_2"),
                                 color.color("lgray", "generates a reverse shell using python_2")],
                                [color.color("green", "cmd/unix/reverse/python_3_1"),
                                 color.color("lgray", "generates a reverse shell using python_3_1")],
                                [color.color("green", "cmd/unix/reverse/python_3_2"),
                                 color.color("lgray", "generates a reverse shell using python_3_2")],
                                [color.color("green", "cmd/unix/reverse/python3_shortest"),
                                 color.color("lgray", "generates a reverse shell using python3_shortest")],
                                [color.color("green", "cmd/unix/reverse/ruby"),
                                 color.color("lgray", "generates a reverse shell using ruby")],
                                [color.color("green", "cmd/unix/reverse/ruby_nosh"),
                                 color.color("lgray", "generates a reverse shell using ruby_nosh")],
                                [color.color("green", "cmd/unix/reverse/socat"),
                                 color.color("lgray", "generates a reverse shell using socat")],
                                [color.color("green", "cmd/unix/reverse/socat_tty"),
                                 color.color("lgray", "generates a reverse shell using socat_tty")],
                                [color.color("green", "cmd/unix/reverse/nodejs"),
                                 color.color("lgray", "generates a reverse shell using nodejs")],
                                [color.color("green", "cmd/unix/reverse/telnet"),
                                 color.color("lgray", "generates a reverse shell using telnet")],
                                [color.color("green", "cmd/unix/reverse/zsh"),
                                 color.color("lgray", "generates a reverse shell using zsh")],
                                [color.color("green", "cmd/unix/reverse/lua"),
                                 color.color("lgray", "generates a reverse shell using lua")],
                                [color.color("green", "cmd/unix/reverse/lua_2"),
                                 color.color("lgray", "generates a reverse shell using lua_2")],
                                [color.color("green", "cmd/unix/reverse/golang"),
                                 color.color("lgray", "generates a reverse shell using golang")],
                                [color.color("green", "cmd/unix/reverse/vlang"),
                                 color.color("lgray", "generates a reverse shell using vlang")],
                                [color.color("green", "cmd/unix/reverse/awk"),
                                 color.color("lgray", "generates a reverse shell using awk")],
                                [color.color("green", "cmd/unix/bind/php_open"),
                                 color.color("lgray", "generates a bind shell using php_open")],
                                [color.color("green", "cmd/unix/bind/python_3_2"),
                                 color.color("lgray", "generates a bind shell using python_3_2")],
                                [color.color("green", "cmd/windows/reverse/nc_exe"),
                                 color.color("lgray", "generates a reverse shell using nc_exe")],
                                [color.color("green", "cmd/windows/reverse/groovy"),
                                 color.color("lgray", "generates a reverse shell using groovy")],
                                [color.color("green", "cmd/windows/reverse/ncat_exe"),
                                 color.color("lgray", "generates a reverse shell using ncat_exe")],
                                [color.color("green", "cmd/windows/reverse/php_system"),
                                 color.color("lgray", "generates a reverse shell using php_system")],
                                [color.color("green", "cmd/windows/reverse/php_popen"),
                                 color.color("lgray", "generates a reverse shell using php_popen")],
                                [color.color("green", "cmd/windows/bind/php_popen"),
                                 color.color("lgray", "generates a bind shell using php_popen")],
                                [color.color("green", "cmd/windows/reverse/php_proc_open"),
                                 color.color("lgray", "generates a reverse shell using php_proc_open")],
                                [color.color("green", "cmd/windows/reverse/powershell"),
                                 color.color("lgray", "generates a reverse shell using powershell")],
                                [color.color("green", "cmd/windows/reverse/powershell_2"),
                                 color.color("lgray", "generates a reverse shell using powershell_2")],
                                [color.color("green", "cmd/windows/reverse/powershell_3"),
                                 color.color("lgray", "generates a reverse shell using powershell_3")],
                                [color.color("green", "cmd/windows/reverse/powershell_3_base64"),
                                 color.color("lgray", "generates a reverse shell using powershell_3_base64")],
                                [color.color("green", "cmd/windows/reverse/powershell_4_tls"),
                                 color.color("lgray", "generates a reverse shell using powershell_4_tls")],
                                [color.color("green", "cmd/windows/reverse/lua_2"),
                                 color.color("lgray", "generates a reverse shell using lua_2")]
                                ]
        print("\n")
        print(color.color("yellow", '\t\t\t\t\tShow Payloads'))
        print(tabulate(self.__show_payloads, headers='firstrow', tablefmt='simple', stralign='left'))


help = Help()
