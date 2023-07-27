# A Self-Documenting Makefile: http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
SHELL = /bin/bash
OS = $(shell uname | tr A-Z a-z)

.PHONY: format
format: ## Formats code
	poetry run black .
	poetry run isort .