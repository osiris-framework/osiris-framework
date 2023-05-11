#!/usr/bin/env python3
# Project: Osiris-Framework
# Version 1.337


from random import choice
from utilities.Colors import color
from importlib import reload
from utilities.Files import files


class Banner:
    def __init__(self):
        """
            Description: This class is in charge of managing the random banners at the start of the framework plus the count of the files in each of the folders to show the summary of auxiliary files, exploits, etc.
        """
        self.__banner = None
        self.__result = None
        self.__unfiltered_result = None
        self.__colors = ['gray', 'blue', 'green', 'yellow', 'cyan', 'cafe', 'black', 'lpurple', 'purple', 'green_ptrl']
        self.__author = '''
                                                    osiris-framework
                                                        version: 1.0
                                  Una forma facil de descubrir cosas
        '''

        self.__banner_1 = '''
                            ██████╗ ███████╗██╗██████╗ ██╗███████╗
                            ██╔═══██╗██╔════╝██║██╔══██╗██║██╔════╝
                            ██║   ██║███████╗██║██████╔╝██║███████╗
                            ██║   ██║╚════██║██║██╔══██╗██║╚════██║
                            ╚██████╔╝███████║██║██║  ██║██║███████║
                            ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═╝╚═╝╚══════╝                                                                                                                        
        '''

        self.__banner_2 = '''
            _______________                        |*\_/*|________
            |  ___________  |     .-.     .-.      ||_/-\_|______  |
            | |           | |    .****. .****.     | |           | |
            | |   0   0   | |    .*****.*****.     | |   0   0   | |
            | |     -     | |     .*********.      | |     -     | |
            | |   \___/   | |      .*******.       | |   \___/   | |
            | |___     ___| |       .*****.        | |___________| |
            |_____|\_/|_____|        .***.         |_______________|
              _|__|/ \|_|_.............*.............._|________|_
             / ********** \                          / ********** \\
           /  ************  \                      /  ************ \\
          --------------------                    --------------------
          '''

        self.__banner_3 = '''
                                      
                                      _ood>H&H&Z?#M#b-\.
                                  .\HMMMMMR?`\M6b."`' ''``v.
                               .. .MMMMMMMMMMHMMM#&.      ``~o.
                             .   ,HMMMMMMMMMM`' '           ?MP?.
                            . |MMMMMMMMMMM'                `"$b&\\
                           -  |MMMMHH##M'                     HMMH?
                          -   TTM|     >..                   \HMMMMH
                         :     |MM\,#-""$~b\.                `MMMMMM+
                        .       ``"H&#        -               &MMMMMM|
                        :            *\\v,#MHddc.             `9MMMMMb
                        .               MMMMMMMM##\             `"":HM
                        -          .  .HMMMMMMMMMMRo_.              |M
                        :             |MMMMMMMMMMMMMMMM#\           :M
                        -              `HMMMMMMMMMMMMMM'            |T
                        :               `*HMMMMMMMMMMM'             H'
                         :                MMMMMMMMMMM|             |T
                          ;               MMMMMMMM?'              ./
                           `              MMMMMMH'               ./'
                            -            |MMMH#'                 .
                             `           `MM*                . `
                               _          #M: .    .       .-'
                                  .          .,         .-'
                                     '-.-~ooHH__,,v~--`'

              __  __           __      __  __            ____  __                 __
             / / / /___ ______/ /__   / /_/ /_  ___     / __ \/ /___ _____  ___  / /_
            / /_/ / __ `/ ___/ //_/  / __/ __ \/ _ \   / /_/ / / __ `/ __ \/ _ \/ __/
           / __  / /_/ / /__/ ,<    / /_/ / / /  __/  / ____/ / /_/ / / / /  __/ /_
          /_/ /_/\__,_/\___/_/|_|   \__/_/ /_/\___/  /_/   /_/\__,_/_/ /_/\___/\__/
        '''

        self.__banner_4 = '''
                            PPPPP   IIIIIII   N    N
                            P   PP     I      NN   N   IDENTIFICATION
                            P   PP     I      N N  N
                            PPPPP      I      N  N N      PROGRAM
                            P          I      N   NN
                            P       IIIIIII   N    N

                            Strike a key when ready ...
        '''

        self.__banner_5 = '''
                                             __    _                                   
                                _wr""        "-q__                             
                             _dP                 9m_     
                           _#P                     9#_                         
                          d#@                       9#m                        
                         d##                         ###                       
                        J###                         ###L                      
                        {###K                       J###K                      
                        ]####K      ___aaa___      J####F                      
                    __gmM######_  w#P""   ""9#m  _d#####Mmw__                  
                 _g##############mZ_         __g##############m_               
               _d####M@PPPP@@M#######Mmp gm#########@@PPP9@M####m_             
              a###""          ,Z"#####@" '######"\\g         ""M##m            
             J#@"             0L  "*##     ##@"  J#              *#K           
             #"               `#    "_gmwgm_~    dF               `#_          
            7F                 "#_   ]#####F   _dK                 JE          
            ]                    *m__ ##### __g@"                   F          
                                   "PJ#####LP"                                 
             `                       0######_                      '           
                                   _0########_                                   
                 .               _d#####^#####m__              ,              
                  "*w_________am#####P"   ~9#####mw_________w*"                  
                      ""9@#####@M""           ""P@#####@M""
        '''

        self.__banner_6 = '''
                                     ___________
                                    ||         ||            _______
                                    || HACKED  ||           | _____ |
                                    ||         ||           ||_____||
                                    ||_________||           |  ___  |
                                    |  + + + +  |           | |___| |
                                        _|_|_   \           |       |
                                       (_____)   \          |       |
                                                  \    ___  |       |
                                           ______  \__/   \_|       |
                                          |   _  |      _/  |       |
                                          |  ( ) |     /    |_______|
                                          |___|__|    /        PLANET
                                               \_____/      
        '''

        self.__banner_7 = '''
                      _
                     | |
                     | |===( )   //////
                     |_|   |||  | o o|
                            ||| ( c  )                  ____
                             ||| \= /                  ||   \_
                              ||||||                   ||     |
                              ||||||                ...||__/|-"
                              ||||||             __|________|__
                                |||             |______________|
                                |||             || ||      || ||
                                |||             || ||      || ||
        ------------------------|||-------------||-||------||-||-------
                                |__>            || ||      || ||
        '''

        self.__banner_8 = '''
                                                      /^\\
                       L L               /   \\              L L
                    __/|/|_             /  .  \             _|\|\__
                   /_| [_[_\           /     .-\           /_]_]|_\\
                  /__\  __`-\_____    /    .    \    _____/-`__ /__\\
                 /___] /=@>  _   {>  /-.         \  <}   _  <@=\ [__\\
                /____/     /` `--/  /      .      \  \--` `\     \___\\
               /____/  \____/`-._> /               \ <_.-`\____/  \___\\
              /____/    /__/      /-._     .   _.-  \      \__\    \___\\
             /____/    /__/      /         .         \      \__\    \___\\
            |____/_  _/__/      /          .          \      \__\_  _\____|
             \__/_ ``_|_/      /      -._  .        _.-\      \_|_`` _\___/
               /__`-`__\      <_         `-;     HACKED_>      /__`-`_\\
                  `-`           `-._       ;       _.-`           `-`
                                    `-._   ;   _.-`
                                        `-._.-`

                     ------------------------------------------------
        '''

        self.__banner_9 = '''
                        ad8888888888ba
                        dP'         `"8b,
                        8  ,aaa,       "Y888a     ,aaaa,     ,aaa,  ,aa,
                        8  8' `8           "8baaaad""""baaaad""""baad""8b
                        8  8   8              """"      """"      ""    8b
                        8  8, ,8         ,aaaaaaaaaaaaaaaaaaaaaaaaddddd88P
                        8  `"""'       ,d8""
                        Yb,         ,ad8"    Access Granted
                         "Y8888888888P"
                        ------------------------------------------------
        '''

        self.__banner_10 = """
           :::::::::::''  ''::'      '::::::  `:::::::::::::'.:::::::::::::::
           :::::::::' :. :  :         ::::::  :::::::::::.:::':::::::::::::::
           ::::::::::  :   :::.       :::::::::::::..::::'     :::: : :::::::
           ::::::::    :':  "::'     '"::::::::::::: :'           '' ':::::::
           :'        : '   :  ::    .::::::::'    '                        .:
           :               :  .:: .::. ::::'                              :::
           :. .,.        :::  ':::::::::::.: '                      .:...::::
           :::::::.      '     .::::::: '''                         :: :::::.
           ::::::::            ':::::::::  '',            '    '   .:::::::::
           ::::::::.        :::::::::::: '':,:   '    :         ''' :::::::::
           ::::::::::      ::::::::::::'                        :::::::::::::
           : .::::::::.   .:''::::::::    '         ::   :   '::.::::::::::::
           :::::::::::::::. '  '::::::.  '  '     :::::.:.:.:.:.:::::::::::::
           :::::::::::::::: :     ':::::::::   ' ,:::::::::: : :.:'::::::::::
           ::::::::::::::::: '     :::::::::   . :'::::::::::::::' ':::::::::
           ::::::::::::::::::''   :::::::::: :' : ,:::::::::::'      ':::::::
           :::::::::::::::::'   .::::::::::::  ::::::::::::::::       :::::::
           :::::::::::::::::. .::::::::::::::::::::::::::::::::::::.'::::::::
           :::::::::::::::::' :::::::::::::::::::::::::::::::::::::::::::::::
           ::::::::::::::::::.:::::::::::::::::::::::::::::::::::::::::::::::
                                                      hacking the system ...
        """

        import utilities.Files
        from utilities.Files import files
        reload(utilities.Files)

        self.__num_auxiliary = str(self.count_result_files(files.count_sub_folder_files('modules/auxiliary')))
        self.__num_exploits = str(self.count_result_files(files.count_sub_folder_files('modules/exploits')))
        self.__num_payloads = str(self.count_result_files(files.count_sub_folder_files('modules/payloads')))

        self.__author += str(
            color.color("red", "\t\t\t[ ") + color.color(choice(self.__colors), self.__num_exploits) + color.color("red",
                                                                                                                " Exploits ") + "- " + color.color(
                choice(self.__colors), self.__num_auxiliary) + color.color("yellow", " Auxiliary ") + "- " + color.color(
                choice(self.__colors), self.__num_payloads) + color.color("cyan", " Payloads ") + color.color("red", "]"))

    def count_result_files(self, void):
        self.__unfiltered_result = []
        self.__result = []

        for first_result in files.count_sub_folder_files_result:
            for second_result in first_result:
                self.__unfiltered_result.append(''.join(second_result))
                for final_result in self.__unfiltered_result:
                    if final_result.endswith('.pyc') or final_result.startswith('__init__') or final_result.startswith(
                            'gen_payload') or not final_result.endswith('.py'):
                        self.__unfiltered_result.remove(final_result)
        for filt_result in self.__unfiltered_result:
            self.__result.append(filt_result.split('.')[0])

        return len(self.__result)

    def banner_welcome(self):
        self.__banner = choice([self.__banner_1, self.__banner_2, self.__banner_3, self.__banner_4, self.__banner_5, self.__banner_6, self.__banner_7, self.__banner_8, self.__banner_9, self.__banner_10])
        print(color.color(choice(self.__colors),self.__banner))
        print(self.__author)


banner = Banner()
