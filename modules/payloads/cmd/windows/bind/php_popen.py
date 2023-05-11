#!/usr/bin/env python3
# Project: Osiris-Framework
# Version 1.337

info = {
    'name': 'Windows Command Shell, Reverse TCP (via PHP)',
    'description': 'Creates an interactive shell via php_popen',
    'author': 'Samir Sanchez Garnica',
    'License': 'GPL v3.0',
    'platform': 'Windows',
    'payload_type': 'cmd => [bind]',
    'required': 'PHP'
}


options_payload = {
    'rhost': ['Yes', 'Set the target you are listening for', ''],
    'rport': ['Yes', 'Set the target port to be listened on', ''],
}
