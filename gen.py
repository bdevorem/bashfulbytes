#!/usr/bin/env python2
# Static site generator
# Author: Breanna Devore-McDonald

# yaml front matter ex.
# ---
# title:
# date:
# tag:
# ---

# TODO: add next/previous posts on each page
# TODO: add syntax highlighting for code posts

import os
import sys
import yaml
import markdown
import markdown.extensions.codehilite
from markdown2 import markdown_path
from datetime import date
import jinja2
from jinja2 import FileSystemLoader
from jinja2.environment import Environment

reload(sys)  
sys.setdefaultencoding('utf8')

SRC_PATH_POST = "./posts_md"
TARGET_PATH_POST = "./posts/templates"
LINK_POST = "./posts/"

SRC_PATH_PAGE = "./pages_md"
TARGET_PATH_PAGE = "./pages/templates"
LINK_PAGE = "./pages/"

RECENT, RESEARCH, PROGRAMMING, RANDOM, LINUX, UNFINISHED = ({} for i in range(6))

def convert_mds(source, target, link, yaml):

	listing = os.listdir(source)
	for infile in listing:
		if infile[0] != '.':
			filepath = os.path.join(source, infile)
			filename, fileext = os.path.splitext(infile)
			
			outfilepath = os.path.join(target, "{}.html".format(filename))
			outlink =  os.path.join(link, "{}.html".format(filename))
			outfile = open(outfilepath, 'w')

			output = markdown_path(filepath, extras=['metadata'])
			
			if yaml:
				gather_metadata(output.metadata, outlink)
				content = '''
{{% extends "base.html" %}}
{{% block content %}}
<span class="label label-primary">{}</span>
<span class="label label-info">{}</span>
{}
{{% endblock %}}
'''.format(output.metadata['date'], output.metadata['tag'], output)

			else:			
				content = '''
{{% extends "base.html" %}}
{{% block content %}}
{}
{{% endblock %}}
'''.format(output)
			outfile.write(content)
			outfile.close()

def gather_metadata(meta, link):

	tags = ['research', 'programming', 'linux', 'unfinished']
	if meta['tag'] in tags:
		globals()[meta['tag'].upper()][meta['title']] = link
	else:
		RANDOM[meta['title']] = link

	dt = [int(d) for d in meta['date'].split()]
	meta['date'] = date(*dt)

	oldest_time = meta['date']
	name = meta['title']
	RECENT[name] = [oldest_time, link]
	tmp = name
	if len(RECENT) > 5:
		for name, [time, link] in RECENT.iteritems():
			if time < oldest_time: # found a new oldest
				oldest_time = time
				tmp = name
		RECENT.pop(tmp, None)

def create_index():
	
	try:
		os.remove("./templates/index.html")
	except Exception as e:
		pass
	index = open("./templates/index.html", 'w')

	recent, research, programming, random, linux, unfinished = ('',)*6
	content = '{% extends "base.html" %}'
	
	for tag in ['RECENT', 'RESEARCH', 'PROGRAMMING', 'LINUX', 'RANDOM', 'UNFINISHED']:
		md = locals()[tag.lower()] = ''
		
		if tag == 'RECENT':
			for title, [time, link] in globals()[tag].iteritems():
				md = md +  "[{}]({})  \r".format(title, link)
		else:
			for title, link in globals()[tag].iteritems():
				md = md +  "[{}]({})  \r".format(title, link)
		content = content + '''
{{% block {} %}}
{}
{{% endblock %}}'''.format(tag.lower(), markdown.markdown(md))

	index.write(content)

def render_jinja():
	pass
	# TODO: make this work, instead of using staticjinja
	#env = Environment(loader=FileSystemLoader('.'))
	#template = env.get_template("./templates/index_template.html")
	#html = template.render(title="dg")

if __name__ == '__main__':

	for params in [[SRC_PATH_POST, TARGET_PATH_POST, LINK_POST, True], \
			[SRC_PATH_PAGE, TARGET_PATH_PAGE, LINK_PAGE, False]]:
		convert_mds(*params)
	create_index()
	#render_jinja()


