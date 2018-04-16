==============================================
Running the Load Balancer + Opportunistic Demo
==============================================

Step 1: Setting up the environment
==================================

In order to have a proper enviroment for this demo we need to have a sample
load running on two of the three servers available.

You need to ssh to the server compute11 and compute22 and:

.. cd CPULoadGenerator
.. python laod_generator.py

This will start a random load on the servers between 40% and 90% changing every
minute to +/- 10%

Step 2: Starting Load Balancer
==============================

For this experiment we use the CPU usage heuristic on the Load Balancer.
It measures CPU utilization and when overload is detected it tries to
migrate instances.

2.1 Clone Load balancer
-----------------------

git clone https://github.com/bigsea-ufcg/bigsea-loadbalancer.git

2.2 Configure cfg
-----------------

Under  [heuristic] change module to cpu_utilization

2.3 Start Load Balancer
-----------------------

Under bigsea-demos/lb_opportunistic run ./run_lb.sh

Step 3: Start demo
==================

Change emaas_sample.cfg to emaas.cfg and configure with correct credentials and IDs

run python demo.py



The progress of execution will be as follow:

1. Job will be submitted and the cluster will be created using opportunistic instances
2. Load balancer will monitor servers
3. If needed Load balancer will trigger migrations.



