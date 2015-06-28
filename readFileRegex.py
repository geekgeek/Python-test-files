import re

#Read file
names_file = open("file.txt", encoding="utf-8")
data = names_file.read()
# close file
names_file.close()

#regex request
regexLine = r'\bSearcHWord1\b|\bSearcHWord2\b'

line = re.findall(regexLine, data, re.X|re.M)
print(line)
