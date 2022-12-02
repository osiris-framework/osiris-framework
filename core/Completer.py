#!/usr/bin/env python3
# Project: osiris-framework
# Author: Samir Sanchez Garnica @sasaga92
# Version 1.0
# Date: 14/11/2022

import readline
from glob import glob


def completer():
    def pathCompleter(text, state):
        line = readline.get_line_buffer().split()
        return [x for x in glob(text + '*')][state]

    class tabCompleter(object):
        """
            Description: This class is in charge of autocompleting the base commands in the osiris prompt, every time you add a new module in osiris you must add the new command to the list or execute the command reload_modules to add it automatic.
        """

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
    t.createListCompleter(
        ["clean", "exit", "banner", "exec", "restart", "upgrade", 'search', 'help', "sessions", "select",
         "reload_modules",
         ### start
                                            "use auxiliary/gather/oracle/weblogic/weblogic_detect",
                            "use auxiliary/gather/http/excalibur",
                            "use auxiliary/gather/http/netscaler_cookie_decrypt",
                            "use auxiliary/gather/http/method_enable",
                            "use auxiliary/gather/http/server_name",
                            "use auxiliary/gather/http/krakedin",
                            "use auxiliary/gather/http/http_security_headers_check",
                            "use auxiliary/gather/http/ip_gather",
                            "use auxiliary/scanner/ftp/ftp_anonymous",
                            "use auxiliary/scanner/ftp/ftp_bruteforce",
                            "use auxiliary/scanner/ftp/ftp_version",
                            "use auxiliary/scanner/rdp/cve-2019-0708-bluekeep-scan",
                            "use auxiliary/scanner/ssh/ssh_bruteforce",
                            "use auxiliary/scanner/ssh/ssh_version",
                            "use auxiliary/scanner/http/robots_txt",
                            "use auxiliary/scanner/http/ssl_info",
                            "use auxiliary/scanner/smb/smb_version",
                            "use auxiliary/scanner/smb/smb_ms17_010",
                            "use exploits/multi/handler"
                                        ### end
         ])
    readline.set_completer_delims('\t')
    readline.parse_and_bind("tab: complete")
    readline.set_completer(t.listCompleter)
