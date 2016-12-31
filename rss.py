#!/usr/bin/env python2
#will be a script to generate rss file when new post is published


# in makefile, under publish
# cycle through posts/ and ethics/ and keep track of 10 most recent posts
# generate xml file (delete previous)
import os
import sys
import time as ostime
from email.Utils import formatdate
from datetime import datetime
from markdown2 import markdown_path

TIMES = {}
NEWEST = {}

reload(sys)

def scan():
	#for source in ["/posts_md /ethics_md ".split()]:
	for source in ["./ethics_md"]:
	
		listing = os.listdir(source)
			
		for filename in listing:
			print filename
			filepath_md = os.path.join(source, filename)
			filepath_html = os.path.join(source.replace('_md', ''),filename.replace('.md','.html'))
				
			md= markdown_path(filepath_md, extras=['metadata'])

			TIMES[filepath_html] = [md.metadata['date'], md.metadata['title'], md.metadata['summary']]


def gather_data():

	for filename, [time, title, summary] in TIMES.iteritems():
		dt = [int(d) for d in time.split()]
		time = datetime(*dt)
		unixtime = ostime.mktime(time.timetuple())
		time = formatdate(unixtime)

		oldest_time = time
		name = filename
		tmp = name
		
		NEWEST[name] = [oldest_time, title, summary]
                #print NEWEST
#		if len(NEWEST) > 5:
#			for n, [t, title, summary] in NEWEST.iteritems():
#				if t < oldest_time: # new oldest
#					oldest_time = t
#					tmp = n
#			NEWEST.pop(tmp, None)
		

def generate_xml():

	content = """<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0">
<channel>

<title>BashfulBytes RSS Feed</title>
<link>http://bashfulbytes.com/</link>
<description>Weblog on life as a computer scientist</description>
"""

	for filename, [time, title, summary] in NEWEST.iteritems():
		link = "http://bashfulbytes.com/ethics" + filename.replace('./ethics', '')
		content = content + """
<item>
	<title>{}</title>
	<link>{}</link>
	<guid>{}</guid>
	<pubDate>{}</pubDate>
	<description>![CDATA[ {} ]]</description>
</item>
""".format(title, link, link, time, summary)

	content = content + """
</channel>
</rss>
"""
	try:
		os.remove("./rss.xml")
	except Exception as e:
		pass
	rss = open("./rss.xml", 'w')
	rss.write(content)
	rss.close

if __name__ == '__main__':
	scan()
	gather_data()
	generate_xml()

