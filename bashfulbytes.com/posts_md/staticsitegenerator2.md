---
title: Create Your Own Static Site Generator (Part 2)
date: 2016 6 26
tag: programming
---

#Create Your Own Static Website Generator (Part 2)

## Choosing a Static Site Generator
So you've decided you want to make a static site and now
you want to choose a static site generator. Well, there are
so many options. Here are the top generators that I looked 
into when designing my site:  
  
#### [Jekyll](https://jekyllrb.com/)
Jekyll is probably the most mainstream and mature project out there at 
this time. The documentation is really good, the community is large, and 
there are numerous in-depth tutorials on how to build a site using Jekyll. 
If you want to just test the waters, Jekyll is very good for 
beginners. One caveat: it's written in Ruby. Many consider that a 
con, but it seems like it's pretty abstracted from the user.

#### [Hugo](https://gohugo.io/)
As the name suggests, Hugo is written in Go, which isn't too common 
among static site generators. It claims to be *extremely* fast because 
it's optimized for speed, but it's very configurable as well. You can 
organize your content any way you want and you can declare your 
own content types. And it's even easy to use: the docs say "Hugo 
doesn’t depend on administrative privileges, 
databases, runtimes, interpreters or external libraries". I'm guessing 
if you're a systems person, this will be your go-to.

#### [Hexo](https://hexo.io/)
It seems a lot to me that Hexo is a Node version of Hugo. It 
supports multi-threaded generating, so it's also extremely fast. 
It's easy to use just as well, assuming you are familiar with Node.js and 
Javascript. Another neat thing about Hexo is that it's super plugin-friendly.
It supports EJS, Swig, and Stylus, and the docs say 
"you can install more plugins for Haml, Jade, and Less." Hexo doesn't have 
as big of a community as other generators, like Jekyll, but installation 
is very easy and manageable because everything is pre-installed, so 
Hexo is a great contender. 

#### [Hyde](http://hyde.github.io/)
So-called, 'Jekyll's evil twin' because it started out as a Jekyll 
rewrite in Python. Hyde is really big on metadata to determine 
how output is written, and it even has custom tags and filters.
Besides this, Hyde is pretty much on par with Jekyll.

#### [Pelican](http://blog.getpelican.com/)
Also written in Python, so also a huge plus. Pelican uses Jinja 
templating, so it can be used for way more than just blogging. It's
very flexible and supports many different languages for content 
posting, so you aren't tied down to Markdown. This is also 
a good choice for beginners because Pelican 
supports importing from WordPress, Dotclear, and RSS feeds. So if you 
have an existing dynamic site that you want to make static, Pelican 
is a great choice.

#### [Nikola](https://getnikola.com/)
Another Python generator! What's even better about Nikola is that it has
an incredibly small codebase. Going through the source is breeze, if 
that's your style. Nikola supports many languages for content 
posting like Pelican, but it also has incredible support for image galleries.
It's compatible with Python 2 and 3, so there should be no 
complaints from programmers, and StaticGen says it "doesn't 
reinvent wheels, it leverages existing tools". In my 
opinion, Nikola is pretty sweet. Example, taken straight 
from the documentation:  
```
DON'T READ THIS MANUAL. IF YOU NEED TO READ IT I FAILED, JUST USE THE THING.
```  
Need I say more?

#### [Acrylamid](https://posativ.org/acrylamid/)
Acrylamid is yet another generator written in Python. Like Hyde, Acrylamid 
is big on metadata, and you can use YAML-style frontmatter or 
the native formats of Markdown, reST, and Pandoc. If 
you want to use something else, you can even 
[extend Acrylamid in 30 LoC](https://posativ.org/git/acrylamid/blob/master/acrylamid/filters/pytextile.py). 
What's also neat? Acrylamid supports TeX hyphenation filters, 
summarizing filters, and acronym-detection. And they're even on 
[Freenode](http://freenode.net/), `#acrylamid`.  
  
Check out [Part 3](http://bashfulbytes.com/posts/staticsitegenerator3.html) to
find out how to create your own static site generator.  
