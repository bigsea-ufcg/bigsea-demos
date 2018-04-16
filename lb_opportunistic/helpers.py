from subprocess import Popen


def start_workload(host, num_cpu):
    command = ('ssh -i ~/Downloads/bigsea ubuntu@%s lookbusy -c 90 &> '
               '/dev/null' % host)
               #'/cpu-load-generator.py -n 1 20 cpu-load-generator/workload &> /dev/null' % host)

    Popen(command, shell=True)
