import os_connector
import ConfigParser

# Conf reading
config = ConfigParser.RawConfigParser()
config.read('./lb_opportunistic.cfg')

user = config.get('credentials', 'user')
password = config.get('credentials', 'password')
domain = config.get('credentials', 'domain')
project_id = config.get('credentials', 'project_id')
auth_ip = config.get('credentials', 'auth_ip')

saharaclient = os_connector.get_sahara_client(user, password, project_id,
                                              auth_ip, domain)

# Submit pi job to running cluster
spark_pi_cluster_id = '5149da78-f896-42c9-9eea-a1abfc6f020a'
spark_pi_job_id = 'ce52a8e5-4ccb-450e-91ce-ac4429cb9a18'

spark_pi_configs = os_connector.get_job_configs(args=['4'],
                                                main_class='main')

spark_pi_exec = os_connector.create_job_execution(saharaclient,
                                                  spark_pi_job_id,
                                                  spark_pi_cluster_id,
                                                  configs=spark_pi_configs)

# Start EMaaS cluster




