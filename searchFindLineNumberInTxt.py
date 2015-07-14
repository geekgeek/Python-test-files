import re

#Finds line number in txt file with regex
#regex:
regex = r'\bword1\b'
pattern = re.compile(regex)

for i, line in enumerate(open('test1_2.txt')): #txt file location
    for match in re.finditer(pattern, line):
        titles = re.findall(pattern,line)
        #print titles
        #print '%s \n %s' % (i+1, match.groups())
        print '%s' % (i+1) #Only prints out matching number
