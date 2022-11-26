#!/usr/bin/env python3
# Project: osiris-framework
# Author: Samir Sanchez Garnica @sasaga92
# Version 1.0
# Date: 16/11/2022

import requests
import threading
from core.ModuleObtainer import obtainer
from utilities.Colors import color
from utilities.Messages import print_message
from utilities.Tools import tools
print_message.name_module = __file__
from time import sleep

info = {
        'author'            :'Samir Sanchez Garnica',
        'date'              :'13/06/2019',
        'rank'              :'Normal',
        'path'              :'auxiliary/scanner/http/robots_txt.py',
        'category'          :'auxiliary',
        'license'           :'GPL-2.0',
        'description'       :'Simple module Detect robots.txt files and analize its content.',
        'references'        :['http://docs.python-requests.org/es/latest/']
}
options = {
            'target'                :['No', 'use to set address target',''],
            'target_file'           :['No', 'use to set target list file',''],
            'proxy'                 :['No', 'use to set a proxy chain of format type:host:port[,type:host:port][...]','']
}

required = {
        'start_required'     :'True',
        'check_required'     :'False'
}

def get_robots_txt(__target, __proxy):
    if __target.startswith("http://") or __target.startswith("https://"):
        try:
            __robots_txt_response = requests.get(__target + str("/robots.txt"), proxies=__proxy)
            if __robots_txt_response.status_code == 200:
                try:
                    print(color.color("green", "[+] ") + color.color("yellow","Extracting information for: ") + color.color("green", __target) + "\n" + color.color("lgray", __robots_txt_response.text))
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
        __proxy = obtainer.options['proxy'][2]
        __threads = []
        __response = tools.http_or_https(__proxy)
        if __response['code'] == 200 or __proxy == "":
            __proxy = {__response['message']: __proxy}

            print_message.start_execution()
            if __target != "":
                get_robots_txt(__target, __proxy)
            else:
                __target_file = tools.read_file(__target_file, __proxy)
                for __target in __target_file:
                    __thread = threading.Thread(target=get_robots_txt,
                                                args=(__target,))
                    __thread.start()
                    __threads.append(__thread)
                    sleep(0.1)

                for __join_thread in __threads:
                    __join_thread.join()
            print_message.end_execution()
    except Exception as Error:
        pass
