#!/usr/bin/env python3
# Project: osiris-framework
# Author: Samir Sanchez Garnica @sasaga92
# Version 1.0
# Date: 14/11/2022

import sys
import threading
import socket
from queue import Queue
from time import sleep
from datetime import datetime
from utilities.Colors import color
from core.thot.ThotCompleter import thot_completer
from core.thot.Help import help
from utilities.ScreenCleaner import ScreenCleaner
from tabulate import tabulate
from os import system
from utilities.Messages import print_message
from utilities.Tools import tools
print_message.name_module = __file__

_exit_flag = False
_all_connections = []
_all_address = []
_all_info = []
_num_connections = 1
_type_connection = []
_connections_name = []

class Thot:
    def __init__(self, __user_connection, __type_connection):
        self.__response_name_id = None
        self.__user = None
        self.__sock = None
        self.__cont_connect_bind_tcp = None
        self.__theConnection = None
        self.__result = None
        self.__command = None
        self.__thread = None
        self.__target_selected = None
        self.__conn = None
        self.__target = None
        self.__buffer = None
        self.__buffer_size = None
        self.__socket_fd = None
        self.__x = None
        self.__connection = None
        self.__user_address = None
        self.__user_connection = None
        self.__time_of_connection = None
        self.__now = None
        self.__socket = None
        self.__host = None
        self.__address, self.__port = __user_connection
        self.__number_threads = 2
        self.__jobs_number = [1, 2]
        self.__queue = Queue()
        self.__connection_retry_bind = 7

        _type_connection.append(__type_connection)

    def socket_create(self, __host, __port):
        try:
            self.__host = __host
            self.__port = __port
            self.__socket = socket.socket()
        except socket.error as Error:
            print_message.execution_error(Error)

    def accept_connections(self):
        self.__now = datetime.now()
        self.__time_of_connection = " Time Local: ", self.__now.strftime('%H:%M:%S %Y/%m/%d')
        global _all_connections
        global _all_address
        global _all_info
        global _num_connections

        while True:
            try:
                self.__user_connection, self.__user_address = self.__socket.accept()
                self.__user_connection.setblocking(1)
                _all_connections.append(self.__user_connection)
                _all_address.append(self.__user_address)

                self.__response_name_id = tools.generate_id(6)
                if self.__response_name_id['code'] == 200:
                    _connections_name.append(self.__response_name_id['message'])

                _all_info.append(
                    color.color("lgray", "(") + color.color("yellow", self.__address) + color.color("red",
                                                                                                    ":") + color.color(
                        "yellow", str(self.__port)) + color.color("red", str(" -> ")) + color.color("yellow", str(
                        self.__user_address[0])) + color.color("red", str(":")) + color.color("yellow", str(
                        self.__user_address[1])) + str(" ") + color.color("lgray", str(
                        self.__time_of_connection[0])) + color.color("red",
                                                                     str(self.__time_of_connection[1])) + color.color(
                        "lgray", str(")"))
                )
                print(
                    color.color("green", "[ info ] ") + color.color("lgray", "THOT interactive session ") + color.color(
                        "yellow", str(_num_connections)) + color.color("lgray", " opened (") + color.color("yellow",
                                                                                                           self.__address) + color.color(
                        "red", ":") + color.color("yellow", str(self.__port)) + color.color("red",
                                                                                            str(" -> ")) + color.color(
                        "yellow", str(self.__user_address[0])) + color.color("red", str(":")) + color.color("yellow",
                                                                                                            str(
                                                                                                                self.__user_address[
                                                                                                                    1])) + str(
                        " ") + color.color("lgray", str(self.__time_of_connection[0])) + color.color("red", str(
                        self.__time_of_connection[1])) + color.color("lgray", str(")")))

                _num_connections += 1
            except Exception as Error:
                print(Error)
                print_message.execution_error("There was an error accepting connections")

    def accept_connections_bind(self, __connection, __data_connection):
        global _all_connections
        global _all_address
        global _all_info
        global _num_connections
        global _connections_name

        self.__now = datetime.now()
        self.__time_of_connection = " Time Local: ", self.__now.strftime('%H:%M:%S %Y/%m/%d')
        self.__connection = __connection
        self.__address = __data_connection

        try:
            _all_connections.append(self.__connection)
            _all_address.append(self.__address)

            self.__response_name_id = tools.generate_id(6)
            if self.__response_name_id['code'] == 200:
                _connections_name.append(self.__response_name_id['message'])

            _all_info.append(
                color.color("lgray", "(") + color.color("yellow", self.__address[0]) + color.color("red",
                                                                                                   ":") + color.color(
                    "yellow", str(self.__port)) + color.color("lgray", str(self.__time_of_connection[0])) + color.color(
                    "red", str(self.__time_of_connection[1])) + color.color("lgray", str(")"))
            )

            print(color.color("green", "[ info ] ") + color.color("lgray", "THOT interactive session ") + color.color(
                "yellow", str(_num_connections)) + color.color("lgray", " opened (") + color.color("yellow",
                                                                                                   self.__address[
                                                                                                       0]) + color.color(
                "red", ":") + color.color("yellow", str(self.__port)) + color.color("red", str(" -> ")) + color.color(
                "yellow", str(self.__address[0])) + color.color("red", str(":")) + color.color("yellow", str(
                self.__address[1])) + str(" ") + color.color("lgray", str(self.__time_of_connection[0])) + color.color(
                "red", str(self.__time_of_connection[1])) + color.color("lgray", str(")")))
            _num_connections += 1
        except Exception as Error:
            print_message.execution_error("There was an error connecting to the remote host {}".format(Error))

    def socket_bind(self):
        try:
            print(color.color("green", "[ info ] ") + color.color("cyan", "Thot is listening on %s:%d..." % (
                self.__host, self.__port)))
            self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.__socket.bind((self.__host, self.__port))
            self.__socket.listen(5)
        except socket.error as Error:
            print_message.execution_error("Error starting binding service {} ".format(Error))

            try:
                self.__queue.task_done()
                self.__queue.task_done()
                sys.exit(0)
            except:
                sys.exit(0)

    def quit_gracefully(self, signal=None, frame=None):
        global _all_connections
        print_message.execution_info("killing connections, please wait ... ")

        for __connection in _all_connections:
            try:
                __connection.shutdown(2)
                __connection.close()
            except Exception as Error:
                print_message.execution_error("Could not close connection {}".format(Error))

            sys.exit(0)

    def create_worker(self):
        for _ in range(self.__number_threads):
            __thread = threading.Thread(target=self.work, daemon=True)
            __thread.start()
        return

    def work(self):
        try:
            self.__host = self.__address
            self.__port = int(self.__port)
        except Exception as Error:
            print_message.execution_error("Connection information not included")
            self.__queue.task_done()
            self.__queue.task_done()
            sys.exit(0)

        while True:
            self.__x = self.__queue.get()

            if self.__x == 1:
                self.socket_create(self.__host, self.__port)
                self.socket_bind()
                self.accept_connections()

            if self.__x == 2:
                try:
                    self.__queue.task_done()
                    self.__queue.task_done()
                    break
                except:
                    break

            try:
                self.__queue.task_done()
            except:
                pass

            return

    def transfer(self, __connection):
        global _exit_flag
        global _connections_name
        self.__socket_fd = __connection
        self.__buffer_size = 0x400

        while True:
            if _exit_flag:
                print_message.execution_info("The interactive session has ended.")
                _exit_flag = False
                break

            try:
                self.__buffer = self.__socket_fd.recv(self.__buffer_size)
                _exit_flag = False
            except Exception as Error:
                print(Error)
                _exit_flag = False
                print(self.__target_selected)
                self.remove_node(self.__socket_fd)
                break

            if not self.__buffer:
                print_message.execution_error("No data Breaking...")
                print(self.__target_selected)
                self.remove_node(self.__socket_fd)
                _exit_flag = False
                try:
                    self.remove_id_connection_target()
                except:
                    pass
                break

            sys.stdout.write(color.color("lgray", self.__buffer.decode('utf-8')))
        return

    def get_id_connection_target(self):
        global _connections_name

        for id, session_name in enumerate(_connections_name):
            if (session_name.strip().lower()) == (self.__target.strip().lower()):
                return id

    def remove_id_connection_target(self):
        global _connections_name
        del _connections_name[self.__target]
        del _type_connection[self.__target]

    def get_targets(self, __cmd):
        global _exit_flag
        global _all_connections
        global _all_address
        global _num_connections

        self.__target = __cmd.replace('select', '')
        self.__target = int(self.get_id_connection_target())
        _exit_flag = False

        try:
            self.__conn = _all_connections[self.__target]
        except Exception as Error:
            print(Error)
            return

        self.__target_selected = color.color("yellow", "[!] ") + color.color("red",
                                                                             "The connection to the target has been lost: ") + color.color(
            "yellow", _all_address[self.__target][0])
        print(color.color("green", "[ info ] ") + color.color("cyan", "Select Target:") + color.color("yellow",
                                                                                                      _all_address[
                                                                                                          self.__target][
                                                                                                          0]))

        self.__thread = threading.Thread(target=self.transfer, args=(self.__conn,))
        self.__thread.start()

        try:
            while True:
                self.__command = input()
                if self.__command == "exit":
                    _exit_flag = True
                    self.__conn.send(str.encode("\n"))
                    break
                _exit_flag = False
                self.__conn.send(str.encode(self.__command + "\n"))
        except:
            _exit_flag = False
            print(self.__target_selected)

        sleep(0.125)

    def remove_node(self, __socked_fd):
        global _all_connections
        global _all_address
        global _all_info
        for __i, __conn in enumerate(_all_connections):
            if __socked_fd == _all_connections[__i]:
                del _all_connections[__i]
                del _all_address[__i]
                del _all_info[__i]
                __conn.close()
                break
        return

    def create_jobs(self):
        for __x in self.__jobs_number:
            self.__queue.put(__x)
        self.__queue.join()

    def list_connections(self):
        global _all_connections
        global _type_connection
        global _all_address
        global _all_info
        global _connections_name

        try:
            self.__result = [[color.color('yellow', 'ID'), color.color('yellow', 'TYPE'), color.color('yellow', 'HOST'),
                              color.color('yellow', 'PORT'), color.color('yellow', 'DESCRIPTION CONNECTION')]]

            for __i, __conn in enumerate(_all_connections):
                try:
                    self.__theConnection = _type_connection[__i]
                except:
                    _type_connection.append("unknown")

                self.__result.append(
                    [color.color("green_ptrl", str(_connections_name[__i])), color.color("lgray", str(_type_connection[__i])),
                     color.color("green", str(_all_address[__i][0])), color.color("green", str(_all_address[__i][1])),
                     str(_all_info[__i])])

                if len(self.__result) == 1:
                    self.__result.append([color.color('red', 'NOT CONNECTIONS'), color.color('red', 'CONNECTIONS'),
                                          color.color('red', 'CONNECTIONS'),color.color('red', 'NOT CONNECTIONS')])
        except Exception as Error:
            print(Error)
            self.__result.append([color.color('red', 'NOT CONNECTIONS'), color.color('red', 'CONNECTIONS'),
                                  color.color('red', 'CONNECTIONS'),color.color('red', 'NOT CONNECTIONS')])

        print('\n')
        print(tabulate(self.__result, headers='firstrow', tablefmt='simple', stralign='center'))

    def search_bind(self):
        self.__thread = threading.Thread(target=self.connect_bind_tcp, args=())
        self.__thread.daemon = True
        self.__thread.start()

    def connect_bind_tcp(self):
        self.__cont_connect_bind_tcp = 1
        while self.__connection_retry_bind > self.__cont_connect_bind_tcp:
            try:
                self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.__sock.connect((self.__address, int(self.__port)))
                self.accept_connections_bind(self.__sock, [self.__address, self.__port])
                return True
            except socket.error as Error:
                print_message.execution_info(
                    "Trying {} to connect with {}:{}".format(self.__cont_connect_bind_tcp, self.__address, self.__port))
            sleep(1)
            self.__cont_connect_bind_tcp += 1

        return True

    def console(self, __session, __path):
        global _exit_flag
        thot_completer()
        _exit_flag = False

        if 'select' in __session:
            self.get_targets(__session)

        self.__user = "interpreter"

        while True:
            self.__command = input(
                color.color("underline", color.color("lgray", "%s" % self.__user)) + " " + color.color('lgray',
                                                                                                       '>') + " ").strip()
            self.__command = self.__command.lower()

            if self.__command == "sessions":
                self.list_connections()
            elif 'select' in self.__command:
                self.get_targets(self.__command)
            elif self.__command == "":
                continue
            elif self.__command == "background" or self.__command == "exit":
                if __path == "module":
                    from core.ModuleInterpreter import module_completer
                    module_completer()
                elif __path == "base":
                    from core.Completer import completer
                    completer()
                else:
                    from core.ModuleInterpreter import module_completer
                    module_completer()

                print_message.execution_info("Running THOT in the background")

                try:
                    self.__queue.task_done()
                    self.__queue.task_done()
                    break
                except:
                    break

            elif self.__command == "help":
                help.commands_core_thot()
            elif self.__command == "clear" or self.__command == "clean":
                ScreenCleaner()
            elif self.__command.split(" ")[0] == 'exec' or self.__command.split(" ")[0] == 'execute':
                try:
                    self.__command = list(self.__command.split(" "))
                    self.__command.remove('exec' if self.__command[0] == 'exec' else 'execute')
                    system(' '.join(self.__command))
                except IndexError:
                    print_message.execution_info("Please Enter command")
            else:
                print_message.execution_error("Command not found")
