#!/usr/bin/env python3
# Project: Osiris-Framework
# Version 1.337

from core.ModuleObtainer import obtainer
from core.ble.BleakBLE import bleakBLE
from utilities.Colors import color
from tabulate import tabulate
import asyncio
from utilities.Messages import print_message

print_message.name_module = __file__

info = {
    'author': 'Samir Sanchez Garnica',
    'date': '2022/12/09',
    'rank': 'Normal',
    'path': 'auxiliary/gather/ble/read.py',
    'category': 'auxiliary',
    'license': 'GPL-2.0',
    'description': 'Module designed for reading features under a BLE service, the return values will be given in hexadecimal format. ',
    'references': ['https://bleak.readthedocs.io/en/latest/']
}
options = {
    'timeout': ['Yes', ' use to set timeout for discover devices', '10'],
    'device': ['Yes', ' use to set device or address for discover device', ''],
    'characteristic': ['Yes', ' use to set characteristic to read your content', ''],
}

required = {
    'start_required': 'True',
    'check_required': 'False'
}


def print_value(return_value):
    __print_value = [[color.color('yellow', 'Device Name'), color.color('yellow', 'Device Address'),
                      color.color('yellow', 'Value in Format HEX')]]
    if return_value['code'] == 200:
        __print_value.append(
            [color.color("green", return_value['message'][0]), color.color("lgray", return_value['message'][1]),
             color.color("cyan", return_value['message'][2])])

    print(tabulate(__print_value, headers='firstrow', tablefmt='simple', stralign='Left'))

    __print_value = [[color.color('yellow', 'Device Name'), color.color('yellow', 'Device Address'),
                      color.color('yellow', 'Value in Format HEX')]]


def exploit():
    print_message.start_execution()

    try:
        __timeout = int(obtainer.options['timeout'][2])
        __device = obtainer.options['device'][2]
        __characteristic = obtainer.options['characteristic'][2]
        __response = asyncio.run(bleakBLE.read_service(__device, __characteristic, __timeout))
    except Exception as Error:
        print_message.execution_error(Error.args[0])
        return False

    if __response['code'] == 200:
        print_value(__response)
    else:
        print_message.execution_error(__response['message'])

    print_message.end_execution()
