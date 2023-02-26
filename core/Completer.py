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
        ["clean", "exit", "banner", "exec", "restart", "upgrade", 'search', 'help', "sessions", "select", "back", "generator list", "generator help", "generator(ShellGenerator, target=, port=, platform=, type=, payload=)",
         "reload_modules", "generator(TemplateGenerator, target=, port=, platform=, type=, payload=)", "pattern_create ", "pattern_find ",
         ### start
                                            "use auxiliary/gather/ble/characteristics",
                            "use auxiliary/gather/ble/write",
                            "use auxiliary/gather/ble/discover",
                            "use auxiliary/gather/ble/write_notify",
                            "use auxiliary/gather/ble/read",
                            "use auxiliary/gather/oracle/weblogic/weblogic_detect",
                            "use auxiliary/gather/http/excalibur",
                            "use auxiliary/gather/http/captcha_solver",
                            "use auxiliary/gather/http/netscaler_cookie_decrypt",
                            "use auxiliary/gather/http/search_mails_365_api",
                            "use auxiliary/gather/http/method_enable",
                            "use auxiliary/gather/http/horus",
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
                            "use exploits/multi/handler",
                            "use exploits/http/oracle/weblogic/weblogic_wsat_deserealization_rce",
                            "use exploits/http/oracle/weblogic/weblogic_async_deserealization_rce",
                            "use exploits/http/uploadify/uploadify_arbitrary_upload",
                            "use exploits/http/geoserver/jt-jiffle/os_command_injection_cve_2022_24816",
                            "use exploits/linux/misc/cdata/onu4ferw/os_command_injection_cve_2022_29337",
                            "use exploits/linux/misc/cdata/onu4ferw/os_command_injection_cve_2021_44132",
                            "use exploits/linux/misc/tplink/tl_wr840n/os_command_injection_cve_2022_25060",
                            "use exploits/linux/misc/tplink/tl_wr840n/os_command_injection_cve_2023_XXXX",
                            "use exploits/linux/misc/tplink/tl_wr840n/os_command_injection_cve_2022_25064",
                            "use exploits/linux/misc/tplink/tl_wr840n/os_command_injection_cve_2022_25061",
                            "use exploits/linux/http/f5_icontrol_rce"
                                        ### end
         ])
    readline.set_completer_delims('\t')
    readline.parse_and_bind("tab: complete")
    readline.set_completer(t.listCompleter)
