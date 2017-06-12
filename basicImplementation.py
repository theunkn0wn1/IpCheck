# # # # #
# Filename: basicImplementation.py
# Author: Joshua Salzedo
# Version 1.0
# Function: Example implementation of ipCheck module
# # #
from requests import get
from ipCheck import check
import ipaddress as ip #built in lib for IP handling

class config():
	"""Stores configuration vars"""
	Filename = "ip-ranges.json"
	remoteHost = "https://ip-ranges.amazonaws.com/ip-ranges.json"
def retrieveJSON():
	"""Retrieves Amazon ip-range JSON from remote host"""
	#open JSON for writing in binary mode
	try:
		with open(config.Filename,"wb") as file:
				#execute GET request
				response = get(config.remoteHost)
				if (response.status_code ==200):
					print("Server returned JSON successfully\tStatus:{}".format(response.status_code))
					#write contents of response to file
					file.write(response.content)
				elif(response.status_code ==403):
					raise ValueError("HTTP GET failed. Access forbidden (403)")
				elif(response.status_code==404):
					raise ValueError("HTTP GET failed: File not found on remote host")
				else:
					raise ValueError("HTTP GET failed:Unspecified error({})".format(response.status_code))
	except Exception as e:
		pass
#get clean copy of the JSON
retrieveJSON()
#demo of implementation
with open(config.Filename,'r') as data_file:
	print(check(data_file,'13.54.42.1'))
	for x in ip.ip_network('13.54.0.0/25'):
		#check the ip
		query = check(data_file,x)
		#and print the result provided its not None
		if type(query)!=type(None):
			print("query value = {}".format(query))