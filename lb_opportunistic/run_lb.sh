#!/bin/bash

LB_PATH=~/bigsea/bigsea-loadbalancer

# Go to lb directory
cd $LB_PATH
# Set the virtualenv to execute the loadbalancer
. loadbalancer/bin/activate
# Export the PYTHONPATH variable
export PYTHONPATH=':'`pwd`
# Execute the LoadBalancer
python loadbalancer/cli/main.py #&> /dev/null
