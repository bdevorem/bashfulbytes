build:
	./gen.py
	staticjinja build > /dev/null 2>&1
	cd posts/ && staticjinja build > /dev/null 2>&1
	cd ethics/ && staticjinja build > /dev/null 2>&1
	cd pages/ && staticjinja build > /dev/null 2>&1
	cp index.html posts/

publish:
	./rss.py
	
clean:
	find . -name '.[!.]*[swo|swp]' -delete
