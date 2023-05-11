#!/usr/bin/env python3
# Project: Osiris-Framework
# Version 1.337

from core.ModuleObtainer import obtainer
from utilities.Colors import color
import socket
import sys
from datetime import datetime
import threading
from utilities.Tools import tools
from utilities.Messages import print_message
print_message.name_module = __file__
from time import sleep

info = {
    'author': 'Samir Sanchez Garnica',
    'date': '26/03/2019',
    'rank': 'Excellent',
    'category': 'auxiliary',
    'path': 'auxiliary/scanner/smb/sbm_version.py',
    'license': 'GPL-2.0',
    'description': 'Display version information about each system',
    'references': ['https://tools.ietf.org/html/rfc1002']
}
options = {
    'rhost': ['Yes', 'use to set target', ''],
    'rport': ['No', 'use to set a port target 139/445', '139']
}

required = {
    'start_required': 'True',
    'check_required': 'False'
}

_lock = threading.Lock()

# from https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc940063(v%3dtechnet.10)
_unique_names = {
    b'\x00': 'Workstation Service',
    b'\x03': 'Messenger Service',
    b'\x06': 'RAS Server Service',
    b'\x1F': 'NetDDE Service',
    b'\x20': 'Server Service',
    b'\x21': 'RAS Client Service',
    b'\xBE': 'Network Monitor Agent',
    b'\xBF': 'Network Monitor Application',
    b'\x03': 'Messenger Service',
    b'\x1D': 'Master Browser',
    b'\x1B': 'Domain Master Browser',
}
_group_names = {
    b'\x00': 'Domain Name',
    b'\x1C': 'Domain Controllers',
    b'\x1E': 'Browser Service Elections',
    # Master Browser
}

_netbios_item_type = {
    b'\x01\x00': 'NetBIOS computer name',
    b'\x02\x00': 'NetBIOS domain name',
    b'\x03\x00': 'DNS computer name',
    b'\x04\x00': 'DNS domain name',
    b'\x05\x00': 'DNS tree name',
    # b'\x06\x00':'',
    b'\x07\x00': 'Time stamp',
}

def nbns_name(_addr):
    _msg = ''
    _data = b'ff\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00 CKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x00\x00!\x00\x01'
    try:
        _s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        _s.settimeout(2)
        _s.sendto(_data, (_addr, 137))
        _rep = _s.recv(2000)
        if isinstance(_rep, str):
            _rep = bytes(_rep)

        _num = ord(_rep[56:57].decode())  # num of the answer
        _data = _rep[57:]  # start of the answer

        _group, _unique = '', ''

        _msg += '\n\t'
        for _i in range(_num):
            _name = _data[18 * _i:18 * _i + 15].decode()
            _flag_bit = bytes(_data[18 * _i + 15:18 * _i + 16])

            if _flag_bit in _group_names and _flag_bit != b'\x00':  # G TODO

                _msg += '%s\t%s\t%s' % (_name, 'G', _group_names[_flag_bit]) + '\n\t'
                pass
            elif _flag_bit in _unique_names and _flag_bit != b'\x00':  # U

                _msg += '%s\t%s\t%s' % (_name, 'U', _unique_names[_flag_bit]) + '\n\t'
                pass
            elif _flag_bit in b'\x00':
                _name_flags = _data[18 * _i + 16:18 * _i + 18]
                if ord(_name_flags[0:1]) >= 128:
                    _group = _name.strip()

                    _msg += '%s\t%s\t%s' % (_name, 'G', _group_names[_flag_bit]) + '\n\t'
                else:
                    _unique = _name

                    _msg += '%s\t%s\t%s' % (_name, 'U', _unique_names[_flag_bit]) + '\n\t'
            else:
                _msg += '%s\t-\t-' % _name + '\n\t'
                pass
        _msg += '\n\t'

        _msg = '%s\\%s' % (_group, _unique) + '\n\t' + _msg

        return {'group': _group, 'unique': _unique, 'msg': _msg}

    except socket.error as e:
        return False

def netbios_encode(_src):
    # from http://weaponx.site/2017/06/07/NETBIOS%E4%B8%BB%E6%9C%BA%E5%90%8D%E7%BC%96%E7%A0%81%E7%AE%97%E6%B3%95/
    _src = _src.ljust(16, "\x20")
    _names = []
    for _c in _src:
        _char_ord = ord(_c)
        _high_4_bits = _char_ord >> 4
        _low_4_bits = _char_ord & 0x0f
        _names.append(_high_4_bits)
        _names.append(_low_4_bits)

    _res = b''
    for _name in _names:
        _res += chr(0x41 + _name).encode()

    return _res

def smb_detect(_addr, _port=139):
    _msg = ''

    if _port == 139:
        _nbns_result = nbns_name(_addr)
        if not _nbns_result:
            return
        elif not _nbns_result['unique']:
            _msg += 'nbns_result_error'
            _lock.acquire()
            print(_addr + '    ' + _msg)
            _lock.release()
            return
        _msg += _nbns_result['msg']

    _s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _s.settimeout(2)
    try:
        _s.connect((_addr, _port))
    except Exception as e:

        _lock.acquire()
        _lock.release()
        return

    if _port == 139:
        _name = netbios_encode(_nbns_result['unique'])

        _payload0 = b'\x81\x00\x00D ' + _name + b'\x00 EOENEBFACACACACACACACACACACACACA\x00'

        _s.send(_payload0)
        _s.recv(1024)

    _payload1 = b'\x00\x00\x00\x85\xff\x53\x4d\x42\x72\x00\x00\x00\x00\x18\x53\xc8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xfe\x00\x00\x00\x00\x00\x62\x00\x02\x50\x43\x20\x4e\x45\x54\x57\x4f\x52\x4b\x20\x50\x52\x4f\x47\x52\x41\x4d\x20\x31\x2e\x30\x00\x02\x4c\x41\x4e\x4d\x41\x4e\x31\x2e\x30\x00\x02\x57\x69\x6e\x64\x6f\x77\x73\x20\x66\x6f\x72\x20\x57\x6f\x72\x6b\x67\x72\x6f\x75\x70\x73\x20\x33\x2e\x31\x61\x00\x02\x4c\x4d\x31\x2e\x32\x58\x30\x30\x32\x00\x02\x4c\x41\x4e\x4d\x41\x4e\x32\x2e\x31\x00\x02\x4e\x54\x20\x4c\x4d\x20\x30\x2e\x31\x32\x00'
    _payload2 = b'\x00\x00\x01\x0a\xff\x53\x4d\x42\x73\x00\x00\x00\x00\x18\x07\xc8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xfe\x00\x00\x40\x00\x0c\xff\x00\x0a\x01\x04\x41\x32\x00\x00\x00\x00\x00\x00\x00\x4a\x00\x00\x00\x00\x00\xd4\x00\x00\xa0\xcf\x00\x60\x48\x06\x06\x2b\x06\x01\x05\x05\x02\xa0\x3e\x30\x3c\xa0\x0e\x30\x0c\x06\x0a\x2b\x06\x01\x04\x01\x82\x37\x02\x02\x0a\xa2\x2a\x04\x28\x4e\x54\x4c\x4d\x53\x53\x50\x00\x01\x00\x00\x00\x07\x82\x08\xa2\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x02\xce\x0e\x00\x00\x00\x0f\x00\x57\x00\x69\x00\x6e\x00\x64\x00\x6f\x00\x77\x00\x73\x00\x20\x00\x53\x00\x65\x00\x72\x00\x76\x00\x65\x00\x72\x00\x20\x00\x32\x00\x30\x00\x30\x00\x33\x00\x20\x00\x33\x00\x37\x00\x39\x00\x30\x00\x20\x00\x53\x00\x65\x00\x72\x00\x76\x00\x69\x00\x63\x00\x65\x00\x20\x00\x50\x00\x61\x00\x63\x00\x6b\x00\x20\x00\x32\x00\x00\x00\x00\x00\x57\x00\x69\x00\x6e\x00\x64\x00\x6f\x00\x77\x00\x73\x00\x20\x00\x53\x00\x65\x00\x72\x00\x76\x00\x65\x00\x72\x00\x20\x00\x32\x00\x30\x00\x30\x00\x33\x00\x20\x00\x35\x00\x2e\x00\x32\x00\x00\x00\x00\x00'

    try:
        _s.send(_payload1)
        _s.recv(1024)

        _s.send(_payload2)
        _ret = _s.recv(1024)
        _length = ord(_ret[43:44]) + ord(_ret[44:45]) * 256
        _os_version = _ret[47 + _length:]

        _msg += _os_version.replace(b'\x00\x00', b'|').replace(b'\x00', b'').decode('UTF-8', errors='ignore') + '\n\t'

        _start = _ret.find(b'NTLMSSP')

        _length = ord(_ret[_start + 40:_start + 41]) + ord(_ret[_start + 41:_start + 42]) * 256

        _offset = ord(_ret[_start + 44:_start + 45])

        _msg += 'Major Version: %d' % ord(_ret[_start + 48:_start + 49]) + '\n\t'
        _msg += 'Minor Version: %d' % ord(_ret[_start + 49:_start + 50]) + '\n\t'
        _msg += 'Bulid Number: %d' % (
                    ord(_ret[_start + 50:_start + 51]) + 256 * ord(_ret[_start + 51:_start + 52])) + '\n\t'
        _msg += 'NTLM Current Revision: %d' % (ord(_ret[_start + 55:_start + 56])) + '\n\t'

        _index = _start + _offset

        while _index < _start + _offset + _length:
            _item_type = _ret[_index:_index + 2]
            _item_length = ord(_ret[_index + 2:_index + 3]) + ord(_ret[_index + 3:_index + 4]) * 256

            _item_content = _ret[_index + 4: _index + 4 + _item_length].replace(b'\x00', b'')
            if _item_type == b'\x07\x00':

                if sys.version_info[0] == 3:
                    timestamp = int.from_bytes(_item_content, byteorder='little')  # only py > 3.2
                elif sys.version_info[0] == 2:  # for py2 from https://www.aliyun.com/jiaocheng/445198.html
                    timestamp = int(''.join(reversed(_item_content)).encode('hex'), 16)

                    # from https://www.e-learn.cn/content/wangluowenzhang/211641
                _EPOCH_AS_FILETIME = 116444736000000000;
                _HUNDREDS_OF_NANOSECONDS = 10000000
                timestamp = datetime.fromtimestamp((timestamp - _EPOCH_AS_FILETIME) / _HUNDREDS_OF_NANOSECONDS)

                _msg += '%s: %s' % (_netbios_item_type[_item_type], timestamp) + '\n\t'
            elif _item_type in _netbios_item_type:
                _msg += '%s: %s' % (_netbios_item_type[_item_type], _item_content.decode(errors='ignore')) + '\n\t'
            elif _item_type == b'\x00\x00':  # end
                break
            else:
                _msg += 'Unknown: %s' % (_item_content) + '\n\t'
            _index += 4 + _item_length

        _lock.acquire()
        print('\n')
        print(color.color("green", "[+] ") + color.color("green", str(_addr + str(":") + str(_port))) + " " + color.color(
            "lgray", _msg))

        _lock.release()
    except:
        pass

def exploit():
    try:
        __target = obtainer.options['rhost'][2]
        __port = int(obtainer.options['rport'][2])
        __threads = []

        if isinstance(__port, int):
            __response =  tools.check_IPV4(__target)

            if __response['code'] != 200:
                print_message.execution_error(__response['message'])
                return False

            if __port == 139 or __port == 445:
                print_message.start_execution()
                for __address in __response['message']:
                    __thread = threading.Thread(target=smb_detect, args=(__address, __port))
                    __thread.start()
                    __threads.append(__thread)
                    sleep(0.1)

                for __join_thread in __threads:
                    __join_thread.join()

                print_message.end_execution()
    except Exception as Error:
        print(Error)

def check():
    pass

