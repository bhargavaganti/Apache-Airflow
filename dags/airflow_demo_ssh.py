


from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.contrib.operators.ssh_operator import SSHOperator
from datetime import datetime, timedelta
import logging


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime.now().replace(second=0, microsecond=0),
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
dag = DAG('airflow_demo_ssh', default_args=default_args, schedule_interval=timedelta(minutes=2) )


# Task to print date
t1 = BashOperator(
    task_id='Start',
    bash_command='date',
    dag=dag)


# Task to execute remote command (via SSH Hook).
t2 = SSHOperator(
       ssh_conn_id='ssh_daza1',
       task_id="remote_task1",
       command="touch zzz.txt",
       #do_xcom_push=True,
       dag=dag)


# Create DAG by specifying upstream tasks
t2.set_upstream(t1)



#ZEND
