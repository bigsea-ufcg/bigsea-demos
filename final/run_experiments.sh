#!/bin/bash

echo "=== BIGSEA WP3 DEMO ==="
echo ""
echo "======== BEGIN ========"

echo "--> Running applications"
for i in `seq 0 2`;
do
    ssh -i ~/.ssh/bigsea ubuntu@10.11.4.225 "source /home/ubuntu/clean.sh" &> /dev/null

    for j in `seq 1 5`;
    do
        exp_number=$(($i*5+$j))
        echo "Experiment $exp_number"
        python client.py config/all/"$exp_number".cfg
    done
done

echo "========= END ========="
