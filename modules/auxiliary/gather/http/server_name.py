#!/usr/bin/env python3
# Project: Osiris-Framework
# Version 1.337

import requests, socket
from core.ModuleObtainer import obtainer
from utilities.Colors import color
from utilities.Tools import tools
from utilities.Messages import print_message
print_message.name_module = __file__
import threading
from time import sleep

info = {
        'author'            :'Samir Sanchez Garnica',
        'date'              :'2019/03/08',
        'rank'              :'Excellent',
        'path'              :'auxiliary/gather/http/method_enable.py',
        'category'          :'auxiliary',
        'license'           :'GPL-2.0',
        'description'       :'Simple module that gets the name of the server that supports the web application',
        'references'        :['http://docs.python-requests.org/es/latest/']
}
options = {
            'target'                :['No', 'use to set target',''],
            'target_file'           :['No', 'use to set target list file',''],
}
required = {
        'start_required'     :'True',
        'check_required'     :'False'
}


def get_server_name(__target):
    if __target.startswith("http://") or __target.startswith("https://"):
        try:
            __name_server = requests.get(__target)
            if __name_server.content:
                try:
                    print(color.color("green", "[+] ") + color.color("green",
                                                                     __target) + " sopported by " + color.color(
                        "yellow", __name_server.headers['Server']) + " " + color.color("lgray",
                                                                                       "successful"))
                except Exception as Error:
                    print_message.execution_error("Imposible Extract Information for {}".format(__target))
                    return False
        except:
            print_message.execution_error("Imposible Extract Information for {}".format(__target))
            return False
    else:
            print_message.execution_error("The url format must contain http:// or https:// for {}".format(__target))
            return False



def exploit():
        try:
                __target = obtainer.options['target'][2]
                __target_file = obtainer.options['target_file'][2]
                __threads = []

                print_message.start_execution()
                if __target != "":
                        get_server_name(__target)
                else:
                    __target_file = tools.read_file(__target_file)
                    for __target in __target_file:
                        __thread = threading.Thread(target=get_server_name,
                                                    args=(__target, ))
                        __thread.start()
                        __threads.append(__thread)
                        sleep(0.1)
                    

                    for __join_thread in __threads:
                            __join_thread.join()
                print_message.end_execution()
        except Exception as Error:
                pass
