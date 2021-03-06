import re

str ='''
255.255.255.255
255.255.255.2
255.255.255.25
255.255.255.0
1.1.1.1
10.1.2.3
10.0.0.0 to 10.255.255.255 
'''

#pattern = re.findall(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$',str)
#pattern = re.findall(r'\d{3}.\d{3}.\d{3}.\d{3}',str)
#pattern = re.findall('\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b',str)
pattern = re.findall(r'^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$',str) #for all 4 parts of IP

#accurate regex for all four parts... of IPv4
'''
^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.
(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.
(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.
(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$ 
'''

print(list(pattern))