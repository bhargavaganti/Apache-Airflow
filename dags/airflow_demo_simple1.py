
###################################################################################
#
#   Cloud Composer (Apache Airflow)
#
#   Simple Demo of local scheduled commands (bash, python)
#
###################################################################################


# Import Packages
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
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
    'retry_delay': timedelta(seconds=10),
    'retry_exponential_backoff': True,
    #'queue': 'bash_queue',
    #'pool': 'backfill',
    #'priority_weight': 10,
    'task_concurrency': 1
}


# Create DAG object (workflow) that runs every 2 minutes.
# https://airflow.apache.org/code.html#airflow.models.DAG
# https://airflow.apache.org/_modules/airflow/models.html#DAG
dag = DAG('airflow_demo_simple1', 
            description='',
            schedule_interval=timedelta(minutes=2),
            #start_date=datetime(2018,8,1),
            start_date=datetime.now(),
            end_date=datetime(2018,12,31),
            default_args=default_args, 
            #concurrency=1,
            default_view='tree',
            orientation='TB'
        )


# Task to print date
t1 = BashOperator(
    task_id='start_print_date',
    description='Bash operation: Print datetime at start of DAG',
    bash_command='date',
    dag=dag)


# Task to sleep for 5 secs.
t2 = BashOperator(
    task_id='sleep',
    description='Bash operation: Sleep for 5 seconds',
    bash_command='sleep 5',
    retries=3,
    dag=dag)


t3 = BashOperator(
    task_id='print_date_bash',
    description='Bash operation: Print datetime',
    bash_command='date',
    dag=dag)


# Simple python function for testing. Print msg with datetime.
def simple_py_func():
    return ('DZ Message executed at ' + str(datetime.now()) )


# Task to call python function ("simple_py_func")
t4 = PythonOperator(
        task_id='simple_py_func',
        description='Python operation: Call function',
        python_callable=simple_py_func,
        #provide_context=True,
        dag=dag)



# Create DAG by specifying upstream tasks
t2.set_upstream(t1)
t3.set_upstream(t2)
t4.set_upstream(t1)


#ZEND
