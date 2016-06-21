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

# TODO: add next/previous posts on each page
# TODO: add syntax highlighting for code posts

SRC_PATH_POST = "./posts_md"
TARGET_PATH_POST = "./posts/templates"
LINK_POST = "./posts/"

SRC_PATH_PAGE = "./pages_md"
TARGET_PATH_PAGE = "./pages/templates"
LINK_PAGE = "./pages/"

RECENT, RESEARCH, PROGRAMMING, RANDOM, LINUX = ({},)*5

def convert_mds(source, target, link, post):

	listing = os.listdir(source)
	for infile in listing:
		filepath = os.path.join(source, infile)
		filename, fileext = os.path.splitext(infile)
		
		outfilepath = os.path.join(target, "{}.html".format(filename))
		outlink =  os.path.join(link, "{}.html".format(filename))
		outfile = open(outfilepath, 'w')

		output = markdown_path(filepath, extras=['metadata'])
		
		if post:
			gather_metadata(output.metadata, outlink)
		
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
		PROGRAMMING[meta['title']] = link
	elif meta['tag'] == 'linux':
		LINUX[meta['title']] = link
	else:
		RANDOM[meta['title']] = link

	dt = [int(d) for d in meta['date'].split()]
	meta['date'] = date(dt[0], dt[1], dt[2])

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

	recent, research, programming, random, linux = ('',)*5
	recent_html, research_html, programming_html, random_html, linux_html = ('',)*5

	for name, [time, link] in RECENT.iteritems():
		recent = recent +  "[{}]({})  \r".format(name, link)
	recent_html = markdown.markdown(recent)

	for tag in ['RESEARCH', 'PROGRAMMING', 'RANDOM', 'LINUX']:
		md = locals()[tag.lower()]
		for title, link in globals()[tag].iteritems():
			md = md +  "[{}]({})  \r".format(title, link)
		html = locals()["{}_html".format(tag.lower())]
		html = markdown.markdown(md)

	content = '''
{{% extends "base.html" %}}
{{% block recent %}}
{}
{{% endblock %}}
{{% block research %}}
{}
{{% endblock %}}
{{% block programming %}}
{}
{{% endblock %}}
{{% block linux %}}
{}
{{% endblock %}}
{{% block random %}}
{}
{{% endblock %}}
'''.format(recent_html, research_html, programming_html, \
			linux_html, random_html)
	index.write(content)

	# TODO: make this work, instead of using staticjinja
	#env = Environment(loader=FileSystemLoader('.'))
	#template = env.get_template("./templates/index_template.html")
	#print template
	#html = template.render(title="dg")
	#print html
	#index.write(html)

def render_jinja():
	for cmd in ["staticjinja build", "cd posts/ && staticjinja build", \
			"cd pages/ && staticjinja build"]:
		os.system(cmd)

if __name__ == '__main__':

	for params in [[SRC_PATH_POST, TARGET_PATH_POST, LINK_POST, True], \
			[SRC_PATH_PAGE, TARGET_PATH_PAGE, LINK_PAGE, False]]:
		convert_mds(*params)
	create_index()
	render_jinja()


