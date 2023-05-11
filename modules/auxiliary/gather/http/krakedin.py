#!/usr/bin/env python3
# Project: Osiris-Framework
# Version 3.0

import os
import json
from json.decoder import JSONDecodeError
import socket
import requests
from core.ModuleObtainer import obtainer
from utilities.Colors import color
from utilities.Messages import print_message
from utilities.Tools import tools
from tabulate import tabulate
from tqdm import tqdm
from time import sleep
print_message.name_module = __file__

info = {
        'author'            :'Luis Eduardo Jacome Valencia',
        'date'              :'2022/11/29',
        'rank'              :'Excellent',
        'path'              :'auxiliary/gather/http/krakedin.py',
        'category'          :'auxiliary',
        'license'           :'GPL-2.0',
        'description'       :'Module that obtains information about the employers via Linkedin ',
        'references'        :['None']
}
options = {
        'path': ['No', 'use to specify a path for processing files', '/tmp'],
        'csrf-token': ['Yes', 'use a token to connect for a linkedin account', ''],
        'cookie': ['Yes', 'use a cookie to connect for a linkedin account', ''],
        'company': ['Yes', 'use to get the information about employees (fsd_company)', ''],
        'timeout':  ['No', 'use to get information with timeout (avoid blocking in almost all the cases)', '1'],
}
required = {
        'start_required'     :'True',
        'check_required'     :'False'
}

session = requests.Session()

class KrakedinScraping():
    def __init__(self, __path, __csrf_token, __cookie, __company):
        self.namesjson = "names.json"  # It's a json file
        self.flag = False
        self.counter = 0
        self.save_information = []

        self.__path = __path
        self.__csrf_token = __csrf_token
        self.__cookie = __cookie
        self.__company = __company

    def checkMainObject(self):
        with open(self.__path + "/" + self.namesjson, 'r') as outfile:
            data = json.load(outfile)
            length_items = len(data["elements"])
            if len(data["elements"]) > 0:
                self.flag = True


    def makeBefore(self):
        try:
            os.remove(self.__path + "/" + self.namesjson)
        except OSError:
            pass

    def decodeJSON(self):
        counter = 0
        with open(self.__path + "/" + self.namesjson, 'r') as outfile:
            data = json.load(outfile)
            length_items = len(data["elements"])
            for userdata in data["elements"]:
                try:
                    if userdata["hitInfo"]["com.linkedin.voyager.search.SearchProfile"]["miniProfile"]["firstName"] != '':
                        user_file = open(self.__path + '/users.txt', "a")
                        user_file.write(str(userdata["hitInfo"]["com.linkedin.voyager.search.SearchProfile"]["miniProfile"]["firstName"]+ " " +str(userdata["hitInfo"]["com.linkedin.voyager.search.SearchProfile"]["miniProfile"]["lastName"])))
                        user_file.write('\n')

                        user_company = open(self.__path + '/users_company.txt', "a")
                        user_company.write('\n')
                        user_company.write(str(userdata["hitInfo"]["com.linkedin.voyager.search.SearchProfile"]["miniProfile"]["firstName"] + " " + str(userdata["hitInfo"]["com.linkedin.voyager.search.SearchProfile"]["miniProfile"]["lastName"])))
                        user_company.write('\n')
                        user_company.write(str(userdata["hitInfo"]["com.linkedin.voyager.search.SearchProfile"]["miniProfile"]["occupation"]))
                        user_company.write('\n')
                        user_company.write('================================')

                        user_file.close()
                        user_company.close()

                        self.save_information.append([str(userdata["hitInfo"]["com.linkedin.voyager.search.SearchProfile"]["miniProfile"][
                                          "firstName"]),
                                            str(userdata["hitInfo"]["com.linkedin.voyager.search.SearchProfile"]["miniProfile"][
                                          "lastName"]),
         str(userdata["hitInfo"]["com.linkedin.voyager.search.SearchProfile"]["miniProfile"][
                                          "occupation"])])
                except Exception as e:
                    pass
            #self.makeBefore()

    def makeRequests(self):
        while True:
            try:

                url_request_linkedin = "https://www.linkedin.com/voyager/api/search/hits?count=12&educationEndYear=List()&educationStartYear=List()&facetCurrentCompany=List(%s)&facetCurrentFunction=List()&facetFieldOfStudy=List()&facetGeoRegion=List()&facetNetwork=List()&facetSchool=List()&facetSkillExplicit=List()&keywords=List()&maxFacetValues=15&origin=organization&q=people&start=%s&supportedFacets=List(GEO_REGION,SCHOOL,CURRENT_COMPANY,CURRENT_FUNCTION,FIELD_OF_STUDY,SKILL_EXPLICIT,NETWORK)" % (self.__company, self.counter)
                response = session.get(url_request_linkedin, headers={'csrf-token': self.__csrf_token, 'Cookie': self.__cookie }, stream=True)

                with open(self.__path + '/' + self.namesjson, 'w') as out_file:
                    out_file.write(response.text)

                self.checkMainObject()

                if self.flag:
                    self.decodeJSON()
                    self.counter = self.counter + 10
                else:
                    break
            except:
                break

        print(tabulate(self.save_information,
                       headers=['First Name', 'Last Name', 'Occupation'],
                       tablefmt='fancy_grid',
                       stralign='center'))


def exploit():
    """ main exploit function """
    try:
        print_message.start_execution()
        #tools.os_detection()

        __path = obtainer.options['path'][2]
        __csrf_token = obtainer.options['csrf-token'][2]
        __cookie = obtainer.options['cookie'][2]
        __company = obtainer.options['company'][2]
        ### NOT DOING NOTHING BTW __timeout = obtainer.options['timeout'][2]

        KrakedinScraping(__path, __csrf_token, __cookie, __company).makeRequests()

    except socket.gaierror:
        print_message.execution_error("lgray", " You must enter the parameters!")
        return False

    print_message.end_execution()
