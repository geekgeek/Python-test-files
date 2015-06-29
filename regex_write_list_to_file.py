import urllib
import re

# url list
urls = ["https://www.nordnet.no/mux/web/marknaden/kurslista/aktier.html?marknad=Norge&lista=1_1&large=on&mid=on&small=on&sektor=0&subtyp=key_ratios&sortera=pe&sorteringsordning=stigande"]

#regex codeline
regex = r'<title>(.+?)</title>'
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

