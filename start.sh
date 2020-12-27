#!/bin/bash
RED="\033[31m"
GREEN="\e[92m"
CYAN="\e[96m"
RESET="\e[0m"


echo -e "***************************************"
echo -e "*----------   ${RED}EAGLE EYE${RESET}  -------------*"
echo -e "*----------   ${RED}BSCS(NUML)${RESET} -------------*"
echo -e "***************************************"



echo -e "${CYAN} Starting\t Mongo\t DB\t Service ${RESET}"
service mongodb start
echo -e "${CYAN} Starting\t Redis\t Server\t For\t Django\t Channels\t   ${RESET}"
service redis-server start
echo -e "${CYAN} Starting\t Supervisor\t For\t Task\t Schedling\t Via\t Celery\t   ${RESET}"
service supervisor start
echo -e "${CYAN} Starting\t RabbitMQ\t For\t Broker\t For \t Celery\t   ${RESET}"
service  rabbitmq-server start

cd crawler
source bin/activate 
cd crawler_auth
python3 manage.py runserver 

echo -e "${GREEN} Ready\t To\t GO\t !!!!! ${RESET}"
