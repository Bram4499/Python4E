#code by Bram Raatjes
#version: 2017/03/13

testurl = 'http://python-data.dr-chuck.net/comments_42.xml'
realurl = 'http://python-data.dr-chuck.net/comments_354721.xml'

import urllib
import xml.etree.ElementTree as ET

data = urllib.urlopen(realurl).read()
#print 'Retrieved',len(data),'characters'

tree = ET.fromstring(data)

#print(type(data))

lst = list()
for comment in tree.findall('comments/comment'):
	count = int(comment.find('count').text)
	lst.append(count)
	#print(count)

print(sum(lst))