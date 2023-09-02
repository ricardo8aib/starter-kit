# A Self-Documenting Makefile: http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
SHELL = /bin/bash
OS = $(shell uname | tr A-Z a-z)

.PHONY: format
format: ## Formats code
	pre-commit run black --all-files
	pre-commit run isort --all-files