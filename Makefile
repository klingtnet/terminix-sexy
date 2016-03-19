.PHONY: all

TERMINIX_SCHEME_PATH?='/usr/share/terminix/schemes'

all:
	@ ./convert.py
	sudo cp -v out/*.json $(TERMINIX_SCHEME_PATH)
