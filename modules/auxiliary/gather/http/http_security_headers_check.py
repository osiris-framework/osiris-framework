#!/usr/bin/env python3
# Project: osiris-framework
# Author: Samir Sanchez Garnica @sasaga92
# Version 1.0
# Date: 22/11/2022


import requests
import urllib3
from core.ModuleObtainer import obtainer
from utilities.Colors import color
from utilities.Tools import tools
from utilities.Messages import print_message
print_message.name_module = __file__
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


info = {
        'author'            :'Samir Sanchez Garnica',
        'date'              :'12/06/2019',
        'rank'              :'Normal',
        'path'              :'auxiliary/gather/http/http_security_headers_check.py',
        'category'          :'auxiliary',
        'license'           :'GPL-2.0',
        'description'       :'This module performs a check of the most popular HTTP security headers.',
        'references'        :['http://docs.python-requests.org/es/latest/']
}
options = {
            'target'               :['Yes', 'use to set address target',''],
            'proxy'                :['No', 'use to set a proxy chain of format type:host:port[,type:host:port][...]','']
}
required = {
        'start_required'     :'True',
        'check_required'     :'False'
}

__security_headers = {
    'X-Frame-Options': 'X-Frame-Options tells the browser whether you want to allow your site to be framed or not. By preventing a browser from framing your site you can defend against attacks like clickjacking.',
    'Strict-Transport-Security': 'HTTP Strict Transport Security is an excellent feature to support on your site and strengthens your implementation of TLS by getting the User Agent to enforce the use of HTTPS.',
    'X-XSS-Protection': 'X-XSS-Protection sets the configuration for the XSS Auditor built into older browsers. The recommended value was "X-XSS-Protection: 1; mode=block" but you should now look at Content Security Policy instead.',
    'Referrer-Policy': 'Referrer Policy is a new header that allows a site to control how much information the browser includes with navigations away from a document and should be set by all sites.',
    'X-Content-Type-Options': 'X-Content-Type-Options stops a browser from trying to MIME-sniff the content type and forces it to stick with the declared content-type. The only valid value for this header is "X-Content-Type-Options: nosniff".',
    'Content-Security-Policy': 'Content Security Policy is an effective measure to protect your site from XSS attacks. By whitelisting sources of approved content, you can prevent the browser from loading malicious assets.',
    'Permissions-Policy': 'Permissions Policy is a new header that allows a site to control which features and APIs can be used in the browser.'
}

_headers = []
_values = []
_status = []

def get_security_http_headers(url, proxy, headers, cookie):
    try:
        __response = requests.get(url=url, proxies=proxy, headers=headers, cookies=cookie,
                                      verify=False)
        __headers_missing =  set(__security_headers) - set(__response.headers)

        __headers_exists = {}
        __headers_missing_complete = {}

        for security_header_key in __security_headers:
            for server_header_key, value in __response.headers.items():
                if security_header_key.lower() == server_header_key.lower():
                    __headers_exists[server_header_key] = value
                    _headers.append(color.color("green", server_header_key))
                    _values.append(color.color("lgray", value))
                    _status.append(color.color("green", "Present"))


        for security_header_key, description in __security_headers.items():
            for server_header_key in __headers_missing:
                if security_header_key.lower() == server_header_key.lower():
                    __headers_missing_complete[server_header_key] = description

                    _headers.append(color.color("red", server_header_key))
                    _values.append(color.color("yellow", description))
                    _status.append(color.color("red", "Missing"))

        print(tools.create_tabulate_list(['Header', 'value', 'Status'],
                                         [_headers, _values, _status])['message'])

    except Exception as Error:
        pass


def exploit():
    __proxy = obtainer.options['proxy'][2]
    __target = obtainer.options['target'][2]

    try:
        print_message.start_execution()
        __response = tools.http_or_https(__proxy)
        if __response['code'] == 200 or __proxy == "":
            __proxy = {__response['message']: __proxy}
            __cookie = {}
            __header = {}
            print_message.execution_info(__target)
            print("\n")
            get_security_http_headers(__target, __proxy, __header, __cookie)
        print_message.end_execution()

    except Exception as Error:
        pass

    try:
        tools.clean_list([_headers, _values, _status])
    except:
        pass