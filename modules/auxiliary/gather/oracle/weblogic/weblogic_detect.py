#!/usr/bin/env python3
# Project: Osiris-Framework
# Version 1.337

import requests
from core.ModuleObtainer import obtainer
from utilities.Colors import color
from utilities.Messages import print_message
from utilities.Tools import tools
print_message.name_module = __file__
from time import sleep
from tqdm import tqdm

info = {
        'author'            :'Samir Sanchez Garnica',
        'date'              :'2019/03/08',
        'rank'              :'Excellent',
        'path'              :'auxiliary/gather/weblogic/weblogic_detect.py',
        'category'          :'auxiliary',
        'license'           :'GPL-2.0',
        'description'       :'Simple module that identifies if the instances of WebLogic /wls-wsat/* and /_async/* exist',
        'references'        :['https://github.com/sasaga/Osiris-framework']
}
options = {
            'target'                :['Yes', 'use to set target',''],
            'proxy'                :['No', 'use to set a proxy chain of format type:host:port[,type:host:port][...]','']
}
required = {
        'start_required'     :'True',
        'check_required'     :'False'
}

__list_path_weblogic = ['/wls-wsat/CoordinatorPortType', '/wls-wsat/CoordinatorPortType11',
                        '/wls-wsat/ParticipantPortType', '/wls-wsat/ParticipantPortType11',
                        '/wls-wsat/RegistrationPortTypeRPC','/wls-wsat/RegistrationRequesterPortType',
                        '/wls-wsat/RegistrationRequesterPortType11','/_async/AsyncResponseService',
                        '/_async/AsyncResponseServiceHttps','/_async/AsyncResponseServiceJms',
                        '/_async/AsyncResponseServiceSoap12','/_async/AsyncResponseServiceSoap12Https',
                        '/_async/AsyncResponseServiceSoap12Jms'
                        ]

_url_valid = []
_status_code = []
_size = []
_reason = []

def status_oracle_weblogic(__url, __proxy, __headers, __cookie, __path):
    try:
        __response = requests.get(url=__url + __path, proxies=__proxy, headers=__headers, cookies=__cookie, verify=False)
        if __response.status_code != 404:
            _url_valid.append(color.color("green", __url + __path))
            _status_code.append(color.color("yellow", __response.status_code))
            _size.append(color.color("green_ptrl", len(__response.text)))
            _reason.append(color.color("green_ptrl", tools.status_code[__response.status_code]))
    except Exception as Error:
        pass

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
            __path_tqdm = tqdm(__list_path_weblogic)

            for __path in __path_tqdm:
                __path_tqdm.set_description("Processing: %s" % __path)
                sleep(0.5)
                status_oracle_weblogic(__target, __proxy, __headers, __cookie, __path)

        print_message.execution_info(__target)
        print("\n")

        print(tools.create_tabulate_list(['Url Valid', 'Status code', 'Length', 'Reason'],
                                         [_url_valid, _status_code, _size, _reason])['message'])

        print_message.end_execution()
    except Exception as Error:
        pass

    tools.clean_list([_url_valid, _status_code, _size, _reason])



