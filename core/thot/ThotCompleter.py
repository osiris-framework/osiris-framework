#!/usr/bin/env python3
# Project: osiris-framework
# Author: Samir Sanchez Garnica @sasaga92
# Version 1.0
# Date: 14/11/2022


import readline
from glob import glob

list_completer = ["clear", "exit", "exec", 'help', "sessions", "background", "select", "kill"]
list_completer_temp = []


def add_new_session(new_sessions):
    global list_completer
    global list_completer_temp

    new_sessions_select = ["select " + x for x in new_sessions]
    new_sessions_select[len(new_sessions_select):] = ["kill " + x for x in new_sessions]

    # add session in multiples list
    for session in new_sessions_select:
        if not session in list_completer_temp:
            list_completer_temp.append(session)
            list_completer.append(session)

    __operation_list = list(set(list_completer_temp).difference(set(new_sessions_select)))
    # remove session
    if len(__operation_list) > 0:
        for remove_session in __operation_list:
            list_completer.remove(remove_session)
            list_completer_temp.remove(remove_session)


def thot_completer():
    global list_completer

    def pathCompleter(text, state):
        line = readline.get_line_buffer().split()
        return [x for x in glob(text + '*')][state]

    class tabCompleter(object):

        def __init__(self):
            global list_completer
            self.listCompleter = None
            self.list_completer = list_completer

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
    t.createListCompleter(t.list_completer)
    readline.set_completer_delims('\t')
    readline.parse_and_bind("tab: complete")
    readline.set_completer(t.listCompleter)
