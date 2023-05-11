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
    'path': 'auxiliary/gather/ble/characteristics.py',
    'category': 'auxiliary',
    'license': 'GPL-2.0',
    'description': 'Lists services, features and descriptors of a given BLe address.',
    'references': ['https://bleak.readthedocs.io/en/latest/']
}
options = {
    'device_address': ['Yes', ' use to set device_address for a BLE address to perform discovery', '']
}

required = {
    'start_required': 'True',
    'check_required': 'False'
}


def print_descriptor_devices(device_information):
    __print_devices = [[color.color('yellow', 'Service'), color.color('yellow', 'Characteristic'),
                        color.color('yellow', 'Descriptor'), color.color('yellow', 'Descriptor Values'),
                        color.color('yellow', 'Values in HEX'),
                        color.color('yellow', 'Property'), color.color('yellow', 'Service Description')]]
    if device_information['code'] == 200:
        for service, service_values in device_information['message'].items():
            for characteristics, characteristics_values in service_values.items():
                if (len(characteristics_values)) == 2:
                    __print_devices.append([color.color("green", service), color.color("blue", characteristics),
                                                 color.color("cyan", characteristics_values[1][0]),
                                                 color.color("cyan", characteristics_values[1][1]),
                                                 color.color("lgray", characteristics_values[0][1]),
                                                 color.color("red", characteristics_values[0][0]),
                                                 color.color("cyan", characteristics_values[0][2])])
                else:
                    __print_devices.append(
                        [color.color("green", service), color.color("blue", characteristics), color.color("cyan", " "),
                         color.color("cyan", " "), color.color("lgray", characteristics_values[0][1]),
                         color.color("red", characteristics_values[0][0]),
                         color.color("cyan", characteristics_values[0][2])])

    print(tabulate(__print_devices, headers='firstrow', tablefmt='simple', stralign='Left'))


def exploit():
    print_message.start_execution()
    __response = asyncio.run(bleakBLE.get_services(obtainer.options['device_address'][2]))

    if __response['code'] == 200:
        print_descriptor_devices(__response)
    else:
        print_message.execution_error(__response['message'])

    print_message.end_execution()
