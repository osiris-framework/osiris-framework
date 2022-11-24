#!/usr/bin/env python3
# Project: osiris-framework
# Author: Samir Sanchez Garnica @sasaga92
# Version 1.0
# Date: 15/11/2022

import socket
from datetime import datetime
from core.ModuleObtainer import obtainer
from utilities.Colors import color
from utilities.Messages import print_message
print_message.name_module = __file__
from utilities.Tools import tools


info = {
        'author'            :'Samir Sanchez Garnica',
        'date'              :'15/06/2019',
        'rank'              :'Normal',
        'path'              :'auxiliary/scanner/http/ssl_info.py',
        'category'          :'auxiliary',
        'license'           :'GPL-2.0',
        'description'       :'This module that obtains information from an SSL digital certificate',
        'references'        :['https://docs.python.org/3/library/ssl.html']
}

options = {
            'rhost'                :['Yes', 'use to set address target',''],
}

required = {
        'start_required'     :'True',
        'check_required'     :'False'
}


def print_status_ssl_info(__host, __context):
    """Print all the usefull info about host."""
    __days_left = (datetime.strptime(__context[__host]['valid_till'], '%Y-%m-%d') - datetime.now()).days
    print('\t\t'+color.color("yellow","Issued domain: ") + color.color("lgray",str(__context[__host]['issued_to'])))
    print('\t\t'+color.color("yellow","Issued to: ") + color.color("lgray",str(__context[__host]['issued_o'])))
    print('\t\t'+color.color("yellow","Issued by: ") + color.color("lgray",str(__context[__host]['issuer_o'])) + color.color("lgray",str(__context[__host]['issuer_c'])))
    print('\t\t'+color.color("yellow","Valid from: ") + color.color("lgray",str(__context[__host]['valid_from'])))
    print('\t\t'+color.color("yellow","Valid to: ") + color.color("lgray",str(__context[__host]['valid_till'])) + color.color("yellow"," (") + color.color("green_ptrl",str(__days_left)) + color.color("green"," days left ") + color.color("yellow",")"))

    print('\t\t'+color.color("yellow","Validity days: ") + color.color("lgray",str(__context[__host]['validity_days'])))
    print('\t\t'+color.color("yellow","Certificate S/N: ") + color.color("lgray",str(__context[__host]['cert_sn'])))
    print('\t\t'+color.color("yellow","Certificate SHA1 FP: ") + color.color("lgray",str(__context[__host]['cert_sha1'].decode())))
    print('\t\t'+color.color("yellow","Certificate version: ") + color.color("lgray",str(__context[__host]['cert_ver'])))
    print('\t\t'+color.color("yellow","Certificate algorithm: ") + color.color("lgray",str(__context[__host]['cert_alg'])))
    print('\t\t'+color.color("yellow","Expired: ") + color.color("lgray",str(__context[__host]['cert_exp'])))
    print('\t\t'+color.color("yellow","Certificate SANs: "))

    for __san in __context[__host]['cert_sans'].split(';'):
        print('\t\t\t'+color.color("lgray",str(__san)))


def exploit():
    try:
        __context = {}
        __target = obtainer.options['rhost'][2]
        try:
            print_message.start_execution()
            __response = tools.filter_hostname(__target)
            __cert = tools.get_certificate(__response['message'][0], __response['message'][1])
            __context[__response['message'][0]] = tools.get_cert_info(__response['message'][0],__cert['message'])['message']
            print_status_ssl_info(__response['message'][0], __context)
        except Exception as Error:
            print(Error)
            print_message.execution_error("Impossible to extract information to SSL!")
    except socket.gaierror:
        print_message.execution_error("You must enter the valid URL!")
        return False
    print_message.end_execution()
