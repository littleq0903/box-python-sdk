""" Box API request module """

__author__ = "Colin Su <littleq0903@gmail.com>"

import common
import json
import urllib
from xml.dom.minidom import parseString
from lib.xml2dict import XML2Dict


class Request(object):
    def __init__(self, rest_path, api_version=2, api_key='', auth_token='', method="GET", params={}):
        """
        params:
            self.rest_url: the URL part of api request
            self.rest_path: the path part of api request

        """
        self.rest_url = common.API_V1_URL
        self.rest_path = rest_path
        self.result_format = 'xml'
        self.api_key = api_key
        self.auth_token = auth_token
        self.method = method
        self.params = params

        if api_version == 1:
            self.rest_url = common.API_V1_URL

        elif api_version == 2:
            self.rest_url = common.API_V2_URL
            self.result_format = 'json'


    def do(self):
        request_url = (self.rest_url + self.rest_path)
        request_params = self.params
        opener = urllib.URLopener()
        opener.addheader('Authorization', 'BoxAuth api_key=%s&auth_token=%s' % (self.api_key, self.auth_token))
        if self.method == 'GET':
            responsor = opener.open( request_url + "?" + urllib.urlencode(request_params) )
        elif self.method == 'POST':
            responsor = opner.open( request_url, urllib.urlencode(request_params) )
        response = responsor.read()
        opener.close()

        if self.result_format == 'json':
            self.result = json.loads(response)
        elif self.result_format == 'xml':
            self.result = XML2Dict(response)
        



