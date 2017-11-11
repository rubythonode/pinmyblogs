from __future__ import print_function
from datetime import datetime
import urllib2


print ( str(datetime.now()))

a=['https://atom.io/',
       'https://docs.python.org/2/howto/urllib2.html',
       'https://www.hackerrank.com/',
       'http://www.pythonforbeginners.com/beautifulsoup/beautifulsoup-4-python',
       'http://127.0.0.1:8000/login/'

       ]

for i in a:
	try:
		print("Reading " + i)
		page = urllib2.urlopen(i).read()
		# print (page)
		if(r'<title>')  and (r'</title>') in page:
			page = page.split("<title>")
			page= page[1].split("</title>")
			if (page):
				title = page[0].strip()
				print (title)



	except Exception, e:
		print("Error" +e.message)

print(str(datetime.now()))
