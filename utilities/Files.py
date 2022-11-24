#!/usr/bin/env python3
# Project: osiris-framework
# Author: Samir Sanchez Garnica @sasaga92
# Version 1.0
# Date: 14/11/2022
import shutil
from os import getcwd, walk, path, listdir, rename, remove, chdir
from getpass import getuser
from importlib import reload
from os import walk
import re
from utilities.Colors import color

class Files(object):
    """
        Description: Class in charge of the management of the files inside osiris, for example listing the .py files in the folders corresponding to their modules.
    """
    def __init__(self):
        self.__files_list = []
        self.__python_files = []
        self.__directory_list = []


    def count_sub_folder_files(self, thePath=str(getcwd())):
        self.count_sub_folder_files_result = []
        for dir, subdir, files in walk(thePath):
            self.count_sub_folder_files_result.append(files)
            if len(files) == 0:
                self.count_sub_folder_files_result.remove(files)

        return len(self.count_sub_folder_files_result)

    def count_files(self, thePath=str(getcwd()), hidden=True):
        for all_element in listdir(thePath):
            self.__files_list.append(all_element)
            for directories in self.__files_list:
                if path.isdir(thePath + '/' + directories):
                    self.__files_list.remove(directories)

        if hidden:
            return len(self.__files_list)
        self.__files_list = [self.__files_list.split(".")[0] for self.__files_list in self.__files_list]
        for hidden in self.__files_list:
            if len(hidden) == 0:
                self.__files_list.remove(hidden)
                for hidden in self.__files_list:
                    if len(hidden) == 0:
                        self.__files_list.remove(hidden)

        return len(self.__files_list)

    def count_python_files(self, thePath=str(getcwd()), hidden=True):
        for dir, subdir, files in walk(thePath):
            for element in files:
                if element.endswith('.py'):
                    self.__python_files.append(element)
        return len(self.__python_files)

    def count_dirs(self, thePath=str(getcwd()), hidden=True):
        for all_element in listdir(thePath):
            self.__directory_list.append(all_element)
            for files in self.__directory_list:
                if path.isfile(thePath + '/' + files):
                    self.__directory_list.remove(files)

        if hidden:
            return len(self.__directory_list)

        self.__directory_list = [self.__directory_list.split(".")[0] for self.__directory_list in self.__directory_list]
        for hidden in self.__directory_list:
            if len(hidden) == 0:
                self.__directory_list.remove(hidden)
                for hidden in self.__directory_list:
                    if len(hidden) == 0:
                        self.__directory_list.remove(hidden)

        return len(self.__directory_list)

    def copy(self, source, dest):
        if type(dest) == list:
            if type(source) == list:
                try:
                    for i in range(0, 10000000):
                        if path.isfile(source[i]):
                            shutil.copy(source[i], dest[i])
                        else:
                            shutil.copytree(source[i], dest[i]+ '/' + source[i])
                except IndexError:
                    pass
            else:
                for src in source:
                    if path.isfile(src):
                        shutil.copy(src, dest)
                    else:
                        shutil.copytree(src, dest + '/' + src)
        else:
            if path.isfile(source):
                shutil.copy(source, dest)
            else:
                shutil.copytree(source, dest + '/' + source)

    def touch(self, name):
        self.__file = open(name, 'w')
        self.__file.close()

    def rename(self, src, dst):
        rename(src, dst)

    def rm(self, thePath):
        if path.isfile(thePath):
            remove(thePath)
        else:
            shutil.rmtree(thePath)

    def ls(self, dir=str(getcwd())):
        for i in listdir(dir):
            print(i)

    def cd(self, thePath):
        chdir(thePath)

    def pwd(self):
        print(getcwd())


class UpdateModuleDB(object):
    """
        Description: Class in charge of updating the new commands for the modules added to the osiris folders.
    """
    def update_path_module(self, name_folder):
        import utilities.Files
        reload(utilities.Files)
        self.__path_finish = ''

        from utilities.Files import files
        self.__cant_modules = files.count_sub_folder_files(name_folder)
        self.__unfiltered_result = []
        self.__result = []

        for first_result in files.count_sub_folder_files_result:
            for second_result in first_result:
                self.__unfiltered_result.append(''.join(second_result))
                for final_result in self.__unfiltered_result:
                    if final_result.endswith('.pyc') or final_result.startswith(
                            '__init__') or not final_result.endswith('.py'):
                        self.__unfiltered_result.remove(final_result)
        for filt_result in self.__unfiltered_result:
            self.__result.append(filt_result.split('.')[0])

        self.__cant_modules = len(self.__result)

        try:
            for i in range(0, int(self.__cant_modules)):
                for root, dirs, files in walk(name_folder):
                    if self.__result[i] + '.py' in files:
                        self.__thePath = path.join(root, self.__result[i])
                        self.__thePath = self.__thePath.split('/')
                        self.__path_first_index = self.__thePath[0]
                        self.__thePath.remove(self.__path_first_index)
                        self.__thePath = '/'.join(self.__thePath)
                        self.__path_finish += "                            \"use " + self.__thePath + "\"" + ',' + '\n'
                        print(color.color("yellow", "[!] Loading {} ".format(name_folder) + color.color("green", "{}".format(self.__thePath))))
        except IndexError:
            pass
        except ImportError:
            pass
        return self.__path_finish[:-1]

    def processor_update_module(self, path_file_config):
        self.__text = '\"'
        self.__text += self.update_path_module('modules/auxiliary')
        self.__text += '\n'
        self.__text += self.update_path_module('modules/exploits')
        self.__text = self.__text[1:-1]

        _new = '''### start
                ''' + self.__text + '''
                                        ### end'''

        with open(path_file_config, 'r+') as _f:
            self.__data = _f.read()
            _f.seek(0)
            _f.truncate()
            patter = re.compile('### start.*?### end', re.I | re.S)
            self.__clean_text = patter.sub(_new, self.__data)
            _f.write(self.__clean_text)

files = Files()
update_modules = UpdateModuleDB()