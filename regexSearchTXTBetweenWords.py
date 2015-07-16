import re

#Read file
names_file = open("foo.txt","r")
data = names_file.read()
# close file
names_file.close()


#regex request
regexLine = r'\bword1\b(.+?)\bword2\b'

line = re.findall(regexLine, data, re.X|re.M)
print(line)
