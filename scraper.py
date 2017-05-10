#code by Bram Raatjes
#version: 2017/03/11

testurl = 'http://python-data.dr-chuck.net/comments_42.html'
realurl = 'http://python-data.dr-chuck.net/comments_354724.html'

import urllib
from BeautifulSoup import *

html = urllib.urlopen(realurl).read()

soup = BeautifulSoup(html)

# Retrieve all of the span tags
tags = soup('span')

lst = list()

for tag in tags:
	# Look at the parts of a tag
	num = float(tag.contents[0])
	lst.append(num)

print (sum(lst))
print (len(lst))