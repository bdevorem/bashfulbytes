---
title: Create Your Own Static Site Generator
date: 2016 6 19
tag: programming
---

##Create Your Own Static Website Generator

### What is a Static Site Generator?
It's simple: a generator that yields static pages to form a 
static site.  
  
I'm serious.  
  
Static sites are the OG of the World Wide Web. When Tim 
Berners-Lee created the first web browser back before my 
generation was born (always late to the party), it was 
more or less simply a document navigator, where the documents 
were just files in a hierarchical file system and hyperlinks 
led you from one document to another- just like navigating 
a Unix-like file system. Each document's content was stored 
the same was it was rendered. If you are familiar with the Web 
nowadays, it's obvious that it doesn't work like this 
anymore, due to the demand for dynamic content and 
the need for efficient databases.  
  
However, some things don't need to be dynamic. In fact, 
some things could be considered overengineered if they were 
dynamic. Take for example this blog: there's no need for 
my content to be rendered dynamically. Most of the content will
not change often, so there's no need to make dynamic decisions 
come delivery time. I might eventually run out 
of disk space for my files, but then I'll just migrate 
the site to a VPS. It just makes the most sense to keep 
it simple (,stupid).  
  
So what is a static site generator? At the most basic 
level, it's a tool that takes content in the form of 
files (typically) and generates a file system-like 
structure of HTML files. Usually, static site generators 
do much more than this: templates can be applied, metadata 
can be gathered, images can be compressed, etc. Rendering 
content statically is generally much faster than rendering 
dynamically, and actually less vulnerable to 
[exploits](https://hackertarget.com/attacking-wordpress/).


### Choosing a Static Site Generator
Soon, this will talk through the differences and similarities
of the major static site generators of the current world.

### Creating You Own Static Site Generator
If those don't please you, this will give a slight roadmap
on how to create your own simple static site generator.

### How This Site Was Born
This will eventually explain the steps it took for me to get to
this blog, and how I created it and why.
