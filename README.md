# $\_Bashful Bytes
Moving Github Pages site to VPS...

A br33zyxr blog

## About
A static blog about CS and life spent programming.  
Created with my own static site generator, converting 
Markdown and YAML frontmatter (idea derived from 
[Nikola](https://getnikola.com/)) into HTML, using
Jinja2 templating and Bootswatch theming (because 
ain't nobody got time for that).  

## Rendering Content
### How It Works
The static site generator is in the root of the repo, named
`gen.py`. To run it, first grant yourself privileges, `chmod +x`,
and then type `./gen.py` from the command line (this assumes you
have access to a terminal- if you don't,
[here's](https://www.archlinux.org/) the path to the light).
What happens first is the generator scans the `posts_md/`
directory for any files. These files are assumed to be Markdown
with YAML frontmatter (which reminds me to do some error-checking...).
Those files will be converted into HTML, written to the 
`posts/templates/` directory, and their metadata will
be extracted to form the index page for the site: an archives list
of every post, with the 5 most recent listed at the top. Then, the
same process happens for the `pages_md/` directory- these files
are anything but blog posts, eg. an about page. The HTML-rendered
files get written to `pages/templates/`, and no metadata is extracted,
since the files in `pages_md/` are assumed to be only Markdown
(yeah, I need to do some error-checking).  
Once all the posts/pages templates are rendered, then the creation
of the index page ensues. This just uses the metadata already 
collected from every post to create an archives page. The content
is created in Markdown, and then converted to HTML and written to
the `templates/` directory.  
The last thing to happen is the rendering of the templates. I use
jinja templating for the sole purpose of inheritance. I dislike
HTML just as much as the next person, so the less amount I have
to write, the better (without using an HTML generator). Currently,
this is semi-automated using staticjinja, but eventually I would
like to code it myself.

### Make a Post
All you have to do to make a post is create a Markdown file in
`posts_md/` with some YAML frontmatter. The frontmatter should
be in the form:
```yaml
---
title: some_title
date: year month day
tag: some_tag
---
```
Then, when the post is done, run the generator from the root
of the project. To deploy, commit and push to Github if
you're using Github Pages for deployment. I use nginx for 
serving, so all I have to do is reload the browser page 
to see new content.

Disclaimer: this static site generator is completely tailored to
my needs and desires. If you want to use it, feel free, but it 
might not fulfill your needs the way it does mine.

## TODO
- [ ] Only regenerate changed files
- [x] Migrate to VPS
- [x] nginx
- [x] map domain to IP
- [ ] create own webserver?  
- [ ] configure staticjinja instead of running defaults  
- [ ] make url more readable (make dirs w index.html instead
of *postname*.html  
- [x] make rss generator 
- [ ] add site email?

