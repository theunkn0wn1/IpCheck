# # # # #
# Filename: ipCheck.py
# Author: Joshua Salzedo
# Version 1.0
# Function: parse Amazon region json and check specified IP
#	if it exists in a given range and return such range.
# # #
import sys
import ipaddress as ip #built in lib for IP handling
import json #built in lib for JSON file handling

# # # # 
# Config
class word():
	"""Stores JSON words"""
	pref = 'prefixes'
	ipPref = 'ip_prefix'
	ipV6Pref = 'ipv6_prefix' #un-used in this version. Not handling IPv6
	region = 'region'
	service = 'service'
#
# # #
isOpen = False
def versionCheck():
	"""Ensures python environment is python3, or errors will occur later on"""
	pyVersion = sys.version
	if int(pyVersion[0])==3:
		#No error, continue program execution
		return() 
	else:
		#incorrect version, halt program execution
		raise ValueError("This script targets python3.x.x")


# # #
# Init
# #
# Check version
versionCheck()

# #
# End init
#
def parseJson(fileObject, ip):
	"""Parse JSON data, checking if IP exists. Returns associated prefix object"""
	global isOpen
	global data
	# # #
	# load JSON into memory
	#with fileObject as data_file:
	if(not isOpen):
		data = json.load(fileObject)
		isOpen = not isOpen
	# # #
	# Checks IP for hit against loaded JSON data
	for entry in data[word.pref]:
		query = isInRange(entry[word.ipPref],ip)
		#check if an error occurred
		if type(query)==bool:
			#no error, check if the return was True
			if query:
				return(entry)
		else:
			#An error object was returned from isInRange
			print("An error occurred!\tSee returned object")
			print("object type = {}".format(type(query)))
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
	return(testIp in ipRange)

def check(fileObject,ip):
	"""Accepts Str IP Address, returns dict object"""
	return(parseJson(fileObject,ip))
