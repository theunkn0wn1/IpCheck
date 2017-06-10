# IpCheck
A python3 module to check if an IPv4 address exists within any of Amazon AWS's known ranges

## Usage
To use this module, one may simply clone this repo and import IpCheck into their Python3 Project

Once imported, the module will automaticially retrieve the list if IPv4 Ranges from AmazonAWS.

This will occur only once at the time the module is imported.
Your script may then call
```Python
IpCheck.check(ip_address)
```
The `ip_address` can be in either an `IPv4Address` object as provided by the `ipaddress` library or passed in as a string of type `str`.
