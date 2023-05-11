#!/usr/bin/env python3
# Project: Osiris-Framework
# Version 1.337

info = {
    'name': 'Unix Command Shell, Reverse TCP (via Groovy)',
    'description': 'Creates an interactive shell via groovy',
    'author': 'Samir Sanchez Garnica',
    'License': 'GPL v3.0',
    'platform': 'Windows',
    'payload_type': 'cmd => [reverse]',
    'required': 'groovy'
}

options_payload = {
    'lhost': ['Yes', 'Set the target you want to connect to', ''],
    'lport': ['Yes', 'Set the target port to which you want to connect', ''],
}
