#!/usr/bin/env python3
# Project: osiris-framework
# Author: Samir Sanchez Garnica @sasaga92
# Version 1.0
# Date: 28/11/2022

info = {
    'name': 'Unix Command Shell, Reverse TCP (via Python3)',
    'description': 'Creates an interactive shell via python3',
    'author': 'Samir Sanchez Garnica',
    'License': 'GPL v3.0',
    'platform': 'Unix',
    'payload_type': 'cmd => [bind]',
    'required': 'Python3'
}

options_payload = {
    'rhost': ['Yes', 'Set the target you are listening for', ''],
    'rport': ['Yes', 'Set the target port to be listened on', ''],
}