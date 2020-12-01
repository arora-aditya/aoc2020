RED=\033[0;31m
GREEN=\033[0;32m
BLUE=\033[36m
NC=\033[0m

day    := $(shell date +%-d)
filetd := day$(shell date +%-d).py

run: ## Run solution for day=X (default based on day of month)
	python3 ${filetd}

input: ## Get input for day=X (default based on day of month)
	@python3 helper/getInput/getInput.py ${day}
	@echo "${GREEN}input stored in input${day}.txt${NC}"

README: ## Update root README
	@python3 helper/generateREADME/generateREADME.py
	@echo "${GREEN}README generated${NC}"

.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "${BLUE}%-20s${NC} %s\n", $$1, $$2}'