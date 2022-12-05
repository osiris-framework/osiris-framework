#!/usr/bin/env python3
# Project: osiris-framework
# Version 2.0
# Date: 02/12/2022

import os
import string
import re
import urllib
import json
import requests
from core.ModuleObtainer import obtainer
from utilities.Colors import color
from utilities.Messages import print_message
from utilities.Tools import tools
import random
from bs4 import BeautifulSoup as bs

print_message.name_module = __file__

info = {
    'author': 'Luis Eduardo Jacome Valencia',
    'date': '2022/12/01',
    'rank': 'Excellent',
    'path': 'auxiliary/gather/http/horus.py',
    'category': 'auxiliary',
    'license': 'GPL-2.0',
    'description': 'Get e-mail addresses about a company by dorks',
    'references': ['']
}
options = {
    'dork': ['Yes', 'Set a dork to search', ''],
    'dork_file': ['No', 'Set a dork to search', ''],
    'regexp': ['No', 'Set a dork to search', '^\S+@\S+\.\S+$'],
    'proxy': ['No', 'Set a proxy list', ''],
    'threads': ['No', 'Set threads', '5'],
    'delay': ['No', 'Set a delay between requests', '5'],
    'results': ['No', 'Save data in a folder', tools.temp_dir()['message'] + '/dorks_result.txt']
}

required = {
    'start_required': 'True',
    'check_required': 'False'
}

session = requests.Session()


class Horus():
    def __init__(self, _proxy_list, _search_engines_config, _dork, _configuration):
        self.dict_links_found = {}
        self._proxy_list = _proxy_list
        self._search_engines_config = _search_engines_config
        self._dork = _dork
        self._configuration = _configuration
        self.pag_start = 0
        self.pag_increment = 0
        self.pag_limit = 0

    def main_search(self):
        self.configuration_search_engines = [
            'https://%s/search?q=%s&num=1500&btnG=Search&pws=1'.format(self.get_random_host(), self._dork),
            'https://www.bing.com/search?q=%s&filt=rf&first=%s&FORM=PERE'.format(self._dork, self.paginator(1, 7, 77)),
            'http://search.yahoo.com/search?p=%s&ei=UTF-8&b=%s'.format(self._dork, self.paginator(1, 10, 471)),
            'https://www.ask.com/web?q=%s&page=%s&qid=1234&qo=pagination&qsrc=998'.format(self._dork,
                                                                                          self.paginator(1, 1, 6)),
            'http://search.lycos.com/web?q=%s&keyvol=%s&pn=%s'.format(self.dork, self.get_value_lycos(), self.paginator(1, 1, 24)),
            'http://us.yhs4.search.yahoo.com/yhs/search?p=%s&fr=goodsearch-yhsif&b=%s'.format(self.dork, self.paginator(1, 10, 561)),
            'http://www.gigablast.com/search?k3h=223119&s=22&rat=0&sc=1&ns=100&n=100&sites=&q=%s'.format(self._dork),
            'https://search.naver.com/search.naver?f=&fd=2&filetype=0&nso=so:r,a:all,p:all&query=%s&research_url=&sm=tab_nmr&start=%s&where=webkr'.format(self._dork, self.paginator(1, 10, 500)),
            'http://www.sogou.com/web?query=%s&cid=&s_from=result_up&page=%s&ie=utf8&dr=1'.format(self._dork, self.paginator(1, 1, 20)),
            'https://duckduckgo.com/?q=%s&t=h_&ia=web'.format(self._dork),
            'https://www.exalead.com/search/web/results/?q=%s&elements_per_page=10&start_index=%s'.format(self._dork, self.paginator(1, 10, 80)),
            'https://www.qwant.com/?q=index.php&t=%s'.format(self._dork)]
        for i in self._dork:
            if self._dork != '':
                for x in self.configuration_search_engines:
                    urllib.parse.quote()
                pass


    def extract_urls_from_search_engine(self, url_found):
        self.url_found = url_found
        soup = bs(self.url_found.content)
        web_links = soup.select('a')
        title_web_link = [web_link.text for web_link in web_links]
        src_web_links = [web_link['href'] for web_link in web_links]

        self.dict_links_found[title_web_link] = src_web_links

        return self.dict_links_found

        # Paginator for searching engines
    def paginator(self, pag_start, pag_increment, pag_limit):
        self.pag_start = pag_start
        self.pag_increment = pag_increment
        self.pag_limit = pag_limit

        while (self.pag_start <= self.pag_limit):
            self.pag_start += 1


        # LOGIC FOR PROCESSING THE PAGINATOR

    def configuration_google_search_engine(self):
        self.google_domains = ['www.google.com', 'www.google.co.uk', 'www.google.us',
                               'www.google.com.uy', 'www.google.co.uz', 'www.google.com.vc', 'www.google.co.ve',
                               'www.google.vg', 'www.google.co.vi', 'www.google.com.vn',
                               'www.google.vu', 'www.google.ws', 'www.google.co.za',
                               'www.google.co.zm', 'www.google.co.zw', 'www.google.ac', 'www.google.ad',
                               'www.google.com.om', 'www.google.ae', 'www.google.com.af',
                               'www.google.com.ag', 'www.google.com.ai', 'www.google.am',
                               'www.google.it.ao', 'www.google.com.ar', 'www.google.cat',
                               'www.google.as', 'www.google.at', 'www.google.com.au',
                               'www.google.az', 'www.google.ba', 'www.google.com.bd',
                               'www.google.be', 'www.google.bf', 'www.google.bg',
                               'www.google.com.bh', 'www.google.bi', 'www.google.bj',
                               'www.google.com.bn', 'www.google.com.bo', 'www.google.com.br',
                               'www.google.bs', 'www.google.co.bw', 'www.google.com.by',
                               'www.google.com.bz', 'www.google.ca', 'www.google.com.kh',
                               'www.google.cc', 'www.google.cd', 'www.google.cf',
                               'www.google.cn', 'www.google.com.co', 'www.google.co.nz',
                               'www.google.cg', 'www.google.ch', 'www.google.ci',
                               'www.google.co.ck', 'www.google.cl', 'www.google.cm',
                               'www.google.co.cr', 'www.google.com.cu', 'www.google.cv',
                               'www.google.cz', 'www.google.de', 'www.google.nu',
                               'www.google.dj', 'www.google.dk', 'www.google.dm',
                               'www.google.com.do', 'www.google.dz', 'www.google.no',
                               'www.google.com.ec', 'www.google.ee', 'www.google.com.eg',
                               'www.google.es', 'www.google.com.et', 'www.google.com.np',
                               'www.google.fi', 'www.google.com.fj', 'www.google.fm',
                               'www.google.fr', 'www.google.ga', 'www.google.nl',
                               'www.google.ge', 'www.google.gf', 'www.google.gg',
                               'www.google.com.gh', 'www.google.com.gi', 'www.google.nr',
                               'www.google.gl', 'www.google.gm', 'www.google.gp',
                               'www.google.gr', 'www.google.com.gt', 'www.google.com.ni',
                               'www.google.gy', 'www.google.com.hk', 'www.google.hn',
                               'www.google.hr', 'www.google.ht', 'www.google.com.ng',
                               'www.google.hu', 'www.google.co.id', 'www.google.iq',
                               'www.google.ie', 'www.google.co.il', 'www.google.com.nf',
                               'www.google.im', 'www.google.co.in', 'www.google.io',
                               'www.google.is', 'www.google.it', 'www.google.ne',
                               'www.google.je', 'www.google.com.jm', 'www.google.jo',
                               'www.google.co.jp', 'www.google.co.ke', 'www.google.com.na',
                               'www.google.ki', 'www.google.kg', 'www.google.co.kr',
                               'www.google.com.kw', 'www.google.kz', 'www.google.co.mz',
                               'www.google.la', 'www.google.com.lb', 'www.google.com.lc',
                               'www.google.li', 'www.google.lk', 'www.google.com.my',
                               'www.google.co.ls', 'www.google.lt', 'www.google.lu',
                               'www.google.lv', 'www.google.com.ly', 'www.google.com.mx',
                               'www.google.co.ma', 'www.google.md', 'www.google.me',
                               'www.google.mg', 'www.google.mk', 'www.google.mw',
                               'www.google.ml', 'www.google.mn', 'www.google.ms',
                               'www.google.com.mt', 'www.google.mu', 'www.google.mv',
                               'www.google.com.pa', 'www.google.com.pe', 'www.google.com.ph',
                               'www.google.com.pk', 'www.google.pn', 'www.google.com.pr',
                               'www.google.ps', 'www.google.pt', 'www.google.com.py',
                               'www.google.com.qa', 'www.google.ro', 'www.google.rs',
                               'www.google.ru', 'www.google.rw', 'www.google.com.sa',
                               'www.google.com.sb', 'www.google.sc', 'www.google.se',
                               'www.google.com.sg', 'www.google.sh', 'www.google.si',
                               'www.google.sk', 'www.google.com.sl', 'www.google.sn',
                               'www.google.sm', 'www.google.so', 'www.google.st',
                               'www.google.com.sv', 'www.google.td', 'www.google.tg',
                               'www.google.co.th', 'www.google.tk', 'www.google.tl',
                               'www.google.tm', 'www.google.to', 'www.google.com.tn',
                               'www.google.com.tr', 'www.google.tt', 'www.google.com.tw',
                               'www.google.co.tz', 'www.google.com.ua', 'www.google.co.ug'
                               ]
    # Important functions for the Engine Class
    def get_random_host(self):
        return random.choice(self.google_domains)

    def get_value_lycos(self):
        regex = r'(\s*<li class=\"rs-result\">.+\n)'
        regex2 = r'href=[\'\"]?([^\'\" >]+)'
        regex3 = r'keyvol=(.*)&'

        get_keyvol_laycos = session.get("https://search.lycos.com/web/?q=a").text

        filter_1 = re.findall(regex, get_keyvol_laycos)
        filter_2 = re.findall(regex2, filter_1[0])
        filter_3 = re.findall(regex3, filter_2[0])

        return filter_3[0]


    def _process_url_(self):


def exploit():
    """ main exploit function """
    try:
        print_message.start_execution()

        _dork = obtainer.options['rhost'][2]
        _dork_file = obtainer.options['rport'][2]
        _regexp = obtainer.options['webpath'][2]
        _proxy = obtainer.options['results'][2]
        _delay = obtainer.options['delay'][2]
        _threads = obtainer.options['results'][2]
        _results = obtainer.options['results'][2]

        if _dork_file != '':
            with open(_dork_file, encoding='utf-8') as _temp_dork_file:
                dork_readline = [line.rstrip('\n') for line in _temp_dork_file]


        # if _proxy != '':
          #  _proxy

        dork_readline.append(_dork)

        Horus(_proxy, 1, dork_readline, 1)

    except (AttributeError, TypeError) as e:
        print_message.execution_error("lgray", " You must enter the parameters!")
        return False

    print_message.end_execution()
