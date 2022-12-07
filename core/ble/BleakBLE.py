#!/usr/bin/env python3
# Project: osiris-framework
# Author: Samir Sanchez Garnica @sasaga92
# Version 1.0
# Date: 07/12/2022

import asyncio
from bleak import BleakScanner, BleakClient
from utilities.Colors import color


class BleakBLE:
    def __init__(self):
        self.__characteristics = {}
        self.__services = {}
        self.__characteristics_discover = []
        self.__descriptors = []
        self.__value = None
        self.__device = None
        self.__status = {}
        self.__devices = {}

    async def scan_devices(self, timeout):
        try:
            for __device in await BleakScanner.discover(timeout=int(timeout)):
                self.__devices[__device.address] = [str(__device.name), str(__device.rssi), str(__device.address)]
        except Exception as Error:
            self.__status['code'] = 500
            self.__status['message'] = Error.args[0]

        if len(self.__devices) > 0:
            self.__status['code'] = 200
            self.__status['message'] = self.__devices

        return self.__status

    async def get_services(self, device_address):
        try:
            self.__characteristics = {}
            self.__services = {}
            self.__characteristics_discover = []
            self.__descriptors = []
            self.__device = await BleakScanner.find_device_by_address(device_address)

            if self.__devices is not None:
                async with BleakClient(self.__device) as client:
                    for service in client.services:
                        for characteristics in service.characteristics:
                            if 'read' in characteristics.properties:

                                try:
                                    self.__value = await client.read_gatt_char(characteristics.uuid)
                                    self.__characteristics_discover.append(",".join(characteristics.properties))
                                    self.__characteristics_discover.append(self.__value)
                                    self.__characteristics_discover.append(characteristics.description)
                                except Exception as Error:
                                    self.__characteristics_discover.append(characteristics.properties)
                                    self.__characteristics_discover.append(Error)
                                    self.__characteristics_discover.append(characteristics.description)

                            else:
                                self.__characteristics_discover.append(",".join(characteristics.properties))
                                self.__characteristics_discover.append("NONE")
                                self.__characteristics_discover.append(characteristics.description)

                            for descriptor in characteristics.descriptors:
                                try:
                                    self.__value = await client.read_gatt_descriptor(descriptor.handle)
                                    self.__descriptors.append(descriptor.uuid)
                                    self.__descriptors.append({descriptor.description: self.__value})
                                except Exception as Error:
                                    self.__descriptors.append(descriptor.uuid)
                                    self.__descriptors.append({descriptor.description: Error})
                                    self.__descriptors.append(Error)

                                self.__characteristics[characteristics.uuid] = [self.__characteristics_discover,
                                                                                self.__descriptors]
                                self.__descriptors = []

                            if characteristics.uuid not in self.__characteristics:
                                self.__characteristics[characteristics.uuid] = [self.__characteristics_discover]
                            self.__characteristics_discover = []

                        self.__services[service.uuid] = self.__characteristics
                        self.__characteristics = {}

            if len(self.__services) > 0:
                self.__status['code'] = 200
                self.__status['message'] = self.__services
            else:
                self.__status['code'] = 500
                self.__status['message'] = color.color("red", "[-] ") + color.color("lgray", "No Services found...")

            return self.__status

        except Exception as Error:
            self.__status['code'] = 500
            self.__status['message'] = Error.args[0]

            return self.__status


bleakBLE = BleakBLE()
