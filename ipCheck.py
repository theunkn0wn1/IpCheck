# # # # #
# Filename: util_ip_check.py
# Author: Joshua Salzedo
# Version 1.0
# Function: parse Amazon region json and check specified IP
#	if it exists in a given range and return such range.
# # #
import sys
import ipaddress as ip #built in lib for IP handling
import json #built in lib for JSON file handling
from requests import get #for retrieving JSON from remote host
# # # # 
# Config
class config(object):
	"""Stores configuration vars"""
	pathToFile = "ip-ranges.json"
	remoteHost = "https://ip-ranges.amazonaws.com/ip-ranges.json"
class word():
	"""Stores JSON words"""
	pref = 'prefixes'
	ipPref = 'ip_prefix'
	ipV6Pref = 'ipv6_prefix' #un-used in this version. Not handling IPv6
	region = 'region'
	service = 'service'
#
# # #

def versionCheck():
	"""Ensures python environment is python3, or errors will occur later on"""
	pyVersion = sys.version
	if int(pyVersion[0])==3:
		#No error, continue program execution
		return() 
	else:
		#incorrect version, halt program execution
		raise ValueError("This script targets python3.x.x")

def retrieveJSON():
	"""Retrieves Amazon ip-range JSON from remote host"""
	#open JSON for writing in binary mode
	with open(config.pathToFile,"wb") as file:
			#execute GET request
			response = get(config.remoteHost)
			if response.status_code ==200:
				print("Server returned JSON successfuly\tStatus:{}".format(response.status_code))
			#write contents of response to file
			file.write(response.content)
# # #
# Init
# #
# Check version
versionCheck()
# Ensure we have a clean copy when module is imported
retrieveJSON()
# #
# End init
#
def parseJson(path, ip):
	"""Parse JSON data, checking if IP exists. Returns associated prefix object"""
	# # #
	# load JSON into memory
	with open(path) as data_file:
		data = json.load(data_file)
	# # #
	# Checks IP for hit against loaded JSON data
	for entry in data[word.pref]:
		query = isInRange(entry[word.ipPref],ip)
		#check if an error occured
		if type(query)==int:
			#no error, check if the return was True
			if query:
				return(entry)
		else:
			#An error object was returned from isInRange
			print("An error occured!\nSee returned object")
			return(query)
	#if the ip is NOT found in any ranges	
	return(None)

def isInRange(testRange,inputValue):
	"""checks if inputValue exists within testRange, if so returns true"""
	try:
		#attempt to parse testRange as a IP address range
		ipRange = ip.ip_network(testRange)
		if type(inputValue)==type(ip.ip_address('255.255.255.255')):
			testIp = inputValue
		else:
			testIp = ip.ip_address(inputValue)
	except Exception as e:
		#input was not a valid network range
		#raise e
		return(e) #return error object for handling
	#test if exists
	if (testIp in ipRange):
		return(1)
	#ip was not in range
	return(0)

def check(ip):
	"""Accepts Str IP Adress, returns dict object"""
	Myobject = parseJson(config.pathToFile,ip)
	return(Myobject)

print((check('13.112.45.40')))
print(check(ip.ip_address('13.112.45.40')))
#print(parseJson(config.pathToFile, '13.112.45.0'))