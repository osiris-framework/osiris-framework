#!/usr/bin/env python3
# Project: Osiris-Framework
# Version 1.337

info = {
    'name': 'Generic Command Shell, Reverse TCP',
    'description': 'Creates an interactive shell reverse tcp',
    'author': 'Samir Sanchez Garnica',
    'License': 'GPL v3.0',
    'platform': 'Generic',
    'payload_type': 'cmd => [reverse]',
    'required': 'Connection'
}

options_payload = {
    'lhost': ['Yes', 'Set the target you want to connect to', ''],
    'lport': ['Yes', 'Set the target port to which you want to connect', ''],
}
