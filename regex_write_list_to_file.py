import urllib
import re

# url list
urls = ["https://www.google.com","https://www.yahoo.com"]

#regex codeline
regex = r'<title>(.+?)</title>'

#code
pattern = re.compile(regex)

#write list to file
fo = open("foo.txt", "w")

#<loop>
i=0
while i<len(urls):
	htmlfile = urllib.urlopen(urls[i])
	htmltext = htmlfile.read()
	titles = re.findall(pattern,htmltext)
	
	print titles
	#<write list to file>
	line = fo.writelines( "%s\n" % item for item in titles )
	fo.close()
	#</>
	i+=1
	
#</loop>

