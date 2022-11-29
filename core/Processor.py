#!/usr/bin/env python3
# Project: osiris-framework
# Author: Samir Sanchez Garnica @sasaga92
# Version 1.0
# Date: 14/11/2022

from core.thot.Thot import Thot
from tabulate import tabulate
from utilities.Colors import color
from utilities.Messages import print_message
print_message.name_module = __file__
from utilities.Tools import tools
import threading

class Processor():
    def __init__(self):
        self.__payload_options  = {}
        self.__exploit_options = {}
        self.__rhost = ""
        self.__rport = ""
        self.__lhost = ""
        self.__lport = ""
        self.__payload_select = ""

    def multi_handler(self, **kwargs):

        try:
            self.__payload_options = kwargs['payload_options']
            self.__exploit_options =  kwargs['exploit_options']
            self.__payload_select = self.__exploit_options['payload'][2]

            if 'generic/shell/bind_tcp' in self.__payload_select:
                self.__data_connection = str(self.__payload_options["rhost"][2] + str(":") + self.__payload_options["rport"][2])
                print_message.execution_info("THOT is starting up for a connection on {}".format(self.__data_connection))
                self.__connection = Thot(tuple(self.__data_connection.split(":")), self.__payload_select)
                self.__connection.search_bind()

            elif 'generic/shell/reverse_tcp' in self.__payload_select:
                self.__data_connection = str(self.__payload_options["lhost"][2] + str(":") + self.__payload_options["lport"][2])
                if tools.get_platform(self.__payload_options['lport'][2])['code'] != 200:
                    try:
                        self.__connection  = Thot(tuple(self.__data_connection.split(":")), self.__payload_select)
                        self.__thread = threading.Thread(target=self.__connection.create_worker, daemon=True)
                        self.__thread2 = threading.Thread(target=self.__connection.create_jobs, daemon=True)

                        self.__thread.start()
                        self.__thread2.start()

                    except Exception as Error:
                        print(Error)
            else:
                pass
        except Exception as Error:
            print(Error)

    def list_sessions(self):
        try:
            self.__connection.list_connections()
        except:
            self.___result_connection = [
                [color.color('yellow', 'ID'), color.color('yellow', 'TYPE'), color.color('yellow', 'HOST'),
                 color.color('yellow', 'PORT'), color.color('yellow', 'DESCRIPTION CONNECTION')]]

            self.___result_connection.append([color.color('red', 'NOT CONNECTIONS'), color.color('red', 'CONNECTIONS'),
                            color.color('red', 'CONNECTIONS'), color.color('red', 'NOT CONNECTIONS'),
                            color.color('red', 'NOT CONNECTIONS')])
            print('\n')
            print(tabulate(self.___result_connection, headers='firstrow', tablefmt='simple', stralign='center'))

    def get_console(self, __sesion, __path):
        try:
            self.__connection.console(__sesion, __path)
        except:
            print(color.color("red", "[-] ") + color.color("c", "Error there are no active connections to select"))

    def kill_connections(self):
        try:
            self.__connection.quit_gracefully()
        except Exception as Error:
            pass

processor = Processor()