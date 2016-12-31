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
import markdown.extensions.tables
from markdown2 import markdown_path
from datetime import date, datetime
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

SRC_PATH_ETHICS = "./ethics_md"
TARGET_PATH_ETHICS = "./ethics/templates"
LINK_ETHICS = "./"

RESEARCH, PROGRAMMING, RANDOM, LINUX, UNFINISHED, ETHICS = ({} for i in range(6))
RECENT = []
TIMES = {}
DS = [RESEARCH, PROGRAMMING, RANDOM, LINUX, UNFINISHED, ETHICS, RECENT]

def convert_mds(source, target, link, yaml):
    listing = os.listdir(source)
    for infile in listing:
	if infile[0] != '.':
	    filepath = os.path.join(source, infile)
	    filename, fileext = os.path.splitext(infile)
	    
	    outfilepath = os.path.join(target, "{}.html".format(filename))
	    outlink =  os.path.join(link, "{}.html".format(filename))
	    outfile = open(outfilepath, 'w')

	    output = markdown_path(filepath, extras=['metadata', 'fenced-code-blocks'])
	    
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

    tags = ['research', 'programming', 'linux', 'unfinished', 'ethics']
    if meta['tag'] in tags:
	globals()[meta['tag'].upper()][meta['title']] = link
    else:
	RANDOM[meta['title']] = link
    TIMES[meta['title']] = meta['date']

    if meta['tag'] != 'ethics' and meta['tag'] != 'unfinished':
	dt = [int(d) for d in meta['date'].split()]
	meta['date'] = date(*dt)
        TIMES[meta['title']] = meta['date']
	
	oldest_time = meta['date']
	name = meta['title']
        RECENT.append({
            'name': name,
            'time': oldest_time,
            'link': link})

	tmp = name
	if len(RECENT) > 5:
            for i, [name, time] in enumerate([d['name'], d['time']] for d in RECENT):
                if time < oldest_time: # found a new oldest
                    oldest_time = time
                    tmp = name
            RECENT[:] = [d for d in RECENT if d.get('name') != tmp]
    else:
	dt = [int(d) for d in meta['date'].split()]
	#meta['date'] = datetime(*dt)
				
def sort():
    global RECENT
    for ds in DS:
        if ds is RECENT:
            new_recent = sorted(RECENT, key=lambda k: k['time'], reverse=True)
            RECENT = new_recent[:]
            del new_recent
        else:
            pass

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
	    for i, [title, time, link] in enumerate([d['name'], d['time'], d['link']] for d in globals()[tag]):
                t = "<b>{}</b> &emsp; ".format(TIMES[title])
                t = "<span class=\"label label-default\"><b>{}</b></span>\t".format(TIMES[title])
                md = md + t + " &emsp; [{}]({})  \r".format(title, link)
        else:
	    for title, link in globals()[tag].iteritems():
                t = "<span class=\"label label-default\"><b>{}</b></span>\t".format(TIMES[title])
		md = md + t + "&emsp; [{}]({})  \r".format(title, link)
	content = content + '''
{{% block {} %}}
{}
{{% endblock %}}'''.format(tag.lower(), markdown.markdown(md))

    index.write(content)

    # create ethics index
    try:
	os.remove("./ethics/templates/index.html")
    except Exception as e:
	pass
    index = open("./ethics/templates/index.html", 'w')
    content = '{% extends "base_index.html" %}'
    tag = 'ETHICS'
    md = locals()[tag.lower()] = ''

    for title, link in globals()[tag].iteritems():
	md = md +  "[{}]({})  \r".format(title, link)
    content = content + '''
{{% block content %}}
<h2>Ethical and Professional Issues Blog Index</h2>
{}
{{% endblock %}}'''.format(markdown.markdown(md))

    index.write(content)
    index.close()



def render_jinja():
    pass
    # TODO: make this work, instead of using staticjinja
    #env = Environment(loader=FileSystemLoader('.'))
    #template = env.get_template("./templates/index_template.html")
    #html = template.render(title="dg")

if __name__ == '__main__':

    for params in [[SRC_PATH_POST, TARGET_PATH_POST, LINK_POST, True], \
		    [SRC_PATH_ETHICS, TARGET_PATH_ETHICS, LINK_ETHICS, True], \
		    [SRC_PATH_PAGE, TARGET_PATH_PAGE, LINK_PAGE, False]]:
	convert_mds(*params)
    sort()
    create_index()
    #render_jinja()


