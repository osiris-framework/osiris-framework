#!/usr/bin/env python3
# Project: Osiris-Framework
# Version 1.337

from utilities.Colors import color
from tabulate import tabulate


class Help:
    def __init__(self):
        self.__show_help_generator = None
        self.__show_generator = None

    def show_payloads(self):
        self.__show_generator = [[color.color('yellow', 'Payload'), color.color('yellow', 'Platform Support'),
                                  color.color('yellow', 'Type Connection'), color.color('yellow', 'Category')],
                                 [color.color("green", "bash_i"), color.color("lgray", "GNU/Linux & MacOSX"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "ShellGenerator")],
                                 [color.color("green", "bash_196"), color.color("lgray", "GNU/Linux & MacOSX"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "ShellGenerator")],
                                 [color.color("green", "bash_readline"), color.color("lgray", "GNU/Linux & MacOSX"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "ShellGenerator")],
                                 [color.color("green", "bash_5"), color.color("lgray", "GNU/Linux & MacOSX"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "ShellGenerator")],
                                 [color.color("green", "bash_udp"), color.color("lgray", "GNU/Linux & MacOSX"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "ShellGenerator")],
                                 [color.color("green", "nc_mkfifo"), color.color("lgray", "GNU/Linux & MacOSX"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "ShellGenerator")],
                                 [color.color("green", "nc_e"), color.color("lgray", "GNU/Linux & MacOSX"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "ShellGenerator")],
                                 [color.color("green", "nc_exe"), color.color("lgray", "Microsoft Windows"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "ShellGenerator")],
                                 [color.color("green", "Groovy"), color.color("lgray", "Microsoft Windows"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "ShellGenerator")],
                                 [color.color("green", "ncat_exe"), color.color("lgray", "Microsoft Windows"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "ShellGenerator")],
                                 [color.color("green", "nc_c"), color.color("lgray", "GNU/Linux & MacOSX"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "ShellGenerator")],
                                 [color.color("green", "ncat_e"), color.color("lgray", "GNU/Linux & MacOSX"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "ShellGenerator")],
                                 [color.color("green", "ncat_udp"), color.color("lgray", "GNU/Linux & MacOSX"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "ShellGenerator")],
                                 [color.color("green", "rustcat"), color.color("lgray", "GNU/Linux & MacOSX"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "ShellGenerator")],
                                 [color.color("green", "perl"), color.color("lgray", "GNU/Linux & MacOSX"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "ShellGenerator")],
                                 [color.color("green", "perl_nosh"), color.color("lgray", "GNU/Linux & MacOSX"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "ShellGenerator")],
                                 [color.color("green", "php_exec"), color.color("lgray", "GNU/Linux & MacOSX"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "ShellGenerator")],
                                 [color.color("green", "php_shell_exec"), color.color("lgray", "GNU/Linux & MacOSX"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "ShellGenerator")],
                                 [color.color("green", "php_system"),
                                  color.color("lgray", "GNU/Linux, MacOSX & Microsoft Windows"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "ShellGenerator")],
                                 [color.color("green", "php_passthru"), color.color("lgray", "GNU/Linux & MacOSX"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "ShellGenerator")],
                                 [color.color("green", "php_popen"),
                                  color.color("lgray", "GNU/Linux, MacOSX & Microsoft Windows"),
                                  color.color("lgray", "Reverse Shell & Bind Shell"),
                                  color.color("lgray", "ShellGenerator")],
                                 [color.color("green", "php_proc_open"),
                                  color.color("lgray", "GNU/Linux, MacOSX & Microsoft Windows"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "ShellGenerator")],
                                 [color.color("green", "powershell"), color.color("lgray", "Microsoft Windows"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "ShellGenerator")],
                                 [color.color("green", "powershell_2"), color.color("lgray", "Microsoft Windows"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "ShellGenerator")],
                                 [color.color("green", "powershell_3"), color.color("lgray", "Microsoft Windows"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "ShellGenerator")],
                                 [color.color("green", "powershell_3_base64"),
                                  color.color("lgray", "Microsoft Windows"), color.color("lgray", "Reverse Shell"),
                                  color.color("lgray", "ShellGenerator")],
                                 [color.color("green", "powershell_4_tls"), color.color("lgray", "Microsoft Windows"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "ShellGenerator")],
                                 [color.color("green", "python_1"), color.color("lgray", "GNU/Linux & MacOSX"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "ShellGenerator")],
                                 [color.color("green", "python_2"), color.color("lgray", "GNU/Linux & MacOSX"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "ShellGenerator")],
                                 [color.color("green", "python_3_1"), color.color("lgray", "GNU/Linux & MacOSX"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "ShellGenerator")],
                                 [color.color("green", "python_3_2"), color.color("lgray", "GNU/Linux & MacOSX"),
                                  color.color("lgray", "Reverse Shell & Bind Shell"),
                                  color.color("lgray", "ShellGenerator")],
                                 [color.color("green", "python3_shortest"), color.color("lgray", "GNU/Linux"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "ShellGenerator")],
                                 [color.color("green", "ruby"), color.color("lgray", "GNU/Linux & MacOSX"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "ShellGenerator")],
                                 [color.color("green", "ruby_nosh"), color.color("lgray", "GNU/Linux & MacOSX"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "ShellGenerator")],
                                 [color.color("green", "socat"), color.color("lgray", "GNU/Linux & MacOSX"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "ShellGenerator")],
                                 [color.color("green", "socat_tty"), color.color("lgray", "GNU/Linux & MacOSX"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "ShellGenerator")],
                                 [color.color("green", "nodejs"), color.color("lgray", "GNU/Linux & MacOSX"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "ShellGenerator")],
                                 [color.color("green", "telnet"), color.color("lgray", "GNU/Linux & MacOSX"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "ShellGenerator")],
                                 [color.color("green", "zsh"), color.color("lgray", "GNU/Linux & MacOSX"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "ShellGenerator")],
                                 [color.color("green", "lua"), color.color("lgray", "GNU/Linux"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "ShellGenerator")],
                                 [color.color("green", "lua_2"),
                                  color.color("lgray", "GNU/Linux & Microsoft Windows"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "ShellGenerator")],
                                 [color.color("green", "golang"), color.color("lgray", "GNU/Linux & MacOSX"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "ShellGenerator")],
                                 [color.color("green", "vlang"), color.color("lgray", "GNU/Linux & MacOSX"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "ShellGenerator")],
                                 [color.color("green", "awk"), color.color("lgray", "GNU/Linux & MacOSX"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "ShellGenerator")],
                                 [color.color("green", "C"),
                                  color.color("lgray", "GNU/Linux, MacOSX & Microsoft Windows"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "TemplateGenerator")],
                                 [color.color("green", "C_Mips"),
                                  color.color("lgray", "GNU/Linux"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "TemplateGenerator")],
                                 [color.color("green", "Dart"),
                                  color.color("lgray", "GNU/Linux, MacOSX & Microsoft Windows"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "TemplateGenerator")],
                                 [color.color("green", "Python3_windows"), color.color("lgray", "Microsoft Windows"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "TemplateGenerator")],
                                 [color.color("green", "Nodejs"),
                                  color.color("lgray", "GNU/Linux, MacOSX & Microsoft Windows"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "TemplateGenerator")],
                                 [color.color("green", "Java"), color.color("lgray", "GNU/Linux & MacOSX"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "TemplateGenerator")],
                                 [color.color("green", "Java_2"), color.color("lgray", "GNU/Linux & MacOSX"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "TemplateGenerator")],
                                 [color.color("green", "Java_3"),
                                  color.color("lgray", "GNU/Linux, MacOSX & Microsoft Windows"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "TemplateGenerator")],
                                 [color.color("green", "Javascript"),
                                  color.color("lgray", "GNU/Linux, MacOSX & Microsoft Windows"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "TemplateGenerator")],
                                 [color.color("green", "PHP"),
                                  color.color("lgray", "GNU/Linux, MacOSX & Microsoft Windows"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "TemplateGenerator")],
                                 [color.color("green", "Perl"), color.color("lgray", "GNU/Linux & MacOSX"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "TemplateGenerator")],
                                 [color.color("green", "Haskell_1"), color.color("lgray", "GNU/Linux & MacOSX"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "TemplateGenerator")],
                                 [color.color("green", "CsharpBash_i"), color.color("lgray", "GNU/Linux"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "TemplateGenerator")],
                                 [color.color("green", "CsharpTcpClient"),
                                  color.color("lgray", "GNU/Linux & Microsoft Windows"),
                                  color.color("lgray", "Reverse Shell"), color.color("lgray", "TemplateGenerator")],

                                 ]
        print('\n')
        print(color.color('yellow', '\t\t\t\t\tGENERATOR PAYLOADS'))
        print(tabulate(self.__show_generator, headers='firstrow', tablefmt='simple', stralign='left'))

    def show_help_generator(self):
        self.__show_help_generator = [[color.color('yellow', 'FunctionName'), color.color('yellow', 'Command'), color.color("yellow", "Arguments"), color.color("yellow","Description")],
                                      [color.color("green", "ShellGenerator"), color.color("lgray", "generator(ShellGenerator, ") + color.color("yellow", "target=,") + color.color("cyan"," port=, ") + color.color("red","platform=,") + color.color("purple"," type=, ") + color.color("blue","payload=") + color.color("lgray",")"), color.color("yellow", "target=ip address,") + color.color("cyan"," port=Connection port, ") + color.color("red","platform=operating system,") + color.color("purple"," type=type of connection, ") + color.color("blue","payload=programming language")
, color.color("lgray","Generates payloads based on parameters passed under a selected language")],
                                      [color.color("green", "TemplateGenerator"),
                                       color.color("lgray", "generator(TemplateGenerator, ") + color.color("yellow",
                                                                                                        "target=,") + color.color(
                                           "cyan", " port=, ") + color.color("red", "platform=,") + color.color(
                                           "purple", " type=, ") + color.color("blue", "payload=") + color.color(
                                           "lgray", ")"),
                                       color.color("yellow", "target=ip address,") + color.color("cyan",
                                                                                                 " port=Connection port, ") + color.color(
                                           "red", "platform=operating system,") + color.color("purple",
                                                                                              " type=type of connection, ") + color.color(
                                           "blue", "payload=programming language")
                                          , color.color("lgray",
                                                        "Generates payloads based on parameters passed under a selected language")]
                                      ]

        print('\n')
        print(tabulate(self.__show_help_generator, headers='firstrow', tablefmt='simple', stralign='left'))
help_generator = Help()



