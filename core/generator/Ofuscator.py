#!/usr/bin/env python3
# Project: osiris-framework
# Author: Samir Sanchez Garnica @sasaga92
# Version 1.0
# Date: 14/11/2022

from base64 import b64encode, b64decode
from requests.utils import quote, unquote

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

    def base64_decode_win(self, __payload):
        try:
            self.__status['code'] = 200
            self.__status['message'] = b64decode(__payload.encode('UTF-16LE')).decode()

        except Exception as Error:
            self.__status['code'] = 500
            self.__status['message'] = str(Error)

        return self.__status

    def base64_encode(self, __payload):
        try:
            self.__status['code'] = 200
            self.__status['message'] = b64encode(__payload.encode('UTF-8')).decode()

        except Exception as Error:
            self.__status['code'] = 500
            self.__status['message'] = str(Error)

        return self.__status

    def base64_decode(self, __payload):
        try:
            self.__status['code'] = 200
            self.__status['message'] = b64decode(__payload.encode('UTF-8')).decode()

        except Exception as Error:
            self.__status['code'] = 500
            self.__status['message'] = str(Error)

        return self.__status

    def url_encode(self, __payload):
        try:
            self.__status['code'] = 200
            self.__status['message'] = quote(__payload.encode('UTF-8'))

        except Exception as Error:
            self.__status['code'] = 500
            self.__status['message'] = str(Error)

        return self.__status

    def url_decode(self, __payload):
        try:
            self.__status['code'] = 200
            self.__status['message'] = unquote(__payload.encode('UTF-8'))

        except Exception as Error:
            self.__status['code'] = 500
            self.__status['message'] = str(Error)

        return self.__status


ofuscator = Ofuscator()
