
###################################################################################
#
#   Cloud Composer (Apache Airflow)
#
#   Interact with MySQL
#
###################################################################################


# Import Packages
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.mysql_operator import MySqlOperator
from datetime import datetime, timedelta


# Default Arguments
# These args are applied to each operator
# https://airflow.apache.org/_modules/airflow/models.html#BaseOperator
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'wait_for_downstream': False,
    #'start_date': datetime(2018, 8, 2),
    #'end_date': datetime(2018, 12, 31),
    #'email': ['airflow@example.com'],
    #'email_on_failure': False,
    #'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(seconds=180),
    'retry_exponential_backoff': True,
    #'queue': 'bash_queue',
    #'pool': 'backfill',
    #'priority_weight': 10,
    'task_concurrency': 1
}


# Create DAG object (workflow) that runs every 2 minutes.
# https://airflow.apache.org/code.html#airflow.models.DAG
# https://airflow.apache.org/_modules/airflow/models.html#DAG
dag = DAG('airflow_demo_mysql',
            description='',
            schedule_interval=timedelta(minutes=5),
            #start_date=datetime.now().replace(second=0, microsecond=0),
            start_date=datetime(2018,8,12,19,35),
            #end_date=datetime(2018,12,31),
            default_args=default_args,
            #concurrency=1,
            default_view='tree',
            orientation='TB'
        )


# Task to print date
t1 = BashOperator(
    task_id='start_print_date',
    bash_command='date',
    dag=dag)


# Task to interact with MySQL
#
# MySQL Connection Info:
#   Conn ID:    mysql_cloudsql
#   Conn Type:  MySQL
#   Host:       <ip_address>
#   Login:      root
#   Password:   <password>
#
t2 = MySqlOperator(
        task_id='interact_with_mysql',
        sql='create table ztable100 (cust_id int)',
        mysql_conn_id='mysql_cloudsql',
        autocommit=False,
        database="zdatabase",
        dag=dag)


# Create DAG by specifying upstream tasks
t2.set_upstream(t1)


#ZEND
