#!/usr/bin/env python3
# Project: osiris-framework
# Author: Samir Sanchez Garnica @sasaga92
# Version 1.0
# Date: 14/11/2022


import readline
from glob import glob


def thot_completer():
    def pathCompleter(text, state):
        line = readline.get_line_buffer().split()
        return [x for x in glob(text + '*')][state]

    class tabCompleter(object):

        def __init__(self):
            self.listCompleter = None

        def createListCompleter(self, ll):
            pass

            def listCompleter(text, state):
                line = readline.get_line_buffer()
                if not line:
                    return None
                else:
                    return [c + " " for c in ll if c.startswith(line)][state]

            self.listCompleter = listCompleter

    t = tabCompleter()

    # tool command
    t.createListCompleter(["clear", "exit", "exec", 'help', "sessions", "background", "select"
                           ### end
                           ])
    readline.set_completer_delims('\t')
    readline.parse_and_bind("tab: complete")
    readline.set_completer(t.listCompleter)
