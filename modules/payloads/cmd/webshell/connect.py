#!/usr/bin/env python3
# Project: Osiris-Framework
# Version 1.337

info = {
    'name': 'Webshell Connect Generic Command',
    'description': 'Connect a interactive webshell via Thot',
    'author': 'Samir Sanchez Garnica',
    'License': 'GPL v3.0',
    'platform': 'Automatic',
    'payload_type': 'webshell => [command]',
    'required': 'ENDPOINT'
}

options_payload = {
    'target': ['Yes', 'set target to attack', ''],
    'username': ['Yes', 'Set a username to authenticate in the webshell', ''],
    'password': ['Yes', 'Set a password to authenticate in the webshell', ''],
    'uri_webshell': ['Yes', 'Set the path where the webshell will be hosted, followed by the webshell name', '/osiris-webshell.php'],
}
