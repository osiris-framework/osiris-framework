#!/usr/bin/env python3
# Project: osiris-framework
# Author: Samir Sanchez Garnica @sasaga92
# Version 1.0
# Date: 28/11/2022

info = {
    'name': 'Windows Command Shell, Reverse TCP (via PHP)',
    'description': 'Creates an interactive shell via php_system',
    'author': 'Samir Sanchez Garnica',
    'License': 'GPL v3.0',
    'platform': 'Windows',
    'payload_type': 'cmd => [reverse]',
    'required': 'PHP'
}

options_payload = {
    'lhost': ['Yes', 'Set the target you want to connect to', ''],
    'lport': ['Yes', 'Set the target port to which you want to connect', ''],
}