""" Box API core module """

__author__ = "Colin Su <littleq0903@gmail.com>"

import os
import common
import auth
from request import Request

class Session(object):
    def __init__(self, api_key, auth_token=None):
        self.api_key = api_key
        self.auth_token = auth_token

    def apply_new_authtoken(self):
        self.ticket = auth.get_ticket(self.api_key)
        self.auth_url = auth.open_for_auth_ticket(self.ticket)

    def authorize(self, ticket):
        result = auth.get_auth_token(self.api_key, ticket)
        try:
            self.auth_token = result['response']['auth_token']['value']
        except:
            raise Exception("[Error] Authorizing failed.")

    def action(self, rest_path):
        params = {
                'api_key': self.api_key,
                'auth_token': self.auth_token
                }
        req = Request(rest_path, **params)
        req.do()
        return req.result
