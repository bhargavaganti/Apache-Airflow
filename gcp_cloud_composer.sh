

###################################################################################################
#
#   Cloud Composer (Apache Airflow)
#
#   Google Cloud Platform (GCP)
#
#   References:
#   https://cloud.google.com/composer/docs/quickstart
#   https://cloud.google.com/composer/docs/how-to/managing/creating
#
###################################################################################################



# Create Cloud Composer (Apache Airflow) Environment
gcloud composer environments create z-cloud-composer1 \
  --location us-east1 \
  --zone us-east1-b \
  --machine-type n1-standard-1 \
  --env-variables=gcp_project=zproject201807,gcs_bucket=gs://z-airflow-dags,gce_zone=us-east1-b



# Delete Cloud Composer (Apache Airflow) Environment
gcloud composer environments delete z-cloud-composer1 \
  --location us-east1



#ZEND
