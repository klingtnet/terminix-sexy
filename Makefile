.PHONY: all clean

TERMINIX_SCHEME_PATH?="$$HOME/.config/terminix/schemes"

all:
	@./convert.py
	mkdir -p $(TERMINIX_SCHEME_PATH)
	cp -v out/*.json $(TERMINIX_SCHEME_PATH)

clean:
	rm -rf out
