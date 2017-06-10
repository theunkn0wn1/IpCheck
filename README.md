# IpCheck
A python3 module to check if an IPv4 address exists within any of Amazon AWS's known ranges

## Usage
To use this module, one may simply clone this repository and import IpCheck into your Python3 Project

Your script may then call
```Python
IpCheck.check(fileObject,ip_address)
```
The `ip_address` can be in either an `IPv4Address` object as provided by the `ipaddress` library or passed in as a string of type `str`.
`fileObject` expects an open file object from your program, ipCheck will not automatically retrieve the file for you.
