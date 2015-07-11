#!/usr/bin/python
#Search and replaces Strings (sub method)
#http://www.tutorialspoint.com/python/python_reg_expressions.htm

import re

#Read file
names_file = open("footo.txt","r")
phone = names_file.read()

# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print "Phone Num : ", num

# Remove anything other than digits
num = re.sub(r'\D', "", phone)    
print "Phone Num : ", num


#readFile
names_file.close()
