###################################################################################
#
#   Cloud Composer (Apache Airflow)
#
#   Write to Google Cloud Storage (gcs)
#
###################################################################################


# Import Packages
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.contrib.hooks.gcs_hook import GoogleCloudStorageHook
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
dag = DAG('airflow_demo_gcs',
            description='',
            schedule_interval=timedelta(minutes=5),
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


# GCS Hook
def list_gcs_objects():
    hook_gcs = GoogleCloudStorageHook("gcs_connection_hook")
    list_of_objs = hook_gcs.list(bucket="zdatasets1")
    return str(list_of_objs)


# Task to call GCS Hook (as python function)
t2 = PythonOperator(
        task_id='list_gcs_objects',
        description='Python operation: Call GCS Hook as python function',
        python_callable=list_gcs_objects,
        #provide_context=True,
        dag=dag)


# Create DAG by specifying upstream tasks
t2.set_upstream(t1)


#ZEND
