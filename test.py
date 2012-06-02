""" Box API testing script """

API_KEY = 'n5hrlxyfxb1iehj15m0sa1ajuyqvicdh'

import boxapi

api = boxapi.Session(API_KEY)
api.apply_new_authtoken()

raw_input("After your authorization, press any button...")

api.authorize(api.ticket)

print "AuthToken: %s" % api.auth_token

print api.action('/folders/0')



