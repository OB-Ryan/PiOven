# Help use the monitoring utility

.PHONY: help stop monitor analyze clean-data show-output default

TEMP_FILE := temperture.log
RED := \033[0;31m
PURPLE := \033[1;35m
GREEN := \033[0;32m
NO_COLOR := \033[0m

help:
	@echo "${GREEN}Usage:${NO_COLOR}"
	@echo "${GREEN} make monitor${NO_COLOR}          - Start temperture monitoring script in the background"
	@echo "${GREEN} make analyze${NO_COLOR}          - Analyze collected data"
	@echo "${GREEN} make stop${NO_COLOR}             - Kill instance of monitoring script, if it exists"
	@echo "${GREEN} make clean-data${NO_COLOR}       - Stop tempreture monitoring script and clear contents of tempreture log"
	@echo "${GREEN} make show-output${NO_COLOR}      - Follow the output appended to ${TEMP_FILE}"

stop:
	-@pkill -f monitor_temp.sh

monitor:
	@$(MAKE) --no-print-directory stop
	@./monitor_temp.sh &

analyze:
	@python3 analyze.py

clean-data:
	@echo "${RED}WARNING${NO_COLOR}: You are about to delete the contents of $(TEMP_FILE). There is a 5 second grace period before this is executed.\n${RED}Press ctrl+C NOW if this was a mistake${NO_COLOR}"
	@sleep 5
	@echo "Time expired. Killing monitor_temp.sh and clearing ${TEMP_FILE}"
	@$(MAKE) --no-print-directory stop
	@truncate -s 0 ${TEMP_FILE}
	@echo "${PURPLE}${TEMP_FILE} contents have been cleared, monitor_temp.sh has been stopped.${NO_COLOR}"

show-output:
	@tail -f ${TEMP_FILE}

default:
	@$(MAKE) --no-print-directory help