#!/bin/bash

echo "=== BIGSEA WP3 DEMO (7 DAYS) ==="
echo ""
echo "======== BEGIN ========"

printf "1. BULMA\n"
python client.py config/7days/bulma.cfg

printf "\n2. BUSTE\n"
python client.py config/7days/buste.cfg

printf "\n3. OD matrix builder\n"
python client.py config/7days/od.cfg

printf "\n4. Pre-processing\n"
python client.py config/7days/preproc.cfg

printf "\n5. Training\n"
python client.py config/7days/train.cfg

echo "========= END ========="
