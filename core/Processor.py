#!/usr/bin/env python3
# Project: Osiris-Framework
# Version 1.337

import threading
from core.thot.Thot import Thot
from tabulate import tabulate
from utilities.Colors import color
from utilities.Tools import tools
from utilities.Messages import print_message

print_message.name_module = __file__


class Processor():
    def __init__(self):
        self.__consumer = None
        self.___result_connection = None
        self.__thread2 = None
        self.__thread = None
        self.__connection = None
        self.__data_connection = None
        self.__payload_options = {}
        self.__exploit_options = {}
        self.__payload_select = ""

    def multi_handler(self, **kwargs):

        try:
            self.__payload_options = kwargs['payload_options']
            self.__exploit_options = kwargs['exploit_options']
            self.__payload_select = self.__exploit_options['payload'][2]

            if 'bind' in self.__payload_select:
                self.__data_connection = str(
                    self.__payload_options["rhost"][2] + str(":") + self.__payload_options["rport"][2])
                print_message.execution_info(
                    "THOT is starting up for a connection on {}".format(self.__data_connection))
                self.__connection = Thot(tuple(self.__data_connection.split(":")), self.__payload_select)
                self.__connection.search_bind()

            elif 'reverse' in self.__payload_select:
                self.__data_connection = str(
                    self.__payload_options["lhost"][2] + str(":") + self.__payload_options["lport"][2])
                if tools.get_port_use(self.__payload_options['lport'][2])['code'] != 200:
                    try:
                        self.__connection = Thot(tuple(self.__data_connection.split(":")), self.__payload_select)
                        self.__thread = threading.Thread(target=self.__connection.create_worker, daemon=True)
                        self.__thread2 = threading.Thread(target=self.__connection.create_jobs, daemon=True)

                        self.__thread.start()
                        self.__thread2.start()

                    except Exception as Error:
                        print(Error)
            elif 'webshell' in self.__payload_select:
                try:
                    try:
                        self.__consumer = [self.__exploit_options['target'][2],
                                           self.__payload_options['uri_webshell'][2],
                                           self.__payload_options['username'][2], self.__payload_options['password'][2]]
                    except KeyError:
                        self.__consumer = [self.__payload_options['target'][2],
                                           self.__payload_options['uri_webshell'][2],
                                           self.__payload_options['username'][2], self.__payload_options['password'][2]]

                    self.__connection = Thot(tuple(list(tools.filter_hostname(self.__consumer[0])['message'])), self.__payload_select, self.__consumer )
                    self.__connection.add_webshell_connection()
                except Exception as Error:
                    print(Error)
            else:
                pass
        except Exception as Error:
            print("aqui")
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

    def get_console(self, __session, __path):
        try:
            self.__connection.console(__session, __path)
        except:
            print(color.color("red", "[-] ") + color.color("c", "Error there are no active connections to select"))

    def kill_connections(self):
        try:
            self.__connection.quit_gracefully()
        except Exception as Error:
            pass


processor = Processor()
