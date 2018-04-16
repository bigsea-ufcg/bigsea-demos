#!/bin/bash

echo "--- BIGSEA WP3 CLIENT ---"
echo ""
echo "========= BEGIN ========="

echo "1. Cleaning old files"
for i in `seq 0 0`;
do
    ssh -i ~/.ssh/bigsea ubuntu@10.11.4.225 "source /home/ubuntu/clean.sh" &> /dev/null

echo "2. Running BULMA"
    for j in `seq 1 1`;
    do
        exp_number=$j
#        echo "Experiment $exp_number"
        python client.py config/all/"$exp_number".cfg
    done
done

echo "========== END =========="
