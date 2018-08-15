

###################################################################################
#
#   Cloud Composer (Apache Airflow)
#
#   Dummy DAG Example
#
###################################################################################


# Import Packages
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta
import logging


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
dag = DAG('airflow_dag_example',
            schedule_interval=timedelta(minutes=5),
            start_date=datetime(2018,8,15),
            #start_date=datetime.now().replace(second=0, microsecond=0),
            end_date=datetime(2018,12,31),
            default_args=default_args,
            #concurrency=1,
            default_view='tree',
            orientation='TB'
        )


# Initial Task - Start Workflow and log datetime stamp
t1 = BashOperator(
    task_id='Start',
    bash_command='date',
    dag=dag)


t2 = DummyOperator(
    task_id='List_Blobs',
    dag=dag)


t3 = DummyOperator(
    task_id='Query_SQL_DB',
    dag=dag)


t4 = DummyOperator(
    task_id='Check_for_new_Blobs',
    dag=dag)


t5 = DummyOperator(
    task_id='Insert_new_Blobs_into_SQL_DB',
    dag=dag)

t6 = DummyOperator(
    task_id='Create_SQL_Stage_Table',
    dag=dag)

t7 = DummyOperator(
    task_id='SQL_Query_of_Updated_DB',
    dag=dag)

t8 = DummyOperator(
    task_id='Copy_Blob_data_into_Stage_Table',
    dag=dag)

t9 = DummyOperator(
    task_id='Merge_Stage_with_Full_Table',
    dag=dag)


# Create DAG by specifying upstream tasks
t2.set_upstream(t1)
t3.set_upstream(t1)
t4.set_upstream(t2)
t4.set_upstream(t3)
t5.set_upstream(t4)
t6.set_upstream(t5)
t7.set_upstream(t6)
t8.set_upstream(t7)
t9.set_upstream(t8)


#ZEND
