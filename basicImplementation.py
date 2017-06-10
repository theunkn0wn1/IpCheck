# # # # #
# Filename: basicImplementation.py
# Author: Joshua Salzedo
# Version 1.0
# Function: Example implementation of ipCheck module
# # #

from requests import get
from ipCheck import check
class config():
	"""Stores configuration vars"""
	pathToFile = "ip-ranges.json"
	remoteHost = "https://ip-ranges.amazonaws.com/ip-ranges.json"

def retrieveJSON():
	"""Retrieves Amazon ip-range JSON from remote host"""
	#open JSON for writing in binary mode
	with open(config.pathToFile,"wb") as file:
			#execute GET request
			response = get(config.remoteHost)
			if (response.status_code ==200):
				print("Server returned JSON successfully\tStatus:{}".format(response.status_code))
			#write contents of response to file
			file.write(response.content)
#get clean copy of the JSON
retrieveJSON()
#demo of implementation
with open(config.pathToFile,'r') as file:
	print(check(file,'13.54.42.1'))