"""
Box API authentication module
"""
__author__ = "Colin Su <littleq0903@gmail.com>"

from xml.dom.minidom import parseString
from lib.xml2dict import XML2Dict
import urllib
import common

def get_ticket(api_key):
    http_params = {
            'action': 'get_ticket',
            'api_key': api_key,
            }
    http_params_encoded = urllib.urlencode(http_params)

    opener = urllib.urlopen( "%s?%s" % (common.API_V1_URL, http_params_encoded) )
    response = opener.read()
    opener.close()

    dom = parseString(response)
    xmlTag = dom.getElementsByTagName('ticket')[0].toxml()
    xmlData = xmlTag.replace('<ticket>', '').replace('</ticket>', '')

    # TODO: exception handling
    return xmlData

def open_for_auth_ticket(ticket):
    ticket_url = "https://www.box.com/api/1.0/auth/" + ticket
    # TODO: use open browser action instead of print url
    print "Please go to the following url for authentication: %s" % ticket_url
    return ticket_url

def get_auth_token(api_key, ticket):
    http_params = {
            'action': 'get_auth_token',
            'api_key': api_key,
            'ticket': ticket
            }
    http_params_encoded = urllib.urlencode(http_params)

    opener = urllib.urlopen("%s?%s" % (common.API_V1_URL, http_params_encoded) )
    response = opener.read()
    opener.close()

    dict_result = XML2Dict().fromstring(response)
    return dict_result

