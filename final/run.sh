#!/bin/bash

echo   "=== BIGSEA WP3 DEMO ==="
echo ""
echo   "======== BEGIN ========"
printf "==== Cleaning existing files ====\n"
ssh -i ~/.ssh/bigsea ubuntu@10.11.4.225 "source /home/ubuntu/clean.sh"

printf "\n==== Running applications ====\n"
printf "\n1. BULMA\n"
python client.py config/"$1"/bulma.cfg

printf "\n2. BUSTE\n"
python client.py config/"$1"/buste.cfg

printf "\n3. OD matrix builder\n"
python client.py config/"$1"/od.cfg

printf "\n4. Pre-processing\n"
python client.py config/"$1"/preproc.cfg

printf "\n5. Training\n"
python client.py config/"$1"/train.cfg

echo "========= END ========="
