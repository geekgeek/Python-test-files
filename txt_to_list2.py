import urllib
import re

# Read txt and convert txt file to list
symbolfile = open("C:\\textfile1.txt", "r")
urls = [line.split("\n") for line in symbolfile.readlines()]
#</>

#<write list to other txt file>
fo = open("textfile2.txt", "w")
#</>

before = "this is a text before"
after = "this is text after"

#<loop>
i=0
while i<len(urls):
    strList = ''.join(urls[i]) # convert list to string
    print strList
    
    #<write list to file>
    fo.writelines(before)
    line = fo.writelines(strList)
    fo.writelines(after)
    fo.writelines("\n")
    #</>
    i+=1

#</>
