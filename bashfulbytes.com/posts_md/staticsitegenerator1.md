---
title: Create Your Own Static Site Generator (Part 1)
date: 2016 6 19
tag: programming
---

#Create Your Own Static Website Generator (Part 1)
  
  

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
  
Check out [Part 2](http://bashfulbytes.com/posts/staticsitegenerator2.html) to find out how to choose a static site generator.  
