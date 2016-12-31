---
title: Create Your Own Static Site Generator (Part 3)
date: 2016 6 30
tag: programming
---

#Create Your Own Static Website Generator (Part 3)

## Creating Your Own Static Site Generator
If you have a very specific goal in mind, or 
[none of these generators](http://bashfulbytes.com/posts/staticsitegenerator2.html) 
really do what you want, or you just feel trapped 
without customization (love you 
[Arch Linux](https://www.archlinux.org/)), you may 
just want to make your own. It may sound like a big feat or 
too complicated to even bother trying, but making a static 
site generator is actually really straightforward. 

I personally think the easiest way to generate and host your own site is
to work on a Linux machine, from the command line. For this site, BashfulBytes,
I host my content with [Nginx](https://www.nginx.com/) on an Ubuntu 
[virtual private server](https://en.wikipedia.org/wiki/Virtual_private_server) 
from [Digital Ocean](https://www.digitalocean.com/products/compute/). The
rest of this post assumes you are familiar with a Unix-like OS.  

A basic generator can 
be broken down into the following steps.  
  
1.  Scan source directory for content to be generated.  
  
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
    skeleton HTML you want your pages/posts to have. You can import your CSS and 
    set up your header, footer, columns, divs, everything. Then, to add your 
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
You can even gather timestamps from your files to create some kind of order 
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
wasn't exactly what I wanted (running Linux has made me a 
spoiled brat).
  
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
popular generators on [StaticGen](https://www.staticgen.com/)
(because I am a proponent of open source projects), and 
came across all the previously mentioned generators from 
[Part 2](http://bashfulbytes.com/posts/staticsitegenerator2.html). I 
quickly narrowed it down to the projects written in 
Python. I was left with [Pelican](http://blog.getpelican.com/),
[Hyde](http://hyde.github.io/), 
[Acrylamid](https://posativ.org/acrylamid/),
and [Nikola](https://getnikola.com/). 
I had a brief peek into all of the source code 
before I decided to narrow it down to two and then get 
my hands dirty.  

Acrylamid is a faster descendant of Pelican, 
so I kicked Pelican off the list. Hyde was just too 
mainstream for me, so I kicked it off the list. Not 
all decisions need to have substantial reasoning. Plus, 
Nikola was named after Nikola Tesla and clearly has 
amazingly sassy documentation, and Acrylamid loves TeX, 
so it seemed like those were meant to be my final picks.  
  
I started with Acrylamid because I was drawn to the sample 
blogs listed in the docs and the flat file system concept. 
As I started going through the 
code and the real world examples, I realized I hadn't 
thought about hosting and deployment *at all*. I 
quickly went through my options and decided on 
Github Pages for the moment, because I didn't want 
to engineer myself into a corner, like Might's 
strategy. I installed Acrylamid and starting 
hacking around, and I noticed that deploying to Github Pages 
wasn't intuitive with the framework. So I moved on to 
Nikola.  
  
Nikola caught my attention immediately with the incredible documentation.
It seemed like Nikola and I were meant to be, and we even had a 
two-day long love affair. You can even go back to the very first 
commits on the Github 
[project page](https://github.com/bdevorem/bdevorem.github.io) 
and see all the lovely `Nikola auto commit`s.  
  
Actually, those commits, along with some slight annoyances in 
the configuration, are what led me to creating my own 
generator. Don't get me wrong, I am a huge fan of Nikola. In 
my opinion, it's the best static site generator I looked into. 
Again, I'm just a spoiled rotten Arch Linux user and I 
wanted to do things my way, no more no less. I felt 
constricted because I couldn't customize it as easily or as 
much as I wanted to, and I didn't know the source well enough 
to fork the project and turn it into my own. So, instead of
spending the time getting to know the source, I decided to 
dedicate my time learning more about static site generators 
to implement *exactly* what I wanted, without limitation or
constriction.  
  
Cue the birth of yet another static site generator, called `gen`. I'm 
creative, I know. You can view the original version of the *single file* 
[here](https://github.com/bdevorem/bdevorem.github.io/blob/master/gen.py).
I don't really keep that repository up to date anymore, since I only used it 
to host on Github Pages. I host the site on my own VPS now, so I've gotten 
lazy with remote version control.  
  
I have my file hierarchy set up to support two different types of documents: 
posts and pages. Posts contain YAML-style frontmatter and are added to my 
appendix, and pages are pretty much everything else. Pages are not explicitly 
added anywhere; unless I insert a hyperlink somewhere, pages are pretty much 
hidden, though not obscured. I write everything in
Markdown in Vim, and save to either `posts_md/` or `pages_md/`.  
  
The first thing my generator does is scan `posts_md/` for every source post, 
and converts them to HTML whilst extracting their metadata. Then, my base 
template is applied to each post, and they all get stored in `posts/`. This 
process is repeated for pages and the corresponding directories, minus the metadata extraction.  
  
After all of that HTML is created, what's left is creating my appendix, which 
is the index of my site. When the metadata was extracted from the posts, each 
file was grouped into a category matching its tag, and the `Recent` category was
populated with the 5 most recently-created posts. This is all created in 
Markdown for simplicity, then converted to HTML. The base template for the 
index page is different than the base template I use to convert the pages and 
posts because of the tag categories. So, this separate base template is applied 
to my HTML and the document gets written to `pages/`.  
  
The last step is to render the Jinja templating. I wanted to make my own function 
for this, but it wasn't working the way I wanted it to. I installed 
[StaticJinja](https://staticjinja.readthedocs.io/en/latest/) to do the 
dirty work instead. Everything comes together in a simple Makefile.  
  
My generator is far from finished. I haven't added syntax highlighting yet, 
I have a hotfix for binaries that I want to make more elegant, and I'm thinking
of changing how the directories are laid out to make the URLs look better. We will
see.  
