""" Box API testing script """

API_KEY = '<Your API Key>'
AUTH_TOKEN = '<Your Auth Token>'
API_ACTION = '/folders/0'

import sys

if len(sys.argv) > 1:
    API_ACTION = sys.argv[1]

import boxapi
import json


if not AUTH_TOKEN or AUTH_TOKEN == '<Your Auth Token>':
    print "Did not find the auth_token, apply for new one..."
    api = boxapi.Session(API_KEY)
    api.apply_new_authtoken()
    raw_input("After your authorization, press any button...")
    api.authorize(api.ticket)
    print "AuthToken: %s" % api.auth_token

else:
    api = boxapi.Session(API_KEY, auth_token=AUTH_TOKEN)


print json.dumps(api.action(API_ACTION))



