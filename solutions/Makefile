RED=\033[0;31m
GREEN=\033[0;32m
BLUE=\033[36m
NC=\033[0m

day    := $(shell date +%-d)
dayp   := $(shell printf '%02d' $(day))
filetd := day$(shell date +%-d).py

run: ## Run solution for day=X (default based on day of month)
	python3 ${filetd}

input: ## Get input for day=X (default based on day of month)
	@python3 helper/getInput/getInput.py ${day}
	@git add .
	@atom inputs/input${day}.txt day${day}.py
	@echo "${GREEN}input stored in input${day}.txt${NC}"

README: ## Update root README
	@python3 helper/generateREADME/generateREADME.py
	@echo "${GREEN}README generated${NC}"

DONE: README ## update README and push up to git
	@git add .
	@git commit -am "day ${day} ✅"
	@git push
	@echo "${GREEN}pushed to git${NC}"
	
CCSS: ## push to CCSS git and create PR
	@cd ~/github/advent-of-code-2020/2020 && git pull other master && mkdir -p day-${dayp}/arora-aditya && cp ~/github/aoc2020/solutions/day${day}.py  day-${dayp}/arora-aditya && git add .  && git commit -am "add day ${day}" && git push && gh pr create -w

.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "${BLUE}%-20s${NC} %s\n", $$1, $$2}'