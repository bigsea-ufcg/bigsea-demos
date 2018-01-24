#!/bin/bash

echo "======== BEGIN ========"

echo "1. BULMA"
python client.py config/bulma.cfg

echo "2. BUSTE"
python client.py config/buste.cfg

echo "3. OD matrix builder"
python client.py config/od.cfg

echo "4. Pre-processing"
python client.py config/preproc.cfg

echo "5. Training"
python client.py config/train.cfg

echo "========= END ========="
