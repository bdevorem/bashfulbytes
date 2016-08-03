build:
	./gen.py
	staticjinja build > /dev/null 2>&1
	cd posts/ && staticjinja build > /dev/null 2>&1
	cd pages/ && staticjinja build > /dev/null 2>&1

publish:
	./make_rss.py
	
clean:
	find . -name '.[!.]*[swo|swp]' -delete
