#!/usr/bin/env python3
# Project: osiris-framework
# Author: Samir Sanchez Garnica @sasaga92
# Version 1.0
# Date: 22/12/2022

info = {
    'name': 'Webshell PHP Generic Command',
    'description': 'Creates an interactive webshell via Thot',
    'author': 'Samir Sanchez Garnica',
    'License': 'GPL v3.0',
    'platform': 'Automatic',
    'payload_type': 'webshell => [command]',
    'required': 'PHP'
}

options_payload = {
    'username': ['Yes', 'Set a username to authenticate in the webshell', ''],
    'password': ['Yes', 'Set a password to authenticate in the webshell', ''],
    'uri_webshell': ['Yes', 'Set the path where the webshell will be hosted, followed by the webshell name', '/osiris-webshell.php'],
}
