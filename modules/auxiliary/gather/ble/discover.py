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
    'date': '2022/12/07',
    'rank': 'Normal',
    'path': 'auxiliary/gather/ble/discover.py',
    'category': 'auxiliary',
    'license': 'GPL-2.0',
    'description': 'Module designed to detect BLE (Bluetooth Low Energy) signals.',
    'references': ['https://bleak.readthedocs.io/en/latest/']
}
options = {
    'timeout': ['Yes', ' use to set timeout for discover devices', '10']
}

required = {
    'start_required': 'True',
    'check_required': 'False'
}


def print_scan_devices(device_list):
    __print_devices = [[color.color('yellow', 'Device Name'), color.color('yellow', 'RSSI'),
                        color.color('yellow', 'Device Address')]]
    if device_list['code'] == 200:

        try:
            for key, values in device_list['message'].items():
                __print_devices.append([color.color("green", values[0]), color.color("lgray", values[1]), color.color("cyan", values[2])])
        except:
            print_message.execution_error("an error has occurred, please try again")

        print(tabulate(__print_devices, headers='firstrow', tablefmt='simple', stralign='Left'))


    __print_devices = [[color.color('yellow', 'Device Name'), color.color('yellow', 'RSSI'),
                        color.color('yellow', 'Device Address')]]


def exploit():
    print_message.start_execution()

    try:
        __timeout = int(obtainer.options['timeout'][2])
        __response = asyncio.run(bleakBLE.scan_devices(__timeout))
    except Exception as Error:
        print_message.execution_error(Error.args[0])
        return False

    if __response['code'] == 200:
        print_scan_devices(__response)
    else:
        print_message.execution_error(__response['message'])

    print_message.end_execution()

