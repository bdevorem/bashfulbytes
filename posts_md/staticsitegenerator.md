---
title: Create Your Own Static Site Generator
date: 2016 6 19
tag: programming
---

#Create Your Own Static Website Generator

## What is a Static Site Generator?
It's simple: a generator that yields static pages to form a 
static site.  
  
I'm serious.  
  
Static sites are the OG of the World Wide Web. When Tim 
Berners-Lee created the first web browser back before my 
generation was born (always late to the party), it was 
more or less simply a document navigator. Documents 
were just files in a hierarchical file system and hyperlinks 
led you from one document to another- just like navigating 
a Unix-like file system. Each document's content was stored 
the same way it was rendered. If you are familiar with the Web 
nowadays, it's obvious that it doesn't work like this 
anymore, due to the demand for dynamic content and 
the need for efficient storage.  
  
However, some things don't need to be dynamic. Take for 
example this blog: there's no need for 
my content to be rendered dynamically. Most of the content
won't change very often, and the content that does change
will just be new pages. I might eventually run out 
of disk space for my files, but then I'll just migrate 
the site to a VPS. No matter what, generating the HTML 
for the page can happen way before a user tries to access
it, in my scenario. It just makes the most sense to keep 
it simple (,stupid).  
  
So what is a static site generator? At the most basic 
level, it's a tool that takes content in the form of 
files (typically) and generates a file system-like 
structure of HTML files. However, static site generators 
can do much more than that: templates can be applied, metadata 
can be gathered, images can be compressed, etc. Rendering 
content statically is generally much faster than rendering 
dynamically, and actually less vulnerable to 
[exploits](https://hackertarget.com/attacking-wordpress/).


## Choosing a Static Site Generator
So you've decided you want to make a static site and now
you want to choose a static site generator. Well, there are
so many options. Here are the top generators that I looked 
into when designing my site:  
  
#### Jekyll
#### Acrylamid
#### Hugo
#### Hyde
#### Hexo
#### Nikola
#### Pelican

## Creating You Own Static Site Generator
If you have a very specific goal in mind, or none of those 
generators really do what you want, or you just feel trapped 
without custimization (love you Arch Linux), you may 
just want to make your own. It may sound like a big feat or 
too complicated to even bother trying, but making a static 
site generator is actually really straightforward. 

A basic generator can 
be broken down into the following steps.  
  
1.  Scan directory/directories for content to be generated.
  
    If you're writing your content in Markdown, for example, you would
    scan your source directory for Markdown files.
  
2.  Convert files to HTML.  
  
    For each source file, convert it to its HTML equivalent. If you're 
    going from Markdown to HTML in Python, I recommend 
    [Python-Markdown](https://pythonhosted.org/Markdown/) and
    [Python-Markdown2](https://github.com/trentm/python-markdown2) 
    for extras.  
  
3.  Optionally, you can apply a template.  
  
    I use [Jinja2](http://jinja.pocoo.org/) for my templating 
    because of its awesome 
    [inheritance feature](http://jinja.pocoo.org/docs/dev/templates/#template-inheritance).
    With Jinja2, you can create a base template consisting of the general 
    skelton HTML you want your pages/posts to have. You can import your CSS and 
    set up your header, footer, columms, divs, everything. Then, to add your 
    content, just follow the 
    [super simple](http://jinja.pocoo.org/docs/dev/templates/#child-template) 
    syntax for inheritance. There's a lot more to Jinja than this, but we're 
    just doing the basics here. If my IBM work ever becomes open source, I'll 
    make another post on how much you can really do with Jinja.
  
4.  Write your HTML to a target directory.  
  
    Or use your generator to build a directory hierarchy. Whatever you do here, 
    make it readable. You can even tailor it to how you plan on deploying 
    your site.  
  
That's it. I bet you can even do all that in less than 15 lines of code.  
Of course, you can add so much more to this. For example, use the extras from 
Python-Markdown2 to gather YAML-style front matter from your Markdown posts. 
You can even gather timstamps for your files to create some kind of order 
on your site. The sky's the limit here.  

## How This Site Was Born
If you've made it this far in the post, you've probably
realized that this site, [BashfulBytes](http://bashfulbytes.com/),
is indeed a static site. When I first decided I wanted to 
create a blog, my mind went straight to 
[Django](https://www.djangoproject.com/) or 
[Flask](http://flask.pocoo.org/),
since I am familiar with those frameworks. But I wanted 
something simpler; I didn't need any bells or whistles, or to
overcomplicate the goal I had in mind. I remembered hearing 
the buzzword 'static site generator' from a class I TA'd for,
where a much-coveted 'Guru Point' was awarded any student 
that created a blog or online portfolio using a static site 
generator. I wasn't familiar with static sites or generators 
at that point, so before I hopped on the bandwagon, I 
took some time to conduct thorough 
research. I didn't want to commit to something that 
wasn't exactly what I wanted (some foreshadowing here...).
  
My first step was to look into how my 
favorite computer science bloggers manage their blogs. 
I happened across a Quora question about [how to achieve 
Matt Might-style blog greatness](https://www.quora.com/How-do-I-create-a-simple-and-clean-blog-like-matt-might-net), to which Matt Might 
answered himself. I really liked his strategy:  
  
> 1. Don't engineer myself into a corner. I opt for more abstraction
> and control via shell scripts wherever possible, and I don't 
> make decisions that are going to be hard to undo later.
>  
> 2. Don't over-engineer it.  I opt for the simplest combination 
> of existing technologies to add the functionality I want.

This solidified my decision to use a static site generator.  
  
I looked into the most 
popular generators on [StaticGen](https://www.staticgen.com/),
(because I am a proponent of open source projects) and 
came across all the previously mentioned generators. I 
quickly narrowed it down to the projects written in 
Python, because duh. I was left with Pelican, Hyde, Acrylamid,
and Nikola. I did a brief peek into all of the source code 
first, then I decided to narrow it down to two and then get 
my hands dirty.

Acrylamid was a faster descendant of Pelican, so I 
kicked Pelican off the list. Hyde was just too 
mainstream for me, so I kicked it off the list. Not 
all decisions need to have substantial reasoning. Plus, 
Nikola was named after Nikola Tesla, and Acrylamid has 
amazingly sassy documentation, so it seemed like those 
were meant to be my final picks.  
