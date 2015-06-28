import urllib
import urllib.request

#  http://www.quora.com/How-do-I-install-urllib-and-urllib2-for-Python-3-3-2
#  http://requests.readthedocs.org/en/latest/
#  Code for python 3.4

from urllib.request import urlopen
content = urlopen("https://www.quora.com/")
print(content)
