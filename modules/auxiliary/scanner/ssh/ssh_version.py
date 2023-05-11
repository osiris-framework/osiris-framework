#!/usr/bin/env python3
# Project: Osiris-Framework
# Version 1.337

from core.ModuleObtainer import obtainer
from utilities.Tools import tools
from utilities.Messages import print_message
from utilities.Colors import color
from time import sleep
print_message.name_module = __file__
import socket, threading

info = {
        'author'            :'Samir Sanchez Garnica',
        'date'              :'2019/03/10',
        'rank'              :'Normal',
        'path'              :'auxiliary/scanner/ssh/ssh_version.py',
        'category'          :'auxiliary',
        'license'           :'GPL-2.0',
        'description'       :'Simple module that obtains the version of an SSH server based on the BannerGrabbing',
        'references'        :['https://wiki.python.org/moin/HowTo/Sockets']
}
options = {
        'rhost'                 :['Yes', ' use to set rhost',''],
        'rport'                 :['Yes', ' use to set rport','22']
}

required = {
        'start_required'     :'True',
        'check_required'     :'False'
}

def grab_banner( __address, __port):
    try:
        socket.setdefaulttimeout(2)
        __socket = socket.socket()
        __socket.connect((__address, __port))
        __banner = str(__socket.recv(1024).decode())
        __socket.close()
        print(color.color("green", "[+] ") + color.color("lgray", str(__address)) + color.color(
            "red", ":") + color.color("lgray", str(__port)) + color.color("yellow", " Banner:") + color.color("lgray",
                                                                                                              str(__banner)))
    except Exception as Error:
        pass


def exploit():
    __target = obtainer.options['rhost'][2]
    __port = int(obtainer.options['rport'][2])
    __threads = []

    if isinstance(__port, int):
        __response =  tools.check_IPV4(__target)

        if __response['code'] != 200:
            print_message.execution_error(__response['message'])
            return False
        print_message.start_execution()
        for __address in __response['message']:
            __thread = threading.Thread(target=grab_banner, args=(__address, __port))
            __thread.start()
            __threads.append(__thread)
            sleep(0.1)

        for __join_thread in __threads:
            __join_thread.join()
        print_message.end_execution()

def check():
  pass