#!/usr/bin/python
#Search and replaces Strings (sub method)
#http://www.tutorialspoint.com/python/python_reg_expressions.htm

import re

phone = "2004-959-559 # This is Phone Number"

# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print "Phone Num : ", num

# Remove anything other than digits
num = re.sub(r'\D', "", phone)    
print "Phone Num : ", num
