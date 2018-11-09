import json
import urllib, urllib2
try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse
try:
    from urllib.request import Request, urlopen  # Python 3
except ImportError:
    from urllib2 import Request, urlopen  # Python 2

with open('constant.json', 'r') as f:
    djubo = json.load(f)


def get_response_from_djubo():
	print('get_response_from_djubo')
	headers = get_headers()
	print headers

def get_headers():
	headers = {}
	try:
		headers["authorization"] = djubo["url"]
		headers["Content-type"] = djubo["api_key"]
	except KeyError:
		print('Key is missing from the headers')		
	
	return headers
