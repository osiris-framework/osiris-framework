#!/usr/bin/env python3
# Project: osiris-framework
# Author: Samir Sanchez Garnica @sasaga92
# Version 1.0
# Date: 21/11/2022

import requests, socket
from core.ModuleObtainer import obtainer
from utilities.Colors import color
from utilities.Tools import tools
from utilities.Messages import print_message
print_message.name_module = __file__
from tqdm import tqdm
from time import sleep
import urllib3
urllib3.disable_warnings()

info = {
        'author'            :'Samir Sanchez Garnica',
        'date'              :'2019/03/08',
        'rank'              :'Excellent',
        'path'              :'auxiliary/gather/http/server_name.py',
        'category'          :'auxiliary',
        'license'           :'GPL-2.0',
        'description'       :'Simple module that obtains HTTP methods enabled',
        'references'        :['http://docs.python-requests.org/en/master/user/quickstart/']
}
options = {
            'target'                :['Yes', 'use to set target',''],
            'proxy'                 :['No', 'use to set proxy',''],
}

required = {
        'start_required'     :'True',
        'check_required'     :'False'
}

"""
    You can add the new methods to be tested in this list 
"""
__methods = [
    'CHECKIN', 'CHECKOUT', 'CONNECT', 'COPY', 'DELETE', 'GET', 'HEAD', 'INDEX',
    'LINK', 'LOCK', 'MKCOL', 'MOVE', 'NOEXISTE', 'OPTIONS', 'ORDERPATCH',
    'PATCH', 'POST', 'PROPFIND', 'PROPPATCH', 'PUT', 'REPORT', 'SEARCH',
    'SHOWMETHOD', 'SPACEJUMP', 'TEXTSEARCH', 'TRACE', 'TRACK', 'UNCHECKOUT',
    'UNLINK', 'UNLOCK', 'VERSION-CONTROL', 'BAMBOOZLE'
]

__response_methods = []
__response_length = []
__response_status_code = []
__response_reason = []

def get_method_request(method, url, proxy, headers, cookie):
    try:
        __response = requests.request(method=method, url=url, proxies=proxy, headers=headers, cookies=cookie, verify=False)
        if __response.status_code in tools.status_code.keys():
            if __response.status_code >= 100 and __response.status_code < 200:
                __response_methods.append(color.color("lgray", method))
                __response_length.append(color.color("lgray", str(len(__response.content))))
                __response_status_code.append(color.color("lgray", str(__response.status_code)))
                __response_reason.append(color.color("lgray", tools.status_code[__response.status_code]))

            elif __response.status_code == 200:
                __response_methods.append(color.color("green", method))
                __response_length.append(color.color("green", str(len(__response.content))))
                __response_status_code.append(color.color("green", str(__response.status_code)))
                __response_reason.append(color.color("green", tools.status_code[__response.status_code]))

            elif __response.status_code > 200 and __response.status_code < 300:
                __response_methods.append(color.color("green_ptrl", method))
                __response_length.append(color.color("green_ptrl", str(len(__response.content))))
                __response_status_code.append(color.color("green_ptrl", str(__response.status_code)))
                __response_reason.append(color.color("green_ptrl", tools.status_code[__response.status_code]))

            elif __response.status_code >= 300 and __response.status_code < 600:
                __response_methods.append(color.color("red", method))
                __response_length.append(color.color("red", str(len(__response.content))))
                __response_status_code.append(color.color("red", str(__response.status_code)))
                __response_reason.append(color.color("red", tools.status_code[__response.status_code]))
    except Exception as Error:
        return False

def exploit():
    __proxy = obtainer.options['proxy'][2]
    __target = obtainer.options['target'][2]

    try:
        __response = tools.http_or_https(__target)
        if __response['code'] == 500:
            print_message.execution_error("URL must start with http or https")
            return False

        print_message.start_execution()
        __response = tools.http_or_https(__proxy)
        if __response['code'] == 200 or __proxy == "":
            __proxy = {__response['message']: __proxy}
            __cookie = {}
            __headers = {}
            __method_tqdm = tqdm(__methods)

            for _method in __method_tqdm:
                __method_tqdm.set_description("Processing: %s" % _method)
                sleep(0.5)
                get_method_request(_method, __target, __proxy, __headers, __cookie)
        print_message.execution_info(__target)
        print("\n")
        print(tools.create_tabulate_list(['Method', 'Length', 'Status code', 'Reason'],
                                         [__response_methods, __response_length, __response_status_code,
                                          __response_reason])['message'])

        print_message.end_execution()

    except Exception as Error:
        pass

    tools.clean_list([__response_methods, __response_length, __response_status_code, __response_reason])