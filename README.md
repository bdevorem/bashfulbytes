## $\_Bashful Bytes

A br33zyxr blog

## About
A static blog about CS and life spent programming.  
Created with my own static site generator, converting 
Markdown and YAML frontmatter (idea derived from 
[Nikola](https://getnikola.com/)) into HTML, using
Jinja2 templating and Bootswatch theming (because 
ain't nobody got time for that).  

## Rendering Content
Create new Markdown/YAML post in the `posts_md/` directory, or
a new page in the `pages_md/` directory. The content for 
any post or page will extend its own respective `base.html`.
Then, navigate back to the root directory of the project 
and run `./gen.py`, assuming you've granted yourseld execution
rights (`chmod +x`). This will generate all of the HTML and
use the YAML frontmatter to decide how posts are listed on
the homepage and in the archives.  
Currently, the jinja rendering is not automated, so from each 
of the root, `pages/`, and `posts/` directories, run 
`staticjinja build`. Make sure to navigate to each of those 
directories before you run the command, because the command
searches the _current_ directory for a `templates/` directory
to render content. The static generator creates HTML files
in the respective `templates/` directories for this exact reason.  
Once all this is done, go back to the root of the project, commit
all your changes, and push it to the remote (assuming you're using
Github Pages for deployment). I have not implemented
a local server yet, because it's my repo and I don't mind cluttering
the commits :)
