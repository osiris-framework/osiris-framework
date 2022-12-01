#!/usr/bin/env python3
# Project: osiris-framework
# Version 2.0
# Date: 27/01/2020

import os
import string
import re
import json
import requests
from core.ModuleObtainer import obtainer
from utilities.Colors import color
from utilities.Messages import print_message
from utilities.Tools import tools
from PyPDF2 import PdfReader
import docx2txt
from exiftool import ExifToolHelper
import shutil
from tqdm import tqdm
from bs4 import BeautifulSoup
from pathlib import Path

print_message.name_module = __file__

info = {
    'author': 'Luis Eduardo Jacome Valencia',
    'date': '2020/01/27',
    'rank': 'Excellent',
    'path': 'auxiliary/gather/http/excalibur.py',
    'category': 'auxiliary',
    'license': 'GPL-2.0',
    'description': 'Get information of Directory Listing (Apache/Nginx/Others) like valuable info',
    'references': ['']
}
options = {
    'rhost': ['Yes', 'Set target to attack', ''],
    'rport': ['No', 'Set port to attack', ''],
    'file_extensions': ['No', 'Set extensions to download and analyze', '.xls,.pdf,.xlsx,.docx,.doc,.txt'],
    'webpath': ['No', 'Set webpath where is the directory listing', '/'],
    'results': ['No', 'Save data in a folder', tools.temp_dir()['message'] + '/excalibur_results/']
}

required = {
    'start_required': 'True',
    'check_required': 'False'
}

find_words_files = ["password", "clave", "contraseña", "contraseñas", "claves", "passwords", "username", "usuario"]

session = requests.Session()


def onlyPDF():
    reader = PdfReader("test.docx")
    for page in reader.pages:
        for image in page.images:
            with open(image.name, "wb") as fp:
                fp.write(image.data)


def onlyDOCX():
    text = docx2txt.process("test.docx", "/tmp/consultor")


def get_metadata(filename):
    find_strings = re.compile(r"^(.*?)\..*")
    save_new_file = re.search(find_strings, filename).group(1)

    save_new_file_metadata = save_new_file + '_metadata_' + '.txt'

    with ExifToolHelper() as exiftool_file:
        for item_file in exiftool_file.get_metadata(filename):
            with open(save_new_file_metadata, 'w') as file_metadata:
                file_metadata.write(json.dumps(item_file))


def strings(filename, min=4):
    with open(filename, errors="ignore") as f:
        result = ""
        for c in f.read():
            if c in string.printable:
                result += c
                continue
            if len(result) >= min:
                yield result
            result = ""
        if len(result) >= min:  # catch result at EOF
            yield result


def find_words(text, search):
    """Find exact words"""
    original_text = text.split()
    search_text = search.split()

    found_word = 0

    for text_word in original_text:
        for search_word in search_text:
            if search_word.lower() == text_word.lower():
                found_word += 1

    if found_word == len(search_text):
        return True
    else:
        return False


def _get_recursive_links(base, _results_folder):
    f = requests.get(base)
    soup = BeautifulSoup(f.text)
    for anchor in soup.find_all('a'):
        href = anchor.get('href')
        if href.startswith('/'):
            print(color.color("blue", "[*] Skipping folder, looks like parent folder ->  " + href))
        elif href.endswith('/'):
            print(color.color("green", "[*] Crawl the next content -> [" + base + href + ']'))
            _get_recursive_links(base + href, _results_folder)
        else:
            try:
                url_extract_filename = base + href
                filename = _results_folder + href
                print(color.color("green", "[*] File found: -> " + href))
                print(color.color("green", "[*] Downloading the file found: -> [" + base + href + "]"))
                if tools.download_files_by_url(base + href, _results_folder + href)['code'] == 200:
                    print(color.color("green", "[*] Get metadata of the file -> [" + base + href + "]"))
                    get_metadata(filename)
                    strings_ = list(strings(filename))
                    for find_text in find_words_files:
                        match = find_words("".join(str(x) for x in strings_), find_text)
                        if match:
                            print(color.color("cyan", "[+] Interesting file found: -> " + str(filename)))
                            interesting_files = open('interesting_files.txt', 'a+')
                            interesting_files.write('\n' + str(filename))

            except Exception as inst:
                pass


def exploit():
    """ main exploit function """
    try:
        print(color.color("blue", "Remember, you need install exiftool before to make the auxiliary work properly."))
        print_message.start_execution()

        _rhost = obtainer.options['rhost'][2]
        _rport = obtainer.options['rport'][2]
        _webpath = obtainer.options['webpath'][2]
        _results_folder = obtainer.options['results'][2]

        if not os.path.exists(_results_folder):
            os.makedirs(_results_folder)

        _complete_url = _rhost + _rport + _webpath

        _get_recursive_links(_complete_url, _results_folder)

    except (AttributeError, TypeError) as e:
        print_message.execution_error("lgray", " You must enter the parameters!")
        return False

    print_message.end_execution()
