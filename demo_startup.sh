

###################################################################################################
#
#   Cloud Composer Demo - Startup Script
#
###################################################################################################


############################################################
#
#   Cloud Composer (Apache Airflow)
#
############################################################

# Create Cloud Composer (Apache Airflow) Environment
gcloud composer environments create z-cloud-composer1 \
  --location us-east1 \
  --zone us-east1-b \
  --machine-type n1-standard-1



# Create MySQL Connection within Cloud Composer



# Clone "airflow_dags" Repo from Google Cloud Source Repo
cd /tmp
rm -rf /tmp/airflow_dags
gcloud source repos clone airflow_dags


# Upload DAG(s) from Google Source Repository
gcloud composer environments storage dags import \
     --environment z-cloud-composer1 \
     --location us-east1 \
     --source /tmp/airflow_dags/airflow_demo1.py


# Upload DAG(s) from Google Source Repository
gcloud composer environments storage dags import \
     --environment z-cloud-composer1 \
     --location us-east1 \
     --source /tmp/airflow_dags/airflow_demo_mysql.py


# Upload DAG(s) from Google Cloud Storage (or other specified source)
#gcloud composer environments storage dags import \
#     --environment z-cloud-composer1 \
#     --location us-east1 \
#     --source gs://mybucket/my_airflow_dag.py



############################################################
#
#   GCE Instance (General VM)
#
############################################################




############################################################
#
#   MySQL
#
############################################################

# Create Cloud SQL (MySQL) Instance
# https://cloud.google.com/sql/docs/mysql/create-instance
gcloud sql instances create z-mysql-1 \
    --database-version=MYSQL_5_7 \
    --tier=db-n1-standard-1 \
    --region=us-east1


# Set the password for the "root@%" MySQL user:
gcloud sql users set-password root % --instance z-mysql-1 --password mysql_123


# Connect to Cloud SQL (MySQL) Instance
gcloud sql connect z-mysql-1 --user=root



#ZEND
