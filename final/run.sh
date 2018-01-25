#!/bin/bash

echo "=== BIGSEA WP3 DEMO ==="
echo ""
echo "======== BEGIN ========"

printf "1. BULMA\n"
python client.py config/bulma.cfg

printf "\n2. BUSTE\n"
python client.py config/buste.cfg

printf "\n3. OD matrix builder\n"
python client.py config/od.cfg

printf "\n4. Pre-processing\n"
python client.py config/preproc.cfg

printf "\n5. Training\n"
python client.py config/train.cfg

echo "========= END ========="
