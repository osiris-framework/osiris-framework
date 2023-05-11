#!/usr/bin/env python3
# Project: Osiris-Framework
# Version 1.337

import asyncio
import re
import io
import openpyxl
import aiohttp
import signal
import random
import zipfile
import PyPDF2
from requests_html import AsyncHTMLSession
from selenium import webdriver
from core.ModuleObtainer import obtainer
from utilities.Colors import color
from utilities.Messages import print_message
import urllib.parse
from bs4 import BeautifulSoup
import urllib.parse
from utilities.Tools import tools

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
    'dork_file': ['No', 'Set a dork list to search. You can combine with the dork option as well.', ''],
    'engine': ['Yes', 'Set the engine for searching the dorks [google, bing, ask, lycos, duckduckgo, sogou, naver, exalead, qwant, gigablast, yahoo, yandex, baidu] or [all]', 'all'],
    'company': ['Yes', 'Set the main domain for filtering into the websites, i.e example.com.co', ''],
    'proxy': ['No', 'Set a proxy list (Not working yet!)', ''],
    'delay': ['No', 'Set a delay between requests', '0'],
    'results': ['No', 'Save data in a folder', tools.temp_dir()['message'] + '/dorks_result.txt']
}

required = {
    'start_required': 'True',
    'check_required': 'False'
}

headers = {
    'User-Agent': 'Mozilla'
}

pattern = r'https?://(?!www.example.com/).*'

# Trash links
blacklist = [
    'https://fonts.example.com/',
    'https://map.example.com/',
    'https://maps.example.com/',
    'https://policies.example.com/',
]

# Rules for each search engine
SEARCH_ENGINES = {
    "google": {
        "or": "|",
        "minus": "-",
        "site": "site",
        "intext": "intext",
        "filetype": "ext"
    },
    "bing": {
        "or": "OR",
        "minus": "-",
        "site": "site",
        "intext": "intext",
        "filetype": "filetype"
    },
    "ask": {
        "or": "|",
        "minus": "-",
        "site": "site",
        "intext": "intext",
        "filetype": "filetype"
    },
    "lycos": {
        "or": "|",
        "minus": "-",
        "site": "site",
        "intext": "intext",
        "filetype": "filetype"
    },
    "duckduckgo": {
        "or": "OR",
        "minus": "-",
        "site": "site",
        "intext": "intext",
        "filetype": "filetype"
    },
    "sogou": {
        "or": "|",
        "minus": "-",
        "site": "site",
        "intext": "intext",
        "filetype": "filetype"
    },
    "naver": {
        "or": "|",
        "minus": "-",
        "site": "site",
        "intext": "intext",
        "filetype": "filetype"
    },
    "exalead": {
        "or": "OR",
        "minus": "-",
        "site": "site",
        "intext": "intext",
        "filetype": "filetype"
    },
    "qwant": {
        "or": "OR",
        "minus": "-",
        "site": "site",
        "intext": "intext",
        "filetype": "filetype"
    },
    "gigablast": {
        "or": "OR",
        "minus": "-",
        "site": "site",
        "intext": "intext",
        "filetype": "filetype"
    },
    "yahoo": {
        "or": "OR",
        "minus": "-",
        "site": "site",
        "intext": "intext",
        "filetype": "filetype"
    },
    "yandex": {
        "or": "OR",
        "minus": "-",
        "site": "site",
        "intext": "intext",
        "filetype": "filetype"
    },
    "baidu": {
        "or": "|",
        "minus": "-",
        "site": "site",
        "intext": "intext",
        "filetype": "filetype"
    },
    "all": {
        "google": {
            "or": "|",
            "minus": "-",
            "site": "site",
            "intext": "intext",
            "filetype": "ext"
        },
        "bing": {
            "or": "OR",
            "minus": "-",
            "site": "site",
            "intext": "intext",
            "filetype": "filetype"
        },
        "ask": {
            "or": "|",
            "minus": "-",
            "site": "site",
            "intext": "intext",
            "filetype": "filetype"
        },
        "lycos": {
            "or": "|",
            "minus": "-",
            "site": "site",
            "intext": "intext",
            "filetype": "filetype"
        },
        "duckduckgo": {
            "or": "OR",
            "minus": "-",
            "site": "site",
            "intext": "intext",
            "filetype": "filetype"
        },
        "sogou": {
            "or": "|",
            "minus": "-",
            "site": "site",
            "intext": "intext",
            "filetype": "filetype"
        },
        "naver": {
            "or": "|",
            "minus": "-",
            "site": "site",
            "intext": "intext",
            "filetype": "filetype"
        },
        "exalead": {
            "or": "OR",
            "minus": "-",
            "site": "site",
            "intext": "intext",
            "filetype": "filetype"
        },
        "qwant": {
            "or": "OR",
            "minus": "-",
            "site": "site",
            "intext": "intext",
            "filetype": "filetype"
        },
        "gigablast": {
            "or": "OR",
            "minus": "-",
            "site": "site",
            "intext": "intext",
            "filetype": "filetype"
        },
        "yahoo": {
            "or": "OR",
            "minus": "-",
            "site": "site",
            "intext": "intext",
            "filetype": "filetype"
        },
        "yandex": {
            "or": "OR",
            "minus": "-",
            "site": "site",
            "intext": "intext",
            "filetype": "filetype"
        },
        "baidu": {
            "or": "|",
            "minus": "-",
            "site": "site",
            "intext": "intext",
            "filetype": "filetype"
}
}
}

google_domains = ['www.google.com', 'www.google.co.uk', 'www.google.us',
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

class Horus():
    def __init__(self, dork, results, company, delay, search_engine_option):
        self.dork = dork  # It's a json file
        self.results = results
        self.company = company
        self.delay = delay
        self.search_engine_option = search_engine_option
        self.session_with_js = AsyncHTMLSession()

        self.list_emails = set()
    def __call__(self):
        asyncio.run(self.main())
        self.save_data()
    def save_data(self):
        with open(self.results, "w") as f:
            f.write('\n' + str(self.list_emails))
    async def get_page_with_js(session, url):
        link_found = await session.get(url)
        link_render = await link_found.html.arender(timeout=20)

        return link_found.text

    # Function to replace ASCII CHARACTERS IN WEBSITES
    async def convert_special_characters(self, text):
        text = text.replace("&amp;", "y")
        text = text.replace("&#064;", "@")
        text = text.replace("&#046", ".")
        text = text.replace("&#045", "-")
        return text

    def get_random_host(self):
        return random.choice(google_domains)

    async def fetch_page(self, url):
        try:

            self.browser.get(url)
            self.url = url
            await asyncio.sleep(self.delay)

            content_loaded = self.browser.execute_script("return document.getElementById('page-content') != null")

            if content_loaded:
                self.browser.implicitly_wait(10)
                print("ENTRO AQUIII1")
                page_source = self.browser.page_source
                page_source = await self.convert_special_characters(page_source)

                return page_source
            else:
                async with self.session.get(self.url, headers=headers) as response:
                    page_content = await response.text()#await response.read()
                    page_content = await self.convert_special_characters(page_content)


                    return page_content
        except:
            pass

    # For checking Facebook URLs
    async def extract_url_until_id(self, url):
        print("The url is " + url)
        regex = r"^https:\/\/.*\.facebook\.com\/([^\/]*)\/photos\/(.*)\/(\d*)"
        match = re.match(regex, url)

        if match:
            print(match)
            return match.group(0)

        return None


    async def remove_trash_from_facebook_url(self, url):
        regex = r"[^0-9]+"
        url = re.sub(regex, "", url)
        return await url

    async def check_url_inside_of(self, url):
        try:
            pattern_remove_trash = r"https://[^&]*"

            match = re.search(pattern_remove_trash, url)

            return match[0]
        except:
            pass

    async def get_file_encoding(self, content):
        for encoding in ('utf-8', 'iso-8859-1', 'windows-1252', 'iso-8859-15'):
            try:
                content.decode(encoding)
                return encoding
            except UnicodeDecodeError:
                continue

        return None


    async def scrape_xlsx(self, url):
        emails = []
        email_pattern = r"[\w\.-]+@[\w\.-]+\.[\w\.-]+"
        async with self.session.get(urllib.parse.unquote(url)) as response:
            content = await response.read()
            file = io.BytesIO(content)
            is_xlsx = zipfile.is_zipfile(file)
            if is_xlsx:
                workbook = openpyxl.load_workbook(file)
                worksheet = workbook.worksheets[0]
                print(worksheet)
                for row in worksheet.rows:
                    for cell in row:
                        data = str(cell.value)
                        emails_workbook = re.findall(email_pattern, data, re.MULTILINE | re.IGNORECASE)
                        emails += emails_workbook
                        self.list_emails.add(emails)
            else:
                print("It's not a XLSX file valid.")
        return emails
    async def scrape_pdf(self, url):
        async with self.session.get(url) as response:
            content = await response.read()

        encoding = await self.get_file_encoding(content)
        if encoding is not None:
            content = content.decode(encoding)

        file = io.BytesIO(content)

        reader = PyPDF2.PdfFileReader(file)

        emails = []
        for page in reader.pages:
            text = page.extractText()

            matches = re.search(r"[a-zA-Z0-9_.+-]+@" + self.company, text, re.MULTILINE | re.IGNORECASE)
            if matches:

                print(matches)
                self.list_emails.add(matches[0])

    async def find_emails(self, url):
        try:
            pattern_facebook = r"https://.*\.facebook.com/[a-zA-Z0-9_]+/[a-zA-Z0-9_]+/.*$"
            if 'uddg' in url:
                pattern_duckduckgo = r'https([^&]*)'
                match_duckduckgo = re.search(pattern_duckduckgo, url)
                url = match_duckduckgo.group(0)

            if re.match(pattern_facebook, url):
                print("ENTROOOOOOOO")
                url = await self.extract_url_until_id(url)

            print(" [+] Link found: " + url)

            if '.xlsx' in url or '.xls' in url:
                await self.scrape_xlsx(url)
            elif '.pdf' in url:
                await self.scrape_pdf(url)
            else:
                page_content = await self.fetch_page(url)
                emails = re.search(r"[a-zA-Z0-9_.+-]+@" + self.company, page_content, re.MULTILINE | re.IGNORECASE)
                if emails:
                    self.list_emails.add(emails[0])

            print(self.list_emails)

        except Exception as e:
            print(e)
            pass

    async def is_valid_url(self, url):
        pattern = "^[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"

        return re.match(url, pattern)

    async def search(self, engine, page):
        if engine == "google":
            self.search_url = f"https://{self.get_random_host()}/search?q={self.dork}&start={page * 10}"
        elif engine == "bing":
            self.search_url = f"https://www.bing.com/search?q={self.dork}&first={page * 10 + 1}"
        elif engine == "ask":
            self.search_url = f"https://www.ask.com/web?q={self.dork}&page={page + 1}"
        elif engine == "lycos":
            self.search_url = f"https://search.lycos.com/web/?q={self.dork}&b={page * 10 + 1}"
        elif engine == "duckduckgo":
            self.search_url = f"https://duckduckgo.com/html/?q={self.dork}&s={(page-1)*10}"
        elif engine == "sogou":
            self.search_url = f"https://www.sogou.com/web?query={self.dork}&page={page}"
        elif engine == "naver":
            self.search_url = f"https://search.naver.com/search.naver?where=nexearch&query={self.dork}&start={(page-1)*10+1}"
        elif engine == "exalead":
            self.search_url = f"https://www.exalead.com/search/web/results/?q={self.dork}&elements_per_page=10&start_index={(page-1)*10}"
        elif engine == "qwant":
            self.search_url = f"https://www.qwant.com/?q={self.dork}&page={page}"
        elif engine == "gigablast":
            self.search_url = f"https://www.gigablast.com/search?q={self.dork}&n=10&s={(page-1)*10}"
        elif engine == "yahoo":
            self.search_url = f"https://search.yahoo.com/search?p={self.dork}&b={(page-1)*10+1}"
        elif engine == "yandex":
            self.search_url = f"https://yandex.com/search/?text={self.dork}&p={page}"
        elif engine == "baidu":
            self.search_url = f"https://www.baidu.com/s?wd={self.dork}&pn={page}"
        else:
            raise ValueError(f"Unrecognized search engine: {engine}")


        search_results = await self.fetch_page(self.search_url)
        ##if response.status_code == 200:
        ## if "Content-Encoding" in response.headers and response.headers["Content-Encoding"] == "gzip":
        ##  html_content = gzip.decode(response.content)
        ##else:
        ##  html_content = response.content

        soup = BeautifulSoup(search_results, "html.parser")

        links = []
        for link in soup.find_all("a"):
            href = link.get("href")
            if href:
                links.append(href)

        print(f"Links from {engine} (page {page + 1}):")
        for link in links:
            if not re.fullmatch(pattern, link) and link not in blacklist:
                link_google_filtered = await self.check_url_inside_of(link)
                print("Original link" + str(link) + " vs Filtered link:" + str(link_google_filtered))
                await self.find_emails(link_google_filtered) if '/url?q=' in link else await self.find_emails(link)
        else:
            pass
    async def main(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        self.browser = webdriver.Chrome(executable_path=r'/opt/google/chrome/chromedrive',options=chrome_options)
        # Crear una sesión de aiohttp
        async with aiohttp.ClientSession() as self.session:
            for page in range(0,1):
                if self.search_engine_option == "all":
                    await self.search("google", page)

                    await self.search("bing", page)

                    await self.search("ask", page)

                    await self.search("lycos", page)

                    await self.search("duckduckgo", page)

                    await self.search("sogou", page)

                    await self.search("naver", page)

                    await self.search("exalead", page)

                    await self.search("qwant", page)

                    await self.search("gigablast", page)

                    await self.search("yahoo", page)

                    await self.search("yandex", page)

                    await self.search("baidu", page)
                else:
                    await self.search(self.search_engine_option, page)

                page = page + 1

            dork_results = open(self.results, 'a+')
            dork_results.write('\n' + str(self.list_emails))
            self.browser.quit()

def replace_example_to_company(replaced_query: str, company: str) -> str:
    return replaced_query.replace("example.com.co", company)
async def search(query: str, engine: str, company: str) -> str:
    if engine == "all":
        for search_engine, operators in SEARCH_ENGINES["all"].items():
            replaced_query = await replace_operators_search_engine(query, search_engine)

    else:
        replaced_query = await replace_operators_search_engine(query, engine)


    return replaced_query
async def replace_operators_search_engine(query: str, search_engine: str) -> str:
    if search_engine not in SEARCH_ENGINES:
        raise ValueError(f"{search_engine} is not a supported search engine.")

    engine = SEARCH_ENGINES[search_engine]

    query = re.sub(r"\b(or)\b", engine["or"], query, flags=re.IGNORECASE)
    query = re.sub(r"\b(minus)\b", engine["minus"], query, flags=re.IGNORECASE)
    query = query.replace("site", engine["site"])
    query = query.replace("intext", engine["intext"])
    query = query.replace("filetype", engine["filetype"])
    return query

def exploit():
    """ main exploit function """
    try:
        print_message.start_execution()

        dork_readline = []

        _dork = obtainer.options['dork'][2]
        _dork_file = obtainer.options['dork_file'][2]
        _proxy = obtainer.options['proxy'][2]
        _engine = obtainer.options['engine'][2]
        _results = obtainer.options['results'][2]
        company = obtainer.options['company'][2]
        delay = int(obtainer.options['delay'][2])

        if _dork_file != '':
            with open(_dork_file, encoding='utf-8') as _temp_dork_file:
                for line in _temp_dork_file:
                    #dork_readline = line.rstrip('\n')
                    _get_dork_file = asyncio.run(search(line, _engine, company)) # await search(line, _engine)
        # if _proxy != '':
        #  _proxyprint(asyncio.run(transform_operator("bing", "|")))
                    dork_readline.append(_get_dork_file.replace("\n", ""))

        dork_readline.append(_dork)
        dork_readline_filtered = [replace_example_to_company(x, company) for x in dork_readline]

        for dork_one_by_one in dork_readline_filtered:
            print(f"Consulta para {_engine}: {dork_one_by_one}")
            horus_instance = Horus(dork_one_by_one, _results, company, delay, _engine)
            horus_instance()
            signal.signal(signal.SIGINT, horus_instance)


    except (AttributeError, TypeError) as e:
        print_message.execution_error("lgray", " You must enter the parameters!")
        return False

    print_message.end_execution()


# Things to do
# - Put the other search engines
# - Regex for mail addresses in 183 line
# - Paginator

"""
--- GOOGLE ---
"palabra clave": Busca la palabra clave exacta entre comillas.
-palabra clave: Excluye la palabra clave de los resultados de búsqueda.
site:sitio.com: Busca en el sitio especificado.
filetype:extensión: Busca solo archivos con la extensión especificada.
related:sitio.com: Muestra sitios relacionados con el sitio especificado.
link:sitio.com: Muestra enlaces que apuntan al sitio especificado.
inurl:palabra clave: Busca en las URLs de los resultados de búsqueda.
intitle:palabra clave: Busca en los títulos de los resultados de búsqueda.
intext:palabra clave: Busca en el contenido de los resultados de búsqueda.
allintitle:palabra clave 1 palabra clave 2: Busca en los títulos de los resultados de búsqueda todas las palabras clave especificadas.
define:palabra clave: Muestra la definición de la palabra clave especificada.
weather:ciudad: Muestra el pronóstico del tiempo en la ciudad especificada.
stocks:símbolo: Muestra las cotizaciones de las acciones del símbolo especificado.
book:título: Muestra información sobre el libro con el título especificado.
movie:título: Muestra información sobre la película con el título especificado.
"""
"""
--- BING ---
"palabra clave": Busca la palabra clave exacta entre comillas.
-palabra clave: Excluye la palabra clave de los resultados de búsqueda.
site:sitio.com: Busca en el sitio especificado.
filetype:extensión: Busca solo archivos con la extensión especificada.
related:sitio.com: Muestra sitios relacionados con el sitio especificado.
link:sitio.com: Muestra enlaces que apuntan al sitio especificado.
inurl:palabra clave: Busca en las URLs de los resultados de búsqueda.
intitle:palabra clave: Busca en los títulos de los resultados de búsqueda.
intext:palabra clave: Busca en el contenido de los resultados de búsqueda.
allintitle:palabra clave 1 palabra clave 2: Busca en los títulos de los resultados de búsqueda todas las palabras clave especificadas.
"""
"""
--- ASK ---
"palabra clave": Busca la palabra clave exacta entre comillas.
-palabra clave: Excluye la palabra clave de los resultados de búsqueda.
site:sitio.com: Busca en el sitio especificado.
filetype:extensión: Busca solo archivos con la extensión especificada.
related:sitio.com: Muestra sitios relacionados con el sitio especificado.
link:sitio.com: Muestra enlaces que apuntan al sitio especificado.
inurl:palabra clave: Busca en las URLs de los resultados de búsqueda.
intitle:palabra clave: Busca en los títulos de los resultados de búsqueda.
intext:palabra clave: Busca en el contenido de los resultados de búsqueda.
allintitle:palabra clave 1 palabra clave 2: Busca en los títulos de los resultados de búsqueda todas las palabras clave especificadas.
"""
"""
--- LYCOS ---
"palabra clave": Busca la palabra clave exacta entre comillas.
-palabra clave: Excluye la palabra clave de los resultados de búsqueda.
site:sitio.com: Busca en el sitio especificado.
filetype:extensión: Busca solo archivos con la extensión especificada.
related:sitio.com: Muestra sitios relacionados con el sitio especificado.
link:sitio.com: Muestra enlaces que apuntan al sitio especificado.
inurl:palabra clave: Busca en las URLs de los resultados de búsqueda.
intitle:palabra clave: Busca en los títulos de los resultados de búsqueda.
intext:palabra clave: Busca en el contenido de los resultados de búsqueda.
allintitle:palabra clave 1 palabra clave 2: Busca en los títulos de los resultados de búsqueda todas las palabras clave especificadas.
"""
"""
--- LYCOS ---
"palabra clave": Busca la palabra clave exacta entre comillas.
-palabra clave: Excluye la palabra clave de los resultados de búsqueda.
site:sitio.com: Busca en el sitio especificado.
filetype:extensión: Busca solo archivos con la extensión especificada.
related:sitio.com: Muestra sitios relacionados con el sitio especificado.
link:sitio.com: Muestra enlaces que apuntan al sitio especificado.
inurl:palabra clave: Busca en las URLs de los resultados de búsqueda.
intitle:palabra clave: Busca en los títulos de los resultados de búsqueda.
intext:palabra clave: Busca en el contenido de los resultados de búsqueda.
allintitle:palabra clave 1 palabra clave 2: Busca en los títulos de los resultados de búsqueda todas las palabras clave especificadas.
"""
"""
--- DUCKDUCKGO ---
"palabra clave": Busca la palabra clave exacta entre comillas.
-palabra clave: Excluye la palabra clave de los resultados de búsqueda.
site:sitio.com: Busca en el sitio especificado.
filetype:extensión: Busca solo archivos con la extensión especificada.
related:sitio.com: Muestra sitios relacionados con el sitio especificado.
link:sitio.com: Muestra enlaces que apuntan al sitio especificado.
inurl:palabra clave: Busca en las URLs de los resultados de búsqueda.
intitle:palabra clave: Busca en los títulos de los resultados de búsqueda.
intext:palabra clave: Busca en el contenido de los resultados de búsqueda.
allintitle:palabra clave 1 palabra clave 2: Busca en los títulos de los resultados de búsqueda todas las palabras clave especificadas.
"""
"""
--- SOGOU ---
"palabra clave": Busca la palabra clave exacta entre comillas.
-palabra clave: Excluye la palabra clave de los resultados de búsqueda.
site:sitio.com: Busca en el sitio especificado.
filetype:extensión: Busca solo archivos con la extensión especificada.
related:sitio.com: Muestra sitios relacionados con el sitio especificado.
link:sitio.com: Muestra enlaces que apuntan al sitio especificado.
inurl:palabra clave: Busca en las URLs de los resultados de búsqueda.
intitle:palabra clave: Busca en los títulos de los resultados de búsqueda.
intext:palabra clave: Busca en el contenido de los resultados de búsqueda.
allintitle:palabra clave 1 palabra clave 2: Busca en los títulos de los resultados de búsqueda todas las palabras clave especificadas.
"""
"""
--- NAVER ---
"palabra clave": Busca la palabra clave exacta entre comillas.
-palabra clave: Excluye la palabra clave de los resultados de búsqueda.
site:sitio.com: Busca en el sitio especificado.
filetype:extensión: Busca solo archivos con la extensión especificada.
related:sitio.com: Muestra sitios relacionados con el sitio especificado.
link:sitio.com: Muestra enlaces que apuntan al sitio especificado.
inurl:palabra clave: Busca en las URLs de los resultados de búsqueda.
intitle:palabra clave: Busca en los títulos de los resultados de búsqueda.
intext:palabra clave: Busca en el contenido de los resultados de búsqueda.
allintitle:palabra clave 1 palabra clave 2: Busca en los títulos de los resultados de búsqueda todas las palabras clave especificadas.
"""
"""
--- EXALEAD ---
"palabra clave": Busca la palabra clave exacta entre comillas.
-palabra clave: Excluye la palabra clave de los resultados de búsqueda.
site:sitio.com: Busca en el sitio especificado.
filetype:extensión: Busca solo archivos con la extensión especificada.
related:sitio.com: Muestra sitios relacionados con el sitio especificado.
link:sitio.com: Muestra enlaces que apuntan al sitio especificado.
inurl:palabra clave: Busca en las URLs de los resultados de búsqueda.
intitle:palabra clave: Busca en los títulos de los resultados de búsqueda.
intext:palabra clave: Busca en el contenido de los resultados de búsqueda.
allintitle:palabra clave 1 palabra clave 2: Busca en los títulos de los resultados de búsqueda todas las palabras clave especificadas.
"""
"""
--- QWANT ---
"palabra clave": Busca la palabra clave exacta entre comillas.
-palabra clave: Excluye la palabra clave de los resultados de búsqueda.
site:sitio.com: Busca en el sitio especificado.
filetype:extensión: Busca solo archivos con la extensión especificada.
related:sitio.com: Muestra sitios relacionados con el sitio especificado.
link:sitio.com: Muestra enlaces que apuntan al sitio especificado.
inurl:palabra clave: Busca en las URLs de los resultados de búsqueda.
intitle:palabra clave: Busca en los títulos de los resultados de búsqueda.
intext:palabra clave: Busca en el contenido de los resultados de búsqueda.
allintitle:palabra clave 1 palabra clave 2: Busca en los títulos de los resultados de búsqueda todas las palabras clave especificadas.
"""
"""
--- GIGABLAST ---
"palabra clave": Busca la palabra clave exacta entre comillas.
-palabra clave: Excluye la palabra clave de los resultados de búsqueda.
site:sitio.com: Busca en el sitio especificado.
filetype:extensión: Busca solo archivos con la extensión especificada.
related:sitio.com: Muestra sitios relacionados con el sitio especificado.
link:sitio.com: Muestra enlaces que apuntan al sitio especificado.
inurl:palabra clave: Busca en las URLs de los resultados de búsqueda.
intitle:palabra clave: Busca en los títulos de los resultados de búsqueda.
intext:palabra clave: Busca en el contenido de los resultados de búsqueda.
allintitle:palabra clave 1 palabra clave 2: Busca en los títulos de los resultados de búsqueda todas las palabras clave especificadas.
"""
"""
--- SEARCH YAHOO ---
"palabra clave": Busca la palabra clave exacta entre comillas.
-palabra clave: Excluye la palabra clave de los resultados de búsqueda.
site:sitio.com: Busca en el sitio especificado.
filetype:extensión: Busca solo archivos con la extensión especificada.
related:sitio.com: Muestra sitios relacionados con el sitio especificado.
link:sitio.com: Muestra enlaces que apuntan al sitio especificado.
inurl:palabra clave: Busca en las URLs de los resultados de búsqueda.
intitle:palabra clave: Busca en los títulos de los resultados de búsqueda.
intext:palabra clave: Busca en el contenido de los resultados de búsqueda.
allintitle:palabra clave 1 palabra clave 2: Busca en los títulos de los resultados de búsqueda todas las palabras clave especificadas.
"""
"""
--- YANDEX ---
"palabra clave": Busca la palabra clave exacta entre comillas.
-palabra clave: Excluye la palabra clave de los resultados de búsqueda.
site:sitio.com: Busca en el sitio especificado.
filetype:extensión: Busca solo archivos con la extensión especificada.
related:sitio.com: Muestra sitios relacionados con el sitio especificado.
link:sitio.com: Muestra enlaces que apuntan al sitio especificado.
inurl:palabra clave: Busca en las URLs de los resultados de búsqueda.
intitle:palabra clave: Busca en los títulos de los resultados de búsqueda.
intext:palabra clave: Busca en el contenido de los resultados de búsqueda.
allintitle:palabra clave 1 palabra clave 2: Busca en los títulos de los resultados de búsqueda todas las palabras clave especificadas.
"""
"""
--- BAIDU ---
"palabra clave": Busca la palabra clave exacta entre comillas.
-palabra clave: Excluye la palabra clave de los resultados de búsqueda.
site:sitio.com: Busca en el sitio especificado.
filetype:extensión: Busca solo archivos con la extensión especificada.
related:sitio.com: Muestra sitios relacionados con el sitio especificado.
link:sitio.com: Muestra enlaces que apuntan al sitio especificado.
inurl:palabra clave: Busca en las URLs de los resultados de búsqueda.
intitle:palabra clave: Busca en los títulos de los resultados de búsqueda.
intext:palabra clave: Busca en el contenido de los resultados de búsqueda.
allintitle:palabra clave 1 palabra clave 2: Busca en los títulos de los resultados de búsqueda todas las palabras clave especificadas.
"""
