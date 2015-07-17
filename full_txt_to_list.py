import urllib
import re
import socket
import errno
import time

s = socket.socket()
s.settimeout(5)


def getdata():
    # Read txt and convert txt file to list
    symbolfile = open("C:\\test.txt", "r")
    urls = [line.split("\n") for line in symbolfile.readlines()]
    #</>

    #Read txt and convert txt file to list
    tickerfile = open("C:\\test1.txt", "r")
    tickers = [line.split("\n") for line in tickerfile.readlines()]
    #</>

    #<write list to other txt file>

    #</>

    #<regex>
    regex r'' #regex line
    pattern = re.compile(regex)
    #</>

    #<loop>
    i=0
    while i<len(urls):
        strList = ''.join(urls[i]) # convert urls list to string
        tickList = ''.join(tickers[i]) # convert tickers list to string
        
        #<regex>
        htmlfile = urllib.urlopen(strList)
        htmltext = htmlfile.read()
        titles = re.findall(pattern,htmltext)    
        #</>
        
        print tickList
        #<write list to file>
        tickerFile = "C:\\" + tickList + ".txt"
        fo = open(tickerFile, "w")
        line = fo.writelines( "%s\n" % item for item in titles )
        fo.close()
        
        #</>
        i+=1



getdata()
