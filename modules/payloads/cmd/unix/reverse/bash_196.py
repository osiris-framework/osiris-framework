#!/usr/bin/env python3
# Project: osiris-framework
# Author: Samir Sanchez Garnica @sasaga92
# Version 1.0
# Date: 28/11/2022

info = {
    'name': 'Unix Command Shell, Reverse TCP (via Bash)',
    'description': 'Creates an interactive shell via bash_196',
    'author': 'Samir Sanchez Garnica',
    'License': 'GPL v3.0',
    'platform': 'Unix',
    'payload_type': 'cmd => [reverse]',
    'required': 'BASH'
}

options_payload = {
    'lhost': ['Yes', 'Set the target you want to connect to', ''],
    'lport': ['Yes', 'Set the target port to which you want to connect', ''],
}