#!/usr/bin/env python3
# Project: Osiris-Framework
# Version 1.337
import os
import platform
from re import search
import socket
import urllib.request
import shutil
from utilities.Colors import color
from OpenSSL import SSL, crypto
from ssl import PROTOCOL_TLSv1
from datetime import datetime
from tabulate import tabulate
from platform import system
from subprocess import STDOUT, check_output
from string import ascii_uppercase, ascii_lowercase, digits
from tempfile import gettempdir
from json import load
import secrets, string


class Tools(object):
    def __init__(self):
        self.__haystack = None
        self.__needle = None
        self.__length = None
        self.__pattern = None
        self.__letters = None
        self.__generate_value = None
        self.__temp_dir = None
        self.__platform = None
        self.___response = None
        self.__result_dictionary = None
        self.__port = None
        self.__host = None
        self.__cert_subject = None
        self.__valid_till = None
        self.__valid_from = None
        self.__context = None
        self.__san = None
        self.__ext_count = None
        self.__cert = None
        self.__oscon = None
        self.__osobj = None
        self.__sock = None
        self.__address = None
        self.__prefix = None
        self.__start = None
        self.___end = None
        self.__dec_address = None
        self.__bin_address = None
        self.__mask = None
        self.__IPV4 = None
        self.__status = {'message': '', 'code': 0}
        self.status_code = {
            100: 'Continue',
            101: 'Switching Protocols',
            102: 'Processing',
            103: 'Early Hints',
            200: 'OK',
            201: 'Created',
            202: 'Accepted',
            203: 'Non-Authoritative Information',
            204: 'No Content',
            205: 'Reset Content',
            206: 'Partial Content',
            207: 'Multi-Status',
            208: 'Already Reported',
            226: 'IM Used',
            300: 'Multiple Choices',
            301: 'Moved Permanently',
            302: 'Found',
            303: 'See Other',
            304: 'Not Modified',
            305: 'Use Proxy',
            306: 'Switch Proxy',
            307: 'Temporary Redirect',
            308: 'Permanent Redirect',
            400: 'Bad Request',
            401: 'Unauthorized',
            402: 'Payment Required',
            403: 'Forbidden',
            404: 'Not Found',
            405: 'Method Not Allowed',
            406: 'Not Acceptable',
            407: 'Proxy Authentication Required',
            408: 'Request Timeout',
            409: 'Conflict',
            410: 'Gone',
            411: 'Length Required',
            412: 'Precondition Failed',
            413: 'Payload Too Large',
            414: 'URI Too Long',
            415: 'Unsupported Media Type',
            416: 'Range Not Satisfiable',
            417: 'Expectation Failed',
            418: 'I"m a teapot',
            421: 'Misdirected Request',
            422: 'Unprocessable Entity',
            423: 'Locked',
            424: 'Failed Dependency',
            425: 'Too Early',
            426: 'Upgrade Required',
            428: 'Precondition Required',
            429: 'Too Many Requests',
            431: 'Request Header Fields Too Large',
            451: 'Unavailable For Legal Reasons',
            500: 'Internal Server Error',
            501: 'Not Implemented',
            502: 'Bad Gateway',
            503: 'Service Unavailable',
            504: 'Gateway Timeout',
            505: 'HTTP Version Not Supported',
            506: 'Variant Also Negotiates',
            507: 'Insufficient Storage',
            508: 'Loop Detected',
            510: 'Not Extended',
            511: 'Network Authentication Required',
        }
        self.__MAX_PATTERN_LENGTH = 20280

    def _isIPV4(self, IPV4):
        # Make a regular expression
        # for validating an Ip-address
        self.__regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
        			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
        			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
        			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''

        if search(self.__regex, IPV4):
            return True
        else:
            return False

    def check_IPV4(self, IPV4):
        self.__status = {'message': '', 'code': 0}
        if self._isIPV4(IPV4):
            self.__IPV4 = IPV4

            if '/' in self.__IPV4:
                self.__address, self.__mask = self.__IPV4.split('/')
                self.__mask = int(self.__mask)

                self.__bin_address = ''.join(
                    [(8 - len(bin(int(_i))[2:])) * '0' + bin(int(_i))[2:] for _i in self.__address.split('.')])
                self.__start = self.__bin_address[:self.__mask] + (32 - self.__mask) * '0'
                self.___end = self.__bin_address[:self.__mask] + (32 - self.__mask) * '1'
                self.__bin_address = [(32 - len(bin(int(_i))[2:])) * '0' + bin(_i)[2:] for _i in
                                      range(int(self.__start, 2), int(self.___end, 2) + 1)]

                self.__dec_address = [
                    '.'.join([str(int(self.__bin_address[8 * _i:8 * (_i + 1)], 2)) for _i in range(0, 4)]) for
                    self.__bin_address in self.__bin_address]

                self.__status['message'] = self.__dec_address
                self.__status['code'] = 200
            elif '-' in self.__IPV4:
                self.__address, self.___end = self.__IPV4.split('-')
                self.___end = int(self.___end)
                self.__start = int(self.__address.split('.')[3])
                self.__prefix = '.'.join(self.__address.split('.')[:-1])
                self.__address = [self.__prefix + '.' + str(_i) for _i in range(self.__start, self.___end + 1)]
                self.__status['message'] = self.__address
                self.__status['code'] = 200
            else:
                self.__status['message'] = [self.__IPV4]
                self.__status['code'] = 200
        else:
            self.__status[
                'message'] = "IPV4 format is not allowed, you can use 127.0.0.1-range, 127.0.0.1/mask or 127.0.0.1 format."
            self.__status['code'] = 500
        return self.__status

    def grab_banner(self, __address, __port):
        self.__status = {'message': '', 'code': 0}
        try:
            socket.setdefaulttimeout(2)
            __socket = socket.socket()
            __socket.connect((__address, __port))
            __banner = str(__socket.recv(1024).decode())
            __socket.close()
            self.__status['message'] = color.color("green", "[+] ") + color.color("lgray",
                                                                                  str(__address)) + color.color("red",
                                                                                                                ":") + color.color(
                "lgray", str(__port)) + color.color("yellow", " Banner:") + color.color("lgray", str(__banner))
            self.__status['code'] = 200

        except Exception as Error:
            self.__status['code'] = 500
        return self.__status

    def read_file(self, file_name):
        try:
            with open(file_name, 'r', encoding="ISO-8859-1") as infile:
                for __data in infile:
                    __data = __data.strip('\r\n')
                    yield __data
        except IOError as Error:
            pass

    def get_certificate(self, __host, __port):
        self.__status = {'message': '', 'code': 0}

        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__osobj = SSL.Context(PROTOCOL_TLSv1)
        self.__sock.connect((__host, int(__port)))
        self.__oscon = SSL.Connection(self.__osobj, self.__sock)
        self.__oscon.set_tlsext_host_name(__host.encode())
        self.__oscon.set_connect_state()
        self.__oscon.do_handshake()
        self.__cert = self.__oscon.get_peer_certificate()
        self.__sock.close()
        self.__status['message'] = self.__cert
        self.__status['code'] = 200

        return self.__status

    def get_cert_sans(self, __x509cert):
        '''
        Get Subject Alt Names from Certificate. Shameless taken from stack overflow:
        https://stackoverflow.com/users/4547691/anatolii-chmykhalo
        '''
        self.__status = {'message': '', 'code': 0}
        self.__san = ''
        self.__ext_count = __x509cert.get_extension_count()
        for _i in range(0, self.__ext_count):
            self.__ext = __x509cert.get_extension(_i)
            if 'subjectAltName' in str(self.__ext.get_short_name()):
                self.__san = self.__ext.__str__()
        # replace commas to not break csv output
        self.__san = self.__san.replace(',', ';')
        self.__status['message'] = self.__san
        self.__status['code'] = 200

        return self.__status

    def get_cert_info(self, __host, __cert):
        self.__context = {}

        self.__cert_subject = self.__cert.get_subject()

        self.__context['issued_to'] = self.__cert_subject.CN
        self.__context['issued_o'] = self.__cert_subject.O
        self.__context['issuer_c'] = self.__cert.get_issuer().countryName
        self.__context['issuer_o'] = self.__cert.get_issuer().organizationName
        self.__context['issuer_ou'] = self.__cert.get_issuer().organizationalUnitName
        self.__context['issuer_cn'] = self.__cert.get_issuer().commonName
        self.__context['cert_sn'] = self.__cert.get_serial_number()
        self.__context['cert_sha1'] = self.__cert.digest("sha1")
        self.__context['cert_alg'] = self.__cert.get_signature_algorithm().decode()
        self.__context['cert_ver'] = self.__cert.get_version()
        self.__context['cert_sans'] = self.get_cert_sans(self.__cert)['message']
        self.__context['cert_exp'] = self.__cert.has_expired()

        # Valid from
        self.__valid_from = datetime.strptime(self.__cert.get_notBefore().decode('ascii'),
                                              '%Y%m%d%H%M%SZ')
        self.__context['valid_from'] = self.__valid_from.strftime('%Y-%m-%d')

        # Valid till
        self.__valid_till = datetime.strptime(self.__cert.get_notAfter().decode('ascii'),
                                              '%Y%m%d%H%M%SZ')
        self.__context['valid_till'] = self.__valid_till.strftime('%Y-%m-%d')

        # Validity days
        self.__context['validity_days'] = (self.__valid_till - self.__valid_from).days
        self.__status['message'] = self.__context
        self.__status['code'] = 200

        return self.__status

    def filter_hostname(self, __host):
        """Remove unused characters and split by address and port."""
        self.__status = {'message': '', 'code': 0}
        self.__host = __host.replace('http://', '').replace('https://', '').replace('/', '')
        self.__port = 443
        if ':' in self.__host:
            self.__host, self.__port = self.__host.split(':')

        self.__status['message'] = [self.__host, self.__port]
        self.__status['code'] = 200
        return self.__status

    def create_tabulate_list(self, keys, contents):
        self.__status = {'message': '', 'code': 0}
        if len(contents) == len(keys):
            self.__result_dictionary = {}
            for key in range(len(keys)):
                self.__result_dictionary[keys[key]] = contents[key]
            self.__status['message'] = tabulate(self.__result_dictionary, headers='keys')
            self.__status['code'] = 200
        else:
            self.__status['code'] = 500

        return self.__status

    def http_or_https(self, _url):
        try:
            self.___response = ""
            self.__status = {'message': '', 'code': 0}
            if 'http://' in _url:
                self.__status['message'] = "http://"
                self.__status['code'] = 200
            elif 'https://' in _url:
                self.__status['message'] = "https://"
                self.__status['code'] = 200
            else:
                self.__status['code'] = 500
        except:
            self.__status['code'] = 500

        return self.__status

    def clean_list(self, list):
        for list in list:
            list.clear()

    def get_port_use(self, __port):
        self.__status = {'message': '', 'code': 0}
        self.__platform = system().lower()
        if 'linux' in self.__platform:
            try:
                if ':{}'.format(__port) in check_output("netstat -ant", stderr=STDOUT, timeout=10, shell=True).decode():
                    self.__status['code'] = 500
            except Exception:
                self.__status['code'] = 200
        elif 'darwin' in self.__platform:
            try:
                if '*.{}'.format(__port) in check_output("netstat -antp tcp", stderr=STDOUT, timeout=10,
                                                         shell=True).decode():
                    self.__status['code'] = 500
            except Exception as Error:
                print(Error)
                self.__status['code'] = 200

        return self.__status

    def temp_dir(self):
        self.__status = {'message': '', 'code': 0}
        try:
            self.__temp_dir = gettempdir()

            self.__status['code'] = 200
            self.__status['message'] = self.__temp_dir
        except Exception as Error:
            self.__status['code'] = 500
            self.__status['message'] = Error

        return self.__status

    def create_dir(self, dir_create):
        self.__status = {'message': '', 'code': 0}
        try:
            os.mkdir(dir_create)
            self.__status['code'] = 200
            self.__status['message'] = dir_create
        except FileExistsError:
            self.__status['code'] = 200
            self.__status['message'] = dir_create
        except Exception as Error:
            self.__status['code'] = 500
            self.__status['message'] = Error

        return self.__status

    def read_json_file(self, __file_name):
        try:
            with open(__file_name) as fh:
                yield load(fh)
        except Exception as Error:
            pass

    def generate_id(self, __uid_length, __session_name="thot-session-"):
        self.__status = {'message': '', 'code': 0}
        self.__generate_value = __session_name
        self.__letters = string.ascii_letters + string.digits

        for i in range(__uid_length):
            self.__generate_value += ''.join(secrets.choice(self.__letters))

        if len(self.__generate_value) - len(__session_name) == __uid_length:
            self.__status['code'] = 200
            self.__status['message'] = self.__generate_value

        return self.__status

    def get_universal_platform(self):
        self.__known_os = ['linux', 'windows', 'osx', 'unknown platform']
        self.__status = {'message': '', 'code': 0}
        self.__platform = system().lower()
        if 'linux' in self.__platform:
            try:
                self.__status['message'] = self.__known_os[0]
                self.__status['code'] = 200
            except Exception:
                self.__status['code'] = 500
        elif 'darwin' in self.__platform:
            try:
                self.__status['message'] = self.__known_os[2]
                self.__status['code'] = 200
            except Exception as Error:
                self.__status['code'] = 500
        elif 'win32' in self.__platform:
            try:
                self.__status['message'] = self.__known_os[1]
                self.__status['code'] = 200
            except Exception as Error:
                self.__status['code'] = 500
        else:
            self.__status['message'] = self.__known_os[3]
            self.__status['code'] = 500

        return self.__status

    # Function for download files through urllib
    def download_files_by_url(self, file_src_url, file_dest) -> 'http://example.com/something.pdf':
        try:
            with urllib.request.urlopen(file_src_url) as response, open(file_dest, 'wb') as out_file:
                shutil.copyfileobj(response, out_file)
                # file_write = open(file_dest, 'w')
                # file_write.write(response)

            self.__status['message'] = [file_src_url, file_dest]
            self.__status['code'] = 200
        except Exception as Error:
            self.__status['message'] = str(Error)
            self.__status['code'] = 500
            print(str(Error))
        return self.__status

    def pattern_create(self, __length: int):
        """
                Generate a pattern of a given length up to a maximum
                of 20280 - after this the pattern would repeat
        """

        self.__status = {'message': '', 'code': 0}
        self.__pattern = ""

        try:
            self.__length = int(__length)
        except ValueError as Error:
            self.__status['code'] = 500
            self.__status['message'] = Error.args[0]
            return self.__status


        if self.__length > self.__MAX_PATTERN_LENGTH:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] " ) + color.color("lgray","Pattern length exceeds maximum of {0} bytes ".format(color.color("yellow", self.__MAX_PATTERN_LENGTH)))
            return self.__status

        for upper in ascii_uppercase:
            for lower in ascii_lowercase:
                for digit in digits:
                    if len(self.__pattern) < self.__length:
                        self.__pattern += upper + lower + digit
                    else:
                        self.__status['code'] = 200
                        self.__status['message'] = self.__pattern[:self.__length]
                        return self.__status

    def pattern_find(self, __search_pattern : str):
        """
            Search for search_pattern in pattern. Convert from hex if needed
            Looking for needle in haystack
        """

        self.__needle = __search_pattern

        try:
            if self.__needle.startswith("0x"):
                # Strip off '0x', convert to ASCII and reverse
                self.__needle = self.__needle[2:]
                self.__needle = bytearray.fromhex(self.__needle).decode("ascii")
                self.__needle = self.__needle[::-1]
        except (ValueError, TypeError) as Error:
            self.__status['code'] = 500
            self.__status['message'] = color.color("lgray","The value {} passed does not seem to correspond to a hexadecimal value.".format(color.color("red", self.__needle)))
            return self.__status

        self.__haystack = ""
        for upper in ascii_uppercase:
            for lower in ascii_lowercase:
                for digit in digits:
                    self.__haystack += upper + lower + digit
                    found_at = self.__haystack.find(self.__needle)
                    if found_at > -1:
                        self.__status['code'] = 200
                        self.__status['message'] = color.color("lgray", "Pattern found in position {}".format(color.color("green", found_at)))
                        return self.__status

        self.__status['code'] = 500
        self.__status['message'] = color.color("lgray", "pattern {} not found".format(color.color("yellow", self.__needle)))
        return self.__status


tools = Tools()
