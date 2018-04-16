#!/bin/bash

echo "=== BIGSEA WP3 DEMO ==="
echo ""
echo "======== BEGIN ========"
printf "Cleaning remote hdfs\n"
ssh -i ~/.ssh/bigsea ubuntu@10.11.4.225 "source /home/ubuntu/clean.sh"

for i in `seq 1 6`;
do
    printf "\nRunning $i iter"
    printf "\n1. BULMA\n"
    python client.py config/"$i"/bulma.cfg
 
    printf "\n2. BUSTE\n"
    python client.py config/"$i"/buste.cfg
 
    printf "\n3. OD matrix builder\n"
    python client.py config/"$i"/od.cfg
 
    printf "\n4. Pre-processing\n"
    python client.py config/"$i"/preproc.cfg
 
    printf "\n5. Training\n"
    python client.py config/"$i"/train.cfg
done

echo "========= END ========="
