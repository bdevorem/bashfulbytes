#!/usr/bin/env python2
# Static site generator
# Author: Breanna Devore-McDonald

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


# yaml front matter ex.
# ---
# title:
# date:
# tag:
# ---

# TODO: files in html to extend base template
# TODO: add next/previous posts on each page

SRC_PATH = "./posts_md"
TARGET_PATH = "./posts"

RECENT = {}
RESEARCH = {}
PROG = {}
RANDOM = {}

def convert_mds(source, target):

	listing = os.listdir(source)
	for infile in listing:
		filepath = os.path.join(source, infile)
		filename, fileext = os.path.splitext(infile)
		
		outfilepath = os.path.join(target, "{}.html".format(filename))
		outfile = open(outfilepath, 'w')

		output = markdown_path(filepath, extras=['metadata'])
		gather_metadata(output.metadata, outfilepath)
	
		
		content = '''
{{% extends "base.html" %}}
{{% block content %}}
{}
{{% endblock %}}
'''.format(output)
		outfile.write(content)
		outfile.close()

def gather_metadata(meta, link):

		if meta['tag'] == 'research':
			RESEARCH[meta['title']] = link
		elif meta['tag'] == 'programming':
			PROG[meta['title']] = link
		else:
			RANDOM[meta['title']] = link

		dt = [int(d) for d in meta['date'].split()]
		meta['date'] = date(dt[0], dt[1], dt[2])

		oldest = meta['date']
		name = meta['title']
		RECENT[name] = oldest

		if len(RECENT) > 5:
			for name, time in RECENT:
				if time < oldest:
					oldest = time
					name = name
			RECENT.pop(name, None)

def create_index():
	
	try:
		os.remove("index.html")
	except Exception as e:
		print e
	index = open("./templates/index.html", 'w')

	recent, research, programming, random = '', '', '', ''
	for title, link in RESEARCH.iteritems():
		research = research + "[{}]({})  \r".format(title, link)
	research_html = markdown.markdown(research)

	for title, link in PROG.iteritems():
		programming = programming + "[{}]({})  \r".format(title, link)
	programming_html = markdown.markdown(programming)

	for title, link in RANDOM.iteritems():
		random = random + "[{}]({})  \r".format(title, link)
	random_html = markdown.markdown(random)

	
	content = '''
{{% extends "base_archive.html" %}}
{{% block recent %}}
{}
{{% endblock %}}
{{% block research %}}
{}
{{% endblock %}}
{{% block programming %}}
{}
{{% endblock %}}
{{% block random %}}
{}
{{% endblock %}}
'''.format(recent, research_html, programming_html, random_html)
	index.write(content)

	# TODO: make this work, instead of using staticjinja
	#env = Environment(loader=FileSystemLoader('.'))
	#template = env.get_template("./templates/index_template.html")
	#print template
	#html = template.render(title="dg")
	#print html
	#index.write(html)


if __name__ == '__main__':

	convert_mds(SRC_PATH, TARGET_PATH)
	create_index()
	#for k, v in RECENT.iteritems():
	#	print k + '-->' + str(v)

