export BRANCH=$(shell git rev-parse --abbrev-ref HEAD)

.PHONY: try
try/$(BRANCH):
	mkdir -p try/$(BRANCH)

try_default: try/$(BRANCH)
	python tests/try_cookiecutter.py --output_dir try/$(BRANCH)
