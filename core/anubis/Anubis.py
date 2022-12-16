#!/usr/bin/env python3
# Project: osiris-framework
# Author: Samir Sanchez Garnica @sasaga92
# Version 1.0
# Date: 14/11/2022
import json

from tabulate import tabulate
from utilities.Colors import color
from utilities.Tools import tools
from utilities.Messages import print_message
print_message.name_module = __file__
import socket
import struct

_blocks = ""


class Anubis:
    def __init__(self):
        self.__sysinfo_result = None
        self.__data = None
        self.__anubis_command_permitted = ['download', 'upload', 'sysinfo', 'recv_download_file', 'size_download_file', 'error']
        self.__socked_fd = None
        self.__tmp_folder = tools.temp_dir()['message'] + "/osiris-download/"

    def processor(self, socket_fd: socket.socket, information: dict):
        self.__socked_fd = socket_fd
        try:
            for __key, __value in information.items():
                if __key in self.__anubis_command_permitted:
                    if __key == 'sysinfo':
                        self._print_sysinfo(__value)
                        break
                    elif __key == 'download':
                        self._download_file(__value)
                        break
                    elif __key == 'size_download_file':
                        self._receive_file_size(__value)
                    elif __key == 'recv_download_file':
                        self._recv_download_file(__value)
                    elif __key == 'error':
                        print_message.execution_error(__value)
                    else:
                        pass
        except KeyError:
            pass

    def _print_sysinfo(self, sysinfo: list):
        self.__sysinfo_result = [
            [color.color('yellow', 'System'), color.color('yellow', 'Processor'), color.color('yellow', 'Node'),
             color.color('yellow', 'Machine'),
             color.color('yellow', 'version'), color.color('yellow', 'Release'), color.color('yellow', 'Username')]]

        self.__sysinfo_result.append(
            [color.color("lgray", sysinfo[0]), color.color("lgray", sysinfo[1]), color.color("lgray", sysinfo[2]),
             color.color("lgray", sysinfo[3]), color.color("lgray", sysinfo[4]), color.color("lgray", sysinfo[5]),
             color.color("cyan", sysinfo[6])])

        if len(self.__sysinfo_result) > 1:
            print(tabulate(self.__sysinfo_result, headers='firstrow', tablefmt='simple', stralign='left'))
            print('')

    def _receive_file_size(self, __packet):
        # Esta función se asegura de que se reciban los bytes
        # que indican el tamaño del archivo que será enviado,
        # que es codificado por el cliente vía struct.pack(),
        # función la cual genera una secuencia de bytes que
        # representan el tamaño del archivo.
        self.__fmt = "<Q"
        self.__expected_bytes = struct.calcsize(self.__fmt)
        self.__received_bytes = 0
        self.__stream = bytes()
        while self.__received_bytes < self.__expected_bytes:
            self.__chunk = bytes.fromhex(__packet)
            self.__stream += self.__chunk
            self.__received_bytes += len(self.__chunk)
        self.__filesize = struct.unpack(self.__fmt, self.__stream)[0]
        return self.__filesize

    def _download_file(self, __filename):
        self.__tmp_folder_created = tools.create_dir(self.__tmp_folder)
        self.__file_name = __filename.split("/")[-1] if '/' in __filename else __filename.split("\\")[-1]

        if self.__tmp_folder_created['code'] == 200:
            self.__tmp_file = self.__tmp_folder_created['message'] + self.__file_name

        self.__socked_fd.send("procedure_download ".encode() + __filename.encode())

    def _recv_download_file(self, __packet):
        global _blocks
        _blocks += __packet

        if self.__filesize == len(bytes.fromhex(_blocks)):

            print(color.color("yellow", "[!] ") + color.color("lgray", "receiving ") + color.color("cyan", str(len(
                __packet))) + color.color("green", " bytes") + color.color("lgray", " full blocks ") + color.color(
                "cyan", str(len(bytes.fromhex(_blocks)))) + color.color("green", " bytes"))

            print(color.color("green", "[+] ") + color.color("yellow", "Name: ") + color.color("green",
                                                                                               self.__file_name) + color.color(
                "yellow", " filesize: ") + color.color("green", self.__filesize) + color.color("green",
                                                                                               " bytes") + color.color(
                "yellow", " path: ") + color.color("green", self.__tmp_file))

            with open(self.__tmp_file, "wb") as f:
                f.write(bytes.fromhex(_blocks))
                f.close()
            _blocks = ""
        else:
            print(color.color("yellow", "[!] ") + color.color("lgray", "receiving ") + color.color("cyan", str(len(
                __packet))) + color.color("green", " bytes") + color.color("lgray", " full blocks ") + color.color(
                "cyan", str(len(bytes.fromhex(_blocks)))) + color.color("green", " bytes"))


anubis = Anubis()
