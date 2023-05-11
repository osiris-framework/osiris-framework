#!/usr/bin/env python3
# Project: Osiris-Framework
# Version 1.337

info = {
    'name': 'Unix Command Shell, Reverse TCP (via Python3)',
    'description': 'Creates an interactive shell via python3 using os.getenv to load environment variables from the connection',
    'author': 'Samir Sanchez Garnica',
    'License': 'GPL v3.0',
    'platform': 'Unix',
    'payload_type': 'cmd => [reverse]',
    'required': 'python3'
}

options_payload = {
    'lhost': ['Yes', 'Set the target you want to connect to', ''],
    'lport': ['Yes', 'Set the target port to which you want to connect', ''],
}
