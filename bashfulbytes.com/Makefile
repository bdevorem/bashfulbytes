build:
	./gen.py
	staticjinja build > /dev/null 2>&1
	cd posts/ && staticjinja build > /dev/null 2>&1
	cd pages/ && staticjinja build > /dev/null 2>&1
	cp index.html posts/

hackers:
	cd hackers/ && staticjinja build > /dev/null 2>&1

ethics:
	cd ethics/ && staticjinja build > /dev/null 2>&1

ggnore:
	cd ggnore/ && staticjinja build > /dev/null 2>&1

publish:
	./rss.py
	
clean:
	find . -name '.[!.]*[swo|swp]' -delete
