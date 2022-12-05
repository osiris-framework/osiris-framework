#!/usr/bin/env python3
# Project: osiris-framework
# Author: Samir Sanchez Garnica @sasaga92
# Version 1.0
# Date: 14/11/2022

from base64 import b64encode


class Ofuscator:
    def __init__(self):
        self.__status = {'message': '', 'code': 0}

    def base64_encode_win(self, __payload):
        try:
            self.__status['code'] = 200
            self.__status['message'] = b64encode(__payload.encode('UTF-16LE')).decode()

        except Exception as Error:
            self.__status['code'] = 500
            self.__status['message'] = str(Error)

        return self.__status


ofuscator = Ofuscator()
