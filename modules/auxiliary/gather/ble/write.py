#!/usr/bin/env python3
# Project: osiris-framework
# Author: Samir Sanchez Garnica @sasaga92
# Version 1.0
# Date: 07/12/2022

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
    'path': 'auxiliary/gather/ble/write.py',
    'category': 'auxiliary',
    'license': 'GPL-2.0',
    'description': 'Module designed to write data through a provided BLE feature, input data must be provided in hexadecimal. ',
    'references': ['https://bleak.readthedocs.io/en/latest/']
}
options = {
    'timeout': ['Yes', ' use to set timeout for discover devices', '5'],
    'device': ['Yes', ' use to set device or address for discover device', ''],
    'characteristic': ['Yes', ' use to set characteristic to read your content', ''],
    'data': ['Yes', ' use to set the data to be written', '']
}

required = {
    'start_required': 'True',
    'check_required': 'False'
}


def exploit():
    print_message.start_execution()

    try:
        __timeout = int(obtainer.options['timeout'][2])
        __device = obtainer.options['device'][2]
        __characteristic = obtainer.options['characteristic'][2]
        __data = obtainer.options['data'][2]
        __response = asyncio.run(bleakBLE.write_service(__device, __characteristic, __data, __timeout))
    except Exception as Error:
        print_message.execution_error(Error.args[0])
        return False

    if __response['code'] == 200:
        print(__response['message'])
    else:
        print_message.execution_error(__response['message'])

    print_message.end_execution()
