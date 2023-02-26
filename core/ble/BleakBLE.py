#!/usr/bin/env python3
# Project: osiris-framework
# Author: Samir Sanchez Garnica @sasaga92
# Version 1.0
# Date: 07/12/2022

import asyncio
from bleak import BleakScanner, BleakClient
from utilities.Colors import color
from utilities.Messages import print_message

print_message.name_module = __file__


class BleakBLE:
    def __init__(self):
        self.__ret_write_value = None
        self.__value_return = None
        self.__address = None
        self.__characteristics = {}
        self.__services = {}
        self.__characteristics_discover = []
        self.__descriptors = []
        self.__value = None
        self.__device = None
        self.__status = {}
        self.__devices = {}
        self.__device_found = None

    async def scan_devices(self, timeout):
        """
            Description: Function in charge of performing a scan and discovery of nearby devices that are detectable through BLE, this function receives as parameter a timeout in seconds to perform the scan.
        """
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

    async def _notification_handler(self, sender, data):
        print(color.color("yellow", "Response: " ) +  color.color("cyan", ', '.join('{:02x}'.format(x) for x in data)))

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
                                    self.__characteristics_discover.append(self.__value.hex())
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
                                    self.__descriptors.append({descriptor.description: self.__value.hex()})
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

    async def read_service(self, __device_name_or_address, __characteristic, __timeout=5):
        self.__device_found = None
        self.__devices = await BleakScanner.discover(timeout=__timeout)
        for __device in self.__devices:
            if __device.name == __device_name_or_address or __device.address == __device_name_or_address:
                self.__device_found = __device
                print_message.execution_info("Device {} Found".format(self.__device_found.name))
                break
        try:
            self.__address = self.__device_found.address

            async with BleakClient(self.__address) as client:
                self.__value_return = await client.read_gatt_char(__characteristic)
                self.__status['code'] = 200
                self.__status['message'] = [self.__device_found.name, self.__device_found.address,
                                            self.__value_return.hex()]

        except Exception as Error:
            self.__status['code'] = 500
            self.__status['message'] = Error.args[0]

        if self.__device_found is None:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Error querying data with the information provided")

        return self.__status

    async def write_service(self, __device_name_or_address, __characteristic, __data, __timeout=5):
        self.__device_found = None
        self.__devices = await BleakScanner.discover(timeout=__timeout)

        for __device in self.__devices:
            if __device.name == __device_name_or_address or __device.address == __device_name_or_address:
                self.__device_found = __device
                print_message.execution_info("Device {} Found".format(self.__device_found.name))
                break

        try:
            self.__address = self.__device_found.address

            async with BleakClient(self.__address) as client:
                try:
                    self.__ret_write_value = await client.write_gatt_char(__characteristic, bytes.fromhex(__data), True)
                    await asyncio.sleep(3)
                    self.__status['code'] = 200
                    self.__status['message'] = color.color("green", "[+] ") + color.color("yellow",
                                                                                          "Device Address: ") + color.color(
                        "lgray", self.__device_found.address) + color.color("yellow",
                                                                            " Characteristic: ") + color.color("lgray",
                                                                                                               __characteristic) + color.color(
                        "yellow", " Data ") + color.color("cyan", "{}".format(__data)) + color.color("lgray",
                                                                                                     " sent correctly")
                except Exception as Error:
                    self.__status['code'] = 500
                    self.__status['message'] = Error.args[0]
        except Exception as Error:
            self.__status['code'] = 500
            self.__status['message'] = Error.args[0]

        if self.__device_found is None:
            self.__status['code'] = 500
            self.__status['message'] = color.color("lgray",
                                                   "Error querying data with the information provided or device ") + color.color(
                "yellow", __device_name_or_address) + color.color("lgray", " not found")

        return self.__status

    async def write_service_notify(self, __device_name_or_address, __characteristic, __characteristic_notify, __data,
                                   __timeout=5):
        self.__device_found = None
        self.__devices = await BleakScanner.discover(timeout=__timeout)

        for __device in self.__devices:
            if __device.name == __device_name_or_address or __device.address == __device_name_or_address:
                self.__device_found = __device
                print_message.execution_info("Device {} Found".format(self.__device_found.name))
                break

        try:
            self.__address = self.__device_found.address

            async with BleakClient(self.__address) as client:
                try:
                    await client.start_notify(__characteristic_notify, self._notification_handler)
                    self.__ret_write_value = await client.write_gatt_char(__characteristic, bytes.fromhex(__data), True)
                    await asyncio.sleep(7)
                    await client.stop_notify(__characteristic_notify)
                    self.__status['code'] = 200
                    self.__status['message'] = color.color("green", "[+] ") + color.color("yellow",
                                                                                          "Device Address: ") + color.color(
                        "lgray", self.__device_found.address) + color.color("yellow",
                                                                            " Characteristic: ") + color.color("lgray",
                                                                                                               __characteristic) + color.color(
                        "yellow", " Data ") + color.color("cyan", "{}".format(__data)) + color.color("lgray",
                                                                                                     " sent correctly")
                except Exception as Error:
                    self.__status['code'] = 500
                    self.__status['message'] = Error.args[0]
        except Exception as Error:
            self.__status['code'] = 500
            self.__status['message'] = Error.args[0]

        if self.__device_found is None:
            self.__status['code'] = 500
            self.__status['message'] = color.color("lgray",
                                                   "Error querying data with the information provided or device ") + color.color(
                "yellow", __device_name_or_address) + color.color("lgray", " not found")

        return self.__status


bleakBLE = BleakBLE()
