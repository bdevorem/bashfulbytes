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


## Creating You Own Static Site Generator
If you have a very specific goal in mind, or none of those 
generators really do what you want, or you just feel trapped 
without customization (love you 
[Arch Linux](https://www.archlinux.org/)), you may 
just want to make your own. It may sound like a big feat or 
too complicated to even bother trying, but making a static 
site generator is actually really straightforward. 

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
You can even gather timestamps for your files to create some kind of order 
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
came across all the previously mentioned generators. I 
quickly narrowed it down to the projects written in 
Python. I was left with Pelican, Hyde, Acrylamid,
and Nikola. I had a brief peek into all of the source code 
before I decided to narrow it down to two and then get 
my hands dirty.

Acrylamid was a faster descendant of Pelican, so I 
kicked Pelican off the list. Hyde was just too 
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
and see all the lovely `Nikola auto commit.`'s.  
  
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
dedicate my time to learning more about static site generators 
to implement *exactly* what I wanted, without limitation or
constriction.  
  
Cue the birth of yet another static site generator, called `gen`. I'm 
creative, I know. You can view the *single file* 
[here](https://github.com/bdevorem/bdevorem.github.io/blob/master/gen.py).  
  
I have my file hierarchy set up to support two different types of documents: 
posts and pages. Posts contain YAML-style frontmatter and are added to my 
appendix, and pages are pretty much everything else. Pages are not explicitly 
added anywhere; unless I insert a hyperlink somewhere, pages are pretty much 
hidden, though not obscured. I write everything in
Markdown in Vim, and save to either `posts_md/` or `pages_md/`.  
  
The first thing my generator does is scan `posts_md` for every source post, 
and converts them to HTML whilst extracting their metadata. Then, my base 
template is applied to each post, and they all get stored in `posts/`. This 
process is repeated for pages, minus the metadata extraction.  
  
After all of that HTML is created, what's left is creating my appendix, which 
is the index of my site. When the metadata was extracted from the posts, each 
file was grouped into a category matching its tag, and the Recent category was
populated with the 5 most recently-created posts. This is all created in 
Markdown for simplicity, and then it gets converted to HTML. The base template for the 
index page is different than the base template I use to convert the pages and 
posts, because of the tag categories. So, this separate base template is applied 
to my HTML and the document gets written to `pages/`.  
  
The last step is to render the Jinja templating. I wanted to make my own function 
for this, but it wasn't working the way I wanted it to. I installed 
[StaticJinja](https://staticjinja.readthedocs.io/en/latest/) to do the 
dirty work instead. Everything comes together in a simple Makefile.  
  
My generator is far from finished. I haven't added syntax highlighting yet, 
I have a hotfix for binaries that I want to make more elegant, I want to add 
a simple webserver so I don't have to rely on committing to see what the site 
will look like, and much more. 
