#!/bin/bash

echo "=== BIGSEA WP3 DEMO ==="
echo ""
echo "======== BEGIN ========"

echo "--> Running applications"
echo "Experiments:"
echo "1. starting_cap: 50 - expected_time: 15min - actuation_size: 25% - min: 50% - max: 100%"
echo "2. starting_cap: 75 - expected_time: 15min - actuation_size: 25% - min: 50% - max: 100%"
echo "3. starting_cap: 50 - expected_time: 15min - actuation_size: 50% - min: 50% - max: 100%"
for i in `seq 1 7`;
do
    echo "Experiment $i"
    ssh -i ~/.ssh/bigsea ubuntu@10.11.4.225 "source /home/ubuntu/clean_bulma.sh" &> /dev/null
    python client.py config/demo/"$i".cfg
    echo ""
done

echo "========= END ========="
