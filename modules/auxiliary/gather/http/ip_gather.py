#!/usr/bin/env python3
# Project: Osiris-Framework
# Version 1.337

import socket
from core.ModuleObtainer import obtainer
from utilities.Colors import color
from utilities.Messages import print_message
from utilities.Tools import tools
print_message.name_module = __file__

info = {
        'author'            :'Samir Sanchez Garnica',
        'date'              :'2019/03/08',
        'rank'              :'Excellent',
        'path'              :'auxiliary/gather/http/ip_gather.py',
        'category'          :'auxiliary',
        'license'           :'GPL-2.0',
        'description'       :'Simple module that obtains the ip address of a url',
        'references'        :['docs.python.org/3/library/socket.html#socket.gethostbyname']
}
options = {
            'target'                :['Yes', 'use to set target','']
}
required = {
        'start_required'     :'True',
        'check_required'     :'False'
}

def exploit():
    """ main exploit function """
    try:
        print_message.start_execution()
        var = socket.gethostbyname(tools.filter_hostname(obtainer.options['target'][2])['message'][0])
        print(color.color("green","[+] ") + color.color("green", obtainer.options['target'][2]) + " resolve to " +color.color("lgray", var) +" "+ color.color("lgray", "successful"))
    except socket.gaierror:
        print_message.execution_error("lgray", " You must enter the URL!")
        return False

    print_message.end_execution()

