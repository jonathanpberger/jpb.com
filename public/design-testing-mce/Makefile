all: deps
	node make all

deps:
	npm install

test:
	node make test

bundle:
	node make bundle

highlighter:
	node make highlighter

run:
	python3 -m http.server
	
.PHONY: deps test bundle highlighter
