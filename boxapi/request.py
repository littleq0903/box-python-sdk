""" Box API request module """

__author__ = "Colin Su <littleq0903@gmail.com>"

import common
import urllib
from xml.dom.minidom import parseString
from lib.xml2dict import XML2Dict


class Request(object):
    def __init__(self, rest_path, api_version=2):
        """
        params:
            self.rest_url: the URL part of api request
            self.rest_path: the path part of api request

        """
        self.rest_url = common.API_V1_URL
        self.rest_path = rest_path
        self.result_format = 'xml'

        if api_version == 1:
            self.rest_url = common.API_V1_URL

        elif api_version == 2:
            self.rest_url = common.API_V2_URL
            self.result_format = 'json'

        super().__init__()

    def do(self):
        opener = urllib.urlopen(self.rest_url + self.rest_path)
        response = opener.read()
        opener.close()

        if self.result_format == 'json':
            self.result = json.loads(response)
        elif self.result_format == 'xml':
            self.result = XML2Dict(response)



