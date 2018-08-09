
###################################################################################
#
#   Cloud Composer (Apache Airflow)
#
#   Demo of local commands (bash, python) + MySQL Remote SQL
#
###################################################################################


# Import Packages
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.mysql_operator import MySqlOperator
from datetime import datetime, timedelta


# Default Arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2018, 8, 2),
    #'email': ['airflow@example.com'],
    #'email_on_failure': False,
    #'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=20),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2018, 12, 31),
}


# Create DAG object (workflow) that runs every 2 minutes.
dag = DAG('airflow_demo_mysql', default_args=default_args, schedule_interval=timedelta(minutes=2) )


# Task to print date
t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag)


# Task to sleep for 5 secs.
t2 = BashOperator(
    task_id='sleep',
    bash_command='sleep 5',
    retries=3,
    dag=dag)


# Python test func, which will be called by Task 3 (t3)
def simple_py_func():
    return ('DZ Message executed at ' + str(datetime.now()) )


# Task to call python function ("simple_py_func")
t3 = PythonOperator(
        task_id='simple_py_func',
        python_callable=simple_py_func,
        #provide_context=True,
        dag=dag)


t4 = MySqlOperator(
        "select * from zdatabase.banking",
        mysql_conn_id="z_mysql_connection1",
        database="zdatabase",
        task_id="mysql_query",
        dag=dag)


# Create DAG by specifying upstream tasks
t2.set_upstream(t1)
t3.set_upstream(t2)
t4.set_upstream(t2)


#ZEND
