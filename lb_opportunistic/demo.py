import os_connector
import ConfigParser
import json
import requests
import subprocess

# Conf reading
config = ConfigParser.RawConfigParser()
config.read('./emaas.cfg')

user = config.get('credentials', 'user')
password = config.get('credentials', 'password')
domain = config.get('credentials', 'domain')
project_id = config.get('credentials', 'project_id')
auth_ip = config.get('credentials', 'auth_ip')

saharaclient = os_connector.get_sahara_client(user, password, project_id,
                                              auth_ip, domain)

# Submit pi job to running cluster
#spark_pi_cluster_id = '5149da78-f896-42c9-9eea-a1abfc6f020a'
#spark_pi_job_id = 'ce52a8e5-4ccb-450e-91ce-ac4429cb9a18'
#
#spark_pi_configs = os_connector.get_job_configs(args=['4'],
#                                                main_class='main')
#
#spark_pi_exec = os_connector.create_job_execution(saharaclient,
#                                                  spark_pi_job_id,
#                                                  spark_pi_cluster_id,
#                                                  configs=spark_pi_configs)

# Start EMaaS cluster
plugin = config.get('manager', 'plugin')
ip = config.get('manager', 'ip')
port = config.get('manager', 'port')
cluster_size = config.getint('manager', 'cluster_size')
flavor_id = config.get('manager', 'flavor_id')
image_id = config.get('manager', 'image_id')
bigsea_username = config.get('manager', 'bigsea_username')
bigsea_password = config.get('manager', 'bigsea_password')

opportunistic = config.get('plugin', 'opportunistic')
dependencies = config.get('plugin', 'dependencies')
args = config.get('plugin', 'args').split()
main_class = config.get('plugin', 'main_class')
job_template_name = config.get('plugin', 'job_template_name')
job_binary_name = config.get('plugin', 'job_binary_name')
job_binary_url = config.get('plugin', 'job_binary_url')
input_ds_id = ''
output_ds_id = ''
plugin_app = config.get('plugin', 'plugin_app')
expected_time = config.getint('plugin', 'expected_time')
collect_period = config.getint('plugin', 'collect_period')
openstack_plugin = config.get('plugin', 'openstack_plugin')
number_of_jobs = config.get('plugin', 'number_of_jobs')
job_type = config.get('plugin', 'job_type')
version = '2.1.0'
cluster_id = config.get('plugin', 'cluster_id')
slave_ng = config.get('plugin', 'slave_ng')
percentage = config.get('plugin', 'percentage')
opportunistic_slave_ng = config.get('plugin', 'opportunistic_slave_ng')
master_ng = config.get('plugin', 'master_ng')
net_id = config.get('plugin', 'net_id')
actuator = config.get('scaler', 'actuator')
starting_cap = config.get('scaler', 'starting_cap')

scaler_plugin = config.get('scaler', 'scaler_plugin')
app_name = config.get('scaler', 'app_name')
days = config.get('scaler', 'days')
scaling_parameters = {}
scaling_parameters['actuator'] = config.get('scaler', 'actuator')
scaling_parameters['metric_source'] = config.get('scaler', 'metric_source')
scaling_parameters['application_type'] = config.get('scaler',
                                                    'application_type')
scaling_parameters['check_interval'] = config.getint('scaler',
                                                     'check_interval')
scaling_parameters['trigger_down'] = config.getint('scaler', 'trigger_down')
scaling_parameters['trigger_up'] = config.getint('scaler', 'trigger_up')
scaling_parameters['min_cap'] = config.getint('scaler', 'min_cap')
scaling_parameters['max_cap'] = config.getint('scaler', 'max_cap')
scaling_parameters['actuation_size'] = config.getint('scaler',
                                                     'actuation_size')
scaling_parameters['metric_rounding'] = config.getint('scaler',
                                                      'metric_rounding')

headers = {'Content-Type': 'application/json'}
body = dict(plugin=plugin, scaler_plugin=scaler_plugin,
            scaling_parameters=scaling_parameters, cluster_size=cluster_size,
            percentage=percentage, starting_cap=starting_cap,
            actuator=actuator, flavor_id=flavor_id, image_id=image_id,
            opportunistic=opportunistic, args=args, main_class=main_class,
            job_template_name=job_template_name, number_of_jobs=number_of_jobs,
            job_binary_name=job_binary_name, job_binary_url=job_binary_url,
            input_ds_id=input_ds_id, output_ds_id=output_ds_id, days=days,
            plugin_app=plugin_app, expected_time=expected_time,
            collect_period=collect_period, bigsea_username=bigsea_username,
            bigsea_password=bigsea_password, openstack_plugin=openstack_plugin,
            job_type=job_type, version=version, app_name=app_name,
            opportunistic_slave_ng=opportunistic_slave_ng, slave_ng=slave_ng,
            master_ng=master_ng, net_id=net_id, dependencies=dependencies)

#Start LB
lb_exec = subprocess.Popen('bash run_lb.sh', shell=True)

url = "http://%s:%s/manager/execute" % (ip, port)
print "Making request to", url
body_log = body.copy()
r = requests.post(url, headers=headers, data=json.dumps(body))

app_id = r.content.replace("\"", "")
print "Application id: %s" % app_id

url_status = "http://%s:%s/manager/logs/execution/%s" % (ip, port, app_id)
url_execution_log = "http://%s:%s/manager/logs/std/%s" % (ip, port, app_id)
print "Running application"

