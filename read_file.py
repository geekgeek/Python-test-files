#https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files
#Read file and executes a regex request

import re

#Read file
names_file = open("foo.txt","r") # r = read, w = write

data = names_file.read()
# close file
names_file.close()
#regex request
regexLine = r'\bwordToSearchFor\b'

line = re.findall(regexLine, data, re.X|re.M)
print(line)
