#!/usr/bin/env python3
# Project: Osiris-Framework
# Version 1.337

from core.ModuleObtainer import obtainer
from utilities.Messages import print_message
print_message.name_module = __file__
from utilities.Tools import tools
import threading
from ftplib import FTP
from utilities.Colors import color
from time import sleep

info = {
        'author'            :'Samir Sanchez Garnica',
        'date'              :'2019/05/25',
        'rank'              :'Normal',
        'path'              :'auxiliary/scanner/ftp/ftp_anonymous.py',
        'category'          :'auxiliary',
        'license'           :'GPL-2.0',
        'description'       :'Simple module Detect anonymous (read/write) FTP server access.',
        'references'        :['http://en.wikipedia.org/wiki/File_Transfer_Protocol#Anonymous_FTP']
}
options = {
        'rhost'                 :['Yes', ' use to set rhost',''],
        'rport'                 :['Yes', ' use to set rport','21']
}

required = {
        'start_required'     :'True',
        'check_required'     :'False'
}


def ftp_anonymous_check(__address, __port):
    __status = {'message': '', 'code': 0}
    __flag = False
    __permission = ''
    __result = []
    try:
        __ftp = FTP()
        __ftp.connect(__address, __port)
        __ftp.login("anonymous", "anonymous")
        __flag = True

        try:
            __dir_list = __ftp.retrlines('LIST', __result.append)
            __permission += 'READ'
        except Exception:
            pass

        try:
            __ftp.mkd('pwned')
            __permission += 'WRITE'
        except:
            pass
        __ftp.quit()
    except Exception as Error:
        __flag = False

    if __flag:
        __banner = tools.grab_banner(__address, __port)['message']
        print(color.color("green", "[+] ") + color.color("lgray", str(__address)) + color.color(
            "red", ":") + color.color("lgray", str(__port)) + color.color("yellow", " Anonymous: ") + color.color(
            "lgray", str(__permission)) + " " + __banner)


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
            __thread = threading.Thread(target=ftp_anonymous_check, args=(__address, __port))
            __thread.start()
            __threads.append(__thread)
            sleep(0.1)
        print_message.end_execution()


def check():
  pass