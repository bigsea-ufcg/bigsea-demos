#!/bin/bash

LB_PATH=/local/nfs/workspace/bigsea/bigsea-loadbalancer

# Go to lb directory
cd $LB_PATH
# Set the virtualenv to execute the loadbalancer
workon loadbalancer
# Export the PYTHONPATH variable
export PYTHONPATH=':'`pwd`
# Execute the LoadBalancer
python loadbalancer/cli/main.py &
