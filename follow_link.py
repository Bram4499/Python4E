#code by Bram Raatjes
#version: 2017/03/11

testurl = 'http://python-data.dr-chuck.net/known_by_Fikret.html'
url = 'http://python-data.dr-chuck.net/known_by_Alexandria.html'

# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *
c = 0
for x in range(0, 7):
	
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	c = c + 1
	# Retrieve all of the anchor tags
	lst = list()
	tags = soup('a')
	for tag in tags:
		lst.append(tag.get('href', None))
	url = lst[17]

	
print c
print(url)