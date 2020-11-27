RED=\033[0;31m
GREEN=\033[0;32m
NC=\033[0m

input:
	@python3 helper/getInput/getInput.py ${day}
	@echo "${GREEN}input stored in day${day}${NC}"

README:
	@python3 helper/generateREADME/generateREADME.py
	@echo "${GREEN}README generated${NC}"

